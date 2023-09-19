#  Copyright (c) 2021 - 2023 DiffusionData Ltd., All Rights Reserved.
#
#  Use is subject to licence terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of DiffusionData. The intellectual and technical
#  concepts contained herein are proprietary to DiffusionData and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.
try:
    from typing import TypeAlias  # type: ignore
except ImportError:
    from typing_extensions import TypeAlias  # type: ignore

from diffusion import DiffusionError


class InvalidBranchMappingError(DiffusionError):
    """
    Exception indicating an invalid BranchMapping or
    BranchMappingTable.

    See Also: SessionTrees
    """


InvalidBranchMappingException: TypeAlias = InvalidBranchMappingError
