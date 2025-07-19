import re

from returns.result import Failure, Result, Success


def extract_input_value(input_name: str, html: str) -> Result[str, Exception]:
    match = re.search(rf"<input.+id=\"{input_name}\".+value=\"(.+)\"", html)
    if match:
        return Success(match.group(1))
    return Failure(ValueError("Token not found"))
