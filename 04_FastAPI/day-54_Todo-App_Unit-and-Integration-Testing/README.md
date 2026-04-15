# 🧪 Day 54 – Todo App: Unit & Integration Testing

Welcome to **Day 54** of the Python learning journey!
Today adds a complete **test suite** to the Todo API using `pytest` and FastAPI's `TestClient`. Every router is covered with unit and integration tests — using a dedicated test database, shared fixtures, and dependency overrides to isolate tests from production data.

A health check endpoint is also added to `main.py` as a simple smoke test target.

---

## 📚 Topics Covered

- Setting up `pytest` with FastAPI's `TestClient`
- Overriding FastAPI dependencies (`get_db`, `get_current_user`) for testing
- Using a separate SQLite test database (`testdb.db`) with `StaticPool`
- Writing `pytest` fixtures for reusable test data (`test_todo`, `test_user`)
- Cleaning up test data after each test with `yield` fixtures
- Unit testing: pure functions (`authenticate_user`, `create_access_token`)
- Integration testing: full HTTP request/response cycle via `TestClient`
- Testing async functions with `@pytest.mark.asyncio`
- Asserting status codes, response bodies, and database state

---

## 📂 Files Overview

### App files (changed)

| File          | Change                                              |
| ------------- | --------------------------------------------------- |
| `main.py`     | Added `GET /healthy` health check endpoint          |
| `database.py` | Migrated `declarative_base` import to `sqlalchemy.orm` |

### Test files (all new)

| File                    | Description                                                    |
| ----------------------- | -------------------------------------------------------------- |
| `test/utils.py`         | Shared test DB setup, dependency overrides, and fixtures       |
| `test/test_example.py`  | Introductory pytest basics: assertions, types, fixtures        |
| `test/test_main.py`     | Smoke test for the `/healthy` endpoint                         |
| `test/test_todos.py`    | Integration tests for all todo CRUD routes                     |
| `test/test_admin.py`    | Integration tests for admin read-all and delete routes         |
| `test/test_users.py`    | Integration tests for user profile and password/phone routes   |
| `test/test_auth.py`     | Unit tests for `authenticate_user`, `create_access_token`, and `get_current_user` |

---

## 🎯 Learning Goal

By the end of Day 54, you should be able to:

- Configure a separate test database and override FastAPI dependencies in tests
- Write reusable pytest fixtures that set up and tear down test data cleanly
- Test every HTTP method and status code across all routers
- Unit test authentication logic directly without going through HTTP
- Test async route dependencies using `pytest-asyncio`

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] pytest pytest-asyncio httpx
```

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest test/test_todos.py -v
```

---

## 🧰 Test Infrastructure (`test/utils.py`)

The shared `utils.py` sets up the entire test environment:

```
testdb.db          ← Separate SQLite database (never touches todosapp.db)
StaticPool         ← Single shared connection for all test queries
override_get_db    ← Replaces the real DB session with the test session
override_get_current_user  ← Returns a fixed admin user (no real JWT needed)
```

Fixtures create records before each test and delete them after:

```python
@pytest.fixture
def test_todo():
    # INSERT todo into testdb
    yield todo
    # DELETE FROM todos  ← runs after the test
```

---

## 🧪 Test Coverage

### `test_example.py` — pytest basics
Covers equality, type checks, booleans, list membership, and object fixture patterns. A reference for pytest fundamentals.

---

### `test_main.py` — health check

| Test                      | Asserts                        |
| ------------------------- | ------------------------------ |
| `test_return_health_check`| `200 OK`, `{"status": "Healthy"}` |

---

### `test_todos.py` — todos router

| Test                              | Method | Route         | Asserts                             |
| --------------------------------- | ------ | ------------- | ----------------------------------- |
| `test_read_all_authenticated`     | GET    | `/todos`      | `200`, correct list                 |
| `test_read_one_authenticated`     | GET    | `/todos/1`    | `200`, correct object               |
| `test_read_one_authenticated_not_found` | GET | `/todos/9` | `404`, detail message              |
| `test_create_todo`                | POST   | `/todos`      | `201`, record in DB                 |
| `test_update_todo`                | PUT    | `/todos/1`    | `204`, updated in DB                |
| `test_update_todo_not_found`      | PUT    | `/todos/9`    | `404`, detail message               |
| `test_delete_todo`                | DELETE | `/todos/1`    | `204`, record gone from DB          |
| `test_delete_todo_not_found`      | DELETE | `/todos/9`    | `404`, detail message               |

---

### `test_admin.py` — admin router

| Test                              | Method | Route              | Asserts                     |
| --------------------------------- | ------ | ------------------ | --------------------------- |
| `test_admin_read_all_authenticated` | GET  | `/admin/todos`     | `200`, all todos returned   |
| `test_admin_delete_todo`          | DELETE | `/admin/todos/1`   | `204`, record gone from DB  |
| `test_admin_delete_todo_not_found`| DELETE | `/admin/todos/9`   | `404`, detail message       |

---

### `test_users.py` — users router

| Test                                 | Method | Route                           | Asserts                          |
| ------------------------------------ | ------ | --------------------------------| -------------------------------- |
| `test_return_user`                   | GET    | `/users/`                       | `200`, all profile fields        |
| `test_change_password_success`       | PUT    | `/users/change-password`        | `204`                            |
| `test_change_password_invalid_current_password` | PUT | `/users/change-password` | `401`, detail message       |
| `test_change_phone_number_success`   | PUT    | `/users/change-phone-number/...`| `204`                            |

---

### `test_auth.py` — auth logic (unit tests)

| Test                                 | Type  | Asserts                                                |
| ------------------------------------ | ----- | ------------------------------------------------------ |
| `test_authenticate_user`             | Unit  | Valid user returns user object; wrong name/password returns `False` |
| `test_create_access_token`           | Unit  | Token decodes to correct `sub`, `id`, `role` claims    |
| `test_get_current_user_valid_token`  | Async | Valid JWT returns correct user dict                    |
| `test_get_current_user_missing_payload` | Async | Token without `sub`/`id` raises `401`               |

---

## 🏗️ Project Structure

```
day-54/
├── main.py
├── database.py
├── models.py
├── alembic.ini
├── todosapp.db
├── testdb.db
├── alembic/
│   └── versions/
│       └── 2045bc1c6a54_create_phone_number_for_user_column.py
├── routers/
│   ├── auth.py
│   ├── todos.py
│   ├── users.py
│   └── admin.py
└── test/
    ├── utils.py
    ├── test_example.py
    ├── test_main.py
    ├── test_todos.py
    ├── test_admin.py
    ├── test_users.py
    └── test_auth.py
```

---

## 💡 Improvements & Ideas

Try extending the test suite by:

- Adding tests for the `POST /auth/` (register) and `POST /auth/token` (login) endpoints
- Testing that a regular user (non-admin) gets `401` on admin routes
- Testing the `change-phone-number` route with an invalid (too short) phone number
- Adding a `conftest.py` to share fixtures across test files without imports
- Measuring test coverage with `pytest-cov`

---

## ⚠️ Notes

- `testdb.db` is a separate database used exclusively by tests — production data in `todosapp.db` is never touched
- `StaticPool` ensures all test queries share the same in-memory connection, preventing SQLite threading issues
- `dependency_overrides` are set at the module level in each test file — they apply for the entire test session
- `@pytest.mark.asyncio` is required to test `async` functions directly (without going through HTTP)
- `declarative_base` is now imported from `sqlalchemy.orm` directly (the old `sqlalchemy.ext.declarative` path is deprecated)

---

Happy coding! 🧪✅🐍🚀