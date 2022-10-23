from pydantic.tools import parse_raw_as
from returns.result import safe

from mediathequeroubaix.fetch_loans.loan import Loan


@safe
def parse_loans(s: str) -> list[Loan]:
    return parse_raw_as(list[Loan], s)
