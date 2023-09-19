#  Copyright (c) 2022 - 2023 DiffusionData Ltd., All Rights Reserved.
#
#  Use is subject to licence terms.
#
#  NOTICE: All information contained herein is, and remains the
#  property of DiffusionData. The intellectual and technical
#  concepts contained herein are proprietary to DiffusionData and
#  may be covered by U.S. and Foreign Patents, patents in process, and
#  are protected by trade secret or copyright law.

from __future__ import annotations
import typing

import diffusion

if typing.TYPE_CHECKING:
    from diffusion import Credentials, Session
    from diffusion.session.session_factory import SessionProperties


class SessionContainerFactory(object):
    async def start_session(
        self,
        url,
        *,
        principal: str = None,
        credentials: Credentials = None,
        session_properties: SessionProperties = None,
    ) -> Session:
        session = diffusion.Session(
            url=url,
            principal=principal,
            credentials=credentials,
            properties=session_properties,
        )
        try:
            await session.connect()
        except Exception as e:
            await session.close()
            raise e
        return session
