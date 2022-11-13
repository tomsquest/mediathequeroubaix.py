import typer
from returns.io import IOFailure, IOSuccess
from returns.result import Success
from rich import box, print
from rich.table import Table

from mediathequeroubaix.authenticate import authenticate
from mediathequeroubaix.config import get_config
from mediathequeroubaix.get_loans.get_loans import get_loans
from mediathequeroubaix.get_loans.loan import Loan
from mediathequeroubaix.login.authenticated_session import AuthenticatedSession, User

app = typer.Typer()


@app.command(name="list")
def list_loans() -> None:
    config = get_config()

    if not config.users:
        print("No users in config file")
        raise typer.Exit(code=1)
    first_user = config.users[0]

    print(f"Getting loans of user: {first_user.login}")
    match authenticate(first_user.login, first_user.password):
        case IOSuccess(Success(authenticated_session)):
            print_loans(authenticated_session)
        case IOFailure(failure):
            print("❌ FAILURE!", failure)


def print_loans(session: AuthenticatedSession) -> None:
    match get_loans(session):
        case IOSuccess(Success(loans)):
            _print(session.user, loans)
        case IOFailure(failure):
            print("❌ FAILURE!", failure)


def _print(user: User, loans: list[Loan]) -> None:
    table = Table(
        title=f"{user}: {len(loans)} loans",
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
