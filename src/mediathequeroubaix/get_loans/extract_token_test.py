from returns.result import Success

from mediathequeroubaix.get_loans.extract_token import extract_token


def test_ok() -> None:
    html = """
        <div class="panel-body">
            <input type="hidden" id="my_issues" value="abc" />
        </div>
    """

    assert extract_token(html) == Success("abc")


def test_empty_html() -> None:
    html = ""

    assert str(extract_token(html)) == "<Failure: Token not found>"


def test_empty_token() -> None:
    html = """
        <div class="panel-body">
            <input type="hidden" id="my_issues" value="" />
        </div>
    """

    assert str(extract_token(html)) == "<Failure: Token not found>"


def test_two_tokens() -> None:
    html = """
        <div class="panel-body">
            <input type="hidden" id="my_issues" value="first" />
            <input type="hidden" id="my_issues" value="another" />
        </div>
    """

    assert extract_token(html) == Success("first")


def test_contain_equal() -> None:
    html = """
        <div class="panel-body">
            <input type="hidden" id="my_issues" value="b64str=" />
        </div>
    """

    assert extract_token(html) == Success("b64str=")
