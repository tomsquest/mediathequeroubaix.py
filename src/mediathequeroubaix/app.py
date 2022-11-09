import typer
from returns.io import IOFailure, IOSuccess
from returns.result import Success

from mediathequeroubaix import config
from mediathequeroubaix.authenticate import authenticate
from mediathequeroubaix.config import get_config
from mediathequeroubaix.print_loans import print_loans

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(config.app, name="config", no_args_is_help=True)


@app.command()
def loans() -> None:
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


if __name__ == "__main__":
    app()
