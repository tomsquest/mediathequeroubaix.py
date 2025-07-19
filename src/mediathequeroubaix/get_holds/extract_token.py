from returns.result import Result

from mediathequeroubaix.shared.extract_input_value import extract_input_value


def extract_token(s: str) -> Result[str, Exception]:
    return extract_input_value("my_holds", s)
