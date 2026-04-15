# ⚡ Day 48 – Move Fast with FastAPI

Welcome to **Day 48** of the Python learning journey!
Today takes FastAPI to the next level by introducing **Pydantic data validation**, **typed path and query parameters**, and **proper HTTP status codes and error handling**.

The book API from Day 47 gets a serious upgrade — with structured models, input constraints, and meaningful error responses.

---

## 📚 Topics Covered

- Pydantic `BaseModel` and `Field` for request validation
- `Path()` and `Query()` for validating URL and query parameters
- Raising `HTTPException` with proper status codes
- Returning correct HTTP status codes via `starlette.status`
- Auto-incrementing IDs with a helper function
- Swagger UI example schemas with `json_schema_extra`
- Filtering books by rating and published date

---

## 📂 Files Overview

| File       | Description                                                        |
| ---------- | ------------------------------------------------------------------ |
| `books.py` | FastAPI app with Pydantic models, validation, and full CRUD routes |

---

## 🎯 Learning Goal

By the end of Day 48, you should be able to:

- Define and use Pydantic models for request body validation
- Validate path and query parameters with `Path()` and `Query()`
- Raise proper HTTP exceptions instead of returning raw error dicts
- Use explicit status codes for every route
- Auto-generate IDs for new resources

---

## 🚀 How to Run

Install required packages (if not already installed):

```bash
pip install fastapi uvicorn pydantic
```

Start the server:

```bash
uvicorn books:app --reload
```

Open the interactive API docs in your browser:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Data Models

### `Book` (internal)

| Field            | Type | Description         |
| ---------------- | ---- | ------------------- |
| `id`             | int  | Unique identifier   |
| `title`          | str  | Book title          |
| `author`         | str  | Author name         |
| `description`    | str  | Short description   |
| `rating`         | int  | Rating from 0 to 5  |
| `published_date` | int  | Year of publication |

### `BookRequest` (Pydantic — used for POST and PUT)

| Field            | Type           | Constraints                    |
| ---------------- | -------------- | ------------------------------ |
| `id`             | int (optional) | Auto-assigned on create        |
| `title`          | str            | Min length: 3                  |
| `author`         | str            | Min length: 1                  |
| `description`    | str            | Min length: 1, max length: 100 |
| `rating`         | int            | 0 – 5                          |
| `published_date` | int            | 2000 – 2030                    |

---

## 🗺️ Routes Overview

### 📖 Get All Books

```
GET /books
```

Returns all books. Status: `200 OK`

---

### 🔍 Get Book by ID

```
GET /books/{book_id}
```

Path parameter `book_id` must be greater than 0. Raises `404` if not found. Status: `200 OK`

---

### ⭐ Get Books by Rating

```
GET /books/?book_rating=5
```

Query parameter `book_rating` must be between 0 and 5. Raises `404` if no books match. Status: `200 OK`

---

### 📅 Get Books by Published Date

```
GET /books/publish/?published_date=2023
```

Query parameter `published_date` must be between 2000 and 2030. Raises `404` if no books match. Status: `200 OK`

---

### ➕ Create Book

```
POST /create-book
```

Expects a `BookRequest` JSON body. ID is auto-assigned. Status: `201 Created`

```json
{
  "title": "A new Book",
  "author": "Stephen King",
  "description": "A new description of a book",
  "rating": 5,
  "published_date": 2026
}
```

---

### ✏️ Update Book

```
PUT /books/update-book
```

Expects a full `BookRequest` body including the `id` of the book to update. Raises `404` if not found. Status: `204 No Content`

---

### 🗑️ Delete Book

```
DELETE /books/{book_id}
```

Path parameter `book_id` must be greater than 0. Raises `404` if not found. Status: `204 No Content`

---

## 🗃️ Sample Data

| ID  | Title                | Author   | Rating | Published |
| --- | -------------------- | -------- | ------ | --------- |
| 1   | Computer Science Pro | Author 1 | 5      | 2005      |
| 2   | Be Fast with FastAPI | Author 1 | 5      | 2013      |
| 3   | Master Endpoints     | Author 2 | 5      | 2023      |
| 4   | HP1                  | Author 2 | 2      | 2019      |
| 5   | HP2                  | Author 2 | 3      | 2025      |
| 6   | HP3                  | Author 3 | 1      | 2009      |

---

## 💡 Improvements & Ideas

Try extending the project by:

- Adding a `GET /books/author/` route to filter by author name
- Persisting data in a database (e.g. SQLite with SQLAlchemy)
- Adding a `PATCH` route for partial updates
- Returning the created or updated book in the response body
- Adding pagination to `GET /books`

---

## ⚠️ Notes

- Data is stored **in memory** — all changes are lost on server restart
- IDs are auto-incremented based on the last entry in the list
- The Swagger UI at `/docs` shows example payloads from `json_schema_extra`
- `starlette.status` constants are used throughout for readable status codes

---

Happy coding! 📚⚡🐍🚀
