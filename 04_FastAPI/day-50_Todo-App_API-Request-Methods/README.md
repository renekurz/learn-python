# ✅ Day 50 – Todo App: API Request Methods

Welcome to **Day 50** of the Python learning journey!
Today completes the Todo API by wiring up the database from Day 49 to a full set of **CRUD routes** — using SQLAlchemy sessions, Pydantic validation, and FastAPI dependency injection.

Data now actually persists in `todos.db` across server restarts.

---

## 📚 Topics Covered

- Injecting database sessions with `Depends()` and `Annotated`
- Querying, filtering, adding, and deleting records via SQLAlchemy ORM
- Pydantic `BaseModel` with `Field` validation for request bodies
- Raising `HTTPException` with detailed error messages
- Full CRUD: GET, POST, PUT, DELETE with proper HTTP status codes
- Using `db.commit()` to persist changes to SQLite

---

## 📂 Files Overview

| File          | Description                                               |
| ------------- | --------------------------------------------------------- |
| `main.py`     | All CRUD routes, DB dependency, and `TodoRequest` model   |
| `database.py` | SQLAlchemy engine, session factory, and Base (unchanged)  |
| `models.py`   | `Todos` ORM model for the `todos` table (unchanged)       |
| `todos.db`    | SQLite database file (auto-created on first run)          |

---

## 🎯 Learning Goal

By the end of Day 50, you should be able to:

- Use `Depends()` to inject a database session into route functions
- Query and filter database records with SQLAlchemy's ORM
- Persist, update, and delete records using `db.add()`, `db.commit()`, `db.delete()`
- Handle missing records cleanly with `HTTPException`
- Build a complete, database-backed REST API with FastAPI

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

Open the interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Request Model

### `TodoRequest` (Pydantic)

| Field         | Type | Constraints               |
| ------------- | ---- | ------------------------- |
| `title`       | str  | Min length: 3             |
| `description` | str  | Min length: 3, max: 100   |
| `priority`    | int  | 0 – 6                     |
| `complete`    | bool | —                         |

Example payload:

```json
{
  "title": "A new Todo",
  "description": "A new Todo description",
  "priority": 5,
  "complete": false
}
```

---

## 🗺️ Routes Overview

### 📋 Get All Todos

```
GET /
```

Returns all todos from the database. Status: `200 OK`

---

### 🔍 Get Todo by ID

```
GET /todos/{todo_id}
```

Path parameter `todo_id` must be greater than 0. Raises `404` if not found. Status: `200 OK`

---

### ➕ Create Todo

```
POST /todos
```

Expects a `TodoRequest` JSON body. Saves the new todo to the database. Status: `201 Created`

---

### ✏️ Update Todo

```
PUT /todos/{todo_id}
```

Updates all fields of an existing todo by ID. Raises `404` if not found. Status: `204 No Content`

---

### 🗑️ Delete Todo

```
DELETE /todos/{todo_id}
```

Deletes a todo by ID. Raises `404` if not found. Status: `204 No Content`

---

## 🔌 Database Dependency

A `get_db()` generator function manages the database session lifecycle:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
```

Every route that needs the database simply declares `db: db_dependency` as a parameter — FastAPI handles the rest automatically.

---

## 🏗️ Project Structure

```
day-50/
├── main.py       # CRUD routes + TodoRequest model + DB dependency
├── database.py   # Engine, SessionLocal, Base
├── models.py     # Todos ORM model
└── todos.db      # SQLite database (auto-created)
```

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding a `GET /todos/priority/{priority}` route to filter by priority
- Adding a `GET /todos/complete` route to list only completed todos
- Implementing user authentication and linking todos to specific users
- Adding pagination with `limit` and `offset` query parameters
- Deploying to a cloud platform with a production-grade database (e.g. PostgreSQL)

---

## ⚠️ Notes

- `todos.db` persists across restarts — data is not lost when the server stops
- `db.commit()` must be called after `db.add()` or `db.delete()` for changes to take effect
- `db.query(Todos).filter(...).first()` returns `None` (not an exception) if no record matches
- The `Annotated` + `Depends` pattern is the idiomatic FastAPI way to inject shared resources

---

Happy coding! ✅🗄️🐍🚀