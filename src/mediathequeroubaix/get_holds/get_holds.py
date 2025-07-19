from returns.io import IOResultE
from returns.pipeline import flow
from returns.pointfree import bind_result
from returns.result import safe

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession
from mediathequeroubaix.get_holds.extract_token import extract_token
from mediathequeroubaix.get_holds.hold import Holds
from mediathequeroubaix.get_holds.parse_holds import parse_holds
from mediathequeroubaix.shared.base64decode import base64decode
from mediathequeroubaix.shared.get_personal_space import get_personal_space


def get_holds(session: AuthenticatedSession) -> IOResultE[Holds]:
    return flow(
        session,
        get_personal_space,
        bind_result(extract_token),
        bind_result(base64decode),
        bind_result(parse_holds),
        bind_result(safe(lambda holds: Holds(username=session.username, items=holds))),
    )
