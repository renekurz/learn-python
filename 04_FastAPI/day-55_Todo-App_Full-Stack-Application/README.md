# 🌐 Day 55 – Todo App: Full-Stack Application

Welcome to **Day 55** of the Python learning journey!
Today transforms the Todo API into a **full-stack web application** by adding a complete HTML frontend with Jinja2 templates, Bootstrap styling, and vanilla JavaScript. Users can now register, log in, and manage their todos entirely through a browser — no API client needed.

The JWT token is stored as a browser cookie and automatically attached to every API call from the frontend.

---

## 📚 Topics Covered

- Serving HTML pages with `Jinja2Templates` in FastAPI
- Mounting a `static/` directory for CSS, JS, and Bootstrap assets
- Cookie-based JWT authentication for browser sessions
- Reading the JWT from `request.cookies` in page routes
- Redirecting unauthenticated users to the login page
- Vanilla JavaScript `fetch()` calls to the existing REST API
- Storing and deleting JWT tokens as browser cookies
- Jinja2 template inheritance with `layout.html` and `{% include %}`
- Conditional rendering in templates with `{% if %}` and `{% for %}`

---

## 📂 Files Overview

### Changed files

| File                | Change                                                              |
| ------------------- | ------------------------------------------------------------------- |
| `main.py`           | Mounts `static/` directory; root `/` redirects to todo page        |
| `routers/auth.py`   | Added `login-page` and `register-page` page routes; `phone_number` added to `CreateUserRequest` |
| `routers/todos.py`  | Added `todo-page`, `add-todo-page`, and `edit-todo-page` page routes |

### New: Templates (`templates/`)

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `layout.html`      | Base layout — loads Bootstrap CSS/JS and includes navbar |
| `navbar.html`      | Responsive navbar; shows Login/Logout based on auth state |
| `home.html`        | Simple welcome page                                      |
| `login.html`       | Login form (username + password)                         |
| `register.html`    | Registration form (all user fields + password confirm)   |
| `todos.html`       | Todo list table; completed todos styled with strikethrough |
| `add-todo.html`    | Form to create a new todo                                |
| `edit-todo.html`   | Form to edit an existing todo; includes delete button    |

### New: Static assets (`static/`)

| File                  | Description                                        |
| --------------------- | -------------------------------------------------- |
| `css/bootstrap.css`   | Bootstrap 4 stylesheet                             |
| `css/base.css`        | Custom app styles                                  |
| `js/base.js`          | All frontend logic: login, register, CRUD, cookies |
| `js/bootstrap.js`     | Bootstrap 4 JavaScript                             |
| `js/jquery-slim.js`   | jQuery (slim) for Bootstrap                        |
| `js/popper.js`        | Popper.js for Bootstrap dropdowns                  |

---

## 🎯 Learning Goal

By the end of Day 55, you should be able to:

- Add an HTML frontend to a FastAPI app using Jinja2 templates
- Serve static files (CSS, JS) with `StaticFiles`
- Authenticate browser sessions using cookies instead of Authorization headers
- Write JavaScript that reads a JWT cookie and attaches it to API requests
- Redirect unauthenticated users gracefully from page routes

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] jinja2 python-multipart
```

Start the server:

```bash
uvicorn main:app --reload
```

Open in your browser:

```
http://127.0.0.1:8000
```

The root `/` redirects automatically to `/todos/todo-page`. Unauthenticated users are redirected to `/auth/login-page`.

---

## 🗺️ Page Routes

These routes render HTML pages for the browser. They are separate from the JSON API endpoints.

### Auth pages (`/auth`)

| Route                  | Template          | Description            |
| ---------------------- | ----------------- | ---------------------- |
| `GET /auth/login-page` | `login.html`      | Login form             |
| `GET /auth/register-page` | `register.html` | Registration form     |

### Todo pages (`/todos`)

| Route                              | Template        | Description                          |
| ---------------------------------- | --------------- | ------------------------------------ |
| `GET /todos/todo-page`             | `todos.html`    | Todo list (auth required via cookie) |
| `GET /todos/add-todo-page`         | `add-todo.html` | Add new todo form                    |
| `GET /todos/edit-todo-page/{id}`   | `edit-todo.html`| Edit / delete existing todo          |

---

## 🔐 Cookie-Based Auth Flow

```
1. User submits login form
   → JS posts credentials to POST /auth/token
   ← Receives JWT access token

2. Token saved as browser cookie:
   document.cookie = `access_token=${data.access_token}; path=/`

3. On each page load, server reads the cookie:
   user = await get_current_user(request.cookies.get("access_token"))

4. Unauthenticated? → 302 redirect to /auth/login-page + cookie deleted

5. Logout:
   → JS deletes all cookies → redirects to /auth/login-page
```

---

## 🖥️ Frontend Logic (`static/js/base.js`)

All user interactions are handled via JavaScript `fetch()` calls to the existing REST API:

| Action           | JS handler        | API call                          |
| ---------------- | ----------------- | --------------------------------- |
| Login            | `loginForm`       | `POST /auth/token`                |
| Register         | `registerForm`    | `POST /auth/`                     |
| Add todo         | `todoForm`        | `POST /todos/`                    |
| Edit todo        | `editTodoForm`    | `PUT /todos/{id}`                 |
| Delete todo      | `deleteButton`    | `DELETE /todos/{id}`              |
| Logout           | `logout()`        | Clears cookies, redirects to login |

The JWT cookie is read by `getCookie('access_token')` and attached as `Authorization: Bearer <token>` on every API call.

---

## 🏗️ Project Structure

```
day-55/
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
├── templates/
│   ├── layout.html
│   ├── navbar.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── todos.html
│   ├── add-todo.html
│   └── edit-todo.html
├── static/
│   ├── css/
│   │   ├── bootstrap.css
│   │   └── base.css
│   └── js/
│       ├── base.js
│       ├── bootstrap.js
│       ├── jquery-slim.js
│       └── popper.js
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

Try extending the project by:

- Adding a `profile` page where users can change their password and phone number in the browser
- Showing flash messages (success/error) after form submissions instead of `alert()`
- Setting the cookie as `HttpOnly` and `Secure` for production safety
- Adding a loading spinner while API requests are in flight
- Deploying the full app to a platform like Render or Railway

---

## ⚠️ Notes

- Page routes read the JWT from `request.cookies` — API routes still use the `Authorization` header
- `python-multipart` is required for `OAuth2PasswordRequestForm` to work with form submissions
- The JWT cookie is **not** `HttpOnly` (by design here) so JavaScript can read and attach it — in production, prefer `HttpOnly` cookies with a separate CSRF strategy
- Completed todos are visually distinguished in `todos.html` with a strikethrough style and green row highlight

---

Happy coding! 🌐✅🐍🚀