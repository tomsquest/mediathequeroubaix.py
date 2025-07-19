from datetime import date, datetime

from pydantic import field_validator
from pydantic.main import BaseModel

from mediathequeroubaix.auth.authenticated_session import Username


class Hold(BaseModel):
    # 1234
    hold_id: int
    # Vampi
    title: str
    # 1234567
    itemnumber: int | None = None
    # C2500011705
    barcode: str
    # 0
    rank: int
    # E BD/FON
    itemcallnumber: str | None = None
    # 2025-07-14
    reservedate: date | None = None

    @field_validator("reservedate", mode="before")
    @classmethod
    def parse_reservedate(cls, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()


class Holds(BaseModel):
    username: Username
    items: list[Hold]
