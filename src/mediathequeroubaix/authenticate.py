import requests
from returns.io import IOResultE

from mediathequeroubaix.config import User
from mediathequeroubaix.login.authenticated_session import AuthenticatedSession
from mediathequeroubaix.login.login import login


def authenticate(user: User) -> IOResultE[AuthenticatedSession]:
    session = requests.Session()
    return login(session, user.login, user.password)
