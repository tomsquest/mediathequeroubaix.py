from pathlib import Path

import typer
from pydantic import BaseModel, BaseSettings
from rich.pretty import pprint

APP_NAME = "mediathequeroubaix"
app = typer.Typer()


@app.command()
def show() -> None:
    config_path = _get_config_path()
    if config_path.is_file():
        _show_config(config_path)
    else:
        print("Missing config file. You can create it with: 'config create'")
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


def get_config() -> Config:
    config_path = _get_config_path()
    if config_path.is_file():
        return _read_config(config_path)
    else:
        print(f"No config file at {config_path}")
        print("Please create config file with 'config create'")
        raise typer.Exit(1)


def _get_config_path() -> Path:
    app_path = Path(typer.get_app_dir(APP_NAME))
    return app_path / "config.json"


def _read_config(config_path: Path) -> Config:
    return Config.parse_file(config_path)


def _show_config(config_path: Path) -> None:
    print(f"Config located at: {config_path}")
    config = _read_config(config_path)
    print("")
    pprint(config, expand_all=True)


def _create_sample_config(config_path: Path) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    sample_config = Config(users=[User(login="X001002003", password="password00")])
    config_path.write_text(sample_config.json())
