# 🔐 Day 51 – Todo App: Authentication & Authorization

Welcome to **Day 51** of the Python learning journey!
Today adds a full **authentication system** to the Todo API — with user registration, password hashing, JWT token generation, and protected routes. The app is also refactored into a proper **router-based structure**.

Users now have their own identities, and todos are linked to their owners via a foreign key.

---

## 📚 Topics Covered

- User registration with bcrypt password hashing (`passlib`)
- JWT access token creation and verification (`python-jose`)
- OAuth2 password flow with `OAuth2PasswordRequestForm`
- Protecting routes with `get_current_user` dependency
- Splitting routes into separate files using `APIRouter`
- Linking todos to users with a `ForeignKey`
- Tagging and prefixing routers for clean API organisation

---

## 📂 Files Overview

| File                | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| `main.py`           | App entry point; registers the `auth` and `todos` routers         |
| `database.py`       | SQLAlchemy engine, session factory, and Base                      |
| `models.py`         | `Users` and `Todos` ORM models; todos linked to users via FK      |
| `routers/auth.py`   | Registration, login, JWT creation, and `get_current_user` helper  |
| `routers/todos.py`  | Full CRUD routes for todos (prefixed under `/todos`)              |
| `todosapp.db`       | SQLite database (auto-created on first run)                       |

---

## 🎯 Learning Goal

By the end of Day 51, you should be able to:

- Register users and store bcrypt-hashed passwords
- Authenticate users and issue signed JWT tokens
- Decode and validate JWTs to identify the current user
- Use `APIRouter` to organise routes across multiple files
- Model relationships between database tables with `ForeignKey`

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

## 📦 Data Models

### `Users` table

| Column            | Type    | Description                        |
| ----------------- | ------- | ---------------------------------- |
| `id`              | Integer | Primary key, auto-incremented      |
| `email`           | String  | Unique email address               |
| `username`        | String  | Unique username                    |
| `first_name`      | String  | First name                         |
| `last_name`       | String  | Last name                          |
| `hashed_password` | String  | bcrypt-hashed password             |
| `is_active`       | Boolean | Account active status (default: True) |
| `role`            | String  | User role                          |

### `Todos` table

| Column      | Type    | Description                            |
| ----------- | ------- | -------------------------------------- |
| `id`        | Integer | Primary key, auto-incremented          |
| `title`     | String  | Todo title                             |
| `description`| String | Short description                      |
| `priority`  | Integer | Priority level (0–6)                   |
| `complete`  | Boolean | Completion status (default: False)     |
| `owner_id`  | Integer | Foreign key → `users.id`              |

---

## 🗺️ Routes Overview

### 🔑 Auth Router (`/auth`)

| Method | Path          | Description                              | Status         |
| ------ | ------------- | ---------------------------------------- | -------------- |
| POST   | `/auth/`      | Register a new user                      | `201 Created`  |
| POST   | `/auth/token` | Log in and receive a JWT access token    | `200 OK`       |

#### Register — example payload:

```json
{
  "username": "jondoe",
  "email": "jon@doe.com",
  "first_name": "Jon",
  "last_name": "Doe",
  "password": "password",
  "role": "User Role"
}
```

#### Login response:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

---

### ✅ Todos Router (`/todos`)

| Method | Path               | Description                  | Status              |
| ------ | ------------------ | ---------------------------- | ------------------- |
| GET    | `/todos/`          | Get all todos                | `200 OK`            |
| GET    | `/todos/{todo_id}` | Get a todo by ID             | `200 OK`            |
| POST   | `/todos/`          | Create a new todo            | `201 Created`       |
| PUT    | `/todos/{todo_id}` | Update an existing todo      | `204 No Content`    |
| DELETE | `/todos/{todo_id}` | Delete a todo                | `204 No Content`    |

---

## 🔐 Authentication Flow

```
1. POST /auth/        → Register user (password stored as bcrypt hash)
2. POST /auth/token   → Login with username + password
                     ← Receive JWT access token (valid 20 minutes)
3. Add header:        Authorization: Bearer <token>
4. Protected routes   → JWT decoded → user identity confirmed
```

The `get_current_user()` function decodes the JWT and returns `{"username": ..., "id": ...}`. Any route can inject it as a dependency to identify the calling user.

---

## 🏗️ Project Structure

```
day-51/
├── main.py
├── database.py
├── models.py
├── todosapp.db
└── routers/
    ├── auth.py
    └── todos.py
```

---

## 💡 Improvements & Ideas

Try extending the project by:

- Filtering todos in `GET /todos/` to only return the current user's todos
- Adding `@login_required`-style protection to all todo routes using `get_current_user`
- Adding an admin role with access to all users' todos
- Implementing token refresh with a longer-lived refresh token
- Adding email verification on registration

---

## ⚠️ Notes

- The `SECRET_KEY` in `auth.py` should be replaced with a strong random value in production — never hardcode it
- JWT tokens expire after **20 minutes** — clients must re-authenticate after expiry
- `owner_id` on todos is stored but not yet enforced in route logic — todos are still accessible by any authenticated user
- `passlib` handles bcrypt hashing; `python-jose` handles JWT encoding and decoding

---

Happy coding! 🔐✅🐍🚀