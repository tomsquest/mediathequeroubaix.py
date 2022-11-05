from requests import Session
from returns.io import IOFailure, IOSuccess
from returns.result import Success

from mediathequeroubaix.login.login import login


def authenticate(*, session: Session, username: str, password: str) -> None:
    match login(session, username, password):
        case IOSuccess(Success(authenticated_session)):
            print(f"User: {authenticated_session.user}")
        case IOFailure(failure):
            print("❌ FAILURE!", failure)
