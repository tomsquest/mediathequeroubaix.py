from pathlib import Path
import typer
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from returns.io import IOFailure, IOResultE, IOSuccess
from returns.pipeline import flow
from returns.pointfree import bind_ioresult
from returns.result import Success
from rich import print
from rich.panel import Panel
from rich.pretty import Pretty

APP_NAME = "mediathequeroubaix"
app = typer.Typer()


@app.command()
def show() -> None:
    match get_config():
        case IOSuccess(Success(config)):
            _show(_get_path(), config)
        case IOFailure(failure):
            print(failure)
            raise typer.Exit(code=1)


@app.command()
def create() -> None:
    config_path = _get_path()
    if config_path.is_file():
        print()
        print(
            f"[bold][yellow] Config file already exists:[/yellow] {_get_path()}[/bold]"
        )
        print()
        raise typer.Exit(code=1)
    else:
        config = _create_sample_config(config_path)
        _show(config_path, config)


class User(BaseModel):
    login: str
    password: str


class Config(BaseSettings):
    users: list[User] = []


def get_config() -> IOResultE[Config]:
    return flow(
        _get_path(),
        _is_readable,
        bind_ioresult(_read),
    )


def _is_readable(path: Path) -> IOResultE[Path]:
    if path.is_file():
        return IOSuccess(path)
    return IOFailure(ValueError(f"File {path} is missing or not readable"))


def _get_path() -> Path:
    app_path = Path(typer.get_app_dir(APP_NAME))
    return app_path / "config.json"


def _read(path: Path) -> IOResultE[Config]:
    try:
        return IOSuccess(Config.parse_file(path))
    except Exception:
        return IOFailure(ValueError(f"Invalid configuration: {path}"))


def _show(config_path: Path, config: Config) -> None:
    print()
    print(f"[bold][yellow] Config:[/yellow] {config_path}[/bold]")
    print()
    panel = Panel(Pretty(config, expand_all=True))
    print(panel)
    print()


def _create_sample_config(config_path: Path) -> Config:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    sample_config = Config(users=[User(login="X001002003", password="password00")])
    config_path.write_text(sample_config.json())
    return sample_config
