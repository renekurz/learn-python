# 🐍 Day 39 – Rendering HTML with Flask (Templates)

Welcome to **Day 39** of the Python learning journey!
Today focuses on rendering real **HTML pages** using Flask with the help of **templates**.

Instead of returning plain text, you will now build proper web pages using HTML.

---

## 📚 Topics Covered

- Rendering HTML with Flask
- Using `render_template()`
- Working with the `templates/` folder
- Connecting Python (backend) with HTML (frontend)
- Basic structure of a web page

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `main.py` | Flask app that renders an HTML page using `render_template()` |

---

### 📁 `templates/`

| File         | Description                          |
| ------------ | ------------------------------------ |
| `index.html` | Main HTML template rendered by Flask |

---

## 🎯 Learning Goal

By the end of Day 39, you should be able to:

- Render HTML files instead of plain text
- Use Flask’s `templates` system
- Understand how backend and frontend connect
- Build simple web pages with Flask

---

## 🚀 How to Run

Install Flask:

```bash id="d8k3pz"
pip install flask
```

Run the app:

```bash id="w5n2ql"
python3 main.py
```

Then open your browser:

```id="c7m9ra"
http://127.0.0.1:5000
```

---

## 🧠 Main Project

### 🌐 First HTML Website with Flask

- Uses `render_template()` to load an HTML file
- Displays structured content in the browser
- Demonstrates how Flask serves real web pages

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding more HTML pages (about, contact)
- Passing data from Python to HTML (Jinja2)
- Adding basic styling (CSS)
- Creating navigation between pages
- Using variables inside templates

---

## ⚠️ Notes

- Flask automatically looks for HTML files inside the `templates/` folder
- File names must match exactly (e.g. `index.html`)
- Restart the server after changes (if debug mode is off)

---

Happy coding! 🌐🐍🚀
