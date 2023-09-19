from diffusion.internal.serialisers.pydantic import MarshalledModel
from diffusion.session import SessionLockScope


class SessionLockRequest(MarshalledModel):
    """
    The request to acquire a session lock.
    """

    lock_name: str
    request_id: int
    scope: SessionLockScope

    def __str__(self):
        return f"{type(self).__name__}[{self.lock_name}, {self.request_id}, {self.scope}]"

    class Config(MarshalledModel.Config):
        alias_generator = None

        @classmethod
        def attr_mappings_all(cls, modelcls):
            return {
                "session-lock-request": {
                    "session-lock-name": "lock_name",
                    "session-lock-request-id": "request_id",
                    "session-lock-scope": "scope",
                }
            }
