import base64

import requests
from requests_mock import mock
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.fetch_loans.fetch_loans import fetch_loans


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

    result = fetch_loans(session=requests.Session())

    assert is_successful(result)
    actual = unsafe_perform_io(result.unwrap())
    assert len(actual) == 1
    assert actual[0].title == "L'épreuve d'Hadès"


def test_no_token(requests_mock: mock) -> None:
    requests_mock.get(
        "http://www.mediathequederoubaix.fr/espace_personnel", text="some html"
    )

    result = fetch_loans(session=requests.Session())

    assert is_successful(result) is False
