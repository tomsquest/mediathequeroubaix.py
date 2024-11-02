from .main import app
from .config import APP_NAME

# Support calling using `python -m`
# https://typer.tiangolo.com/tutorial/package/#support-python-m-optional
app(prog_name=APP_NAME)
