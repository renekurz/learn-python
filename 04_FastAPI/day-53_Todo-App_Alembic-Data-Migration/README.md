# 🔄 Day 53 – Todo App: Alembic Data Migration

Welcome to **Day 53** of the Python learning journey!
Today introduces **Alembic** — the standard database migration tool for SQLAlchemy. Instead of dropping and recreating tables when the schema changes, Alembic applies incremental, versioned migrations that preserve existing data.

The first real migration adds a `phone_number` column to the `users` table, and a new route lets authenticated users update their phone number.

---

## 📚 Topics Covered

- Setting up Alembic in a FastAPI project (`alembic init`)
- Connecting Alembic to SQLAlchemy models via `env.py`
- Creating a migration script manually with `alembic revision`
- Writing `upgrade()` and `downgrade()` functions
- Applying migrations with `alembic upgrade head`
- Rolling back migrations with `alembic downgrade`
- Adding a `phone_number` column to an existing live database
- New route: `PUT /users/change-phone-number/{phone_number}`

---

## 📂 Files Overview

| File                                                        | Description                                              |
| ----------------------------------------------------------- | -------------------------------------------------------- |
| `main.py`                                                   | App entry point (unchanged)                              |
| `database.py`                                               | SQLAlchemy engine and session (unchanged)                |
| `models.py`                                                 | `Users` model — now includes `phone_number` column       |
| `routers/auth.py`                                           | Auth router (unchanged)                                  |
| `routers/todos.py`                                          | Todos router (unchanged)                                 |
| `routers/admin.py`                                          | Admin router (unchanged)                                 |
| `routers/users.py`                                          | Users router — new `change-phone-number` route added     |
| `alembic.ini`                                               | Alembic configuration file                               |
| `alembic/env.py`                                            | Migration environment — linked to `models.Base.metadata` |
| `alembic/versions/2045bc1c6a54_create_phone_number_...py`  | First migration: adds `phone_number` to `users`          |
| `todosapp.db`                                               | SQLite database with migration already applied           |

---

## 🎯 Learning Goal

By the end of Day 53, you should be able to:

- Initialise Alembic and configure it to work with your SQLAlchemy models
- Write `upgrade()` and `downgrade()` functions for a schema change
- Apply and roll back migrations without losing data
- Understand the Alembic revision chain (`revision`, `down_revision`)
- Add new columns to a live database safely

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] alembic
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

## 🔄 Alembic Migration Workflow

### Initial setup (already done)

```bash
alembic init alembic
```

Then in `alembic/env.py`, import your models and set:

```python
import models
target_metadata = models.Base.metadata
```

And in `alembic.ini`, set the database URL:

```ini
sqlalchemy.url = sqlite:///todosapp.db
```

---

### Create a new migration

```bash
alembic revision -m "Create phone number for User Column"
```

This generates a new file in `alembic/versions/` with empty `upgrade()` and `downgrade()` stubs.

---

### Write the migration

```python
def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column("users", "phone_number")
```

---

### Apply the migration

```bash
alembic upgrade head
```

### Roll back one step

```bash
alembic downgrade -1
```

### Check current migration state

```bash
alembic current
alembic history
```

---

## 🗺️ New Route

### 📱 Update Phone Number (`/users`)

| Method | Path                                    | Description                   | Auth required |
| ------ | --------------------------------------- | ----------------------------- | ------------- |
| PUT    | `/users/change-phone-number/{phone_number}` | Update current user's phone number | ✅       |

The phone number is passed as a path parameter:

```
PUT /users/change-phone-number/+4367612345678
```

---

## 📦 Updated `Users` Model

| Column            | Type    | New? | Description                          |
| ----------------- | ------- | ---- | ------------------------------------ |
| `id`              | Integer |      | Primary key                          |
| `email`           | String  |      | Unique email                         |
| `username`        | String  |      | Unique username                      |
| `first_name`      | String  |      | First name                           |
| `last_name`       | String  |      | Last name                            |
| `hashed_password` | String  |      | bcrypt hash                          |
| `is_active`       | Boolean |      | Account status                       |
| `role`            | String  |      | User role                            |
| `phone_number`    | String  | ✅   | Optional phone number (nullable)     |

---

## 🏗️ Project Structure

```
day-53/
├── main.py
├── database.py
├── models.py
├── alembic.ini
├── todosapp.db
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   ├── README
│   └── versions/
│       └── 2045bc1c6a54_create_phone_number_for_user_column.py
└── routers/
    ├── auth.py
    ├── todos.py
    ├── users.py
    └── admin.py
```

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding a second migration to make `phone_number` unique
- Using `alembic revision --autogenerate` to auto-detect model changes
- Migrating from SQLite to PostgreSQL by updating `sqlalchemy.url` in `alembic.ini`
- Writing a migration that backfills data (e.g. setting a default role for existing users)
- Adding a `created_at` timestamp column to `todos` via a new migration

---

## ⚠️ Notes

- Alembic tracks the current migration state in a `alembic_version` table in the database
- `downgrade()` is just as important as `upgrade()` — always implement it for safe rollbacks
- SQLite has limited `ALTER TABLE` support; Alembic handles this with a table-recreation strategy for complex changes
- The `phone_number` column is `nullable=True` so existing users are not affected by the migration
- Never edit a migration file after it has been applied to a shared or production database

---

Happy coding! 🔄🗄️🐍🚀