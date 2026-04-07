# 🐍 Day 45 – Building Your Own API with RESTful Routing

Welcome to **Day 45** of the Python learning journey!
Today focuses on building your own **RESTful API** using Flask and connecting it to a **database**.

Instead of only rendering HTML pages, you will now create endpoints that return **data (JSON)** and can be used by other applications.

---

## 📚 Topics Covered

- What an API is
- RESTful routing
- Creating endpoints in Flask
- Returning JSON responses
- Working with query parameters
- Using a database inside an API
- Basic error handling

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                              |
| --------- | ------------------------------------------------------------------------ |
| `main.py` | Flask app that defines API routes and interacts with the SQLite database |

---

### 📁 `templates/`

| File         | Description                                       |
| ------------ | ------------------------------------------------- |
| `index.html` | Simple homepage to test or describe API endpoints |

---

### 📁 `instance/`

| File       | Description                       |
| ---------- | --------------------------------- |
| `cafes.db` | SQLite database storing cafe data |

---

## 🎯 Learning Goal

By the end of Day 45, you should be able to:

- Understand how APIs work
- Build RESTful endpoints with Flask
- Return JSON data instead of HTML
- Use query parameters in requests
- Connect an API to a database

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install flask flask-sqlalchemy
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

### 🌐 Cafe API

This project creates a simple API to manage and retrieve cafe data.

---

### 🔍 Example Endpoints

#### 📋 Get a Random Cafe

```
/random
```

Returns a random cafe from the database.

---

#### 🔎 Search Cafe by Location

```
/search?loc=London
```

Uses a query parameter to filter cafes by location.

---

#### ➕ Add New Cafe

```
/add
```

Adds a new cafe via request data.

---

#### ❌ Delete Cafe

```
/delete/<id>
```

Deletes a cafe by ID.

---

## 🧪 Testing with Postman

You can use **Postman** to test your API endpoints more easily than in a browser.

- Send **GET requests** to endpoints like `/random` or `/search`
- Send **POST requests** to `/add` with form or JSON data
- Test delete endpoints like `/delete/<id>`
- Inspect responses (JSON + status codes)

Postman is useful because browsers mainly support GET requests, while APIs require multiple request types.

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding authentication (API key protection)
- Improving error handling with proper status codes
- Creating a frontend to consume the API
- Adding update (PUT/PATCH) endpoints
- Deploying the API online

---

## ⚠️ Notes

- The database file is stored in the `instance/` folder
- API responses are typically returned in JSON format
- Query parameters are accessed via `request.args`

---

Happy coding! 🌐🐍📡🚀
