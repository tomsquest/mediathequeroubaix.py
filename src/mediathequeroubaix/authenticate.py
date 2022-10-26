from requests import Session
from returns.io import IO, IOResultE
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.login.do_login import do_login


def authenticate(*, session: Session, username: str, password: str) -> None:
    result: IOResultE[str] = do_login(session, username, password)
    if is_successful(result):
        success: IO[str] = result.unwrap()
        user = unsafe_perform_io(success)
        print(f"User: {user}")
    else:
        failure = result.failure()
        print("❌ FAILURE!", failure)
