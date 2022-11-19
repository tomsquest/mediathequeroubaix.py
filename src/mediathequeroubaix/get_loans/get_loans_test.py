import base64

import requests
from requests_mock import mock
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession, Username
from mediathequeroubaix.get_loans.get_loans import get_loans


def test_ok(requests_mock: mock) -> None:
    loans = base64.b64encode(
        '[{"issuedate": "2022-10-08T14:30:14", "barcode": "C2500002968", "itemcallnumber": "E BD/LEG", "date_due": "2022-11-19T23:59:00", "renewable": true, "title": "L\'\u00e9preuve d\'Had\u00e8s", "itemnumber": 360556}]'.encode()
    ).decode("utf-8")
    requests_mock.get(
        "http://www.mediathequederoubaix.fr/espace_personnel",
        text=f"""
        Welcome
        <input type="hidden" id="my_issues" value="{loans}" />
    """,
    )

    result = get_loans(AuthenticatedSession(requests.Session(), Username("John Doe")))

    assert is_successful(result)
    actual = unsafe_perform_io(result.unwrap())
    assert actual.username == "John Doe"
    assert len(actual.items) == 1
    assert actual.items[0].title == "L'épreuve d'Hadès"


def test_no_token(requests_mock: mock) -> None:
    requests_mock.get(
        "http://www.mediathequederoubaix.fr/espace_personnel", text="some html"
    )

    result = get_loans(AuthenticatedSession(requests.Session(), Username("John doe")))

    assert is_successful(result) is False
