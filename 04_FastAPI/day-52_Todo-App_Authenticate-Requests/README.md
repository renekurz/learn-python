# 🛡️ Day 52 – Todo App: Authenticate Requests

Welcome to **Day 52** of the Python learning journey!
Today enforces **full request authentication** across all routes — every todo operation is now scoped to the logged-in user, and a new **admin role** grants elevated access. Two new routers for user self-management and admin controls round out the API.

The `owner_id` foreign key from Day 51 is now actively used to filter data per user.

---

## 📚 Topics Covered

- Enforcing ownership: todos are filtered by the authenticated user's ID
- Embedding `role` in the JWT payload for role-based access control
- Admin-only routes protected by role checking (`role == "admin"`)
- New `users` router: get own profile and change password
- New `admin` router: view and delete any user's todos
- `user_dependency` pattern for injecting the current user into routes

---

## 📂 Files Overview

| File                | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| `main.py`           | App entry point; registers all four routers                            |
| `database.py`       | SQLAlchemy engine, session factory, and Base (unchanged)               |
| `models.py`         | `Users` and `Todos` ORM models (unchanged)                             |
| `routers/auth.py`   | Registration, login, JWT with role claim, `get_current_user`           |
| `routers/todos.py`  | CRUD routes — all scoped to the authenticated user's todos             |
| `routers/users.py`  | Get own profile, change password                                       |
| `routers/admin.py`  | Admin-only: view all todos, delete any todo                            |
| `todosapp.db`       | SQLite database (auto-created on first run)                            |

---

## 🎯 Learning Goal

By the end of Day 52, you should be able to:

- Scope all database queries to the current authenticated user
- Embed and read a `role` claim from a JWT token
- Implement role-based access control (RBAC) with a simple role check
- Let users view their own profile and securely change their password
- Give admins elevated read/delete access across all users' data

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography]
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

## 🗺️ Routes Overview

### 🔑 Auth Router (`/auth`)

| Method | Path          | Description                           | Auth required |
| ------ | ------------- | ------------------------------------- | ------------- |
| POST   | `/auth/`      | Register a new user                   | ❌            |
| POST   | `/auth/token` | Log in and receive a JWT access token | ❌            |

---

### ✅ Todos Router (`/todos`) — scoped to current user

| Method | Path               | Description                              | Auth required |
| ------ | ------------------ | ---------------------------------------- | ------------- |
| GET    | `/todos/`          | Get all todos belonging to current user  | ✅            |
| GET    | `/todos/{todo_id}` | Get one todo (must belong to user)       | ✅            |
| POST   | `/todos/`          | Create a todo (auto-assigned to user)    | ✅            |
| PUT    | `/todos/{todo_id}` | Update a todo (must belong to user)      | ✅            |
| DELETE | `/todos/{todo_id}` | Delete a todo (must belong to user)      | ✅            |

---

### 👤 Users Router (`/users`)

| Method | Path                    | Description                              | Auth required |
| ------ | ----------------------- | ---------------------------------------- | ------------- |
| GET    | `/users/`               | Get current user's profile               | ✅            |
| PUT    | `/users/change-password`| Change password (verifies current first) | ✅            |

#### Change password — example payload:

```json
{
  "password": "current_password",
  "new_password": "new_secure_password"
}
```

---

### 🔒 Admin Router (`/admin`) — role `"admin"` required

| Method | Path                    | Description               | Auth required     |
| ------ | ----------------------- | ------------------------- | ----------------- |
| GET    | `/admin/todos`          | View all todos (all users)| ✅ admin only     |
| DELETE | `/admin/todos/{todo_id}`| Delete any todo           | ✅ admin only     |

Non-admin users receive `401 Unauthorized` on any admin route.

---

## 🔐 Role-Based Access Control

The `role` field is now included in the JWT payload at login:

```python
encode = {"sub": username, "id": user_id, "role": role}
```

`get_current_user()` decodes and returns it:

```python
return {"username": username, "id": user_id, "role": user_role}
```

Admin routes check it directly:

```python
if user is None or user.get("role") != "admin":
    raise HTTPException(status_code=401, detail="Authentication Failed")
```

To create an admin user, register with `"role": "admin"` in the request body.

---

## 🔒 Ownership Enforcement

All todo queries now include a second filter on `owner_id`:

```python
db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
```

This ensures users can only read, update, or delete their own todos — even if they guess another todo's ID.

---

## 🏗️ Project Structure

```
day-52/
├── main.py
├── database.py
├── models.py
├── todosapp.db
└── routers/
    ├── auth.py
    ├── todos.py
    ├── users.py
    └── admin.py
```

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding a `phone_number` field to the `Users` model and a route to update it
- Implementing token refresh so users don't have to log in every 20 minutes
- Returning `403 Forbidden` instead of `401` for role violations (semantically more correct)
- Adding pagination to `GET /admin/todos`
- Writing unit tests for each router using `pytest` and FastAPI's `TestClient`

---

## ⚠️ Notes

- The `SECRET_KEY` in `auth.py` must be replaced with a strong random value in production
- JWT tokens expire after **20 minutes** — clients must re-authenticate after expiry
- The new password in `change-password` requires a minimum length of 6 characters
- Admin access is purely role-string based — set `role = "admin"` at registration to gain admin rights

---

Happy coding! 🛡️✅🐍🚀