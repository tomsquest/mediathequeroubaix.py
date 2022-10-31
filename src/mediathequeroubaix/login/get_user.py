import re

from returns.result import Failure, ResultE, Success


def get_user(html: str) -> ResultE[str]:
    match = re.search(
        r'<a class="connect" href="/espace_personnel">\s*'
        r'<em class="icon icon-profile-white"></em>\s*'
        r"<div>\s*"
        r"<p>(.+?)</p>\s*"
        r"</div>",
        html,
    )
    if match:
        return Success(match.group(1))
    return Failure(ValueError("User not found"))
