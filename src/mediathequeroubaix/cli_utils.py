import typer
from returns.unsafe import unsafe_perform_io
from rich import print

from mediathequeroubaix.config import Config, get_config, User


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
