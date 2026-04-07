# 🐍 Day 41 – POST Requests with Flask & HTML Forms

Welcome to **Day 41** of the Python learning journey!
Today focuses on handling **HTML forms** and making **POST requests** with Flask.

You will learn how users can send data from a webpage to your Flask backend and how to process that data in Python.

---

## 📚 Topics Covered

- HTML forms (`<form>`)
- GET vs POST requests
- Handling form data in Flask
- Using `request` from Flask
- Sending data from frontend → backend
- Creating simple user interactions

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `main.py` | Flask app handling GET and POST requests and processing form input |

---

### 📁 `templates/`

| File         | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| `index.html` | Homepage with navigation or link to the form                   |
| `login.html` | HTML form where the user submits data (e.g. username/password) |

---

## 🎯 Learning Goal

By the end of Day 41, you should be able to:

- Create HTML forms
- Send data using POST requests
- Access form data in Flask
- Handle user input on the backend
- Build interactive web pages

---

## 🚀 How to Run

Install Flask:

```bash id="a8k3mz"
pip install flask
```

Run the app:

```bash id="w2n9qx"
python3 main.py
```

Open in your browser:

```id="p4r7lt"
http://127.0.0.1:5000
```

---

## 🧠 Main Project

### 📝 Login Form (GET & POST)

- Displays a form where the user enters data
- Sends data to Flask using **POST**
- Flask processes the input using:

```python id="f3k8zd"
from flask import request
```

- Access form values:

```python id="m7q2xp"
request.form.get("username")
```

---

## 🔄 GET vs POST

| Method | Description                           |
| ------ | ------------------------------------- |
| GET    | Retrieves data (URL parameters)       |
| POST   | Sends data securely (form submission) |

---

## 💡 Improvements & Ideas

Try extending the project by:

- Validating user input
- Adding error messages
- Redirecting after form submission
- Storing data in a database
- Creating a real login system
- Styling the form with CSS

---

## ⚠️ Notes

- Form `method="POST"` is required for sending secure data
- Always validate user input (never trust raw input)
- Flask automatically handles routing for GET/POST

---

Happy coding! 🌐🐍🚀
