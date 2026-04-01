# 🐍 Day 35 – Habit Tracking Project (Pixela API)

Welcome to **Day 35** of the Python learning journey!
Today focuses on building a real-world **Habit Tracking system** using an external API called **Pixela**.

You will learn how to **create users, graphs, and track daily habits** by sending different types of HTTP requests.

---

## 📚 Topics Covered

- Working with a real-world API (**Pixela**)
- Creating users via API
- Authentication using tokens
- Sending POST, PUT, and DELETE requests
- Tracking daily habits with data points (“pixels”)
- Using environment variables (`.env`) for secure data
- Working with dates in Python (`datetime`)

---

## 📂 Files Overview

### 📄 Core Script

| File      | Description                                                             |
| --------- | ----------------------------------------------------------------------- |
| `main.py` | Complete habit tracking workflow using Pixela API (user, graph, pixels) |

---

### 🔐 `.env` File

Stores sensitive data such as your Pixela username and token.

Example structure:

```bash
USERNAME=
TOKEN=
```

_(Never commit real credentials to GitHub!)_

---

## 🎯 Learning Goal

By the end of Day 35, you should be able to:

- Understand how to interact with a REST API
- Authenticate requests using tokens
- Create and manage data on external services
- Track habits programmatically
- Use `.env` files to secure sensitive information

---

## 🚀 How to Run

Install required packages:

```bash
pip install requests python-dotenv
```

Run the script:

```bash
python3 main.py
```

---

## 🧠 Main Project

### 📈 Habit Tracker (Pixela)

This project walks through multiple API steps:

#### 👤 Create User

- Registers a new Pixela account
- Requires username and token
- ⚠️ Only run once (then comment it out)

#### 📊 Create Graph

- Creates a habit graph (e.g. sleep tracking)
- Defines unit, type, and color

#### ➕ Add Pixel (Track Habit)

- Adds a daily data point (e.g. hours slept)
- Uses current date (`datetime`)

#### ✏️ Update Pixel

- Modify an existing entry

#### ❌ Delete Pixel

- Remove a specific day entry

#### 🗑️ Delete Graph

- Removes the entire graph

---

## 💡 Improvements & Ideas

Try extending the project by:

- Asking user input for daily habit values
- Tracking multiple habits (e.g. gym, reading)
- Creating multiple graphs
- Automating daily logging with a scheduler
- Building a simple UI or CLI tool
- Visualizing data locally

---

## 🌐 Useful Link

After creating your graph, you can view it in the browser:

```
https://pixe.la/v1/users/<USERNAME>/graphs/<GRAPH_ID>.html
```

---

Happy coding! 📊🚀💻
