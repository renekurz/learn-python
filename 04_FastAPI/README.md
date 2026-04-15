# ⚡ 04 FastAPI — Days 47 – 55

Welcome to the **FastAPI section** of the Python learning journey!

These 9 days cover modern Python API development from the ground up — starting with basic request handling, advancing through a fully database-backed API, and finishing with a complete full-stack web application. The centrepiece is a **Todo App** built incrementally over 7 days, growing from a bare database setup into a production-style app with authentication, role-based access control, database migrations, a full test suite, and a browser frontend.

---

## 🎯 What You'll Learn

By the end of this section you will be able to:

- Build REST APIs with FastAPI using all HTTP methods
- Validate request data with Pydantic models and `Field` constraints
- Validate path and query parameters with `Path()` and `Query()`
- Connect FastAPI to a SQLite database via SQLAlchemy
- Inject database sessions using FastAPI's `Depends()` system
- Implement JWT authentication with `python-jose` and `passlib`
- Structure large APIs into multiple routers with `APIRouter`
- Enforce per-user data ownership and role-based access control
- Run database schema migrations with Alembic
- Write unit and integration tests with `pytest` and `TestClient`
- Serve HTML pages with Jinja2 templates and Bootstrap
- Handle cookie-based authentication in a browser session

---

## 📅 Day-by-Day Overview

| Day | Topic | Project / Focus |
| --- | ----- | --------------- |
| 47 | FastAPI basics, HTTP methods, in-memory data | Books API |
| 48 | Pydantic, `Field`, `Path()`, `Query()`, `HTTPException` | Books API with validation |
| 49 | SQLAlchemy setup, ORM models, `create_all()` | Todo App — Database setup |
| 50 | CRUD routes, `Depends()`, `db.commit()` | Todo App — API endpoints |
| 51 | JWT, bcrypt, `APIRouter`, role in token | Todo App — Auth & routers |
| 52 | Ownership filtering, admin router, users router | Todo App — Authenticate requests |
| 53 | Alembic migrations, `upgrade()`/`downgrade()` | Todo App — Phone number migration |
| 54 | pytest, `TestClient`, fixtures, dependency overrides | Todo App — Test suite |
| 55 | Jinja2 templates, `StaticFiles`, cookie auth, JS fetch | Todo App — Full-stack app |

---

## 🧠 Key Projects

### 📚 Books API (Days 47–48)
Two iterations of a book management API, showing the evolution from a simple in-memory CRUD setup (Day 47) to a properly validated API with Pydantic models, `Field` constraints, `HTTPException`, and explicit HTTP status codes (Day 48).

### ✅ Todo App (Days 49–55)
The main capstone. A complete full-stack application built layer by layer:

```
Day 49  SQLAlchemy + SQLite        models.py, database.py, create_all()
Day 50  Full CRUD API              GET, POST, PUT, DELETE with DB sessions
Day 51  Auth system                JWT tokens, bcrypt, APIRouter split
Day 52  Security enforcement       User-scoped data, admin role, users router
Day 53  Schema migrations          Alembic, phone_number column added
Day 54  Test suite                 pytest, TestClient, fixtures, async tests
Day 55  Browser frontend           Jinja2 HTML, Bootstrap, JS fetch, cookies
```

---

## 📂 Folder Structure

```
04_FastAPI/
├── day-47_FastAPI-Request-Method-Logic/
│   └── books.py
├── day-48_Move-Fast-with-FastAPI/
│   └── books.py
├── day-49_Todo-App_Setup-Database/
│   ├── main.py
│   ├── database.py
│   └── models.py
├── day-50_Todo-App_API-Request-Methods/
│   ├── main.py
│   ├── database.py
│   └── models.py
├── day-51_Todo-App_Authentication-and-Authorization/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routers/
│       ├── auth.py
│       └── todos.py
├── day-52_Todo-App_Authenticate-Requests/
│   ├── main.py + database.py + models.py
│   └── routers/
│       ├── auth.py
│       ├── todos.py
│       ├── users.py
│       └── admin.py
├── day-53_Todo-App_Alembic-Data-Migration/
│   ├── alembic.ini
│   ├── alembic/
│   │   └── versions/
│   └── routers/
├── day-54_Todo-App_Unit-and-Integration-Testing/
│   ├── test/
│   │   ├── utils.py
│   │   ├── test_todos.py
│   │   ├── test_auth.py
│   │   ├── test_admin.py
│   │   ├── test_users.py
│   │   └── test_main.py
│   └── routers/
└── day-55_Todo-App_Full-Stack-Application/
    ├── templates/
    │   ├── layout.html
    │   ├── login.html
    │   ├── register.html
    │   ├── todos.html
    │   ├── add-todo.html
    │   └── edit-todo.html
    ├── static/
    │   ├── css/
    │   └── js/
    └── routers/
```

---

## 🔐 Authentication Flow (Day 51+)

```
POST /auth/        →  Register (bcrypt-hashed password stored in DB)
POST /auth/token   →  Login → JWT issued (contains username, id, role)
                   →  JWT stored as browser cookie (Day 55) or Authorization header
All /todos/* routes  →  JWT decoded → user identity confirmed → data scoped to user
/admin/* routes    →  role == "admin" required
```

---

## 🧪 Testing Setup (Day 54)

Tests run against a separate `testdb.db` — production data is never touched.

```bash
pytest          # run all tests
pytest -v       # verbose output
pytest test/test_todos.py -v   # single file
```

Key techniques:
- `app.dependency_overrides` replaces `get_db` and `get_current_user` for isolation
- `@pytest.fixture` with `yield` for clean per-test setup and teardown
- `@pytest.mark.asyncio` for testing async functions directly

---

## 🚀 How to Run

Install all required packages:

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] alembic jinja2 python-multipart pytest pytest-asyncio httpx
```

Start any day's app:

```bash
cd day-<N>_<name>
uvicorn main:app --reload
```

Open the interactive Swagger docs:

```
http://127.0.0.1:8000/docs
```

For the full-stack app (Day 55), open the browser at:

```
http://127.0.0.1:8000
```

---

Happy coding! 🐍⚡