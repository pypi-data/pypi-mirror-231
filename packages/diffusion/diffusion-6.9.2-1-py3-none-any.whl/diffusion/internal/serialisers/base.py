#  Copyright (c) 2020-2023 Push Technology Ltd., All Rights Reserved.
#
#  Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

""" Base classes for implementation of serialisers. """

from __future__ import annotations

import collections
import functools
import inspect
import io
import os
import textwrap
import typing
from typing import Any, cast, Iterable, List, Mapping, MutableMapping, Sequence, Type

import structlog
from stringcase import pascalcase, snakecase
from typing_extensions import runtime_checkable, Protocol

from diffusion.internal.encoded_data import Byte, EncodingType, is_encoder
from diffusion.internal.utils import flatten_mapping
from .compound import (
    GenericMapSerialiser,
    GenericScalarSetSerialiser, KeyValue,
)
from .generic_model import GenericModel_T, GenericModel
from .spec import (
    SERIALISER_SPECS,
    SerialiserMap,
    NULL_VALUE_KEY,
    Compound,
    CompoundSpec,
    SerialiserMapValue, MutableSerialiserMap,
)
from diffusion.internal.encoded_data.abstract import Enc_MetaType_Str, Enc_MetaType, \
    EncodingTypeVar, EncodingProtocol
from diffusion.internal.protocol.exceptions import ErrorReport, ReportsError
from diffusion.internal.encoded_data.exceptions import StreamExhausted

LOG = structlog.get_logger()

ID_Type = typing.TypeVar("ID_Type", bound=int, covariant=True)


def log(x: str):
    stack_length = len(inspect.stack(0))-30
    to_log = textwrap.indent(x, "    "*stack_length)
    if os.getenv("DEBUG_RESOLVER"):
        LOG.debug(to_log)


@runtime_checkable
class ChoiceProvider(Protocol[ID_Type]):
    @classmethod
    def id(cls) -> ID_Type:
        raise NotImplementedError()


class Serialiser:
    """ Class for individual serialisers. """

    spec: SerialiserMap
    resolver: Resolver

    def __init__(self, name: str, spec: SerialiserMap, resolver: Resolver = None):
        self.name = name
        self.spec = spec
        self.resolver = resolver or resolve

    def from_bytes(self, value: bytes):
        """ Deserialise a bytes value. """
        yield from self.read(io.BytesIO(value))

    def read(self, stream: io.BytesIO):
        """ Read the value from a binary stream. """
        yield from self._recurse_read(self.spec.values(), stream)

    def _recurse_read(self, types, stream):
        types = tuple(flatten_mapping(types))
        for item in types:
            if is_encoder(item):
                try:
                    result = item.read(stream).value
                    yield result
                except StreamExhausted:
                    break
            elif item is not None:
                yield tuple(self._recurse_read(item, stream))
            else:
                yield None

    def to_bytes(self, *values) -> bytes:
        """ Serialise the value into bytes. """
        return self._recurse_write(self.spec.values(), values)

    def write(self, stream: io.BytesIO, *values) -> io.BytesIO:
        """ Write the value into a binary stream. """
        stream.write(self.to_bytes(*values))
        return stream

    def _recurse_write(self, types, values):
        result = b""
        types = tuple(flatten_mapping(types))
        for item, value in zip(types, values):
            if is_encoder(item):
                result += item(value).to_bytes()
            elif item is not None and isinstance(value, Iterable):
                result += self._recurse_write(item, value)
        return result

    def __iter__(self):
        return iter(self.spec.items())

    @property
    def fields(self):
        """ Returns a list of all the field names. """
        return list(self.spec)

    def __repr__(self):
        return f"<{type(self).__name__} name={self.name}>"

    @classmethod
    def by_name(cls, name: str = NULL_VALUE_KEY, resolver: Resolver = None) -> Serialiser:
        """ Retrieve a serialiser instance based on the spec name. """
        resolver = resolver or resolve
        return Serialiser(name, resolver(name), resolver=resolver)

    def __bool__(self):
        return self.name != NULL_VALUE_KEY

    async def error_from(self,
                         value: Mapping[typing.Union[str, int], Any],
                         tp: Type[ReportsError]):
        if self.name in ("error-report-list",):
            next_err: Any = next(iter(value.values()), [])
            next_next_err: Any = next(iter(next_err), [])
            if next_next_err:
                reports = [
                    ErrorReport(*x) for x in
                    typing.cast(typing.Iterable[Any], next_next_err)
                ]
                raise tp(reports)

    @functools.lru_cache(maxsize=None)
    def get_choice_encoder_from_list(self) -> typing.Type[ChoiceEncoder]:
        list_encoder = self.to_encoder(ListEncoder)
        return ChoiceEncoder.extract_from(list_encoder.serialiser)

    def get_encoder(
        self, *cls: typing.Type[EncodingTypeVar]
    ) -> typing.Optional[typing.Type[EncodingTypeVar]]:
        if not len(self.spec.values()) == 1:
            return None
        encoder_candidate = typing.cast(
            typing.Type[EncodingTypeVar],
            next(iter(self.spec.values())),
        )
        # noinspection PyTypeHints
        if inspect.isclass(encoder_candidate) and issubclass(
            encoder_candidate, cls
        ):
            return encoder_candidate
        return None

    def to_encoder(
            self, cls: typing.Type[EncodingTypeVar]
    ) -> typing.Type[EncodingTypeVar]:
        result = self.get_encoder(cls)
        assert result
        return result


class ChoiceEncoder(EncodingType[SerialiserMap]):
    """ Special "encoding type" for choice-based values (i.e. `one-of'). """

    serialisers: Mapping[int, Serialiser]
    serialiser_names: Mapping[typing.Hashable, str]
    resolver: Resolver

    def __init__(self, value: Sequence):
        super().__init__(value)

    @classmethod
    def read(cls, stream: io.BytesIO) -> EncodingType:
        """Read the encoded value from a binary stream.

        It converts the read value to the correct type and constructs a new
        instance of the encoding type.
        """
        choice = Byte.read(stream).value
        try:
            serialiser = cls.serialisers[choice]
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise
        values: tuple = tuple(*cast(Iterable, serialiser.read(stream)))
        LOG.debug("Read choice values.", serialiser=serialiser, choice=choice, values=values)
        return cls((choice, *values))

    def to_bytes(self) -> bytes:
        """ Convert the value into its bytes representation. """
        result = Byte(self.choice).to_bytes()
        result += self.serialiser.to_bytes(self.values)
        return result

    @property
    def choice(self):
        """ Return the current value of the choice. """
        return self.value[0]

    @property
    def values(self):
        """ Return the current collection of values. """
        return self.value[1:]

    @property
    def serialiser(self):
        """ Return the serialises spec for the current choice. """
        return self.serialisers[self.choice]

    @classmethod
    def from_name(
        cls, serialiser_name: str, resolver: Resolver = None
    ) -> typing.Type[ChoiceEncoder]:
        """Instantiate the class by resolving the serialiser name."""
        resolver = resolver or resolve
        return resolver.resolve_generic(ChoiceEncoder, resolver(serialiser_name),
                                        serialiser_name)

    @classmethod
    def get_serialiser_by_id(cls, id: int, resolver: Resolver = None):
        serialiser_name = cls.serialiser_names.get(id)
        assert serialiser_name is not None
        return Serialiser.by_name(serialiser_name, resolver=resolver)

    @classmethod
    def get_serialiser_by_provider(
        cls, provider: typing.Union[ChoiceProvider, typing.Type[ChoiceProvider]]
    ):
        assert isinstance(provider, ChoiceProvider) or (
            inspect.isclass(provider)
            and issubclass(
                typing.cast(typing.Type[ChoiceProvider], provider), ChoiceProvider
            )
        )
        return cls.get_serialiser_by_id(provider.id(), resolver=cls.resolver)

    @classmethod
    def as_tuple(cls, item: GenericModel):
        return item.Config.as_tuple(
            item, cls.get_serialiser_by_provider(typing.cast(ChoiceProvider, item.Config))
        )

    @classmethod
    def create(
        cls: typing.Type[EncodingTypeVar],
        spec: SerialiserMap,
        name: str,
        parents: typing.List[str] = None,
        resolver: Resolver = None,
    ) -> typing.Type[EncodingTypeVar]:
        """Construct a new choice encoder based on the serialiser specs."""
        resolver = resolver or resolve
        serialisers: MutableMapping[int, Serialiser] = {}
        serialiser_names: MutableMapping[typing.Hashable, str] = {}
        for key, value in spec.items():
            if not (isinstance(key, int) and isinstance(value, Sequence)):
                raise ValueError(
                    "Keys have to be integers and values have to be sequences."
                )
            serialiser_name = f"{name}.{key}"
            if all(map(is_encoder, value)):
                sub_spec = value
            elif isinstance(value, CompoundSpec):
                sub_spec = resolver.resolve_compound(key, value)
            else:
                sub_spec = []
                for num, val in enumerate(value):
                    if isinstance(val, CompoundSpec):
                        sub_spec.append(resolver.resolve_compound(str(num), val))
                    else:
                        sub_spec.append(resolver(val))
                sub_spec = tuple(sub_spec)
                if isinstance(value, str):
                    serialiser_names[key] = value
                elif (
                    isinstance(value, tuple)
                    and len(value) == 1
                    and isinstance(value[0], str)
                ):
                    serialiser_names[key] = value[0]
            serialisers[key] = Serialiser(
                serialiser_name, {serialiser_name: sub_spec}, resolver=resolver
            )
        class_name = f"{pascalcase(snakecase(name))}ChoiceEncoder"

        return typing.cast(
            typing.Type[EncodingTypeVar],
            type(
                class_name,
                (ChoiceEncoder,),
                {
                    "serialisers": serialisers,
                    "serialiser_names": serialiser_names,
                    "resolver": resolver,
                },
            ),
        )


class ListEncoder(EncodingType):
    """ Special "encoding type" for choice-based values (i.e. `n-of'). """

    serialiser: Serialiser

    def __init__(self, value: Sequence):
        super().__init__(value)

    @classmethod
    def read(cls, stream: io.BytesIO) -> EncodingType:
        """Read the encoded value from a binary stream.

        It converts the read value to the correct type and constructs a new
        instance of the encoding type.
        """
        count = Byte.read(stream).value
        serialiser = cls.serialiser
        values = []
        for entry in range(0, count):
            deserialised = serialiser.read(stream)
            values.append(list(deserialised))
        return cls(values)

    def to_bytes(self) -> bytes:
        """ Convert the value into its bytes representation. """
        if self.values is None:
            return b''
        result = Byte(len(self.values)).to_bytes()
        for value in self.values:
            serialiser = self.serialiser
            if inspect.isclass(serialiser):
                result += serialiser(value).to_bytes()
            else:
                result += serialiser.to_bytes(*value)
        return result

    @property
    def values(self) -> Sequence[Any]:
        """ Return the current collection of values. """
        return self.value

    @classmethod
    def from_tuple(
        cls,
        item: typing.Iterable[typing.Tuple[typing.Any, ...]],
        item_type: typing.Type[GenericModel_T],
    ) -> typing.List[GenericModel_T]:
        assert isinstance(item, collections.Iterable)
        return [item_type.Config.from_tuple(item_type, x, cls.serialiser) for x in item]

    @classmethod
    def as_tuple(
        cls, item: typing.Iterable[GenericModel]
    ) -> typing.Tuple[typing.Tuple[typing.Any, ...], ...]:
        assert isinstance(item, collections.Iterable)
        return tuple(x.Config.as_tuple(x, cls.serialiser) for x in item)

    @classmethod
    def create(cls, spec: SerialiserMap, name: str, parents: List[str] = None,
               resolver: Resolver = None) -> typing.Type[ListEncoder]:
        """Construct a new list encoder based on the serialiser specs."""
        resolver = resolver or resolve
        hashed_name = f"{id(resolver)}{name}"
        if "conjunction" in name and resolver.name != "Default":
            log("Initialising conjunction")
        log(
            f"Constructing {cls.__name__}({name}, {spec}, {parents}, {resolver})="
            f"{hashed_name}"
        )
        if is_encoder(spec):
            serialiser = spec
        elif isinstance(spec, CompoundSpec):
            serialiser = resolver.resolve_compound(f"{name}.{spec.type.name}", spec)
        elif isinstance(spec, str):
            serialiser = Serialiser.by_name(spec, resolver=resolver)
        else:
            raise Exception(f"can't handle ListEncoder of {spec}")
        class_name = f"{pascalcase(snakecase(name))}ListSerialiser"
        if not isinstance(serialiser, Serialiser):
            log(f"{cls}: {serialiser} is not a Serialiser")
        else:
            log(f"{cls}: {serialiser} *is* a Serialiser")
        new_type = cast(
            typing.Type[ListEncoder],
            type(class_name, (ListEncoder,), {"serialiser": serialiser}),
        )
        return new_type


class Resolver(object):
    def __init__(self, name: str, specs: typing.Mapping[str, typing.Any], cached: bool = True):
        self.name = name
        self.specs = specs
        self.cached = cached
        self.cached_items: typing.Dict[str, typing.Type[EncodingProtocol]] = {}

    def __repr__(self):
        return f"{type(self).__name__}({(self.name, id(self.specs))}) at {id(self)}"

    def __call__(
        self, serialiser_name: str, parents: List[str] = None
    ) -> SerialiserMap:
        """Extract the serialiser types for any serialiser key in the spec.

        The `parents` argument is used internally to carry the list of all
        recursive parents, which is eventually concatenated to an internal key.

        The name must be a key in the serialiser spec. The value for a key is
        recursively expanded into a mapping of encoding type classes.
        """
        log(f"{self}: Resolving {serialiser_name}, parents {parents}")

        result: MutableSerialiserMap = {}
        if parents is None:
            parents = []
        parents.append(serialiser_name)
        try:
            spec: Any = None
            found = False
            elements = serialiser_name.split(".")
            ser_name = ""
            while elements:
                ser_name = ".".join(elements)

                if ser_name in self.specs:
                    spec = self.specs.get(ser_name)
                    found = True
                    break
                elements.pop(0)
            if not found:
                raise IndexError(f"No such serialiser {ser_name}, {serialiser_name}")
        except Exception as e:  # pragma: no cover
            LOG.error(f"Got exception {e}")
            raise
        if not (spec is None or is_encoder(spec)):
            if isinstance(spec, str) or not isinstance(spec, Sequence):
                spec = [spec]
            if isinstance(spec, CompoundSpec):
                spec = self.resolve_compound(serialiser_name, spec)
            elif not all(map(is_encoder, spec)):
                for value in spec:
                    name = ".".join(parents)
                    if isinstance(value, CompoundSpec):
                        result[name] = self.resolve_compound(name, value)
                    elif is_encoder(value):
                        result[name] = value
                    else:
                        result.update(self(value, parents.copy()))
                return result
        return {".".join(parents): spec}

    def resolve_compound(self, name: str, spec: CompoundSpec) -> SerialiserMapValue:
        log(f"{self}: Resolving complex {name} and {spec}")
        if name == "conjunction-constraint" and self.name != "Default":
            log(f"{self}: Resolving complex {name} and {spec}")
        # this is where proper pattern matching would come in handy :)
        if spec.type is Compound.MAP_OF:
            key, value = typing.cast(
                typing.Tuple[Enc_MetaType_Str, Enc_MetaType_Str],
                tuple(self.specs.get(sp, sp) for sp in spec.args),
            )
            return self.resolve_generic(GenericMapSerialiser, KeyValue(key, value))
        if spec.type is Compound.SET_OF:
            set_spec = spec.args[0]
            serialiser = typing.cast(Enc_MetaType, self.specs.get(set_spec, set_spec))
            return self.resolve_generic(GenericScalarSetSerialiser, serialiser,
                                        serialiser.__name__)
        if spec.type is Compound.ONE_OF:
            return self.resolve_generic(ChoiceEncoder, spec.args[0], name)
        if spec.type is Compound.N_OF:
            return self.resolve_generic(ListEncoder, spec.args[0], name)
        raise NotImplementedError()

    def resolve_generic(
        self, encoding_type: typing.Type[EncodingTypeVar], spec, name: str = ""
    ) -> typing.Type[EncodingTypeVar]:
        if name == "":
            name = f"{spec}{encoding_type}"
        if name not in self.cached_items:
            result = encoding_type.create(spec, name, resolver=self)
            self.cached_items[name] = result
        return typing.cast(typing.Type[EncodingTypeVar], self.cached_items[name])


resolve = Resolver("Default", SERIALISER_SPECS)
