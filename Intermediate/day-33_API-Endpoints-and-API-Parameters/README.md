# 🐍 Day 33 – API Endpoints & API Parameters

Welcome to **Day 33** of the Python learning journey!
Today focuses on working with **APIs (Application Programming Interfaces)**, understanding **endpoints**, and using **parameters** to interact with real-world data services.

You will learn how to fetch live data from the internet and build automation scripts based on API responses.

---

## 📚 Topics Covered

- What APIs are and how they work
- Making HTTP requests in Python
- Understanding API endpoints
- Using query parameters
- Parsing JSON responses
- Working with environment variables (`.env`)

---

## 📂 Files Overview

### 📄 Core Scripts

| File                          | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| `01-iss-now.py`               | Fetches real-time location data of the ISS         |
| `03-api-parameters.py`        | Demonstrates how to use API parameters in requests |
| `04-iss-overhead-notifier.py` | Sends a notification when the ISS is overhead      |

---

### 📁 `02-kanye-quotes/`

| File             | Description                                       |
| ---------------- | ------------------------------------------------- |
| `main.py`        | GUI app fetching random Kanye West quotes via API |
| `kanye.png`      | Image asset used in the app                       |
| `background.png` | Background image for GUI                          |

---

### 🔐 `.env` File

Used to store sensitive data such as email credentials or API keys.

Example structure:

```
EMAIL=
PASSWORD=
API_KEY=
```

_(Never commit real credentials to GitHub!)_

---

## 🎯 Learning Goal

By the end of Day 33, you should be able to:

- Make API requests in Python
- Work with JSON responses from APIs
- Use query parameters effectively
- Build applications using live data
- Secure sensitive information using `.env`

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash id="n2v4pl"
python3 filename.py
```

Example:

```bash id="m9z7kc"
cd day-33_API-Endpoints-and-API-Parameters
python3 04-iss-overhead-notifier.py
```

---

## 🧠 Main Projects

### 🛰️ ISS Tracker

- Fetches real-time position of the ISS
- Checks if it is overhead
- Can trigger notifications

### 🎤 Kanye Quotes App

- Fetches random quotes from an API
- Displays them in a GUI

Try enhancing them by:

- Adding more APIs (weather, news, etc.)
- Improving UI design
- Adding notifications (desktop/email)
- Handling API errors gracefully
- Caching responses locally

---

Happy coding! 🌐🚀💻
