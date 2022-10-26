from requests import Session
from returns.io import IOResultE, impure_safe
from returns.pipeline import flow
from returns.pointfree import bind_ioresult, bind_result

from mediathequeroubaix.login.get_user import get_user


def do_login(session: Session, username: str, password: str) -> IOResultE[str]:
    return flow(
        (session, username, password),
        log_in,
        bind_ioresult(get_espace_personnel),
        bind_result(get_user),
    )


@impure_safe
def log_in(data: tuple[Session, str, str]) -> Session:
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
    return session


@impure_safe
def get_espace_personnel(session: Session) -> str:
    response = session.get("http://www.mediathequederoubaix.fr/espace_personnel")
    response.raise_for_status()
    return response.text
