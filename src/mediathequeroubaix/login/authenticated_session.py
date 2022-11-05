from dataclasses import dataclass
from typing import NewType

from requests import Session

User = NewType("User", str)


@dataclass
class AuthenticatedSession:
    session: Session
    user: User
