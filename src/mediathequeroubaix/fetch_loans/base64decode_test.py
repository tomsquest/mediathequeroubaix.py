from returns.result import Success

from mediathequeroubaix.fetch_loans.base64decode import base64decode


def test_ok() -> None:
    assert base64decode("YWJj") == Success("abc")


def test_invalid() -> None:
    assert str(base64decode("[]{}").failure()) == "Non-base64 digit found"


def test_empty() -> None:
    assert base64decode("") == Success("")
