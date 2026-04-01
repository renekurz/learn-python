# 🐍 Day 40 – Templating with Jinja & Dynamic Web Apps in Flask

Welcome to **Day 40** of the Python learning journey!
Today dives deeper into **Jinja templating** in Flask and shows how to build **fully dynamic web applications** by combining templates, logic, and even external APIs.

You will progress from simple variable injection to **multi-page apps with dynamic data and URL handling**.

---

## 📚 Topics Covered

- Jinja templating (`{{ }}`, `{% %}`)
- Passing data from Python to HTML
- Using conditionals and loops in templates
- Combining Flask with external APIs
- Rendering multiple pages
- Building dynamic URLs with Flask (`url_for`)
- Structuring multi-page Flask apps

---

## 📂 Files Overview

### 📁 `01-using-jinja-to-produce-dynamic-html-pages/`

| File                   | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| `main.py`              | Basic Flask app passing variables to a template       |
| `templates/index.html` | Displays dynamic values using Jinja (e.g. name, year) |

---

### 📁 `02-combining-jinja-templating-with-api/`

| File                   | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `main.py`              | Fetches data (e.g. age/gender prediction) from APIs |
| `templates/index.html` | Input page or homepage                              |
| `templates/guess.html` | Displays dynamic API results (name → age/gender)    |

---

### 📁 `03-multiline-statements-with-jinja/`

| File                   | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `main.py`              | Passes structured data (e.g. blog posts) to templates        |
| `templates/index.html` | Entry page                                                   |
| `templates/guess.html` | Dynamic result page                                          |
| `templates/blog.html`  | Uses Jinja loops (`{% for %}`) to render multiple blog posts |

---

### 📁 `04-url-building-with-flask/`

| File                   | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `main.py`              | Demonstrates dynamic routing and `url_for()` usage |
| `templates/index.html` | Homepage with navigation links                     |
| `templates/guess.html` | Dynamic page using URL parameters                  |
| `templates/blog.html`  | Blog page with dynamic routing                     |

---

## 🎯 Learning Goal

By the end of Day 40, you should be able to:

- Use Jinja to render dynamic HTML
- Pass variables, lists, and objects to templates
- Use loops and conditionals in HTML
- Combine Flask with external APIs
- Build multi-page web applications
- Generate dynamic URLs with `url_for()`

---

## 🚀 How to Run

Install Flask (and requests if needed):

```bash id="x8n3pz"
pip install flask requests
```

Run any project folder:

```bash id="k4m2vl"
cd 01-using-jinja-to-produce-dynamic-html-pages
python3 main.py
```

Then open:

```id="p7r9dw"
http://127.0.0.1:5000
```

---

## 🧠 Main Projects & Concepts

### 🌐 Dynamic HTML with Jinja

- Inject variables into HTML:

```html id="q1x7mz"
{{ name }}
```

- Example:
  - Current year
  - Random numbers
  - User input

---

### 🔮 API + Templates

- Fetch data from APIs (e.g. age prediction)
- Pass results to templates
- Display dynamic user-specific content

---

### 🔁 Loops & Conditions

- Use loops:

```html id="t6k2pa"
{% for post in posts %}
```

- Render multiple elements dynamically (e.g. blog posts)

---

### 🔗 URL Building

- Use Flask’s `url_for()` instead of hardcoding URLs
- Create dynamic routes and navigation
- Build scalable multi-page apps

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding forms for user input
- Styling pages with CSS
- Creating reusable layouts (base template)
- Connecting to a real database
- Adding error handling for API requests
- Building a complete blog system

---

## ⚠️ Notes

- Jinja syntax:
  - `{{ }}` → variables
  - `{% %}` → logic (loops, conditions)

- Flask automatically uses the `templates/` folder

---

Happy coding! 🌐🐍🚀
