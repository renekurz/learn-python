# 🐍 Day 42 – Building Advanced Forms with WTForms

Welcome to **Day 42** of the Python learning journey!
Today focuses on building **advanced and secure forms** using **WTForms** and integrating them into a **multi-page Flask application**.

You will learn how to validate user input, structure templates properly, and control access based on form data.

---

## 📚 Topics Covered

- WTForms & Flask-WTF basics
- Creating forms in Flask
- Form validation
- Handling POST requests
- Template inheritance (`base.html`)
- Redirecting users based on input
- Building multi-page Flask apps

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                               |
| --------- | ------------------------------------------------------------------------- |
| `main.py` | Flask app that defines the form, handles validation, and controls routing |

---

### 📁 `templates/`

| File           | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| `base.html`    | Base template used for layout and structure (template inheritance) |
| `index.html`   | Homepage                                                           |
| `login.html`   | Form page where user submits login data                            |
| `success.html` | Page shown when login/validation is successful                     |
| `denied.html`  | Page shown when validation fails                                   |

---

## 🎯 Learning Goal

By the end of Day 42, you should be able to:

- Build forms using WTForms inside Flask
- Validate user input securely
- Use template inheritance for cleaner HTML
- Redirect users based on logic
- Create multi-page applications with Flask

---

## 🚀 How to Run

Install required packages:

```bash id="c8m2pz"
pip install flask flask-wtf
```

Run the app:

```bash id="v4n9ql"
python3 main.py
```

Open in your browser:

```id="k7r3lt"
http://127.0.0.1:5000
```

---

## 🧠 Main Project

### 🔐 Login System with Validation

- User enters login data via form (`login.html`)
- WTForms validates the input
- Flask processes the data
- User is redirected based on result:
  - ✅ `success.html` → correct input
  - ❌ `denied.html` → incorrect input

---

## 🧩 Template Structure

- `base.html` → shared layout (header, structure)
- Other templates extend it using:

```html id="t9x2pa"
{% extends "base.html" %}
```

This avoids repeating HTML and keeps code clean.

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding more form fields (email, password rules)
- Showing validation error messages
- Connecting to a real user database
- Hashing passwords (security)
- Adding sessions (login state)
- Styling with Bootstrap

---

## ⚠️ Notes

- Always set a `SECRET_KEY` for Flask-WTF
- Use `form.validate_on_submit()` for validation
- Template inheritance is key for scalable apps

---

Happy coding! 🌐🐍🔐🚀
