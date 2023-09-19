#  Copyright (c) 2020-2023 Push Technology Ltd., All Rights Reserved.
#
#  Use is subject to license terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of Push Technology. The intellectual and technical
#  concepts contained herein are proprietary to Push Technology and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

""" Specifications for serialisers, based on `spec.clj`. """

from __future__ import annotations

import typing
from enum import Enum
from typing import Iterator, Optional, Sequence, Type, Union, Mapping, MutableMapping

try:
    from typing_extensions import Final  # type: ignore  # pragma: no cover
except ImportError:
    from typing import Final  # type: ignore  # pragma: no cover

import structlog

from diffusion.internal.encoded_data import (
    Byte,
    Bytes,
    EncodingProtocol,
    Int32,
    Int64,
    String,
)
import diffusion.internal.encoded_data as encoded_data

LOG = structlog.get_logger()

EncodingClass = Type[EncodingProtocol]
SerialiserChain = Sequence[Optional[EncodingClass]]
SerialiserMapValue = Union[EncodingClass, SerialiserChain]
SerialiserMap = Mapping[str, SerialiserMapValue]
MutableSerialiserMap = MutableMapping[str, SerialiserMapValue]
SerialiserOutput = Iterator[Optional[Type[EncodingProtocol]]]

NULL_VALUE_KEY = "void"
ENCODING_TYPE_KEYS = {
    NULL_VALUE_KEY: [],
    "BYTE": Byte,
    "BYTES": Bytes,
    "FIXED_BYTES": Bytes,
    "INT32": Int32,
    "INT64": Int64,
    "STRING": String,
}


class CompoundSpec(typing.NamedTuple):
    type: Compound
    args: typing.Tuple[typing.Any, ...]

    def __repr__(self):
        return f"{self.type}({','.join(map(repr, self.args))})"


class Compound(Enum):
    """Types of compound types."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values):
        return name

    ONE_OF = "one-of"
    N_OF = "n-of"
    SET_OF = "set-of"
    SORTED_SET = "sorted-set"
    MAP_OF = "map-of"

    def __call__(self, *args) -> CompoundSpec:
        """Return an instance of the corresponding spec."""
        return CompoundSpec(type=self, args=args)

    def __repr__(self, *args):
        return f"Compound.{self._name_}"


SpecItem = Union[str, CompoundSpec]
SerialiserSpecItem = Optional[Union[EncodingClass, Sequence[SpecItem], SerialiserChain]]


SERIALISER_SPECS: Final = {
    "add-and-set-topic-request": (
        "topic-path",
        "protocol14-topic-specification",
        "bytes",
        "update-constraint",
    ),
    "add-serialised": ("generation-id", "update-id", "serialised-object"),
    "add-topic-persistence-record": (
        "persistence-origin",
        "persistence-topic-key",
        "persistence-specification-key",
        "path",
    ),
    "add-topic-result": encoded_data.Byte,
    "anonymous-connection-action": encoded_data.Byte,
    "append-record": ("generation-id", "update-id", "persistence-record"),
    "append-record-pair": (
        "generation-id",
        "update-id",
        "persistence-record",
        "persistence-record",
    ),
    "append-records": (
        "generation-id",
        "update-id",
        Compound.N_OF("persistence-record"),
    ),
    "append-result": encoded_data.Byte,
    "apply-json-patch-request": ("string", "string", "update-constraint"),
    "apply-selection-event": "topic-selection-event",
    "authenticated-principal": (encoded_data.String, "role-set"),
    "authenticator-registration-parameters": (
        "service-id",
        "control-group",
        "handler-name",
    ),
    "authenticator-registration-request": (
        "authenticator-registration-parameters",
        "conversation-id",
    ),
    "authenticator-request": (
        "principal",
        "credentials",
        "session-properties",
        "session-properties",
        "conversation-id",
    ),
    "authenticator-response": Compound.ONE_OF(
        {0: (), 1: (), 2: ("session-properties",)}
    ),
    "backup-claim-partition": encoded_data.Int32,
    "backup-claim-session-lock": "cluster-lock-allocation",
    "binary-value-constraint": "bytes",
    "boolean": encoded_data.Byte,
    "branch-mapping": ("session-filter", "path"),
    "branch-mapping-table": ("path", Compound.N_OF("branch-mapping")),
    "byte": encoded_data.Byte,
    "bytes": encoded_data.Bytes,
    "change-authorisation-roles-filter-request": (
        "session-filter",
        "role-set",
        "role-set",
    ),
    "change-authorisation-roles-filter-result": "count-or-parser-errors",
    "change-authorisation-roles-request": ("session-id", "role-set", "role-set"),
    "change-principal-request": ("principal", "credentials"),
    "check-remote-server-result": (
        "remote-server-connection-state",
        encoded_data.String,
    ),
    "claim-partition": (encoded_data.String, encoded_data.Int32),
    "claim-partition-result": (encoded_data.Int32, "file-restore-complete"),
    "claim-session-lock": ("session-lock-name", "session-lock-owner"),
    "client-info": ("session-token", "connection-info", "session-properties"),
    "client-type": encoded_data.Byte,
    "close-client-request": "protocol5-close-client-request",
    "close-reason": encoded_data.Byte,
    "cluster-lock-allocation": (
        "server-uuid",
        "session-lock-owner",
        "session-lock-sequence",
    ),
    "command-header": ("service-id", encoded_data.Byte, "conversation-id"),
    "conjunction-constraint": Compound.N_OF(
        Compound.ONE_OF(
            {
                0: ("unconstrained-constraint",),
                2: ("binary-value-constraint",),
                3: ("no-value-constraint",),
                4: ("locked-constraint",),
                5: ("no-topic-constraint",),
            }
        )
    ),
    "connection-capabilities": encoded_data.Byte,
    "connection-info": (
        "protocol-version",
        encoded_data.Int32,
        "connection-capabilities",
        encoded_data.Int32,
    ),
    "content": ("encoding", encoded_data.Bytes),
    "control-group": encoded_data.String,
    "control-registration-parameters": ("service-id", "control-group"),
    "control-registration-request-impl": (
        "control-registration-parameters",
        "conversation-id",
    ),
    "conversation-id": encoded_data.Int64,
    "count-or-parser-errors": (encoded_data.Int32, "error-report-list"),
    "count-or-parser-errors2": Compound.ONE_OF(
        {0: (encoded_data.Int32,), 1: ("error-report",)}
    ),
    "create-topic-view-result": Compound.ONE_OF(
        {
            0: ("topic-view",),
            1: ("error-report",),
            2: ("error-report", "error-report"),
            3: ("error-report", "error-report", "error-report"),
            4: ("error-report", "error-report", "error-report", "error-report"),
        }
    ),
    "create-update-stream-and-set-request": (
        "path",
        "protocol14-topic-type",
        "bytes",
        "update-constraint",
    ),
    "create-update-stream-request": (
        "path",
        "protocol14-topic-type",
        "update-constraint",
    ),
    "credentials": (encoded_data.Byte, encoded_data.Bytes),
    "data-type-name": encoded_data.String,
    "delta-id": encoded_data.Int32,
    "deregister-global-scope-handler": encoded_data.String,
    "deregister-path-scope-handler": (encoded_data.String, encoded_data.String),
    "deregister-path-scope-handlers-for-server": encoded_data.String,
    "description": encoded_data.String,
    "dimension-label": encoded_data.String,
    "dimension-value": encoded_data.String,
    "encoding": encoded_data.Byte,
    "error-reason": ("reason-code", "description"),
    "error-report": (encoded_data.String, encoded_data.Int32, encoded_data.Int32),
    "error-report-list": Compound.N_OF("error-report"),
    "exports-to-prometheus": "boolean",
    "fetch-branch-depth-parameters": (encoded_data.Int32, encoded_data.Int32),
    "fetch-has-more": "boolean",
    "fetch-limit": encoded_data.Int32,
    "fetch-maximum-result-size": encoded_data.Int32,
    "fetch-properties-index": encoded_data.Int32,
    "fetch-query-result": (
        Compound.N_OF("topic-properties"),
        Compound.N_OF("fetch-topic-result"),
        "fetch-has-more",
    ),
    "fetch-range": (
        {0: (), 1: ("path", "fetch-range-includes-path")},
        {0: (), 1: ("path", "fetch-range-includes-path")},
    ),
    "fetch-range-includes-path": "boolean",
    "fetch-topic-result": (
        "path",
        "protocol14-topic-type",
        {0: (), 1: "bytes"},
        "fetch-properties-index",
    ),
    "fetch-with-properties": "boolean",
    "fetch-with-values": "boolean",
    "file-restore-complete": "boolean",
    "filter-and-selector": ("session-filter", "topic-selector"),
    "filter-response": (
        "conversation-id",
        "session-id",
        Compound.ONE_OF({0: ("messaging-response",), 1: ("error-reason",)}),
    ),
    "filter-subscription-result": "count-or-parser-errors2",
    "forwarded-command-request": ("service-id", "session-description", "i-bytes"),
    "gateway-client": ("gateway-client-key", "gateway-configuration"),
    "gateway-client-id": encoded_data.String,
    "gateway-client-key": ("gateway-client-type", "gateway-client-id"),
    "gateway-client-list": Compound.N_OF("gateway-client-key"),
    "gateway-client-request": ("session-id", "gateway-request"),
    "gateway-client-type": encoded_data.String,
    "gateway-configuration": (
        "gateway-schema-type",
        encoded_data.String,
        encoded_data.String,
    ),
    "gateway-configuration-mode": encoded_data.Byte,
    "gateway-operation": ("gateway-operation-name", "gateway-operation-summary"),
    "gateway-operation-description": encoded_data.String,
    "gateway-operation-detail": (
        "gateway-operation-description",
        {0: (), 1: "gateway-operation-input-schema"},
        {0: (), 1: "gateway-operation-output-schema"},
    ),
    "gateway-operation-input": encoded_data.String,
    "gateway-operation-input-schema": encoded_data.String,
    "gateway-operation-name": encoded_data.String,
    "gateway-operation-output": encoded_data.String,
    "gateway-operation-output-schema": encoded_data.String,
    "gateway-operation-summary": encoded_data.String,
    "gateway-operations": Compound.N_OF("gateway-operation"),
    "gateway-registration-error": encoded_data.Byte,
    "gateway-registration-response": Compound.ONE_OF(
        {0: ("gateway-client",), 1: ("gateway-registration-error",)}
    ),
    "gateway-request": Compound.ONE_OF(
        {
            1: (),
            2: (),
            3: (),
            4: ("gateway-operation-name",),
            5: ("gateway-operation-name", {0: (), 1: "gateway-operation-input"}),
            6: ("gateway-service-detail",),
            7: ("gateway-service-detail",),
            8: ("gateway-service-id",),
            9: (),
            10: (),
            11: ("gateway-service-id",),
            12: ("gateway-service-id",),
            13: ("gateway-service-id",),
            14: ("gateway-service-id", "gateway-operation-name"),
            15: (
                "gateway-service-id",
                "gateway-operation-name",
                {0: (), 1: "gateway-operation-input"},
            ),
        }
    ),
    "gateway-response": Compound.ONE_OF(
        {
            1: ("gateway-configuration",),
            2: ("gateway-status",),
            3: ("gateway-operations",),
            4: ("gateway-operation-detail",),
            5: ({0: (), 1: "gateway-operation-output"},),
            6: ("gateway-service-detail",),
            7: ("gateway-service-detail",),
            8: (),
            9: (Compound.N_OF("gateway-service-detail"),),
            10: (Compound.N_OF("gateway-service-type"),),
            11: ("gateway-configuration",),
            12: ("gateway-status",),
            13: ("gateway-operations",),
            14: ("gateway-operation-detail",),
            15: ({0: (), 1: "gateway-operation-output"},),
        }
    ),
    "gateway-schema-type": encoded_data.Byte,
    "gateway-service-configuration": encoded_data.String,
    "gateway-service-description": encoded_data.String,
    "gateway-service-detail": (
        "gateway-service-id",
        {0: (), 1: "gateway-service-description"},
        {0: (), 1: "gateway-service-configuration"},
    ),
    "gateway-service-id": ("gateway-service-type-name", "gateway-service-name"),
    "gateway-service-name": encoded_data.String,
    "gateway-service-type": (
        "gateway-service-type-name",
        "gateway-service-type-description",
        "gateway-service-type-schema",
    ),
    "gateway-service-type-description": encoded_data.String,
    "gateway-service-type-name": encoded_data.String,
    "gateway-service-type-schema": encoded_data.String,
    "gateway-status": Compound.N_OF("gateway-status-item"),
    "gateway-status-item": (
        "gateway-status-level",
        encoded_data.Int64,
        encoded_data.String,
        encoded_data.String,
    ),
    "gateway-status-level": encoded_data.Byte,
    "gateway-validation-request": (
        "gateway-client-key",
        "gateway-configuration-mode",
        encoded_data.Bytes,
    ),
    "gateway-validation-response": encoded_data.Byte,
    "generation-id": encoded_data.Int32,
    "get-session-properties-request": ("session-id", "session-property-keys"),
    "get-session-properties-result": {0: (), 1: "session-properties"},
    "get-topic-view-result": {0: (), 1: "topic-view"},
    "global-handler-backup-processor": Compound.SET_OF(encoded_data.String),
    "group-by-path-prefix-parts": encoded_data.Int32,
    "groups-by-topic-type": "boolean",
    "groups-by-topic-view": "boolean",
    "handler-name": encoded_data.String,
    "hazelcast-address": (Compound.N_OF(encoded_data.Byte), "port"),
    "i-bytes": encoded_data.Bytes,
    "integer": encoded_data.Int32,
    "internal-session-id": "session-id",
    "is-session-lock-for-unknown-server": (),
    "json-pointer": encoded_data.String,
    "list-topic-views-result": Compound.N_OF("topic-view"),
    "locked-constraint": ("session-lock-name", "session-lock-sequence"),
    "log-entries-fetch-request": (encoded_data.Int64, encoded_data.Int64),
    "mark-partition-file-recovery-complete": ("generation-id", "update-id"),
    "maximum-groups": encoded_data.Int32,
    "measured-entity-class-metrics": (
        Compound.N_OF("metric-name"),
        Compound.MAP_OF(
            Compound.N_OF("dimension-label"),
            Compound.MAP_OF(
                Compound.N_OF("dimension-value"), Compound.N_OF("metric-value")
            ),
        ),
    ),
    "measured-entity-class-name": encoded_data.String,
    "message-path": encoded_data.String,
    "message-queue-policy": ("boolean", "throttler-type", "throttling-limit"),
    "message-receiver-control-registration-parameters": (
        "service-id",
        "control-group",
        "topic-path",
        "session-property-keys",
    ),
    "message-receiver-control-registration-request": (
        "message-receiver-control-registration-parameters",
        "conversation-id",
    ),
    "messaging-client-filter-send-request": (
        "conversation-id",
        "session-filter",
        "message-path",
        "serialised-value",
    ),
    "messaging-client-filter-send-result": "count-or-parser-errors2",
    "messaging-client-forward-send-request": (
        "conversation-id",
        "session-id",
        "message-path",
        "session-properties",
        "serialised-value",
    ),
    "messaging-client-send-request": ("session-id", "message-path", "serialised-value"),
    "messaging-response": ("serialised-value",),
    "messaging-send-request": ("message-path", "serialised-value"),
    "metadata-type": encoded_data.Byte,
    "metric-collector-name": encoded_data.String,
    "metric-name": encoded_data.String,
    "metric-value": encoded_data.Int64,
    "missing-topic-event": (
        "topic-selector",
        "session-properties",
        "server-names",
        "server-ids",
    ),
    "missing-topic-propagation-request": ("session-id", "topic-selector"),
    "missing-topic-request": ("session-id", "topic-selector", "conversation-id"),
    "mqtt-client-id": encoded_data.String,
    "mqtt-payload": "bytes",
    "mqtt-payload-format": encoded_data.Byte,
    "mqtt-publish-request": ("mqtt-topic-name", "mqtt-payload-format", "mqtt-payload"),
    "mqtt-session-notification": ("internal-session-id", "mqtt-client-id", "principal"),
    "mqtt-session-takeover-result": Compound.N_OF("internal-session-id"),
    "mqtt-topic-name": encoded_data.String,
    "named-topic-view-specification": ("topic-view-name", "topic-view-specification"),
    "no-topic-constraint": (),
    "no-value-constraint": (),
    "null-count-or-parser-errors": [],
    "null-integer": [],
    "owned-topic-removal-result": ("integer", "integer"),
    "partial-json-constraint-with": Compound.MAP_OF("json-pointer", encoded_data.Bytes),
    "partial-json-constraint-without": Compound.SET_OF("json-pointer"),
    "partial-json-constraint": (
        "partial-json-constraint-with",
        "partial-json-constraint-without",
    ),
    "partition-event": (encoded_data.Byte, "partition-generation"),
    "partition-generation": ("partition-id", "generation-id", "file-restore-complete"),
    "partition-id": encoded_data.Int32,
    "partition-log": (
        "partition-id",
        "generation-id",
        "update-id",
        "file-restore-complete",
        Compound.N_OF("persistence-record"),
        Compound.N_OF("serialised-object"),
    ),
    "password-hash": encoded_data.String,
    "path": encoded_data.String,
    "path-handler-backup-processor": "string-set-hierarchy-index-wrapper",
    "path-set": Compound.SET_OF("path"),
    "peer-authenticator-request": (
        encoded_data.String,
        "principal",
        "credentials",
        "session-properties",
        "session-properties",
    ),
    "peer-authenticator-response": {0: (), 1: "authenticator-response"},
    "peer-messaging-send-request": (
        "internal-session-id",
        Compound.MAP_OF(encoded_data.String, encoded_data.String),
        "messaging-send-request",
    ),
    "persistence-origin": encoded_data.Byte,
    "persistence-record": Compound.ONE_OF(
        {
            1: ("topic-specification-persistence-record",),
            2: ("add-topic-persistence-record",),
            3: ("remove-topic-persistence-record",),
            4: ("update-topic-persistence-record",),
        }
    ),
    "persistence-records": Compound.N_OF("persistence-record"),
    "persistence-specification-key": (encoded_data.Int32, encoded_data.Int32),
    "persistence-topic-key": (encoded_data.Int32, encoded_data.Int32),
    "ping-request": (),
    "ping-response": (),
    "port": encoded_data.Int32,
    "principal": encoded_data.String,
    "protocol-15-create-update-stream-response": "update-stream-id",
    "protocol-15-update-stream-add-topic-response": (
        "add-topic-result",
        "update-stream-id",
    ),
    "protocol-19-create-update-stream-response": (
        "update-stream-id",
        encoded_data.Byte,
    ),
    "protocol-19-update-stream-add-topic-response": (
        "add-topic-result",
        "update-stream-id",
        encoded_data.Byte,
    ),
    "protocol-version": encoded_data.Byte,
    "protocol12-close-client-request": "session-id",
    "protocol12-topic-add-request": ("path", "protocol12-topic-specification"),
    "protocol12-topic-notification-event": (
        "conversation-id",
        "path",
        encoded_data.Byte,
        "protocol12-topic-specification",
    ),
    "protocol12-topic-specification": ("protocol12-topic-type", "topic-properties"),
    "protocol12-topic-specification-info": (
        "topic-id",
        "path",
        "protocol12-topic-specification",
    ),
    "protocol12-topic-type": encoded_data.Byte,
    "protocol14-global-permission": encoded_data.Byte,
    "protocol14-global-permission-set": Compound.SET_OF("protocol14-global-permission"),
    "protocol14-path-permission": encoded_data.Byte,
    "protocol14-path-permission-set": Compound.SET_OF("protocol14-path-permission"),
    "protocol14-role": (
        "role-name",
        "protocol14-global-permission-set",
        "protocol14-path-permission-set",
        Compound.MAP_OF("path", "protocol14-path-permission-set"),
        "role-set",
    ),
    "protocol14-security-configuration": (
        "role-set",
        "role-set",
        Compound.N_OF("protocol14-role"),
    ),
    "protocol14-topic-add-request": ("topic-path", "protocol14-topic-specification"),
    "protocol14-topic-notification-event": (
        "conversation-id",
        "path",
        encoded_data.Byte,
        "protocol14-topic-specification",
    ),
    "protocol14-topic-specification": ("protocol14-topic-type", "topic-properties"),
    "protocol14-topic-specification-info": (
        "topic-id",
        "topic-path",
        "protocol14-topic-specification",
    ),
    "protocol14-topic-type": encoded_data.Byte,
    "protocol14-unsubscription-notification": ("topic-id", encoded_data.Byte),
    "protocol15-fetch-query": (
        "topic-selector",
        "fetch-range",
        "topic-type-set",
        "fetch-with-values",
        "fetch-with-properties",
        "fetch-limit",
        "fetch-maximum-result-size",
    ),
    "protocol15-log-entries-fetch-response": (
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.String,
    ),
    "protocol15-session-properties-event-batch": (
        "conversation-id",
        Compound.N_OF("protocol15-session-properties-event-core"),
    ),
    "protocol15-session-properties-event-core": (
        "session-id",
        Compound.ONE_OF(
            {
                0: ("session-properties",),
                1: (
                    "session-properties-update-type",
                    "session-properties",
                    "session-properties",
                ),
                2: ("close-reason", "session-properties"),
            }
        ),
    ),
    "protocol16-fetch-query": "protocol15-fetch-query",
    "protocol16-global-permission": encoded_data.Byte,
    "protocol16-global-permission-set": Compound.SET_OF("protocol16-global-permission"),
    "protocol16-measured-entity-class-request": encoded_data.String,
    "protocol16-role": (
        "role-name",
        "protocol16-global-permission-set",
        "protocol14-path-permission-set",
        Compound.MAP_OF("path", "protocol14-path-permission-set"),
        "role-set",
    ),
    "protocol16-security-configuration": (
        "role-set",
        "role-set",
        Compound.N_OF("protocol16-role"),
    ),
    "protocol16-session-metric-collector": (
        "metric-collector-name",
        "boolean",
        "boolean",
        "session-filter",
        "session-property-keys",
    ),
    "protocol16-session-metric-collectors": Compound.N_OF(
        "protocol16-session-metric-collector"
    ),
    "protocol16-session-properties-event-batch": (
        "conversation-id",
        Compound.N_OF("protocol16-session-properties-event-core"),
    ),
    "protocol16-session-properties-event-core": (
        "session-id",
        Compound.ONE_OF(
            {
                0: ("session-properties",),
                1: ("session-properties-update-type", "session-properties-changes"),
                2: ("close-reason", "session-properties"),
            }
        ),
    ),
    "protocol16-topic-metric-collector": (
        "metric-collector-name",
        "boolean",
        "topic-selector",
        "boolean",
    ),
    "protocol16-topic-metric-collectors": Compound.N_OF(
        "protocol16-topic-metric-collector"
    ),
    "protocol17-fetch-query": (
        "protocol16-fetch-query",
        "fetch-branch-depth-parameters",
    ),
    "protocol17-jmx-fetch-request": Compound.N_OF(encoded_data.String),
    "protocol17-jmx-fetch-response": "i-bytes",
    "protocol17-role": (
        "role-name",
        "protocol16-global-permission-set",
        "protocol14-path-permission-set",
        Compound.MAP_OF("path", "protocol14-path-permission-set"),
        "role-set",
        {0: (), 1: "string"},
    ),
    "protocol17-security-configuration": (
        "role-set",
        "role-set",
        Compound.N_OF("protocol17-role"),
    ),
    "protocol17-system-authentication-configuration": (
        Compound.N_OF("protocol17-system-principal"),
        "anonymous-connection-action",
        "role-set",
    ),
    "protocol17-system-principal": ("string", "role-set", {0: (), 1: "string"}),
    "protocol18-create-remote-server-result": Compound.ONE_OF(
        {
            0: ("protocol18-remote-server",),
            1: ("error-report",),
            2: ("error-report", "error-report"),
        }
    ),
    "protocol18-fetch-query": (
        "protocol16-fetch-query",
        "fetch-branch-depth-parameters",
        "boolean",
    ),
    "protocol18-list-remote-servers-result": Compound.N_OF("protocol18-remote-server"),
    "protocol18-log-entries-fetch-response": (
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.Int64,
        encoded_data.String,
        encoded_data.Int64,
    ),
    "protocol18-remote-server": (
        "remote-server-name",
        "remote-server-url",
        "principal",
        "remote-server-connection-options",
    ),
    "protocol18-remote-server-definition": ("protocol18-remote-server", "credentials"),
    "protocol18-security-configuration": (
        "role-set",
        "role-set",
        Compound.N_OF("protocol17-role"),
        "path-set",
    ),
    "protocol18-system-authentication-configuration": (
        Compound.N_OF("protocol17-system-principal"),
        "anonymous-connection-action",
        "role-set",
        Compound.MAP_OF(encoded_data.String, "session-property-validation"),
    ),
    "protocol20-jmx-fetch-request": (Compound.N_OF(encoded_data.String), "boolean"),
    "protocol20-jmx-fetch-response": Compound.MAP_OF(
        encoded_data.String, Compound.ONE_OF({0: ("i-bytes",), 1: ("error-reason",)})
    ),
    "protocol21-measured-entity-class-request": (
        encoded_data.String,
        {0: (), 1: "string"},
    ),
    "protocol22-path-permission": encoded_data.Byte,
    "protocol22-path-permission-set": Compound.SET_OF("protocol22-path-permission"),
    "protocol22-role": (
        "role-name",
        "protocol16-global-permission-set",
        "protocol22-path-permission-set",
        Compound.MAP_OF("path", "protocol22-path-permission-set"),
        "role-set",
        {0: (), 1: "string"},
    ),
    "protocol22-security-configuration": (
        "role-set",
        "role-set",
        Compound.N_OF("protocol22-role"),
        "path-set",
    ),
    "protocol22-unsubscription-notification": ("topic-id", encoded_data.Byte),
    "protocol23-create-remote-server-result": Compound.ONE_OF(
        {
            0: ("protocol23-remote-server",),
            1: ("error-report",),
            2: ("error-report", "error-report"),
        }
    ),
    "protocol23-list-remote-servers-result": Compound.N_OF("protocol23-remote-server"),
    "protocol23-missing-topic-request": (
        "topic-selector",
        "session-properties",
        "server-names",
        "conversation-id",
    ),
    "protocol23-remote-server": (
        "remote-server-name",
        "remote-server-url",
        "principal",
        "remote-server-connection-options",
        "topic-selector",
    ),
    "protocol23-remote-server-definition": ("protocol23-remote-server", "credentials"),
    "protocol24-gateway-response": Compound.ONE_OF(
        {
            1: ("gateway-configuration",),
            2: ("gateway-status",),
            3: ("gateway-operations",),
            4: ("gateway-operation-detail",),
            5: ({0: (), 1: "gateway-operation-output"},),
            6: ("gateway-service-detail",),
            7: ("gateway-service-detail",),
            8: (),
            9: (Compound.N_OF("gateway-service-detail"),),
            10: (Compound.N_OF("protocol24-gateway-service-type"),),
            11: ("gateway-configuration",),
            12: ("gateway-status",),
            13: ("gateway-operations",),
            14: ("gateway-operation-detail",),
            15: ({0: (), 1: "gateway-operation-output"},),
        }
    ),
    "protocol24-gateway-service-type": (
        "gateway-service-type-name",
        "gateway-service-type-description",
        "gateway-service-type-schema",
        "boolean",
    ),
    "protocol24-topic-metric-collector": (
        "metric-collector-name",
        "exports-to-prometheus",
        "maximum-groups",
        "topic-selector",
        "groups-by-topic-type",
        "group-by-path-prefix-parts"
    ),
    "protocol24-topic-metric-collectors": Compound.N_OF(
        "protocol24-topic-metric-collector"
    ),
    "protocol25-create-remote-server-result": Compound.ONE_OF(
        {
            0: ("protocol25-remote-server",),
            1: ("error-report",),
            2: ("error-report", "error-report"),
        }
    ),
    "protocol25-list-remote-servers-result": Compound.N_OF("protocol25-remote-server"),
    "protocol25-remote-server": (
        "remote-server-type",
        "remote-server-name",
        Compound.N_OF("remote-server-url"),
        "principal",
        "remote-server-connection-options",
        "topic-selector",
        "remote-server-connector",
    ),
    "protocol25-remote-server-definition": ("protocol25-remote-server", "credentials"),
    "protocol4-system-authentication-configuration": (
        Compound.N_OF("protocol4-system-principal"),
        "anonymous-connection-action",
        "role-set",
    ),
    "protocol4-system-principal": ("string", "role-set"),
    "protocol5-close-client-request": ("session-id", encoded_data.String),
    "protocol5-unsubscription-notification": ("topic-id", encoded_data.Byte),
    "protocol9-unsubscription-notification": ("topic-id", encoded_data.Byte),
    "queue-event": encoded_data.Byte,
    "queue-event-request": (
        "queue-event",
        "session-id",
        "message-queue-policy",
        "conversation-id",
    ),
    "removes-metrics-with-no-matches": "boolean",
    "range-query-anchor": (encoded_data.Int64, encoded_data.Byte),
    "range-query-edit-event": (
        "rq-time-series-event-metadata",
        "range-query-original-event",
    ),
    "range-query-event-data": Compound.ONE_OF(
        {
            0: ("range-query-original-event",),
            1: ("range-query-edit-event",),
            2: ("range-query-metadata-offsets",),
            3: ("range-query-author-encoding",),
        }
    ),
    "range-query-metadata-offsets": ("time-series-sequence", "timestamp"),
    "author-code": "bytes",
    "range-query-author-encoding": ("author-code", "author"),
    "rq-time-series-event-metadata": (
        "time-series-sequence",
        "timestamp",
        "author-code",
    ),
    "range-query-original-event": ("rq-time-series-event-metadata", "value"),
    "edit-event": (
        "time-series-event-metadata",
        "original-event",
    ),
    "original-event": ("time-series-event-metadata", "value"),
    "range-query-parameters": ("range-query-type", "view-range", "edit-range", "limit"),
    "limit": encoded_data.Int64,
    "edit-range": "range-query-range",
    "view-range": "range-query-range",
    "range-query-range": ("range-query-anchor", "range-query-span"),
    "range-query-request": ("path", "range-query-parameters"),
    "selected-count": encoded_data.Int64,
    "range-query-result": (
        "data-type-name",
        "selected-count",
        "selected-events",
    ),
    "selected-events": Compound.N_OF("range-query-event-data"),
    "range-query-span": (encoded_data.Int64, encoded_data.Byte),
    "range-query-type": encoded_data.Byte,
    "reason-code": encoded_data.Int32,
    "register-global-scope-handler": encoded_data.String,
    "register-path-scope-handler": (encoded_data.String, encoded_data.String),
    "registration-path": encoded_data.String,
    "remote-server-connection-options": Compound.MAP_OF(
        encoded_data.Byte, encoded_data.String
    ),
    "remote-server-connection-state": encoded_data.Byte,
    "remote-server-connector": encoded_data.String,
    "remote-server-name": encoded_data.String,
    "remote-server-type": encoded_data.Byte,
    "remote-server-url": encoded_data.String,
    "remove-owned-topics-request": ("authenticated-principal", "topic-selector"),
    "remove-serialised": ("generation-id", "update-id", "serialised-key"),
    "remove-topic-persistence-record": ("persistence-origin", "persistence-topic-key"),
    "remove-topics-request": "topic-selector",
    "replace-licence-response": encoded_data.Byte,
    "replicate-session": "session-data",
    "role-name": encoded_data.String,
    "role-set": Compound.SET_OF(encoded_data.String),
    "routing-subscription-control-request": (
        "conversation-id",
        "conversation-id",
        "session-id",
        encoded_data.String,
    ),
    "routing-subscription-response": ("conversation-id", encoded_data.String),
    "secondary-acceptor-registration": (encoded_data.String, encoded_data.String),
    "security-command-script": encoded_data.String,
    "security-command-script-result": "error-report-list",
    "serialised-key": ("serialised-key-type", encoded_data.String),
    "serialised-key-type": encoded_data.Byte,
    "serialised-object": ("serialised-key", encoded_data.String, "bytes"),
    "serialised-objects": Compound.N_OF("serialised-object"),
    "serialised-value": ("data-type-name", "bytes"),
    "server-ids": Compound.N_OF(encoded_data.Int64),
    "server-metrics": Compound.MAP_OF(
        "measured-entity-class-name", Compound.MAP_OF("metric-name", "metric-value")
    ),
    "server-name": encoded_data.String,
    "server-names": Compound.N_OF("server-name"),
    "server-peer-session-info": ("password-hash", "server-uuid"),
    "server-uuid": encoded_data.String,
    "service-id": encoded_data.Int32,
    "session-data": ("client-info", "server-uuid", "topic-selections"),
    "session-description": (
        encoded_data.String,
        "role-set",
        "client-type",
        "protocol-version",
        "internal-session-id",
    ),
    "session-fetch-info": ({0: (), 1: "session-start-time"}, "session-properties"),
    "session-fetch-query": (
        "session-filter",
        {0: (), 1: "session-property-keys"},
        {0: (), 1: "time-millis"},
        {0: (), 1: "time-millis"},
        {0: (), 1: "fetch-limit"},
        "fetch-maximum-result-size",
        "boolean",
    ),
    "session-fetch-query-result": Compound.ONE_OF(
        {
            0: (Compound.N_OF("session-fetch-info"), "total-selected"),
            1: (Compound.N_OF("error-report"),),
        }
    ),
    "session-filter": encoded_data.String,
    "session-id": (encoded_data.Int64, encoded_data.Int64),
    "session-lock-acquisition": (
        "session-lock-name",
        "session-lock-sequence",
        "session-lock-scope",
    ),
    "session-lock-name": encoded_data.String,
    "session-lock-owner": encoded_data.String,
    "session-lock-request": (
        "session-lock-name",
        "session-lock-request-id",
        "session-lock-scope",
    ),
    "session-lock-request-cancellation": (
        "session-lock-name",
        "session-lock-request-id",
    ),
    "session-lock-request-id": encoded_data.Int64,
    "session-lock-scope": encoded_data.Byte,
    "session-lock-sequence": encoded_data.Int64,
    "session-metric-collector": (
        "metric-collector-name",
        "exports-to-prometheus",
        "maximum-groups",
        "removes-metrics-with-no-matches",
        "session-filter",
        "session-property-keys",
    ),
    "session-metric-collectors": Compound.N_OF("session-metric-collector"),
    "session-properties": Compound.MAP_OF(encoded_data.String, encoded_data.String),
    "session-properties-change": (
        encoded_data.String,
        Compound.ONE_OF(
            {
                1: (encoded_data.String,),
                2: (encoded_data.String, encoded_data.String),
                3: (encoded_data.String,),
                4: (encoded_data.String,),
            }
        ),
    ),
    "session-properties-changes": Compound.N_OF("session-properties-change"),
    "session-properties-event": (
        "conversation-id",
        "protocol15-session-properties-event-core",
    ),
    "session-properties-listener-registration-request": (
        Compound.ONE_OF({0: ("session-property-keys",), 1: ()}),
        "conversation-id",
    ),
    "session-properties-update-type": encoded_data.Byte,
    "session-property-keys": Compound.SET_OF(encoded_data.String),
    "session-property-validation": Compound.ONE_OF(
        {0: (encoded_data.String,), 1: (Compound.N_OF(encoded_data.String),)}
    ),
    "session-start-time": encoded_data.Int64,
    "session-token": encoded_data.Bytes,
    "session-tree-branch-list": Compound.N_OF("path"),
    "sessions-container": Compound.MAP_OF(encoded_data.String, "sessions-slice"),
    "sessions-slice": Compound.N_OF("session-data"),
    "set-client-queue-conflation-filter-request": ("session-filter", "boolean"),
    "set-client-queue-conflation-request": ("session-id", "boolean"),
    "set-session-properties-filter-request": (
        "session-filter",
        {0: (), 1: "session-properties"},
        {0: (), 1: "session-property-keys"},
    ),
    "set-session-properties-request": (
        "session-id",
        {0: (), 1: "session-properties"},
        {0: (), 1: "session-property-keys"},
    ),
    "set-session-properties-result": (
        {0: (), 1: "session-properties"},
        {0: (), 1: "session-property-keys"},
    ),
    "set-topic-details-level-request": encoded_data.Byte,
    "set-topic-request": (
        "topic-path",
        "protocol14-topic-type",
        "bytes",
        "update-constraint",
    ),
    "string": encoded_data.String,
    "string-set-hierarchy-index-wrapper": Compound.MAP_OF(
        encoded_data.String, Compound.SET_OF(encoded_data.String)
    ),
    "subscription-request": ("session-id", "topic-selector"),
    "throttler-type": encoded_data.Byte,
    "throttling-limit": encoded_data.Int32,
    "time-millis": encoded_data.Int64,
    "time-series-append-request": ("path", "data-type-name", "value"),
    "time-series-edit-request": (
        "path",
        "data-type-name",
        "time-series-sequence",
        "value",
    ),
    "time-series-event-metadata": (
        "time-series-sequence",
        "timestamp",
        "author"
    ),
    "timestamp": encoded_data.Int64,
    "author": encoded_data.String,
    "time-series-sequence": encoded_data.Int64,
    "time-series-timestamp-append-request": (
        "time-series-append-request",
        "timestamp"
    ),
    "time-series-update-response": "time-series-event-metadata",
    "topic-control-registration-parameters": ("service-id", "control-group", "path"),
    "topic-control-registration-request": (
        "topic-control-registration-parameters",
        "conversation-id",
    ),
    "topic-descendant-event": ("conversation-id", "path", encoded_data.Byte),
    "topic-id": encoded_data.Int32,
    "topic-notification-selection": ("conversation-id", "topic-selector"),
    "topic-path": encoded_data.String,
    "topic-properties": Compound.MAP_OF("topic-property-key", encoded_data.String),
    "topic-property-key": encoded_data.String,
    "topic-removal-cluster-state-request": "path",
    "topic-removal-criteria-satisfied": "boolean",
    "topic-removal-state-change-event": (
        "topic-id",
        "topic-removal-criteria-satisfied",
    ),
    "topic-removal-state-request": "topic-id",
    "topic-removal-state-response": (
        "topic-removal-criteria-satisfied",
        "topic-removal-subscription-count",
    ),
    "topic-removal-subscription-count": encoded_data.Int32,
    "topic-removed": encoded_data.Int32,
    "topic-selection-event": ("topic-selector", "topic-selection-type"),
    "topic-selection-type": encoded_data.Byte,
    "topic-selections": Compound.MAP_OF("topic-selector", "topic-selection-type"),
    "topic-selector": encoded_data.String,
    "topic-specification-persistence-record": (
        "persistence-origin",
        "persistence-specification-key",
        "protocol14-topic-specification",
    ),
    "topic-type-set": encoded_data.Int64,
    "topic-view": ("topic-view-name", "topic-view-specification", "role-set"),
    "topic-view-name": encoded_data.String,
    "topic-view-specification": encoded_data.String,
    "total-selected": encoded_data.Int32,
    "try-get-owned-partition-records": encoded_data.Int32,
    "try-get-owned-serialised-objects": encoded_data.Int32,
    "unconstrained-constraint": (),
    "unsubscribe-request": "topic-selector",
    "update-assigned-roles": "role-set",
    "update-client-info": "client-info",
    "update-constraint": Compound.ONE_OF(
        {
            0: ("unconstrained-constraint",),
            1: ("conjunction-constraint",),
            2: ("binary-value-constraint",),
            3: ("no-value-constraint",),
            4: ("locked-constraint",),
            5: ("no-topic-constraint",),
            6: ("partial-json-constraint",),
        }
    ),
    "update-id": encoded_data.Int32,
    "update-stream-add-topic-request": (
        "path",
        "protocol14-topic-specification",
        "update-constraint",
    ),
    "update-stream-id": (
        encoded_data.Int32,
        encoded_data.Int32,
        "update-stream-partition-and-generation",
    ),
    "update-stream-partition-and-generation": Compound.ONE_OF(
        {0: (encoded_data.Int32,), 1: ("generation-id",), 127: ("generation-id",)}
    ),
    "update-stream-request": ("update-stream-id", "bytes"),
    "update-topic-persistence-record": (
        "persistence-origin",
        "persistence-topic-key",
        encoded_data.Byte,
        encoded_data.Bytes,
    ),
    "update-type": encoded_data.Byte,
    "value": encoded_data.Bytes,
    "void": None,
}
