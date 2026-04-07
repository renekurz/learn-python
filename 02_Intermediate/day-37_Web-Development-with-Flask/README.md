# 🐍 Day 37 – Web Development with Flask & Python Decorators

Welcome to **Day 37** of the Python learning journey!
Today introduces **Flask**, your first **web server in Python**, and also explores an important Python concept used heavily in Flask: **functions as first-class objects** and **decorators**.

You will learn how routing works in Flask and why decorators are such a powerful feature in Python.

---

## 📚 Topics Covered

- Creating your first web server with **Flask**
- Understanding `@app.route()`
- Running Flask apps in different ways
- The special `__name__ == "__main__"` check
- Functions as first-class objects
- Passing functions as arguments
- Nested functions
- Returning functions from functions
- Python decorators
- Creating your own custom decorator

---

## 📂 Files Overview

### 📄 Core Scripts

| File                                         | Description                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `01-first-web-server-with-flask.py`          | Creates the first basic Flask server with a single `/` route returning `"Hello, World!"`                                |
| `02-special-attributes-built-into-python.py` | Expands the Flask example with an additional `/bye` route and uses `if __name__ == "__main__":` to run the app directly |
| `03-passing-and-nesting-functions.py`        | Demonstrates function basics beyond Flask: passing functions, nested functions, and returning functions                 |
| `04-python-decorater-functions.py`           | Introduces Python decorators by adding a delay before function execution                                                |
| `05-create-your-own-python-decorator.py`     | Builds a custom decorator that measures and prints how long a function takes to run                                     |

---

## 🎯 Learning Goal

By the end of Day 37, you should be able to:

- Start a simple Flask web app
- Understand how Flask routes use decorators
- Run Flask apps from Python files
- Pass functions as arguments in Python
- Understand nested and returned functions
- Write and use your own decorators

---

## 🚀 How to Run

Install Flask first:

```bash id="20831a"
pip install flask
```

You can run the first Flask example with:

```bash id="7c4f1e"
export FLASK_APP=01-first-web-server-with-flask.py
flask run
```

Or run the second Flask example directly with Python:

```bash id="0de5a1"
python3 02-special-attributes-built-into-python.py
```

For the decorator examples:

```bash id="4c7d90"
python3 03-passing-and-nesting-functions.py
python3 04-python-decorater-functions.py
python3 05-create-your-own-python-decorator.py
```

---

## 🧠 Main Projects & Exercises

### 🌐 First Flask Web Server

The first two files focus on Flask basics:

- creating a Flask app
- defining routes with `@app.route()`
- returning text in the browser
- understanding how to launch the server

### 🧩 Functions & Decorators

The later files explain the Python concepts that make Flask possible:

- functions can be passed like variables
- functions can live inside other functions
- functions can be returned from other functions
- decorators wrap extra behavior around existing functions

### ⏱️ Custom Speed Decorator

The final script creates a decorator that:

- records the start time
- runs the target function
- records the end time
- prints how long the function needed

This is a great introduction to reusable function wrappers.

---

## 💡 Improvements & Ideas

Try extending the exercises by:

- adding more Flask routes like `/about` or `/contact`
- returning HTML instead of plain text
- creating a decorator that logs function calls
- creating a decorator with arguments
- measuring runtime for functions with parameters
- combining Flask with your own custom decorators

---

## ⚠️ Notes

- `01-first-web-server-with-flask.py` is meant to be started with `flask run`
- `02-special-attributes-built-into-python.py` can be started directly with `python3`
- The ZIP also contains a `__pycache__/` folder, which only stores compiled Python cache files and is usually not important for learning

---

Happy coding! 🌐🐍🚀
