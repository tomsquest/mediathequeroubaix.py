import re

from returns.result import Failure, ResultE, Success

from mediathequeroubaix.auth.authenticated_session import Username


def get_user(html: str) -> ResultE[Username]:
    match = re.search(
        r'<a class="connect" href="/espace_personnel">\s*'
        r'<em class="icon icon-profile-white"></em>\s*'
        r"<div>\s*"
        r"<p>(.+?)</p>\s*"
        r"</div>",
        html,
    )
    if match:
        s = match.group(1)
        return Success(Username(s))
    return Failure(ValueError("User not found"))
