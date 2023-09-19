from __future__ import annotations

import asyncio
import traceback
from typing import (
    Optional,
    Set,
    TYPE_CHECKING,
)

import diffusion.datatypes
from diffusion.internal.serialisers.attrs import MarshalledModel

try:
    from typing import overload, TypeAlias  # type: ignore
except ImportError:
    from typing_extensions import overload, TypeAlias    # type: ignore
import attr
import structlog
import typing

from diffusion.datatypes.foundation.abstract import (
    AbstractDataType,
)
from diffusion.features.topics.details.topic_specification import TopicSpecification
from diffusion.handlers import AbstractHandlerSet

if typing.TYPE_CHECKING:
    from diffusion.features.topics.streams import ValueStreamHandler
from diffusion.internal.encoder import Encoder, DefaultEncoder
import diffusion_core.delta as delta  # type: ignore

if TYPE_CHECKING:  # pragma: no cover
    from diffusion.internal.session import HandlersMapping

LOG = structlog.get_logger()


def spec_conv(
    val: typing.Union[diffusion.datatypes.DataTypeArgument, TopicSpecification]
) -> TopicSpecification:
    from diffusion.datatypes import UnknownDataTypeError
    if isinstance(val, TopicSpecification):
        return val
    val = diffusion.datatypes.get(val)
    if isinstance(val, type(AbstractDataType)):
        result = typing.cast(typing.Type[AbstractDataType], val).with_properties()
        return result
    raise UnknownDataTypeError(
        f"{val} is none of {(TopicSpecification, type(AbstractDataType))}"
    )


T = typing.TypeVar('T', bound="Topic")


@attr.s(slots=True, auto_attribs=True)
class Topic(MarshalledModel):
    """
    A Diffusion topic.
    """
    encoder: typing.ClassVar[Encoder] = DefaultEncoder()
    CBOR_NULL_VALUE = b"\xf6"

    path: str = attr.ib(on_setattr=attr.setters.frozen)
    """ The topic path. """
    spec: TopicSpecification = attr.ib(converter=spec_conv)  # type: ignore
    """ Specification of the topic. """

    @property
    def type(self) -> typing.Type[AbstractDataType]:
        return self.spec.topic_type
    """ Type of the topic. """

    @property
    def topic_type(self) -> int:
        return self.spec.topic_type.type_code
    """ The type code of the topic. """

    @property
    def properties(self) -> typing.Mapping[str, str]:
        return self.spec.properties_as_json()

    """ A mapping of topic properties. """

    id: Optional[int] = None
    """ Internal ID of the topic on this session. """
    binary_value: Optional[bytes] = attr.ib(default=None)
    """ The current value of the property. `None` by default. """
    streams: Set[ValueStreamHandler] = attr.ib(default=attr.Factory(set))
    """ A mapping of streams available for various events. """
    @property
    def value(self):
        """ Returns the current value for the topic. """
        if self.binary_value is None:
            return None
        return self.type.decode(self.binary_value)

    @value.setter
    def value(self, value):
        self.binary_value = self.type.encode(value)

    def update_streams(self, handlers: HandlersMapping) -> None:
        """Updates the collection of registered stream handlers for the topic.

        First it tries to locate any registered handlers with selectors that
        match the topic's type and path. If none are available, it selects
        the fallback stream handlers which match the topic's type.

        Args:
            handlers: The `Session.handlers` mapping containing all the registered handlers.
        """
        self.streams.update(
            self.compatible_handlers(handlers)
        )
        if not self.streams:
            # include fallback streams
            self.initialise_streams(handlers)

    def compatible_handlers(self, handlers) -> typing.Iterable[ValueStreamHandler]:
        from diffusion.features.topics.selectors import Selector
        result: typing.Set[ValueStreamHandler] = set()
        for key, handler in handlers.items():
            if (
                    isinstance(key, Selector)
                    and key.match(self.path)
            ):
                result.update(self.expand_handlers(handler))
        return result

    def get_compatible_handler(
        self, handler: ValueStreamHandler
    ) -> typing.Optional[ValueStreamHandler]:
        if handler.type == self.type:
            return handler
        return handler.get_converter(self.type)

    def initialise_streams(self, handlers: HandlersMapping) -> None:
        result = [
            self.get_compatible_handler(handler)
            for key, handlers in handlers.items()
            if isinstance(handlers, AbstractHandlerSet)
            for handler in self.expand_handlers(handlers)
            if (key is type(self) or self.get_compatible_handler(handler))
        ]
        self.streams.update(x for x in result if x)

    def expand_handlers(self, handler) -> typing.Set[ValueStreamHandler]:
        from diffusion.features.topics.streams import ValueStreamHandler
        result: typing.Set[ValueStreamHandler] = set()
        if isinstance(handler, AbstractHandlerSet):

            for x in handler:
                result.update(self.expand_handlers(x))
        elif isinstance(handler, ValueStreamHandler):
            comp_handler = self.get_compatible_handler(handler)
            if comp_handler:
                result.add(comp_handler)
        else:
            LOG.error(f"Got unkonown type {handler}")
        return result

    async def handle(self, event: str, **kwargs: typing.Any) -> None:
        """Runs registered stream handlers for the topic and event.

        Args:
            event: Textual identifier for the event: `update`, `subscribe` etc.
            **kwargs: Additional parameters. The topic's path and current value are
                    injected at runtime.
        """
        kwargs.update(
            {"topic_path": self.path, "topic_value": self.value, "topic_spec": self.spec}
        )
        await asyncio.gather(
            *(handler.handle(event, **kwargs) for handler in self.streams)
        )

    def update(self, value: bytes, is_delta: bool = False) -> None:
        """Updates the binary value of the topic.

        Args:
            value: The new binary value to apply.
            is_delta: If `True`, the new binary value is a binary delta to be
                    applied to the current value. If `False`, the current value
                    is replaced by the new value.
        """
        LOG.debug("Applying binary value.", value=value, is_delta=is_delta)
        if is_delta:
            value = bytes(delta.patch(bytes(self.binary_value or []), bytes(value)))
        self.binary_value = value

    @classmethod
    def from_fields(cls: typing.Type[T], **kwargs) -> T:
        tp: typing.Type[AbstractDataType] = diffusion.datatypes.get(kwargs.pop("topic_type"))
        properties: dict = kwargs.pop("properties", {})
        return cls(kwargs.pop("path"), spec=tp.with_properties(**properties), **kwargs)

    class Config(MarshalledModel.Config):
        alias = "protocol14-topic-specification-info"

        @classmethod
        def attr_mappings_all(cls, modelcls: typing.Type[Topic]):
            return {
                "protocol14-topic-specification-info": {
                    "protocol14-topic-specification.protocol14-topic-type": "topic_type",
                    "protocol14-topic-specification.topic-properties": "properties",
                    "topic-path": modelcls.path,
                    "protocol14-topic-specification-info.topic-id": modelcls.id,
                }
            }
