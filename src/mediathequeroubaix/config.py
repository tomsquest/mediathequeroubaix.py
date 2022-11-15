from pathlib import Path

import typer
from pydantic import BaseModel, BaseSettings
from returns.io import IOFailure, IOResultE, IOSuccess
from returns.pipeline import flow
from returns.pointfree import bind_ioresult
from returns.result import Success
from rich.pretty import pprint

APP_NAME = "mediathequeroubaix"
app = typer.Typer()


@app.command()
def show() -> None:
    match get_config():
        case IOSuccess(Success(config)):
            print(f"Config located at: {_get_config_path()}")
            print("")
            pprint(config, expand_all=True)
        case IOFailure(failure):
            print(failure)
            raise typer.Exit(code=1)


@app.command()
def create() -> None:
    config_path = _get_config_path()
    if config_path.is_file():
        print(f"Config file already exists: {config_path}")
        raise typer.Exit(code=1)
    else:
        _create_sample_config(config_path)
        _show_config(config_path)


class User(BaseModel):
    login: str
    password: str


class Config(BaseSettings):
    users: list[User] = []

    class Config:
        env_prefix = "MR_"  # defaults to no prefix


def get_config() -> IOResultE[Config]:
    return flow(
        _get_config_path(),
        _is_path_readable,
        bind_ioresult(_read_as_config),
    )


def _is_path_readable(path: Path) -> IOResultE[Path]:
    if path.is_file():
        return IOSuccess(path)
    return IOFailure(ValueError(f"File {path} is missing or not readable"))


def _get_config_path() -> Path:
    app_path = Path(typer.get_app_dir(APP_NAME))
    return app_path / "config.json"


def _read_as_config(path: Path) -> IOResultE[Config]:
    try:
        return IOSuccess(Config.parse_file(path))
    except Exception:
        return IOFailure(ValueError(f"Invalid configuration: {path}"))


def _show_config(config_path: Path) -> None:
    print(f"Config located at: {config_path}")
    config = _read_as_config(config_path)
    print("")
    pprint(config, expand_all=True)


def _create_sample_config(config_path: Path) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    sample_config = Config(users=[User(login="X001002003", password="password00")])
    config_path.write_text(sample_config.json())
