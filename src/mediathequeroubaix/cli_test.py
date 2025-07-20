from typer.testing import CliRunner

from mediathequeroubaix.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
