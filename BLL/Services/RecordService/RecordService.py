from BLL.Services.RecordService.IRecordService import IRecordService
from DAL.Entities.Record import Record
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException
from DAL.IStorage import IStorage

class RecordService(IRecordService):
    def __init__(self, storage: IStorage[str, Record]):
        self.storage = storage

    def save(self, new_record: Record) -> None:
        self._validate_record(new_record)

        if self.has(new_record.name.value):
            raise InvalidException(f"Record '{new_record.name.value}' already exists")

        self.storage.add(new_record)

    def update(self, record_name: str, new_record: Record) -> Record:
        self._validate_record(new_record)

        if not self.has(record_name):
            raise NotFoundException(f"Record '{record_name}' not found")

        self.storage.update_item(record_name, new_record)

        return new_record

    def get_by_name(self, record_name: str) -> Record | None:
        if not self.has(record_name):
            raise NotFoundException(f"Record '{record_name}' does not exist")

        return self.storage.find(record_name)

    def get_all(self) -> list[Record]:
        return self.storage.all_values()

    def rename(self, record_name: str, new_name: str) -> Record:
        if not self.has(record_name):
            raise NotFoundException(f"Record '{record_name}' not found")

        record = self.get_by_name(record_name)
        record.name.value = new_name

        self.delete(record_name)
        self.save(record)

        return record

    def delete(self, record_name: str) -> None:
        if not self.has(record_name):
            raise NotFoundException(f"Record '{record_name}' not found")

        self.storage.delete(record_name)

    def has(self, record_name: str) -> bool:
        self._validate_record_name(record_name)
        return self.storage.has(record_name)

    @staticmethod
    def _validate_record_name(record_name: str) -> None:
        if record_name is None:
            raise InvalidException("Record name cannot be None")

        if not isinstance(record_name, str):
            raise InvalidException("Record name has invalid type")

    @staticmethod
    def _validate_record(record: Record) -> None:
        if record is None:
            raise NotFoundException("Record cannot be None")

        if not isinstance(record, Record):
            raise InvalidException("Record has invalid type")
