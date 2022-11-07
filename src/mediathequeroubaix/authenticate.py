import requests
from returns.io import IOResultE

from mediathequeroubaix.login.authenticated_session import AuthenticatedSession
from mediathequeroubaix.login.login import login


def authenticate(username: str, password: str) -> IOResultE[AuthenticatedSession]:
    session = requests.Session()
    return login(session, username, password)
