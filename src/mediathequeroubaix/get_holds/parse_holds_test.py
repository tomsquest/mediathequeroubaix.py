from returns.pipeline import is_successful
from returns.result import Success

from mediathequeroubaix.get_holds.hold import Hold
from mediathequeroubaix.get_holds.parse_holds import parse_holds


def test_empty() -> None:
    assert is_successful(parse_holds("")) is False


def test_object() -> None:
    assert is_successful(parse_holds("{}")) is False


def test_empty_array() -> None:
    assert parse_holds("[]") == Success([])


def test_some_holds() -> None:
    assert parse_holds(
        '[{"hold_id":507643,"title":"Apprendre, si par bonheur","itemnumber":null,"barcode":"","found":null,'
        '"cancellationdate":null,"rank":2,"biblionumber":329375,"itemcallnumber":"","reservedate":"2025-07-14",'
        '"branchcode":"MED","branchname":"M\u00e9diath\u00e8que"},{"hold_id":507642,"cancellationdate":null,'
        '"rank":0,"biblionumber":302152,"found":"W","itemnumber":368084,"barcode":"C1400002454",'
        '"title":"L\'espace d\'un an","reservedate":"2025-07-14","itemcallnumber":"SF\/CHA",'
        '"branchname":"M\u00e9diath\u00e8que","branchcode":"MED"}]'
    ) == Success(
        [
            Hold(
                hold_id=507643,
                title="Apprendre, si par bonheur",
                itemnumber=None,
                barcode="",
                rank=2,
                itemcallnumber="",
                reservedate="2025-07-14",
            ),
            Hold(
                hold_id=507642,
                title="L'espace d'un an",
                itemnumber=368084,
                barcode="C1400002454",
                rank=0,
                itemcallnumber="SF/CHA",
                reservedate="2025-07-14",
            ),
        ]
    )
