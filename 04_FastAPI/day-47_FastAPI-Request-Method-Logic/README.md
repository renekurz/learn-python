# 📚 Day 47 – FastAPI Request Method Logic

Welcome to **Day 47** of the Python learning journey!
Today focuses on building a **RESTful API with FastAPI** — using all core HTTP request methods to manage a book collection in memory.

Instead of just reading data, your API now supports full **CRUD operations**: Create, Read, Update, and Delete.

---

## 📚 Topics Covered

- Setting up a FastAPI app
- Defining routes with `@app.get`, `@app.post`, `@app.put`, `@app.delete`
- Path parameters and query parameters
- Reading request body with `Body()`
- Case-insensitive filtering and lookups
- In-memory data storage with a Python list

---

## 📂 Files Overview

| File       | Description                                         |
| ---------- | --------------------------------------------------- |
| `books.py` | FastAPI app with all CRUD routes for managing books |

---

## 🎯 Learning Goal

By the end of Day 47, you should be able to:

- Build a working REST API with FastAPI
- Use path parameters to identify resources
- Use query parameters to filter results
- Read JSON body data from POST and PUT requests
- Implement all four core HTTP methods: GET, POST, PUT, DELETE

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn
```

Start the server:

```bash
uvicorn books:app --reload
```

Open in your browser or use the interactive docs:

```
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

---

## 🗺️ Routes Overview

### 🏠 Home

```
GET /
```

Returns a welcome message.

---

### 📖 Get All Books

```
GET /books
```

Returns all books. Optionally filter by category using a query parameter:

```
GET /books?category=math
```

---

### 🔍 Get Book by Title

```
GET /books/{book_title}
```

Returns a single book by its title (case-insensitive). Returns an error if not found.

---

### ➕ Create Book

```
POST /books/create_book
```

Adds a new book. Expects a JSON body:

```json
{
  "title": "Title Seven",
  "author": "Author Seven",
  "category": "science"
}
```

---

### ✏️ Update Book

```
PUT /books/update_book
```

Updates an existing book matched by title. Expects a full JSON body with the updated data.

---

### 🗑️ Delete Book

```
DELETE /books/delete_book/{book_title}
```

Deletes a book by its title (case-insensitive). Returns an error if not found.

---

## 🗃️ Sample Data

The app comes pre-loaded with 6 books:

| Title       | Author       | Category |
| ----------- | ------------ | -------- |
| Title One   | Author One   | science  |
| Title Two   | Author Two   | science  |
| Title Three | Author Three | history  |
| Title Four  | Author Four  | math     |
| Title Five  | Author Five  | math     |
| Title Six   | Author Two   | math     |

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding Pydantic models for request body validation
- Returning proper HTTP status codes (e.g. `404`, `204`) using `HTTPException`
- Persisting data in a database (e.g. SQLite with SQLAlchemy)
- Adding a `/books/author/{author_name}` route to filter by author
- Adding pagination to `GET /books`

---

## ⚠️ Notes

- Data is stored **in memory** — all changes are lost when the server restarts
- The interactive Swagger UI at `/docs` is a great way to test all endpoints
- FastAPI auto-generates OpenAPI documentation at `/openapi.json`

---

Happy coding! 📚🐍⚡🚀
