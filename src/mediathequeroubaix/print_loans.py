from requests import Session
from returns.io import IOFailure, IOSuccess
from returns.result import Success

from mediathequeroubaix.get_loans.get_loans import get_loans
from mediathequeroubaix.get_loans.loan import Loan


def print_loans(*, session: Session) -> None:
    match get_loans(session):
        case IOSuccess(Success(loans)):
            _print(loans)
        case IOFailure(failure):
            print("❌ FAILURE!", failure)


def _print(loans: list[Loan]) -> None:
    total = len(loans)
    print(f"Number of loans: {total}")
    for index, loan in enumerate(loans):
        renewable = "renewable" if loan.renewable else "NOT renewable"
        print(
            f"- [{index+1:>2}/{total}] {loan.title}, due on: {loan.date_due}, {renewable}"
        )
