import datetime

from mediathequeroubaix.get_holds.hold import Hold


def test_convert_due_date_to_date() -> None:
    hold = Hold(
        hold_id=1234,
        title="Test Book",
        barcode="c123",
        rank=1,
        reservedate="2023-04-05",
    )

    assert hold.reservedate == datetime.date.fromisoformat("2023-04-05")
