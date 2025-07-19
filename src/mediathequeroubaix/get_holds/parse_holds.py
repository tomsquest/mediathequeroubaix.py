from returns.result import safe
from typing import List
from pydantic import BaseModel, Json

from mediathequeroubaix.get_holds.hold import Hold


class JsonStringWrapper(BaseModel):
    json_obj: Json[List[Hold]]


@safe
def parse_holds(s: str) -> list[Hold]:
    return JsonStringWrapper(json_obj=s).json_obj
