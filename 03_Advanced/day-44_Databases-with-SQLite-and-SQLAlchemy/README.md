# 🐍 Day 44 – Databases with SQLite & SQLAlchemy

Welcome to **Day 44** of the Python learning journey!
Today introduces working with **databases** in Flask using **SQLite** and **SQLAlchemy**.

Instead of storing data in plain files like CSV, this project saves data in a real database and displays it through a Flask web app.

---

## 📚 Topics Covered

- SQLite basics
- Using SQLAlchemy with Flask
- Creating a database model
- Storing persistent data
- Reading data from a database
- Adding new entries through a Flask form
- Connecting Flask routes with database operations

---

## 📂 Files Overview

### 📄 Core Files

| File               | Description                                                                         |
| ------------------ | ----------------------------------------------------------------------------------- |
| `main.py`          | Flask app that defines the database model, creates the database, and handles routes |
| `requirements.txt` | Lists the Python packages needed for this project                                   |

---

### 📁 `templates/`

| File         | Description                                       |
| ------------ | ------------------------------------------------- |
| `index.html` | Displays the list of books stored in the database |
| `add.html`   | Form page to add a new book                       |

---

### 📁 `instance/`

| File       | Description                                |
| ---------- | ------------------------------------------ |
| `books.db` | SQLite database file storing the book data |

---

## 🎯 Learning Goal

By the end of Day 44, you should be able to:

- Understand how SQLite databases work in Flask
- Use SQLAlchemy to define a model
- Save and retrieve data from a database
- Display database content in HTML templates
- Add new records through a web form

---

## 🚀 How to Run

Install the required packages:

```bash id="67102a"
pip install -r requirements.txt
```

Run the app:

```bash id="41783b"
python3 main.py
```

Open in your browser:

```id="95831c"
http://127.0.0.1:5000
```

---

## 🧠 Main Project

### 📚 Book Collection App

This project builds a small Flask app for storing books in a database.

#### Features

- View all saved books on the homepage
- Add a new book through a form
- Store the data permanently in `books.db`

---

## 🧩 Database Model

The database model in `main.py` includes:

- `id` → unique identifier
- `title` → book title
- `author` → author name
- `rating` → book rating

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding an edit route for updating ratings
- Adding a delete function
- Sorting books by rating or title
- Adding search functionality
- Moving from SQLite to PostgreSQL later

---

## ⚠️ Notes

- The database file is stored in the `instance/` folder
- `requirements.txt` should be installed before running the app
- On Windows type:
  - python -m pip install -r requirements.txt
- On MacOS type:
  - pip3 install -r requirements.txt

---

Happy coding! 📚🐍💾🚀
