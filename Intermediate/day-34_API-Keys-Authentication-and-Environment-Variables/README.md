# 🐍 Day 34 – API Keys, Authentication & Environment Variables

Welcome to **Day 34** of the Python learning journey!
Today focuses on working with **API authentication**, specifically using **API keys**, and securely managing sensitive data using **environment variables (`.env`)**.

You will learn how to access protected APIs and structure your code in a secure and reusable way.

---

## 📚 Topics Covered

- What API keys are and why they are needed
- Authentication using API keys
- Making authenticated HTTP requests
- Using environment variables with `.env`
- Loading environment variables in Python (`python-dotenv`)
- Securing sensitive data (API keys, coordinates, etc.)

---

## 📂 Files Overview

### 📄 Core Script

| File                           | Description                                                    |
| ------------------------------ | -------------------------------------------------------------- |
| `01-api-key-authentication.py` | Fetches weather data from the OpenWeather API using an API key |

---

### 🔐 `.env` File

Stores sensitive data such as API keys and personal coordinates.

Example structure:

```
OPENWEATHERMAP_API_KEY=
LATITUDE=
LONGITUDE=
```

_(Never commit real credentials to GitHub!)_

---

## 🎯 Learning Goal

By the end of Day 34, you should be able to:

- Understand how APIs use authentication
- Use API keys in requests
- Protect sensitive data using environment variables
- Load `.env` variables in Python scripts
- Work with real-world APIs that require authentication

---

## 🚀 How to Run

Make sure you have installed the required package:

```bash
pip install python-dotenv requests
```

Then run the script:

```bash
python3 01-api-key-authentication.py
```

---

## 🧠 Main Project

### 🌦️ Weather API Request

- Uses the **OpenWeatherMap API**
- Sends latitude & longitude as parameters
- Authenticates using an API key
- Returns weather forecast data (status code check)

---

## 💡 Improvements & Ideas

Try extending the project by:

- Parsing and printing actual weather data instead of just the status code
- Adding error handling for invalid API keys
- Converting timestamps into readable formats
- Creating a CLI tool for weather lookup
- Sending weather alerts via email or notifications

---

Happy coding! 🌍🔑💻
