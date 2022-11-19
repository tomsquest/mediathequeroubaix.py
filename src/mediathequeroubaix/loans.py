import typer
from returns.io import IOFailure, IOSuccess, impure_safe
from returns.pipeline import flow
from returns.pointfree import bind_ioresult, bind_result
from returns.result import Failure, ResultE, Success
from rich import box, print
from rich.table import Table

from mediathequeroubaix.auth.authenticate import authenticate
from mediathequeroubaix.config import Config, User, get_config
from mediathequeroubaix.get_loans.get_loans import get_loans
from mediathequeroubaix.get_loans.loan import Loans

app = typer.Typer()


@app.command(name="list")
def list_loans() -> None:
    loans = flow(
        get_config(),
        bind_result(_get_first_user),
        bind_ioresult(_print_user),
        bind_ioresult(authenticate),
        bind_ioresult(get_loans),
    )

    match loans:
        case IOSuccess(Success(loans)):
            _pretty_print(loans)
        case IOFailure(failure):
            print("❌ FAILURE!", failure)


def _get_first_user(config: Config) -> ResultE[User]:
    if config.users:
        # We only support having one user
        first_user = config.users[0]
        return Success(first_user)
    return Failure(ValueError("No user defined in configuration"))


@impure_safe
def _print_user(user: User) -> User:
    print(f"Getting loans of {user.login}")
    return user


def _pretty_print(loans: Loans) -> None:
    table = Table(
        title=f"{loans.username}: {len(loans.items)} loans",
        title_style="bold magenta",
        box=box.HEAVY_EDGE,
        expand=True,
    )
    table.add_column("#", justify="center")
    table.add_column("Title", style="blue", ratio=2)
    table.add_column("Due date", justify="center")
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
