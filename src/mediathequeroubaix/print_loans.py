from requests import Session
from returns.pipeline import is_successful
from returns.unsafe import unsafe_perform_io

from mediathequeroubaix.fetch_loans.fetch_loans import fetch_loans
from mediathequeroubaix.fetch_loans.loan import Loan


def print_loans(*, session: Session) -> None:
    result = fetch_loans(session)
    if is_successful(result):
        success = result.unwrap()
        loans = unsafe_perform_io(success)
        _print(loans)
    else:
        failure = result.failure()
        print("❌ FAILURE!", failure)


def _print(loans: list[Loan]) -> None:
    total = len(loans)
    print(f"Number of loans: {total}")
    for index, loan in enumerate(loans):
        renewable = "renewable" if loan.renewable else "NOT renewable"
        print(
            f"- [{index+1:>2}/{total}] {loan.title}, due on: {loan.date_due}, {renewable}"
        )
