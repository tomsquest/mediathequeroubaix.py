from returns.pipeline import is_successful
from returns.result import Success

from mediathequeroubaix.get_loans.loan import Loan
from mediathequeroubaix.get_loans.parse_loans import parse_loans


def test_empty() -> None:
    assert is_successful(parse_loans("")) is False


def test_object() -> None:
    assert is_successful(parse_loans("{}")) is False


def test_empty_array() -> None:
    assert parse_loans("[]") == Success([])


def test_someloans() -> None:
    assert parse_loans(
        '[{"reasons_not_renewable": "too_many", "biblionumber": 298309, "issuedate": "2022-10-08T14:30:14", '
        '"barcode": "C2500002968", "branchcode": "MED", "itemcallnumber": "E BD/LEG", "date_due": "2022-11-19T23:59:00", "holdingbranch": "M\u00e9diath\u00e8que", "renewable": false, "borrowernumber": 48742, "title": "L\'\u00e9preuve d\'Had\u00e8s", "itemnumber": 360556}, '
        '{"barcode": "C2100005871", "biblionumber": 287420, "issuedate": "2020-01-02T03:04:05", "itemcallnumber": '
        'null, "date_due": "2020-01-02T03:04:06", "branchcode": "MED", "itemnumber": 341991, "holdingbranch": "M\u00e9diath\u00e8que", "renewable": true, "borrowernumber": 48742, "title": "Le secret d\'H\u00e9racl\u00e8s"}]'
    ) == Success(
        [
            Loan(
                title="L'épreuve d'Hadès",
                barcode="C2500002968",
                issuedate="2022-10-08T14:30:14",
                date_due="2022-11-19T23:59:00",
                itemcallnumber="E BD/LEG",
                itemnumber=360556,
                renewable=False,
                reasons_not_renewable="too_many",
            ),
            Loan(
                title="Le secret d'Héraclès",
                barcode="C2100005871",
                issuedate="2020-01-02T03:04:05",
                date_due="2020-01-02T03:04:06",
                itemcallnumber=None,
                itemnumber=341991,
                renewable=True,
            ),
        ]
    )
