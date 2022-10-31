from requests import Response, Session
from returns.io import IOResultE, impure_safe
from returns.pipeline import flow
from returns.pointfree import bind_result
from returns.result import safe

from mediathequeroubaix.login.get_user import get_user


def login(session: Session, username: str, password: str) -> IOResultE[str]:
    return flow(
        (session, username, password),
        connect,
        bind_result(get_html),
        bind_result(get_user),
    )


@impure_safe
def connect(data: tuple[Session, str, str]) -> Response:
    session, username, password = data
    response = session.post(
        "http://www.mediathequederoubaix.fr/user",
        data={
            "name": username,
            "pass": password,
            "form_id": "user_login_block",
        },
    )
    response.raise_for_status()
    return response


@safe
def get_html(response: Response) -> str:
    return response.text
