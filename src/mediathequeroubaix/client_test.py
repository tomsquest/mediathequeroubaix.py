from mediathequeroubaix.client import auth


def test_auth() -> None:
    assert auth() == "ok"
