"""Session token verification service."""
from datetime import datetime, timezone

class AuthenticationError(Exception):
    pass

class SessionContext:
    def __init__(self, user_id: str, expires_at: datetime):
        self.user_id = user_id
        self.expires_at = expires_at

    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.expires_at

def verify_session(session: SessionContext) -> bool:
    """Validate active session status."""
    if not session:
        raise AuthenticationError("Invalid session")
    if session.is_expired():
        raise AuthenticationError("Session token expired")
    return True
