from returns.result import safe
from typing import List
from pydantic import BaseModel, Json

from mediathequeroubaix.get_loans.loan import Loan


class JsonStringWrapper(BaseModel):
    json_obj: Json[List[Loan]]


@safe
def parse_loans(s: str) -> list[Loan]:
    return JsonStringWrapper(json_obj=s).json_obj
