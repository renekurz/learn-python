# 🐍 Day 46 – Authentication with Flask

Welcome to **Day 46** of the Python learning journey!
Today focuses on implementing **user authentication** in Flask — including registration, login, logout, and protecting routes so only logged-in users can access them.

Instead of just displaying data, your app now manages **user identities** securely with hashed passwords and session management.

---

## 📚 Topics Covered

- User registration with form data
- Password hashing with Werkzeug
- User login and session management with Flask-Login
- Protecting routes with `@login_required`
- Flash messages for user feedback
- Storing users in a SQLite database
- Serving files to authenticated users only

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                                          |
| --------- | ------------------------------------------------------------------------------------ |
| `main.py` | Flask app with all routes: home, register, login, logout, secrets, and file download |

---

### 📁 `templates/`

| File            | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `base.html`     | Base layout with Bootstrap navbar; shows Login/Register only when logged out |
| `index.html`    | Homepage with Login and Register buttons                                     |
| `register.html` | Registration form (name, email, password)                                    |
| `login.html`    | Login form with flash message support                                        |
| `secrets.html`  | Protected page shown only to logged-in users; includes file download link    |

---

### 📁 `static/`

| File                    | Description                           |
| ----------------------- | ------------------------------------- |
| `css/styles.css`        | Custom CSS styles for the app         |
| `files/cheat_sheet.pdf` | Downloadable file for logged-in users |

---

### 📁 `instance/`

| File       | Description                          |
| ---------- | ------------------------------------ |
| `users.db` | SQLite database storing user records |

---

## 🎯 Learning Goal

By the end of Day 46, you should be able to:

- Register users and store hashed passwords securely
- Implement login and logout with Flask-Login
- Protect routes so only authenticated users can access them
- Display flash messages as user feedback
- Serve files exclusively to logged-in users

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```

Run the app:

```bash
python3 main.py
```

Open in your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 Main Project

### 🔐 Flask Authentication App

This project builds a complete authentication system for a Flask web app.
Users can register, log in, and access a protected secrets page — where they can also download a file.

---

### 🗺️ Routes Overview

#### 🏠 Home

```
/
```

Landing page with Login and Register buttons.

---

#### 📝 Register

```
/register
```

GET: Renders the registration form.
POST: Creates a new user with a hashed password and logs them in immediately.
Redirects to the login page if the email is already registered.

---

#### 🔑 Login

```
/login
```

GET: Renders the login form.
POST: Validates email and password. Redirects to `/secrets` on success, or shows a flash message on failure.

---

#### 🔒 Secrets _(protected)_

```
/secrets
```

Only accessible to logged-in users (`@login_required`).
Welcomes the user by name and shows a link to download the cheat sheet.

---

#### 📥 Download _(protected)_

```
/download
```

Serves `cheat_sheet.pdf` from the `static/files/` folder.

---

#### 🚪 Logout

```
/logout
```

Logs the current user out and redirects to the homepage.

---

## 🔐 Security Details

- Passwords are hashed using **PBKDF2-SHA256** with a salt via `werkzeug.security`
- Duplicate email registrations are caught and redirected with a flash message
- Sessions are managed by **Flask-Login** using a secret key
- The `/secrets` route is protected with `@login_required`

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding email verification on registration
- Implementing a "Forgot Password" flow
- Adding OAuth login (e.g. Google, GitHub)
- Protecting the `/download` route with `@login_required`
- Deploying the app to a cloud platform

---

## ⚠️ Notes

- The `SECRET_KEY` in `main.py` should be replaced with a strong random value in production
- The database file is stored in the `instance/` folder and created automatically on first run
- Flash messages are displayed on the login page using Jinja2's `get_flashed_messages()`

---

Happy coding! 🔐🐍🌐🚀
