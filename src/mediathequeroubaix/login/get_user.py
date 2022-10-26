import re

from returns.result import Failure, ResultE, Success


def get_user(html: str) -> ResultE[str]:
    match = re.search(
        r"<input type=\"hidden\" id=\"userDisplayName\" value=\"(.+)\"", html
    )
    if match:
        return Success(match.group(1))
    return Failure(ValueError("User not found"))
