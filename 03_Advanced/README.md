# 🔴 03 Advanced — Days 41 – 46

Welcome to the **Advanced section** of the Python learning journey!

These 6 days take Flask web development to a professional level — covering HTML forms, validated input with WTForms, Bootstrap styling, CSV and database backends, a full REST API, and a complete user authentication system with hashed passwords and session management.

---

## 🎯 What You'll Learn

By the end of this section you will be able to:

- Handle HTML form submissions with GET and POST requests in Flask
- Build and validate forms securely using Flask-WTF and WTForms
- Style web applications with Bootstrap
- Store and retrieve data using CSV files and SQLite databases
- Use SQLAlchemy as an ORM for database interactions
- Build a complete RESTful API with all HTTP methods
- Implement full user authentication: registration, login, logout
- Hash passwords securely with Werkzeug's PBKDF2-SHA256
- Protect routes with `@login_required` using Flask-Login
- Serve files exclusively to authenticated users

---

## 📅 Day-by-Day Overview

| Day | Topic | Project |
| --- | ----- | ------- |
| 41 | POST requests, HTML forms, GET vs POST | Login Form |
| 42 | WTForms, CSRF protection, multi-page flow | WTForms Login & Validation |
| 43 | Flask + WTForms + Bootstrap + CSV storage | Café Directory App |
| 44 | SQLite, SQLAlchemy ORM, CRUD operations | Book Library |
| 45 | REST API design, all HTTP methods, JSON responses | Café REST API |
| 46 | Flask-Login, password hashing, protected routes | User Authentication App |

---

## 🧠 Key Projects

### ☕ Café Directory App (Day 43)
A full web app where users can browse cafés (loaded from CSV) and submit new ones via a Bootstrap-styled WTForms form. Covers the complete request/response cycle with validation and feedback.

### 📚 Book Library (Day 44)
A CRUD web app backed by a real SQLite database via SQLAlchemy. Users can add books, update their ratings, and delete entries — all through a browser interface.

### 🔌 Café REST API (Day 45)
A proper RESTful API that exposes all HTTP methods (`GET`, `POST`, `PATCH`, `DELETE`) on a café database. Returns JSON responses and uses query parameters for filtering. The API is fully testable via Postman or the browser.

### 🔐 User Authentication App (Day 46)
A complete multi-page Flask app with:
- **Registration** — new users stored in SQLite with PBKDF2-SHA256 hashed passwords
- **Login / Logout** — session management via Flask-Login
- **Protected routes** — secrets page and file download only accessible to logged-in users
- **Flash messages** — feedback on failed logins and duplicate registrations

---

## 📂 Folder Structure

```
03_Advanced/
├── day-41_Make-POST-Requests-with-Flask-and-HTML-Forms/
│   └── templates/
├── day-42_Building-Advanced-Forms-with-WTForms/
│   └── templates/
├── day-43_Flask-WTForms-Bootstrap-and-CSV/
│   └── templates/
├── day-44_Databases-with-SQLite-and-SQLAlchemy/
│   └── templates/
├── day-45_Building-your-own-API-with-RESTful-Routing/
│   └── templates/
└── day-46-Authentication-with-Flask/
    ├── templates/
    └── static/
```

---

## 🚀 How to Run

Install required packages:

```bash
pip install flask flask-sqlalchemy flask-login flask-wtf werkzeug
```

Start the server for any day:

```bash
cd day-<N>_<Name>
python3 main.py
```

Then open:

```
http://127.0.0.1:5000
```

Each day folder has its own `README.md` with exact install, route, and usage details.

---

## 🔗 Progression into FastAPI

This section is the bridge between Flask and FastAPI. By the end of Day 46 you are comfortable with:
- Database-backed web apps
- RESTful API design
- User authentication flows

These concepts carry directly into the **04 FastAPI** section, where the same patterns are implemented with a more modern, faster framework.

---

Happy coding! 🐍