import typer

from mediathequeroubaix import config, loans

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(config.app, name="config", no_args_is_help=True)
app.add_typer(loans.app, name="loans", no_args_is_help=True)
