from BLL.Services.RecordService.RecordService import RecordService
from DAL.AddressBookStorage import AddressBookStorage
from DAL.Entities.Record import Record
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException


def main():
    try:
        book_storage = AddressBookStorage()

        print("AddressBookStorage was created")

        record_service = RecordService(book_storage)

        print("RecordService was created")

        john_record = Record("John", "1234567890")
        john_record.add_phone("1234567891")

        print("John record was created")

        record_service.save(john_record)

        print("John record was saved")

        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")

        print("Jane record was created")

        record_service.save(jane_record)

        print("Jane record was saved")

        print("All records:")
        for record in record_service.get_all():
            print(record)

        john_record = record_service.get_by_name("John")
        john_record.update_phone("1234567890", "1112223333")

        print("John record phone 1234567890 was changed to 1112223333")

        record_service.update("John", john_record)

        print("John record was updated")
        print(john_record)  # Виведення: Contact name: John, phones: 1112223333; 1234567891

        print("Search 1234567891 phone in John record")
        found_phone = john_record.find_phone("1234567891")
        print(f"{john_record.name}: {found_phone}")  # Виведення: 1112223333

        record_service.delete("Jane")
        print("Jane record was deleted")

        print("All records:")
        for record in record_service.get_all():
            print(record)

    except NotFoundException as nfe:
        print(nfe)
    except InvalidException as infe:
        print(infe)
    except Exception as err:
        print(f"An unhandled exception: {err}")

if __name__ == "__main__":
    main()

