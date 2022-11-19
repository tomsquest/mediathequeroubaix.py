from returns.result import Success

from mediathequeroubaix.auth.get_user import get_user


def test_ok() -> None:
    html = """
        <a class="connect" href="/espace_personnel">\r
            <em class="icon icon-profile-white"></em>\r
            <div>\r
                <p>John DOE</p>\r
            </div>\r
    """

    assert get_user(html) == Success("John DOE")


def test_some_html_around() -> None:
    html = """
        <div>
            <p>some stuff</p>
        </div>
        ...
        <a class="connect" href="/espace_personnel">
            <em class="icon icon-profile-white"></em>
            <div>
                <p>John DOE</p>
            </div>
            ...
            <div>
                <p>some other stuff</p>
            </div>
    """

    assert get_user(html) == Success("John DOE")


def test_empty_html() -> None:
    html = ""

    assert str(get_user(html)) == "<Failure: User not found>"


def test_empty_user() -> None:
    html = r"""
        <a class="connect" href="/espace_personnel">
            <em class="icon icon-profile-white"></em>
            <div>
                <p></p>
            </div>
    """

    assert str(get_user(html)) == "<Failure: User not found>"
