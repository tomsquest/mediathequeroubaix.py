from returns.io import impure_safe

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession


@impure_safe
def get_personal_space(session: AuthenticatedSession) -> str:
    response = session.session.get(
        "http://www.mediathequederoubaix.fr/espace_personnel"
    )
    response.raise_for_status()
    return response.text
