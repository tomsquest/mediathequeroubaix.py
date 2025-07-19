import typer
from returns.io import IOFailure, IOSuccess
from returns.pipeline import flow
from returns.pointfree import bind_ioresult
from returns.result import Success
from rich import box, print
from rich.table import Table

from .auth.authenticate import authenticate
from .cli_utils import _load_config_or_raise, _get_users_or_raise
from .get_holds.get_holds import get_holds
from .get_holds.hold import Holds

app = typer.Typer()


@app.command(name="list")
def list_holds() -> None:
    config = _load_config_or_raise()
    users = _get_users_or_raise(config)
    for user in users:
        print(f"Getting holds of user '{user.login}'")

        holds = flow(user, authenticate, bind_ioresult(get_holds))
        match holds:
            case IOSuccess(Success(holds)):
                _print_holds(holds)
            case IOFailure(failure):
                print(f"❌ Unable to get holds of user '{user.login}'", failure)
                raise typer.Exit(1)


def _print_holds(holds: Holds) -> None:
    table = Table(
        title=f"{holds.username}: {len(holds.items)} holds",
        title_style="bold magenta",
        box=box.HEAVY_EDGE,
        expand=True,
        show_footer=True,
    )

    if not holds.items:
        print(f"No holds for user {holds.username}...")
    else:
        table.add_column("#", justify="center")
        table.add_column("Barcode")
        table.add_column("Title", style="blue", ratio=2)
        table.add_column("Reserve date", justify="center")
        table.add_column("Available", justify="center")

        for index, hold in enumerate(holds.items):
            available = "✅" if hold.rank == 0 else "❌"
            table.add_row(
                f"{index + 1:>2}/{len(holds.items)}",
                hold.barcode,
                hold.title,
                f"{hold.reservedate:%d/%m/%Y}",
                available,
            )

        print(table)
