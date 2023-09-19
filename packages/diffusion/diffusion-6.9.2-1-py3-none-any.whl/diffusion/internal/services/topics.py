""" Topic services module. """
from __future__ import annotations

import io
import typing
from enum import IntEnum
from typing import TYPE_CHECKING

import structlog

from diffusion.internal.serialisers import get_serialiser
from .abstract import (
    InboundService,
    OutboundService,
    Service_T,
    OutboundService_T,
)
from ...features.topics import TopicAddResponse

if TYPE_CHECKING:  # pragma: no cover
    from diffusion.internal.session import InternalSession

LOG = structlog.get_logger()


class TopicAdd(OutboundService):
    """ Add a topic using a specification. """

    service_id = 112
    name = "TOPIC_ADD"
    request_serialiser = get_serialiser("protocol14-topic-add-request")
    response_serialiser = get_serialiser("add-topic-result")

    def _read_response(self: Service_T, stream: io.BytesIO) -> Service_T:
        """ Read the value of the response attribute from the stream. """
        response_values = list(self.response_serialiser.read(stream))
        self.response.set(TopicAddResponse(response_values[0]))
        return self


class AddAndSetTopic(OutboundService):
    """Add and set topic service."""

    service_id = 122
    name = "ADD_AND_SET_TOPIC"
    request_serialiser = get_serialiser(
        "add-and-set-topic-request"
    )
    response_serialiser = get_serialiser("add-topic-result")

    def _read_response(
        self: OutboundService_T, stream: io.BytesIO
    ) -> OutboundService_T:
        """Read the value of the response attribute from the stream."""
        response_values = list(
            self.response_serialiser.read(stream)
        )
        self.response.set(
            TopicAddResponse(response_values[0])
        )
        return self


class TopicRemoval(OutboundService):
    """Topic removal service."""

    service_id = 83
    name = "TOPIC_REMOVAL"
    request_serialiser = get_serialiser(
        "remove-topics-request"
    )
    response_serialiser = get_serialiser("integer")

    def _read_response(
        self: OutboundService_T, stream: io.BytesIO
    ) -> OutboundService_T:
        """Read the value of the response attribute from the stream."""
        self.response.set(
            *self.response_serialiser.read(stream)
        )
        return self


class Subscribe(OutboundService):
    """ Subscribe service. """

    service_id = 3
    name = "SUBSCRIBE"
    request_serialiser = get_serialiser("string")
    response_serialiser = get_serialiser("void")


class Unsubscribe(OutboundService):
    """ Unsubscribe service. """

    service_id = 4
    name = "UNSUBSCRIBE"
    request_serialiser = get_serialiser("string")
    response_serialiser = get_serialiser("void")


NotifySubscription_T = typing.TypeVar(
    "NotifySubscription_T", bound="NotifySubscription"
)


class NotifySubscription(InboundService):
    """Topic subscription notification using TopicSpecification."""

    service_id = 87
    name = "NOTIFY_SUBSCRIPTION"
    request_serialiser = get_serialiser(
        "protocol14-topic-specification-info"
    )
    response_serialiser = get_serialiser()
    event = "subscribe"

    async def consume(
        self: NotifySubscription_T,
        stream: io.BytesIO,
        session: InternalSession,
    ) -> NotifySubscription_T:
        """Receive the request from the server."""
        from diffusion.internal.topics import Topic

        consumed = typing.cast(
            NotifySubscription_T,
            await super().consume(stream, session),
        )
        topics = session.data[Topic]
        topic_id = consumed.request["topic-id"]
        if topic_id in topics:
            topic = topics[topic_id]
            log_message = "Resubscribed to topic."
        else:
            topic = Topic.from_service_value(
                consumed.request
            )
            topic.id = topic_id
            topics[topic_id] = topic
            log_message = "Subscribed to topic."
        topic.update_streams(session.handlers)
        LOG.debug(log_message, topic=topic)
        await topic.handle(self.event)
        return consumed


NotifyUnsubscription_T = typing.TypeVar(
    "NotifyUnsubscription_T", bound="NotifyUnsubscription"
)


class NotifyUnsubscription(InboundService):
    """Topic unsubscription notification."""

    service_id = 42
    name = "NOTIFY_UNSUBSCRIPTION"
    request_serialiser = get_serialiser(
        "protocol22-unsubscription-notification"
    )
    response_serialiser = get_serialiser()
    event = "unsubscribe"

    async def consume(
        self: NotifyUnsubscription_T,
        stream: io.BytesIO,
        session: InternalSession,
    ) -> NotifyUnsubscription_T:
        """Receive the request from the server."""
        from diffusion.internal.topics import Topic

        consumed = typing.cast(
            NotifyUnsubscription_T,
            await super().consume(stream, session),
        )
        topics = session.data[Topic]
        topic_id = consumed.request["topic-id"]
        reason = UnsubscribeReason(consumed.request[1])
        if topic_id in topics:
            topic = topics[topic_id]
            LOG.debug(
                "Unsubscribed from topic.",
                topic=topic,
                reason=reason,
            )
            await topic.handle(self.event, reason=reason)
        else:
            LOG.warning("Unknown topic.", topic_id=topic_id)
        return consumed


class UnsubscribeReason(IntEnum):
    """ Unsubscribe reason ID values. """

    REQUESTED = 0
    CONTROL = 1
    REMOVAL = 2
    AUTHORIZATION = 3
    UNKNOWN_UNSUBSCRIBE_REASON = 4
    BACK_PRESSURE = 5
    BRANCH_MAPPINGS = 6

    def __str__(self):
        return self.name
