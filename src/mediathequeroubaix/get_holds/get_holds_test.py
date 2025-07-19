import base64

import requests
from requests_mock import mock
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession, Username
from mediathequeroubaix.get_holds.get_holds import get_holds


def test_ok(requests_mock: mock) -> None:
    holds = base64.b64encode(
        '[{"hold_id":507643,"title":"Apprendre, si par bonheur","itemnumber":null,"barcode":"","found":null,"cancellationdate":null,"rank":2,"biblionumber":329375,"itemcallnumber":"","reservedate":"2025-07-14","branchcode":"MED","branchname":"M\u00e9diath\u00e8que"}]'.encode()
    ).decode("utf-8")
    requests_mock.get(
        "http://www.mediathequederoubaix.fr/espace_personnel",
        text=f"""
        Welcome
        <input type="hidden" id="my_holds" value="{holds}" />
    """,
    )

    result = get_holds(AuthenticatedSession(requests.Session(), Username("John Doe")))

    assert is_successful(result)
    actual = unsafe_perform_io(result.unwrap())
    assert actual.username == "John Doe"
    assert len(actual.items) == 1
    assert actual.items[0].title == "Apprendre, si par bonheur"


def test_no_token(requests_mock: mock) -> None:
    requests_mock.get(
        "http://www.mediathequederoubaix.fr/espace_personnel", text="some html"
    )

    result = get_holds(AuthenticatedSession(requests.Session(), Username("John doe")))

    assert is_successful(result) is False
