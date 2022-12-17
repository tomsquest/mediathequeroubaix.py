import requests
from requests_mock import mock
from returns.pipeline import is_successful

from mediathequeroubaix.auth.authenticated_session import AuthenticatedSession, Username
from mediathequeroubaix.get_loans.loan import Loan, Loans
from mediathequeroubaix.renew.renew import renew


def test_ok(requests_mock: mock) -> None:
    loans = [
        Loan(
            title="1",
            barcode="",
            issuedate="2020-01-01T00:00:00",
            date_due="2020-01-01T00:00:00",
            itemcallnumber="",
            itemnumber=1,
            renewable=False,
            reasons_not_renewable="too_many",
        ),
        Loan(
            title="2",
            barcode="",
            issuedate="2020-01-01T00:00:00",
            date_due="2020-01-01T00:00:00",
            itemcallnumber="",
            itemnumber=2,
            renewable=True,
        ),
        Loan(
            title="3",
            barcode="",
            issuedate="2020-01-01T00:00:00",
            date_due="2020-01-01T00:00:00",
            itemcallnumber="",
            itemnumber=3,
            renewable=True,
        ),
    ]
    requests_mock.post(
        "http://www.mediathequederoubaix.fr/espace_personnel",
        text="item_renew[]=2&item_renew[]=3&submit_renew=",
    )

    result = renew(
        AuthenticatedSession(requests.Session(), Username("John Doe")),
        Loans(
            username=Username("John Doe"),
            items=loans,
        ),
    )

    assert is_successful(result)


def test_no_renewable() -> None:
    loans = [
        Loan(
            title="1",
            barcode="",
            issuedate="2020-01-01T00:00:00",
            date_due="2020-01-01T00:00:00",
            itemcallnumber="",
            itemnumber=1,
            renewable=False,
            reasons_not_renewable="too_many",
        ),
    ]

    result = renew(
        AuthenticatedSession(requests.Session(), Username("John Doe")),
        Loans(
            username=Username("John Doe"),
            items=loans,
        ),
    )

    assert is_successful(result)
