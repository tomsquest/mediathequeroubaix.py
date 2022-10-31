from requests import Session
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.login.login import login


def authenticate(*, session: Session, username: str, password: str) -> None:
    result = login(session, username, password)
    if is_successful(result):
        success = result.unwrap()
        user = unsafe_perform_io(success)
        print(f"User: {user}")
    else:
        failure = result.failure()
        print("❌ FAILURE!", failure)
