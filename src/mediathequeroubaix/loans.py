import typer
from returns.io import IOFailure, IOResultE, IOSuccess
from returns.pipeline import flow
from returns.pointfree import bind_ioresult
from returns.result import Success
from rich import box, print
from rich.table import Table

from mediathequeroubaix.auth.authenticate import authenticate
from mediathequeroubaix.config import User, get_config
from mediathequeroubaix.get_loans.get_loans import get_loans
from mediathequeroubaix.get_loans.loan import Loans

app = typer.Typer()


@app.command(name="list")
def list_loans() -> None:
    match get_config():
        case IOSuccess(Success(config)):
            if not config.users:
                print("❌ No user defined in configuration")
                raise typer.Exit(1)

            for user in config.users:
                print(f"Getting loans of user '{user.login}'")
                match _get_user_loans(user):
                    case IOSuccess(Success(loans)):
                        _pretty_print(loans)
                    case IOFailure(failure):
                        print(f"❌ Unable to get loans of user '{user.login}'", failure)
        case IOFailure(failure):
            print("❌ Unable to read configuration!", failure)
            raise typer.Exit(1)


def _get_user_loans(user: User) -> IOResultE[Loans]:
    return flow(
        user,
        authenticate,
        bind_ioresult(get_loans),
    )


def _pretty_print(loans: Loans) -> None:
    table = Table(
        title=f"{loans.username}: {len(loans.items)} loans",
        title_style="bold magenta",
        box=box.HEAVY_EDGE,
        expand=True,
        show_footer=True,
    )

    if not loans.items:
        print(f"No loans for user {loans.username}...")
    else:
        soonest_due_loan = min(loans.items, key=lambda l: l.date_due)

        table.add_column("#", justify="center")
        table.add_column("Title", style="blue", ratio=2)
        table.add_column(
            "Due date", justify="center", footer=f"{soonest_due_loan.date_due:%d/%m/%Y}"
        )
        table.add_column("Renewable", justify="center")

        for index, loan in enumerate(loans.items):
            renewable = "✅" if loan.renewable else "❌"
            table.add_row(
                f"{index+1:>2}/{len(loans.items)}",
                loan.title,
                f"{loan.date_due:%d/%m/%Y}",
                renewable,
            )

        print(table)
