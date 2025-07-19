import base64

from returns.result import safe


@safe
def base64decode(b64str: str) -> str:
    data = base64.b64decode(b64str, validate=True)
    return data.decode("utf-8")
