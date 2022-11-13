from dataclasses import dataclass
from typing import NewType

from requests import Session

Username = NewType("Username", str)


@dataclass
class AuthenticatedSession:
    session: Session
    username: Username
