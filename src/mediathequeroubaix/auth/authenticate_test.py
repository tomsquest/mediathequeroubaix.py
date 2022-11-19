from typing import Any

from requests_mock import mock
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.auth.authenticate import authenticate
from mediathequeroubaix.config import User


def match_user_pass(request: Any) -> bool:
    return "name=myuser&pass=mypass&form_id=user_login_block" in request.text


def test_ok(requests_mock: mock) -> None:
    requests_mock.post(
        "http://www.mediathequederoubaix.fr/user",
        additional_matcher=match_user_pass,
        text="""
            <a class="connect" href="/espace_personnel">
                <em class="icon icon-profile-white"></em>
                <div>
                    <p>John DOE</p>
                </div>
        """,
    )

    result = authenticate(User(login="myuser", password="mypass"))

    assert is_successful(result)
    actual = unsafe_perform_io(result.unwrap())
    assert actual.username == "John DOE"


def test_login_failure(requests_mock: mock) -> None:
    requests_mock.post("http://www.mediathequederoubaix.fr/user", text="some html")

    result = authenticate(User(login="myuser", password="mypass"))

    assert is_successful(result) is False
