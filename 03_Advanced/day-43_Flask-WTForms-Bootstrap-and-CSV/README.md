# 🐍 Day 43 – Flask, WTForms, Bootstrap & CSV Data

Welcome to **Day 43** of the Python learning journey!
Today combines multiple concepts to build a complete web application using **Flask**, **WTForms**, **Bootstrap**, and **CSV data storage**.

You will create a web app where users can **add cafes** and **view a list of cafes**, with data stored in a CSV file.

---

## 📚 Topics Covered

- Flask routing & multi-page apps
- WTForms (defined inside `main.py`)
- Bootstrap for styling
- Working with static files (CSS)
- Reading and writing CSV files
- Handling form submissions
- Template inheritance

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| `main.py` | Flask app that defines the WTForms form, handles routes, and manages CSV data |

---

### 📊 Data File

| File            | Description                                      |
| --------------- | ------------------------------------------------ |
| `cafe-data.csv` | Stores cafe data (name, location, ratings, etc.) |

---

### 📁 `templates/`

| File         | Description                                         |
| ------------ | --------------------------------------------------- |
| `base.html`  | Base layout template (shared structure + Bootstrap) |
| `index.html` | Homepage                                            |
| `add.html`   | Form page to add a new cafe                         |
| `cafes.html` | Displays all cafes from the CSV file                |

---

### 📁 `static/`

| File            | Description                    |
| --------------- | ------------------------------ |
| `css/style.css` | Custom styling for the web app |

---

## 🎯 Learning Goal

By the end of Day 43, you should be able to:

- Build a multi-page Flask application
- Create and handle forms using WTForms
- Store and retrieve data using CSV files
- Use Bootstrap and custom CSS for styling
- Structure a real-world mini web app

---

## 🚀 How to Run

Install required packages:

```bash id="z3k8pz"
pip install flask flask-wtf
```

Run the app:

```bash id="x4n2ql"
python3 main.py
```

Open in your browser:

```id="p9r7lt"
http://127.0.0.1:5002
```

---

## 🧠 Main Project

### ☕ Cafe Tracker App

#### ➕ Add Cafe

- User fills out a form (`add.html`)
- WTForms validates input
- Data is saved into `cafe-data.csv`

#### 📋 View Cafes

- Reads data from CSV file
- Displays all cafes in a table (`cafes.html`)

---

## 🧩 Template Structure

- `base.html` → shared layout (Bootstrap + structure)
- Other templates extend it:

```html id="t8x2pa"
{% extends "base.html" %}
```

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding edit/delete functionality
- Sorting or filtering cafes
- Switching from CSV to a database (SQLite)
- Adding maps or location links
- Improving UI with more Bootstrap components

---

## ⚠️ Notes

- WTForms is defined inside `main.py`
- Static files must be placed inside the `static/` folder
- Use `url_for('static', filename='css/style.css')` to link CSS
- CSV is simple but not scalable for production apps

---

Happy coding! ☕🌐🐍🚀
