import typer
from returns.io import IOFailure, IOSuccess
from returns.iterables import Fold
from returns.pipeline import flow
from returns.pointfree import bind_ioresult
from returns.result import Success
from returns.unsafe import unsafe_perform_io
from rich import box, print
from rich.table import Table

from .auth.authenticate import authenticate
from .config import Config, User, get_config
from .get_loans.get_loans import get_loans
from .get_loans.loan import Loans
from .renew.renew import renew

app = typer.Typer()


@app.command(name="list")
def list_loans() -> None:
    config = _load_config_or_raise()
    users = _get_users_or_raise(config)
    for user in users:
        print(f"Getting loans of user '{user.login}'")

        loans = flow(user, authenticate, bind_ioresult(get_loans))
        match loans:
            case IOSuccess(Success(loans)):
                _print_loans(loans)
            case IOFailure(failure):
                print(f"❌ Unable to get loans of user '{user.login}'", failure)
                raise typer.Exit(1)


@app.command(name="renew")
def renew_loans() -> None:
    config = _load_config_or_raise()
    users = _get_users_or_raise(config)
    for user in users:
        print(f"Renewing loans of user '{user.login}'")

        auth = flow(user, authenticate)
        loans = flow(auth, bind_ioresult(get_loans))
        results = Fold.collect([auth, loans], IOSuccess(()))
        match results:
            case IOSuccess(Success(successes)):
                the_session, the_loans = successes
                renew(the_session, the_loans)
            case IOFailure(failure):
                print("❌ Failed to renew loans!", failure)
                raise typer.Exit(1)

        # After renew, print the loans with their new due date
        loans = flow(auth, bind_ioresult(get_loans))
        match loans:
            case IOSuccess(Success(loans)):
                _print_loans(loans)
            case IOFailure(failure):
                print(f"❌ Unable to get loans of user '{user.login}'", failure)
                raise typer.Exit(1)


def _load_config_or_raise() -> Config:
    try:
        result = get_config()
        io = result.unwrap()
        config = unsafe_perform_io(io)
    except Exception as e:
        print("❌ Unable to read configuration!", e)
        raise typer.Exit(1) from e
    else:
        return config


def _get_users_or_raise(config: Config) -> list[User]:
    if not config.users:
        print("❌ No user defined in configuration")
        raise typer.Exit(1)
    return config.users


def _print_loans(loans: Loans) -> None:
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
        table.add_column("Barcode")
        table.add_column("Call number")
        table.add_column("Title", style="blue", ratio=2)
        table.add_column(
            "Due date", justify="center", footer=f"{soonest_due_loan.date_due:%d/%m/%Y}"
        )
        table.add_column("Renewable", justify="center")

        for index, loan in enumerate(loans.items):
            renewable = "✅" if loan.renewable else "❌"
            table.add_row(
                f"{index + 1:>2}/{len(loans.items)}",
                loan.barcode,
                loan.itemcallnumber,
                loan.title,
                f"{loan.date_due:%d/%m/%Y}",
                renewable,
            )

        print(table)
