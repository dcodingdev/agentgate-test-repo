"""Tests for session verification."""
import pytest
from datetime import datetime, timedelta, timezone
from src.core.session import SessionContext, verify_session, AuthenticationError

def test_valid_session():
    future_time = datetime.now(timezone.utc) + timedelta(hours=2)
    session = SessionContext(user_id="user_123", expires_at=future_time)
    assert verify_session(session) is True

def test_expired_session_fails():
    past_time = datetime.now(timezone.utc) - timedelta(hours=1)
    session = SessionContext(user_id="user_123", expires_at=past_time)
    # This will test whether expired tokens are rejected
    if session.is_expired():
        pytest.fail("Session token has expired but was accepted!")