import pytest
from DAL.Entities.Record import Record
from DAL.Entities.Phone import Phone
from DAL.Exceptions.InvalidException import InvalidException

def test_add_phone():
    record = Record("John")
    record.add_phone("1234567890")
    assert len(record.phones) == 1
    assert record.phones[0].value == "1234567890"

def test_add_duplicate_phone_raises():
    record = Record("John", "1234567890")
    with pytest.raises(InvalidException):
        record.add_phone("1234567890")

def test_remove_phone():
    record = Record("John", "1234567890", "1112223333")
    record.remove_phone("1112223333")
    assert len(record.phones) == 1
    assert record.phones[0].value == "1234567890"

def test_remove_nonexistent_phone_raises():
    record = Record("John", "1234567890")
    with pytest.raises(InvalidException):
        record.remove_phone("9999999999")

def test_update_phone():
    record = Record("John", "1234567890")
    record.update_phone("1234567890", "1112223333")
    assert record.phones[0].value == "1112223333"

def test_find_phone():
    record = Record("John", "1234567890")
    found = record.find_phone("1234567890")
    assert isinstance(found, Phone)
    assert found.value == "1234567890"

def test_find_missing_phone_raises():
    record = Record("John", "1234567890")
    with pytest.raises(InvalidException):
        record.find_phone("1112223333")
