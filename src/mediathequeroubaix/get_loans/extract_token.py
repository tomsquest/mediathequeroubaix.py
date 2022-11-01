import re

from returns.result import Failure, Result, Success


def extract_token(s: str) -> Result[str, Exception]:
    match = re.search(r"<input.+id=\"my_issues\".+value=\"(.+)\"", s)
    if match:
        return Success(match.group(1))
    return Failure(ValueError("Token not found"))
