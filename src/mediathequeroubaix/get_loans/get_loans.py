from requests import Session
from returns.io import IOResultE, impure_safe
from returns.pipeline import flow
from returns.pointfree import bind_result

from mediathequeroubaix.get_loans.base64decode import base64decode
from mediathequeroubaix.get_loans.extract_token import extract_token
from mediathequeroubaix.get_loans.loan import Loan
from mediathequeroubaix.get_loans.parse_loans import parse_loans


def get_loans(session: Session) -> IOResultE[list[Loan]]:
    return flow(
        session,
        get_personal_space,
        bind_result(extract_token),
        bind_result(base64decode),
        bind_result(parse_loans),
    )


@impure_safe
def get_personal_space(session: Session) -> str:
    response = session.get("http://www.mediathequederoubaix.fr/espace_personnel")
    response.raise_for_status()
    return response.text