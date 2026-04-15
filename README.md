# Learn Python 🐍

A **55-day Python learning journey** from absolute beginner to full-stack web developer.
The course covers core Python fundamentals, GUI programming, APIs, databases, web frameworks, and modern API development with FastAPI — with a new project or concept introduced every day.

---

## 🗺️ Course Overview

| Section | Days | Focus |
| ------- | ---- | ----- |
| [01 Beginner](#01_Beginner) | 1 – 14 | Python fundamentals, logic, functions, mini games |
| [02 Intermediate](#02_Intermediate) | 15 – 40 | OOP, GUIs, APIs, data, web scraping, Flask intro |
| [03 Advanced](#03_Advanced) | 41 – 46 | Flask forms, databases, REST APIs, authentication |
| [04 FastAPI](#04_FastAPI) | 47 – 55 | FastAPI, SQLAlchemy, JWT auth, testing, full-stack |

---

## 🟢 01 Beginner — Days 1 – 14

Core Python syntax and problem-solving through progressively more complex mini projects.

| Day | Topic | Project |
| --- | ----- | ------- |
| 01 | Variables & Strings | Band Name Generator |
| 02 | Data Types & Type Conversion | Tip Calculator |
| 03 | Control Flow & Logical Operators | Treasure Island Adventure |
| 04 | Randomisation & Lists | Rock Paper Scissors |
| 05 | Loops & Range | Password Generator |
| 06 | Functions & While Loops | — |
| 07 | Functions & Parameters | Hangman |
| 08 | Function Parameters & Caesar Cipher | Caesar Cipher |
| 09 | Dictionaries & Nesting | Auction Program |
| 10 | Functions with Outputs & Docstrings | Calculator |
| 11 | Capstone | Blackjack |
| 12 | Scope (Local, Global, Constants) | Number Guessing Game |
| 13 | Debugging Techniques | Debugging Exercises |
| 14 | Capstone | Higher Lower Game |

---

## 🟡 02 Intermediate — Days 15 – 40

Object-oriented programming, GUI development, data handling, external APIs, web scraping, and an introduction to Flask.

| Day | Topic | Project |
| --- | ----- | ------- |
| 15 | Capstone | Coffee Machine |
| 16 | Object-Oriented Programming | Coffee Machine (OOP refactor) |
| 17 | OOP & Classes | Quiz Game |
| 18 | Turtle Graphics & GUI | Spot Painting / Spirograph |
| 19 | Instances, State & Higher-Order Functions | Etch-a-Sketch / Turtle Race |
| 20 | Turtle & OOP | Snake Game Part 1 |
| 21 | OOP & File I/O | Snake Game Part 2 (with high score) |
| 22 | OOP & Multi-class Design | Pong Game |
| 23 | OOP & Game Logic | Turtle Crossing Game |
| 24 | Files, Directories & Paths | Mail Merge / Snake High Score |
| 25 | CSV Files & Pandas | US States Game |
| 26 | List & Dictionary Comprehensions | NATO Alphabet / US States |
| 27 | GUI with Tkinter | Mile to Kilometres Converter |
| 28 | Tkinter Canvas & Dynamic UI | Pomodoro Timer |
| 29 | Tkinter & File I/O | Password Manager |
| 30 | Errors, Exceptions & JSON | Password Manager with JSON |
| 31 | Capstone | Flash Card App |
| 32 | Email, Datetime & Scheduling | Birthday Wisher |
| 33 | API Endpoints & Parameters | ISS Overhead Notifier / Kanye Quotes |
| 34 | API Keys, Auth & Environment Variables | Weather API |
| 35 | Capstone | Habit Tracker (Pixela API) |
| 36 | Web Scraping with BeautifulSoup | Live Website Scraper |
| 37 | Flask & Python Decorators | First Web Server |
| 38 | Flask URL Routing & Debugger | URL Paths & Decorators |
| 39 | Rendering HTML & Static Files | Flask HTML Templates |
| 40 | Jinja2 Templating in Flask | Blog / Guess the Number with Jinja |

---

## 🔴 03 Advanced — Days 41 – 46

Server-side web development with Flask: forms, databases, REST APIs, and user authentication.

| Day | Topic | Project |
| --- | ----- | ------- |
| 41 | POST Requests & HTML Forms in Flask | Login Form |
| 42 | Advanced Forms with WTForms | WTForms Login & Validation |
| 43 | Flask, WTForms, Bootstrap & CSV | Café Directory App |
| 44 | Databases with SQLite & SQLAlchemy | Book Library (CRUD with DB) |
| 45 | Building a REST API with Flask | Café API |
| 46 | Authentication with Flask | User Auth App (register, login, protected routes) |

---

## ⚡ 04 FastAPI — Days 47 – 55

Modern API development with FastAPI, building a complete full-stack Todo application from scratch — with a real database, JWT authentication, role-based access control, Alembic migrations, a full test suite, and an HTML frontend.

| Day | Topic | Project / Focus |
| --- | ----- | --------------- |
| 47 | FastAPI Basics & HTTP Methods | Books API (in-memory CRUD) |
| 48 | Pydantic, Path/Query Validation, HTTPException | Books API with validation |
| 49 | SQLAlchemy Setup & ORM Models | Todo App — Database setup |
| 50 | CRUD with SQLAlchemy & Depends() | Todo App — API endpoints |
| 51 | JWT Auth, APIRouter, bcrypt | Todo App — Auth & Authorization |
| 52 | Ownership Enforcement & RBAC | Todo App — Authenticate Requests |
| 53 | Alembic Migrations | Todo App — `phone_number` migration |
| 54 | pytest, TestClient, Fixtures | Todo App — Unit & Integration Tests |
| 55 | Jinja2 Templates, StaticFiles, Cookies | Todo App — Full-Stack Browser App |

### 📈 Todo App — Day-by-Day Evolution

The Todo App (Days 49–55) is the main capstone project, built incrementally over 7 days:

```
Day 49  Database setup          models.py + database.py + SQLite
Day 50  CRUD API                GET / POST / PUT / DELETE with SQLAlchemy sessions
Day 51  Auth + Routers          JWT, bcrypt, APIRouter (auth + todos)
Day 52  Ownership + RBAC        User-scoped todos, admin router, users router
Day 53  Migrations              Alembic + phone_number column
Day 54  Testing                 pytest, TestClient, fixtures, dependency overrides
Day 55  Full-Stack              Jinja2 templates, Bootstrap, cookie-based auth
```

---

## 🏗️ Repository Structure

```
learn-python/
├── 01_Beginner/
│   ├── day-01_Working-with-Variables/
│   ├── day-02_Understanding-Data-Types/
│   ├── ...
│   └── day-14_Higher-Lower-Game/
│
├── 02_Intermediate/
│   ├── day-15_Coffee-Machine/
│   ├── day-16_Object-Oriented-Programming/
│   ├── ...
│   └── day-40_Templating-with-Jinja-in-Flask/
│
├── 03_Advanced/
│   ├── day-41_Make-POST-Requests-with-Flask-and-HTML-Forms/
│   ├── ...
│   └── day-46-Authentication-with-Flask/
│
└── 04_FastAPI/
    ├── day-47_FastAPI-Request-Method-Logic/
    ├── ...
    └── day-55_Todo-App_Full-Stack-Application/
```

Each day folder contains its own `README.md` with a detailed breakdown of topics, routes, models, and usage instructions.

---

## 🛠️ Technologies Used

| Category | Tools |
| -------- | ----- |
| Language | Python 3 |
| GUI | Turtle, Tkinter |
| Data | Pandas, CSV, JSON |
| Web Scraping | BeautifulSoup4 |
| Web Framework | Flask, FastAPI |
| Templating | Jinja2 |
| Database | SQLite, SQLAlchemy |
| Migrations | Alembic |
| Auth | Flask-Login, Werkzeug, JWT (`python-jose`), bcrypt (`passlib`) |
| Validation | Pydantic, Flask-WTF |
| Testing | pytest, pytest-asyncio, FastAPI TestClient |
| Frontend | Bootstrap 4, vanilla JavaScript, HTML/CSS |

---

## 🚀 Getting Started

Clone the repo and navigate to any day's folder:

```bash
git clone https://github.com/renekurz/learn-python.git
cd learn-python
```

Install dependencies for a specific section (example for FastAPI days):

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] alembic jinja2 python-multipart pytest pytest-asyncio
```

Each day folder has its own README with exact install and run instructions.

---

## 📌 Highlights

- **Hangman** (Day 7) — classic word game with ASCII art and lives tracking
- **Blackjack** (Day 11) — fully playable card game with dealer logic
- **Snake Game** (Days 20–21) — OOP Turtle game with persistent high score
- **Pong** (Day 22) — two-player OOP Turtle game
- **Password Manager** (Days 29–30) — Tkinter GUI with JSON storage
- **Habit Tracker** (Day 35) — integrates with the real Pixela API
- **Café Directory API** (Day 43) — Flask REST API with WTForms and Bootstrap
- **Flask Auth App** (Day 46) — full user auth with hashed passwords and protected routes
- **Todo App** (Days 49–55) — complete full-stack application with database, JWT auth, RBAC, migrations, tests, and a browser frontend

---

Happy coding! 🐍🚀