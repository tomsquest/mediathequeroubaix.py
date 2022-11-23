import requests
from requests import Response, Session
from returns.io import IOResultE, impure_safe
from returns.pipeline import flow
from returns.pointfree import bind_result
from returns.result import safe

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession
from mediathequeroubaix.auth.get_user import get_user
from mediathequeroubaix.config import User


def authenticate(user: User) -> IOResultE[AuthenticatedSession]:
    session = requests.Session()
    return flow(
        (session, user.login, user.password),
        _connect,
        bind_result(_get_html),
        bind_result(get_user),
        bind_result(safe(lambda user: AuthenticatedSession(session, user))),
    )


@impure_safe
def _connect(data: tuple[Session, str, str]) -> Response:
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
def _get_html(response: Response) -> str:
    return response.text
