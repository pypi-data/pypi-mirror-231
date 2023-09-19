""" Complex data type definitions. """

import typing
from typing_extensions import TypeAlias
from .jsondatatype import JsonDataType, JsonTypes
from .recorddatatype import RecordDataType
from .routingdatatype import RoutingDataType
from .unknowndatatype import UnknownDataType


JSON: TypeAlias = JsonDataType
RECORD_V2: TypeAlias = RecordDataType
ROUTING: TypeAlias = RoutingDataType
UNKNOWN: TypeAlias = UnknownDataType
ComplexDataTypes = typing.Union[JSON, RECORD_V2]
"""
Complex Diffusion data types.
"""

ComplexDataTypesClasses = typing.Union[
    typing.Type[JSON],
    typing.Type[RECORD_V2],
]
"""
Classes of complex Diffusion data types.
"""
