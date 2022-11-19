from dataclasses import dataclass
from typing import NewType

from requests import Session

Username = NewType("Username", str)


@dataclass(frozen=True)
class AuthenticatedSession:
    session: Session
    username: Username
