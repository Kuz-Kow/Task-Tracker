import pytest
from task_manager import add, delete, update, mark_done, mark_in_progress, data_base

db: data_base = {}


def test_add() -> None:

    add(db, "hi")
    assert len(db) == 1 and db["1"]["description"] == "hi"
    add(db, "lol")
    add(db, "new information")
    assert len(db) == 3 and db["3"]["description"] == "new information"


def test_update() -> None:
    update(db, "1", "new tekst")
    assert db["1"]["description"] == "new tekst"
    with pytest.raises(KeyError):
        update(db, "0", "other task")
    with pytest.raises(KeyError):
        update(db, "9", "some other task")


def test_delete() -> None:
    delete(db, "1")
    assert len(db) == 2 and "1" not in db
    with pytest.raises(KeyError):
        delete(db, "0")
    with pytest.raises(KeyError):
        delete(db, "19")


def test_mark_done() -> None:
    mark_done(db, "2")
    assert db["2"]["status"] == "done"
    with pytest.raises(KeyError):
        mark_done(db, "0")
    with pytest.raises(KeyError):
        mark_done(db, "6")


def test_mark_in_progress() -> None:
    mark_in_progress(db, "3")
    assert db["3"]["status"] == "in-progress"
    with pytest.raises(KeyError):
        mark_in_progress(db, "0")
    with pytest.raises(KeyError):
        mark_in_progress(db, "7")
