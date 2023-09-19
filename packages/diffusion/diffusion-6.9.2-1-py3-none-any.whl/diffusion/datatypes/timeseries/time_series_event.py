#   Copyright (c) 2022-2023 Push Technology Ltd., All Rights Reserved.
#
#   Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

from __future__ import annotations

import datetime
import enum
import functools
import inspect
import typing

from pydantic import StrictInt

from diffusion.datatypes.timeseries.types import (
    VT,
    VT_other,
    TimeSeriesValueType,
)
from diffusion.internal.serialisers.base import ChoiceProvider
from diffusion.internal.serialisers.generic_model import GenericModel
from diffusion.internal.validation import StrictNonNegativeInt

from typing_extensions import final, Literal  # type: ignore
from io import BytesIO

import pydantic
import stringcase

from diffusion.datatypes import AbstractDataType
from diffusion.datatypes.foundation.abstract import (
    TS_T_target,
    Converter,
    ValueType_target,
    RealValue,
)
from diffusion.datatypes.timeseries.time_series_event_metadata import (
    EventMetadata,
)
from diffusion.internal.encoded_data import Int64
from diffusion.internal.encoder import Encoder, DefaultEncoder
from diffusion.internal.serialisers.pydantic import MarshalledModel


class EventType(enum.IntEnum):
    """
    Event type constants
    """

    ORIGINAL_EVENT = 0x00
    EDIT_EVENT = 0x01
    METADATA_OFFSETS = 0x02
    AUTHOR_ENCODING = 0x03

    def __int__(self):
        return self.value

    @functools.lru_cache(maxsize=None)
    def get_type(
        self,
    ) -> typing.Type["Event"]:
        for x in (OriginalEvent, EditEvent, AuthorEncoding, Offsets):
            if (
                typing.cast(ChoiceProvider, typing.cast(GenericModel, x).Config).id()
                == self
            ):
                return typing.cast(typing.Type[Event], x)
        raise RuntimeError(f"Cannot convert {self} to an Event class")

    @classmethod
    def from_int(
        cls, event_type: int
    ) -> typing.Optional[typing.Type["Event"]]:
        if event_type not in cls.__members__.values():
            return None
        ev = cls(event_type)
        return ev.get_type()

    @classmethod
    @typing.overload
    def from_type(cls, tp: typing.Type[Event_Variants]) -> EventType: ...

    @classmethod
    @typing.overload
    def from_type(cls, tp: typing.Hashable) -> typing.Optional[EventType]: ...

    @classmethod
    def from_type(
        cls, tp: typing.Union[typing.Hashable, typing.Type[Event_Variants]]
    ) -> typing.Optional[EventType]:
        return cls._from_type(tp)

    @classmethod
    @functools.lru_cache(maxsize=None)
    def _from_type(
        cls, tp: typing.Union[typing.Hashable, typing.Type[Event_Variants]]
    ) -> EventType:
        if not inspect.isclass(tp):
            tp = type(tp)
        return typing.cast(EventType, tp.Config.id())


Event_T = typing.TypeVar("Event_T", bound="Event")


class EventTypeFactory(typing.Generic[VT]):
    @classmethod
    @functools.lru_cache(maxsize=None)
    def _of(
        cls,
        model_cls: typing.Type[Event_T],
        val_type: typing.Type[TimeSeriesValueType],
    ) -> typing.Type[Event_T]:
        # if typing.cast(typing.Type[Event], cls).value_type_real() == val_type:
        #    return cls
        type_name = typing.cast(AbstractDataType, val_type).type_name
        return typing.cast(
            typing.Type[Event_T],
            type(
                f"{model_cls.__name__}{stringcase.pascalcase(type_name)}",
                (model_cls,),
                {"_value_type": val_type, "type_name": f"event-{type_name}"}
            ),
        )

    @classmethod
    def of(
        cls, model_cls: typing.Type[Event], val_type: typing.Type[VT_other]
    ) -> typing.Type[Event[VT_other]]:
        return typing.cast(
            typing.Type[Event[VT_other]],
            cls._of(model_cls, typing.cast(typing.Type[TimeSeriesValueType], val_type)),
        )


class Event(typing.Generic[VT], MarshalledModel):
    """
    Implementation of a time series event
    """

    metadata: EventMetadata = pydantic.Field()
    """ Event metadata """

    original_event: EventMetadata
    """ Original event metadata """

    value: typing.Optional[VT] = pydantic.Field()
    """ Value of event payload """

    _value_type: typing.ClassVar[type]

    encoder: typing.Type[Encoder] = DefaultEncoder

    class Config(MarshalledModel.Config, ChoiceProvider[EventType]):
        allow_mutation = False
        frozen = True
        alias_generator = None

        @classmethod
        def id(cls) -> EventType:
            raise NotImplementedError()

    @property
    def is_original_event(self):
        """
        Flag indicating whether this is an original event
        """
        return not self.is_edit_event

    @property
    def is_edit_event(self):
        return self.metadata != self.original_event

    @classmethod
    def create(
        cls: typing.Type[Event_T],
        metadata: EventMetadata,
        original_event: typing.Optional[EventMetadata],
        value: typing.Optional[VT_other],
        value_type: typing.Type[VT_other],
    ) -> Event[VT_other]:
        """
        Static factory to create a new Event instance

        Args:
            metadata: the metadata of the event
            original_event: the original event
            value: the value of the event
            value_type: the type of the value

        Returns:
            a new Event instance
        """
        result = EventTypeFactory.of(cls, value_type).construct(
            metadata=metadata, original_event=(original_event or metadata), value=value
        )
        return typing.cast(Event[VT_other], result)

    def with_value(
        self, new_value: typing.Optional[VT_other], type: typing.Type[VT_other]
    ) -> Event[VT_other]:
        """
        Create a copy of this Event with a different value

        Args:
            new_value: the new value
            type: type of the new value

        Returns:
            a new Event instance
        """
        return self.create(
            metadata=self.metadata,
            original_event=self.original_event,
            value=new_value,
            value_type=type,
        )

    def __str__(self) -> str:
        s = f"Edit of [{self.original_event}]" if self.is_edit_event else ""
        return f"{s}[{self.metadata}] {self.value}"

    @classmethod
    def validate_type(cls, source_type: typing.Type[AbstractDataType]) -> bool:
        if not issubclass(source_type, Event):
            return False
        return cls.value_type_real().validate_type(source_type.value_type_real())

    def write_value(self, stream: BytesIO) -> BytesIO:
        if self.is_edit_event:
            stream.write(self.encoder.dumps(EventType.EDIT_EVENT))

            if self.original_event:
                stream.write(self.original_event.to_bytes())
        else:
            stream.write(self.encoder.dumps(EventType.ORIGINAL_EVENT))
        if self.metadata:
            stream.write(self.metadata.to_bytes())
        if self.value is None:
            Int64(0).write(stream)
        else:
            self.value.codec_write_bytes(stream)

        return stream

    @classmethod
    def from_bytes(cls, input: bytes):
        stream = BytesIO(input)
        event_type = DefaultEncoder.load(stream)
        event_type_class = EventType.from_int(event_type)
        if not event_type_class or not issubclass(event_type_class, Event):
            raise Exception(f"Unrecognised event type: {event_type}")
        action = EventTypeFactory.of(event_type_class, cls.value_type_real()).read_value

        return typing.cast(Event[VT], action(stream))

    @classmethod
    def converter_to(
        cls: typing.Type[Event[VT]],
        entity: typing.Type[AbstractDataType[TS_T_target, ValueType_target, RealValue]],
    ) -> typing.Optional[Converter[Event[VT], ValueType_target]]:
        vt_real = typing.cast(AbstractDataType, cls.value_type_real())

        value_converter = typing.cast(
            typing.Optional[Converter[VT, ValueType_target]],
            vt_real.converter_to(entity),
        )

        if value_converter:
            val_converter_real = typing.cast(
                Converter[VT, ValueType_target], value_converter
            )

            def convert(value: Event[VT]) -> typing.Optional[ValueType_target]:
                value_to_convert: typing.Optional[VT] = value.value if value else None
                converted_value = (
                    val_converter_real(value_to_convert) if value_to_convert else None
                )
                return typing.cast(typing.Optional[ValueType_target], converted_value)

            return typing.cast(Converter[Event[VT], ValueType_target], convert)
        return None

    @classmethod
    def convert_from(
        cls: typing.Type[Event[VT]], entity: typing.Type[Event[VT_other]]
    ) -> typing.Optional[Converter[Event[VT_other], Event[VT]]]:
        entity_vt_real = typing.cast(
            typing.Type[AbstractDataType], entity.value_type_real()
        )
        cls_vt_real = typing.cast(typing.Type[AbstractDataType], cls.value_type_real())
        converter: typing.Optional[
            Converter[VT_other, VT]
        ] = entity_vt_real.converter_to(cls_vt_real)
        if converter:
            converter_real = typing.cast(Converter[VT_other, VT], converter)

            def convert_value_from(
                source_data: Event[VT_other],
            ) -> typing.Optional[Event[VT]]:
                fresh_value = typing.cast(
                    typing.Optional[VT],
                    converter_real(source_data.value)
                    if source_data and source_data.value and source_data.value.value
                    else None,
                )
                return typing.cast(
                    typing.Optional[Event[VT]],
                    source_data.with_value(fresh_value, cls.value_type_real())
                    if fresh_value
                    else None,
                )

            return typing.cast(
                Converter[Event[VT_other], Event[VT]], convert_value_from
            )
        return None

    @classmethod
    def value_type_real(cls) -> typing.Type[VT]:
        return typing.cast(typing.Type[VT], cls._value_type)

    def offset(self, offset: Offsets):
        return self.copy(
            update={
                "original_event": offset.apply(self.original_event),
                "metadata": offset.apply(self.metadata),
            }
        )

    @classmethod
    def read_value(cls: typing.Type[Event[VT]], stream: BytesIO) -> Event[VT]:
        """
        Read an original event from an input stream

        Args:
            stream: the input stream


        Returns:
            the event that was read from the stream
        """
        raise NotImplementedError()

    @property
    def sequence(self):
        return self.metadata.sequence

    @property
    def timestamp(self):
        return self.metadata.timestamp

    @property
    def author(self):
        return self.metadata.author

    @property
    def author_code(self):
        return self.metadata.author

    @property
    def original_sequence(self):
        return self.original_event.sequence

    @property
    def original_timestamp(self):
        return self.original_event.timestamp

    @property
    def original_author(self):
        return self.original_event.author

    @property
    def original_author_code(self):
        return self.original_event.author

    @property
    def edit_sequence(self):
        return self.metadata.sequence

    @property
    def edit_timestamp(self):
        return self.metadata.timestamp

    @property
    def edit_author(self):
        return self.metadata.author

    @property
    def edit_author_code(self):
        return self.metadata.author


@final
class OriginalEvent(typing.Generic[VT], Event[VT]):
    class Config(Event.Config):
        @classmethod
        def id(cls) -> Literal[EventType.ORIGINAL_EVENT]:
            return EventType.ORIGINAL_EVENT

        alias = "range-query-original-event"

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {
                "range-query-original-event": {
                    "rq-time-series-event-metadata.time-series-sequence": "original_sequence",
                    "rq-time-series-event-metadata.timestamp": "original_timestamp",
                    "rq-time-series-event-metadata.author-code.bytes": "original_author_code",
                    "value": "value",
                },
                "original-event": {
                    "original-event.time-series-event-metadata.time-series-sequence":
                        "original_sequence",
                    "original-event.time-series-event-metadata.timestamp": "original_timestamp",
                    "original-event.time-series-event-metadata.author": "original_author",
                    "original-event.value": "value",
                },
            }

    @classmethod
    def from_fields(
        cls,
        *,
        value,
        original_sequence,
        original_timestamp,
        original_author,
        **kwargs,
    ):
        value: bytes
        original_sequence: int
        original_timestamp: int
        original_author: str

        metadata = EventMetadata(
            sequence=original_sequence, timestamp=original_timestamp, author=original_author
        )

        decoded_value = typing.cast(
            typing.Type[TimeSeriesValueType], cls.value_type_real()
        ).from_bytes(value)

        return cls(
            original_event=metadata,
            metadata=metadata,
            value=decoded_value,
            **kwargs,
        )

    @classmethod
    def read_value(
        cls: typing.Type[OriginalEvent[VT]], stream: BytesIO
    ) -> OriginalEvent[VT]:
        """
        Read an original event from an input stream

        Args:
            stream: the input stream


        Returns:
            the event that was read from the stream
        """
        return cls.Config.read(cls, stream, cls.Config.serialiser("original-event"))


@final
class EditEvent(typing.Generic[VT], Event[VT]):
    class Config(Event.Config):
        @classmethod
        def id(cls):
            return EventType.EDIT_EVENT

        alias = "range-query-edit-event"
        # fmt: off
        mappings = {
            "range-query-edit-event": {
                "rq-time-series-event-metadata.time-series-sequence": "original_sequence",
                "rq-time-series-event-metadata.timestamp": "original_timestamp",
                "rq-time-series-event-metadata.author-code.bytes": "original_author_code",
                "range-query-original-event.rq-time-series-event-metadata.time-series-sequence":
                    "edit_sequence",
                "range-query-original-event.rq-time-series-event-metadata.timestamp":
                    "edit_timestamp",
                "range-query-original-event.rq-time-series-event-metadata.author-code.bytes":
                    "edit_author_code",
                "range-query-original-event.value": "value",
            },
            "edit-event": {
                "time-series-event-metadata.time-series-sequence": "original_sequence",
                "time-series-event-metadata.timestamp": "original_timestamp",
                "time-series-event-metadata.author": "original_author",
                "original-event.time-series-event-metadata.time-series-sequence":
                    "edit_sequence",
                "original-event.time-series-event-metadata.timestamp": "edit_timestamp",
                "original-event.time-series-event-metadata.author": "edit_author",
                "original-event.value": "value",
            },
        }
        # fmt: on

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return cls.mappings

    original_event: EventMetadata
    """ Original event metadata """

    @classmethod
    def from_fields(
        cls,
        *,
        value,
        edit_sequence,
        edit_timestamp,
        edit_author,
        original_sequence,
        original_timestamp,
        original_author,
        **kwargs,
    ):
        value: bytes
        edit_sequence: int
        edit_timestamp: int
        edit_author: str
        original_sequence: int
        original_timestamp: int
        original_author: str

        metadata = EventMetadata(
            sequence=original_sequence,
            timestamp=original_timestamp,
            author=original_author,
        )
        edit_metadata = EventMetadata(
            sequence=edit_sequence, timestamp=edit_timestamp, author=edit_author
        )
        return cls(
            original_event=metadata,
            metadata=edit_metadata,
            value=cls.value_type_real().from_bytes(value),
            **kwargs,
        )

    @classmethod
    def read_value(cls: typing.Type[EditEvent[VT]], stream: BytesIO) -> EditEvent[VT]:
        """
        Read an edit event from an input stream

        Args:
            stream: the input stream

        Returns:
            the event that was read from the stream
        """
        # return cls.from_bytes(bytes(stream), sys.byteorder)
        return cls.Config.read(cls, stream, serialiser=cls.Config.serialiser("edit-event"))


@final
class Offsets(MarshalledModel):
    class Config(MarshalledModel.Config, ChoiceProvider):
        @classmethod
        def id(cls) -> int:
            return EventType.METADATA_OFFSETS

        alias = "range-query-metadata-offsets"
        frozen = True

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {
                "range-query-metadata-offsets": {
                    "time-series-sequence": "sequence",
                    "timestamp": "timestamp",
                }
            }

    sequence: StrictNonNegativeInt = 0

    timestamp: StrictInt = 0

    def __str__(self):
        return (
            f"{type(self).__name__}({self.sequence}, "
            f"{repr(datetime.datetime.fromtimestamp(self.timestamp/1000))})"
        )

    def __repr__(self):
        return str(self)

    def apply(
        self, original_event: typing.Optional[EventMetadata]
    ) -> typing.Optional[EventMetadata]:
        if not original_event:
            return None
        return original_event.offset(self)


@final
class AuthorEncoding(MarshalledModel):
    class Config(MarshalledModel.Config, ChoiceProvider):
        @classmethod
        def id(cls) -> int:
            return EventType.AUTHOR_ENCODING

        alias = "range-query-author-encoding"
        alias_generator = None

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {
                "range-query-author-encoding": {
                    "range-query-author-encoding.author-code.bytes": "author_code",
                    "range-query-author-encoding.author": "author",
                }
            }

    author_code: bytes
    author: str


Event_Variants = typing.Union["OriginalEvent", "EditEvent", "Offsets", "AuthorEncoding"]
