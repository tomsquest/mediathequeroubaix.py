import datetime

from mediathequeroubaix.get_loans.loan import Loan


def test_convert_due_date_to_date() -> None:
    loan = Loan(
        title="L'épreuve d'Hadès",
        barcode="C2500002968",
        issuedate="2010-01-02T14:30:14",
        date_due="2023-04-05T23:59:00",
        itemcallnumber="E BD/LEG",
        itemnumber=1234567,
        renewable=False,
    )

    assert loan.date_due == datetime.date.fromisoformat("2023-04-05")
