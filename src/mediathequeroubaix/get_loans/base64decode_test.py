from returns.result import Success

from mediathequeroubaix.get_loans.base64decode import base64decode


def test_ok() -> None:
    assert base64decode("YWJj") == Success("abc")


def test_empty() -> None:
    assert base64decode("") == Success("")


def test_invalid() -> None:
    assert str(base64decode("[]{}")) == "<Failure: Non-base64 digit found>"
