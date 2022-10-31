from datetime import date, datetime

from pydantic import validator
from pydantic.main import BaseModel


class Loan(BaseModel):
    # Vampi
    title: str
    # C2500011705
    barcode: str
    # 2022-10-08T14:30:35
    issuedate: str
    # 2022-11-19T23:59:00
    date_due: date
    # E BD/FON
    itemcallnumber: str
    # Boolean
    renewable: bool
    # too_many
    reasons_not_renewable: str | None

    @validator("date_due", pre=True)
    def parse_date_due(cls, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
