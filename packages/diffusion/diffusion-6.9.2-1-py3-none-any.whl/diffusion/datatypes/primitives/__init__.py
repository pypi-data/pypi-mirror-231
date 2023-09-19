import typing

from pydantic import StrictFloat, StrictInt, StrictStr, StrictBytes

from .doubledatatype import DoubleDataType
from .binarydatatype import BinaryDataType
from .int64datatype import Int64DataType
from .stringdatatype import StringDataType
from .primitivedatatype import PrimitiveDataType

try:
    from typing_extensions import TypeAlias  # type: ignore   # pragma: no cover
except ImportError:
    from typing import TypeAlias  # type: ignore  # pragma: no cover

# datatype aliases for convenience

BINARY: TypeAlias = BinaryDataType
DOUBLE: TypeAlias = DoubleDataType
INT64: TypeAlias = Int64DataType
STRING: TypeAlias = StringDataType

RawDataTypes = typing.Union[StrictFloat, StrictInt, StrictStr, StrictBytes]
"""
Raw data types that are used to populate Diffusion datatypes
"""

PrimitiveDataTypes = typing.Union[BINARY, DOUBLE, INT64, STRING]
"""
Primitive diffusion data types.
"""

PrimitiveDataTypesClasses = typing.Union[
    typing.Type[BINARY], typing.Type[DOUBLE], typing.Type[INT64], typing.Type[STRING]
]
"""
Classes of primitive Diffusion data types.
"""
