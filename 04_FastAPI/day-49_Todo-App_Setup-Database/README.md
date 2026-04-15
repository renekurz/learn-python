# 🗄️ Day 49 – Todo App: Setup & Database

Welcome to **Day 49** of the Python learning journey!
Today shifts from in-memory data to a **real database** — setting up SQLite with SQLAlchemy as the foundation for a full Todo API.

Instead of a list in memory, todos are now stored in a persistent `todos.db` file, with a proper ORM model and database session management.

---

## 📚 Topics Covered

- Connecting FastAPI to a SQLite database via SQLAlchemy
- Creating a `declarative_base` for ORM models
- Defining a database model with `Column` types
- Setting up a `SessionLocal` for database sessions
- Auto-creating tables on app startup with `create_all()`

---

## 📂 Files Overview

| File          | Description                                               |
| ------------- | --------------------------------------------------------- |
| `main.py`     | FastAPI app entry point; triggers table creation on start |
| `database.py` | Database engine, session factory, and Base declaration    |
| `models.py`   | SQLAlchemy ORM model for the `todos` table                |
| `todos.db`    | SQLite database file (auto-created on first run)          |

---

## 🎯 Learning Goal

By the end of Day 49, you should be able to:

- Configure a SQLAlchemy database connection for FastAPI
- Define an ORM model that maps to a database table
- Understand the role of `engine`, `SessionLocal`, and `Base`
- Auto-create database tables when the app starts

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn sqlalchemy
```

Start the server:

```bash
uvicorn main:app --reload
```

On startup, FastAPI automatically creates the `todos` table in `todos.db` if it doesn't exist yet.

Open the interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## 🗃️ Database Setup

### `database.py`

| Component      | Description                               |
| -------------- | ----------------------------------------- |
| `engine`       | SQLAlchemy engine connected to `todos.db` |
| `SessionLocal` | Factory for creating database sessions    |
| `Base`         | Declarative base class for all ORM models |

SQLite is configured with `check_same_thread=False` to work correctly with FastAPI's async request handling.

---

## 📦 Data Model

### `Todos` table (`models.py`)

| Column        | Type    | Description                            |
| ------------- | ------- | -------------------------------------- |
| `id`          | Integer | Primary key, auto-incremented, indexed |
| `title`       | String  | Title of the todo item                 |
| `description` | String  | Detailed description                   |
| `priority`    | Integer | Priority level of the todo             |
| `complete`    | Boolean | Completion status (default: False)     |

---

## 🏗️ App Structure

```
day-49/
├── main.py       # App entry point
├── database.py   # DB connection & session setup
├── models.py     # ORM table definition
└── todos.db      # SQLite database (auto-created)
```

---

## 💡 Improvements & Ideas

This day sets the foundation — next steps will build on top of it:

- Add CRUD routes in `main.py` using database sessions
- Create a Pydantic `TodoRequest` model for input validation
- Add a dependency function to inject `db: Session` into routes
- Implement user authentication and associate todos with users

---

## ⚠️ Notes

- `todos.db` is created automatically in the project root on first run
- `create_all()` only creates tables that don't exist yet — it won't overwrite existing data
- `SessionLocal` should be used with a `try/finally` block (or as a FastAPI dependency) to ensure sessions are always closed

---

Happy coding! 🗄️🐍⚡🚀
