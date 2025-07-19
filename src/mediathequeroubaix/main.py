import typer

from mediathequeroubaix import config, loans, holds

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(config.app, name="config", no_args_is_help=True)
app.add_typer(loans.app, name="loans", no_args_is_help=True)
app.add_typer(holds.app, name="holds", no_args_is_help=True)

if __name__ == "__main__":
    app(prog_name=config.APP_NAME)
