## 🤖 AI Usage Disclaimer / Дісклеймер щодо використання ШІ

🇬🇧 **Note:** Artificial Intelligence (AI) was used **only** for writing this README file and for general consultation and documentation.  
All source code, algorithms, and logic were **written and designed by the author**.

🇺🇦 **Примітка:** Штучний інтелект (AI) використовувався **лише** для створення цього README-файлу та отримання консультацій й оформлення.  
Увесь код, алгоритми та логіка були **написані й продумані автором**.

---

# 🧠 GOIT Python Core — Homework #6
## Address Book — Record Management System
A modular address book system built with clean architecture principles (BLL/DAL separation), type safety, and full unit test coverage.

🌐 **Languages:** [🇺🇸 English](#-english) • [🇺🇦 Українська](#-українська)

---

## 🇺🇸 English

### 📖 Overview

This project is a **modular Python-based address book** designed with a clear separation between:
- **DAL (Data Access Layer)** — data storage and entity logic,
- **BLL (Business Logic Layer)** — record management and validation.

The system supports CRUD operations on records, manages multiple phone numbers per contact, ensures strict validation, and includes full **Pytest-based unit and integration tests**.

---

### 🧩 Project Structure

```
📦 goit-pycore-hw-06
┣━━ BLL
┃   ┗━━ Services
┃       ┗━━ RecordService
┃           ┣━━ IRecordService.py
┃           ┗━━ RecordService.py
┣━━ DAL
┃   ┣━━ AddressBookStorage.py
┃   ┣━━ Entities
┃   ┃   ┣━━ Field.py
┃   ┃   ┣━━ Name.py
┃   ┃   ┣━━ Phone.py
┃   ┃   ┗━━ Record.py
┃   ┣━━ Exceptions
┃   ┃   ┣━━ InvalidException.py
┃   ┃   ┗━━ NotFoundException.py
┃   ┗━━ IStorage.py
┣━━ main.py
┣━━ README.md
┗━━ Tests
    ┣━━ test_address_book_storage.py
    ┣━━ test_end_to_end_address_book.py
    ┣━━ test_field_name_phone.py
    ┣━━ test_record_phones.py
    ┗━━ test_record_service.py
```

---

### ⚙️ Installation

```bash
git clone https://github.com/<your-repo>/goit-pycore-hw-06.git
cd goit-pycore-hw-06
python -m venv .venv
source .venv/bin/activate        # (on Windows: .venv\Scripts\activate)
pip install -r requirements.txt  # if you have one
```

---

### 🚀 Running the Project

```bash
python main.py
```

This will:
1. Create an in-memory address book,
2. Add and manage multiple records,
3. Print intermediate results to the console.

---

### 🧪 Running Tests

All tests use **Pytest** and are located in the `/Tests` directory.

#### Run all tests:
```bash
pytest
```

#### Run with detailed report:
```bash
pytest -v --cov=DAL --cov=BLL --cov-report=term-missing
```

#### Run a specific test:
```bash
pytest Tests/test_record_service.py
```

---

### 🧱 Features

- 📘 **Entity-based architecture** — records, names, and phones as first-class objects.  
- 🧩 **Storage abstraction** — easily replace in-memory `AddressBookStorage` with database-backed storage.  
- ⚙️ **Service layer validation** — prevents invalid states and enforces business rules.  
- 🧪 **Comprehensive test coverage** — includes unit, integration, and E2E scenarios.  
- 🔒 **Custom exceptions** — `InvalidException`, `NotFoundException` for clarity.

---

### 🧰 Example Output

```
AddressBookStorage was created
RecordService was created
John record was created
John record was saved
Jane record was created
Jane record was saved
All records:
Contact name: John, phones: 1234567890; 1234567891
Contact name: Jane, phones: 9876543210
John record phone 1234567890 was changed to 1112223333
John record was updated
Search 1234567891 phone in John record
John: 1234567891
Jane record was deleted
```

---

### 🧑‍💻 Author
**Roman Kulchytskyi**  
.NET / Python Full Stack Developer  
📎 [LinkedIn](https://www.linkedin.com/in/kulchitskiy-r)

[🔽 До української версії](#-українська)

---

---

## 🇺🇦 Українська

### 📖 Огляд

Цей проєкт — це **модульна адресна книга на Python**, розроблена за принципами чистої архітектури:
- **DAL (Data Access Layer)** — зберігання даних і логіка сутностей,
- **BLL (Business Logic Layer)** — бізнес-логіка керування записами.

Система підтримує повний набір CRUD-операцій, роботу з кількома телефонами для одного контакту, має жорстку валідацію та повне **покриття юніт- і інтеграційними тестами** через Pytest.

---

### 🧩 Структура проєкту

```
📦 goit-pycore-hw-06
┣━━ BLL
┃   ┗━━ Services
┃       ┗━━ RecordService
┃           ┣━━ IRecordService.py
┃           ┗━━ RecordService.py
┣━━ DAL
┃   ┣━━ AddressBookStorage.py
┃   ┣━━ Entities
┃   ┃   ┣━━ Field.py
┃   ┃   ┣━━ Name.py
┃   ┃   ┣━━ Phone.py
┃   ┃   ┗━━ Record.py
┃   ┣━━ Exceptions
┃   ┃   ┣━━ InvalidException.py
┃   ┃   ┗━━ NotFoundException.py
┃   ┗━━ IStorage.py
┣━━ main.py
┣━━ README.md
┗━━ Tests
    ┣━━ test_address_book_storage.py
    ┣━━ test_end_to_end_address_book.py
    ┣━━ test_field_name_phone.py
    ┣━━ test_record_phones.py
    ┗━━ test_record_service.py
```

---

### ⚙️ Встановлення

```bash
git clone https://github.com/<your-repo>/goit-pycore-hw-06.git
cd goit-pycore-hw-06
python -m venv .venv
.venv\Scripts\activate      # або source .venv/bin/activate для Linux/macOS
pip install -r requirements.txt
```

---

### 🚀 Запуск програми

```bash
python main.py
```

Програма:
1. Створює нову адресну книгу,  
2. Додає кілька записів,  
3. Показує їх у консолі,  
4. Оновлює, шукає та видаляє записи.

---

### 🧪 Запуск тестів

Усі тести розташовані в папці `/Tests` і використовують **Pytest**.

#### Запустити всі тести:
```bash
pytest
```

#### З докладним звітом:
```bash
pytest -v --cov=DAL --cov=BLL --cov-report=term-missing
```

#### Запустити один тест:
```bash
pytest Tests/test_record_service.py
```

---

### 🧱 Основні можливості

- 🧩 **Чітке розділення шарів (BLL/DAL)**  
- 📘 **Сутності як об’єкти першого класу** — Name, Phone, Record  
- ⚙️ **Валідація та винятки** — жодного невалідного стану  
- 🧪 **Повне тестове покриття** — юніт + інтеграційні + e2e тести  
- 🔧 **Гнучке сховище** — можна легко підключити реальну БД  

---

### 🧰 Приклад роботи

```
AddressBookStorage was created
RecordService was created
John record was created
John record was saved
Jane record was created
Jane record was saved
All records:
Contact name: John, phones: 1234567890; 1234567891
Contact name: Jane, phones: 9876543210
John record phone 1234567890 was changed to 1112223333
John record was updated
Search 1234567891 phone in John record
John: 1234567891
Jane record was deleted
```

---

### 👨‍💻 Автор

**Роман Кульчицький**  
.NET / Python Full Stack Developer  
📎 [LinkedIn](https://www.linkedin.com/in/kulchitskiy-r)

[🔼 To English version](#-english)
