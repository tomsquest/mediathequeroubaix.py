from returns.io import IOFailure, IOResultE, IOSuccess
from returns.result import Success
from rich import box, print
from rich.table import Table

from mediathequeroubaix.get_loans.get_loans import get_loans
from mediathequeroubaix.get_loans.loan import Loan
from mediathequeroubaix.login.authenticated_session import AuthenticatedSession


def print_loans(session: IOResultE[AuthenticatedSession]) -> None:
    match get_loans(session):
        case IOSuccess(Success(loans)):
            _print(loans)
        case IOFailure(failure):
            print("❌ FAILURE!", failure)


def _print(loans: list[Loan]) -> None:
    table = Table(
        title=f"{len(loans)} LOANS",
        title_style="bold magenta",
        box=box.HEAVY_EDGE,
        expand=True,
    )
    table.add_column("#", justify="center")
    table.add_column("Title", style="blue", ratio=2)
    table.add_column("Due date", justify="center")
    table.add_column("Renewable")

    for index, loan in enumerate(loans):
        renewable = "✅" if loan.renewable else "❌"
        table.add_row(
            f"{index+1:>2}/{len(loans)}",
            loan.title,
            f"{loan.date_due:%d/%m/%Y}",
            renewable,
        )

    print(table)
