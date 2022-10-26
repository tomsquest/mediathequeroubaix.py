from returns.result import Success

from mediathequeroubaix.login.get_user import get_user


def test_ok() -> None:
    html = """
        <input type="hidden" id="userDisplayName" value="foo bar">
    """

    assert get_user(html) == Success("foo bar")


def test_empty_html() -> None:
    html = ""

    assert str(get_user(html)) == "<Failure: User not found>"


def test_empty_token() -> None:
    html = """
        <input type="hidden" id="userDisplayName" value="">
    """

    assert str(get_user(html)) == "<Failure: User not found>"
