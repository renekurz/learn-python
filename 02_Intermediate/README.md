# 🟡 02 Intermediate — Days 15 – 40

Welcome to the **Intermediate section** of the Python learning journey!

These 26 days dramatically expand the toolkit — introducing Object-Oriented Programming, graphical interfaces, file and data handling, external APIs, web scraping, and the first steps into web development with Flask. Projects grow significantly in size and complexity.

---

## 🎯 What You'll Learn

By the end of this section you will be able to:

- Design programs using classes and objects (OOP)
- Build graphical desktop applications with Turtle and Tkinter
- Read and write files, CSVs, and JSON data
- Use list and dictionary comprehensions for clean Pythonic code
- Send emails and work with dates and times programmatically
- Call external APIs with authentication and parameters
- Scrape and parse HTML from live websites
- Build and deploy basic web servers with Flask
- Render dynamic HTML pages using Jinja2 templates

---

## 📅 Day-by-Day Overview

| Day | Topic | Project |
| --- | ----- | ------- |
| 15 | Capstone (procedural) | Coffee Machine |
| 16 | OOP: classes, objects, `__init__` | Coffee Machine (OOP refactor) |
| 17 | OOP: multi-class design | Quiz Game |
| 18 | Turtle graphics, drawing, loops | Spot Painting / Spirograph |
| 19 | Instances, state, higher-order functions, event binding | Etch-a-Sketch / Turtle Race |
| 20 | OOP game development | Snake Game Part 1 |
| 21 | Inheritance, file I/O, persistent high score | Snake Game Part 2 |
| 22 | Multi-class OOP, collision detection | Pong Game |
| 23 | OOP, random spawning, scoreboard | Turtle Crossing Game |
| 24 | File reading/writing, paths, mail merge | Snake High Score / Mail Merge |
| 25 | CSV files, Pandas DataFrames | US States Game |
| 26 | List & dictionary comprehensions, `lambda` | NATO Alphabet / US States |
| 27 | Tkinter widgets, layouts, event handling | Mile to Kilometres Converter |
| 28 | Tkinter Canvas, timers, dynamic UI | Pomodoro Timer |
| 29 | Tkinter + file storage | Password Manager |
| 30 | Exceptions, `try/except`, JSON data | Password Manager with JSON |
| 31 | Capstone — Tkinter + Pandas + CSV | Flash Card App |
| 32 | `smtplib`, `datetime`, scheduling | Birthday Wisher |
| 33 | `requests`, REST APIs, query parameters | ISS Overhead Notifier / Kanye Quotes |
| 34 | API keys, `.env`, `python-dotenv` | Weather API |
| 35 | Capstone — real external API (POST/PUT/DELETE) | Habit Tracker (Pixela) |
| 36 | BeautifulSoup, HTML parsing, live scraping | Website Scraper |
| 37 | Flask, routes, Python decorators | First Web Server |
| 38 | Flask URL routing, dynamic paths, debugger | URL Paths & Decorators |
| 39 | `render_template`, static files | Flask HTML Pages |
| 40 | Jinja2 templating, `{% for %}`, `{% if %}`, URL building | Blog & Guessing Game with Jinja |

---

## 🧠 Key Projects

### 🐍 Snake Game (Days 20–21)
A fully playable OOP Snake game in Turtle graphics. Part 1 builds the snake movement; Part 2 adds food, a scoreboard, collision detection, and a persistent high score saved to a file.

### 🏓 Pong Game (Day 22)
A two-player OOP Pong game. Four separate classes (`Ball`, `Paddle`, `Scoreboard`, `main`) — the largest multi-class project so far.

### 🚗 Turtle Crossing Game (Day 23)
A Frogger-style crossing game with randomly spawning cars that speed up over time, a player character, and a scoreboard.

### 🔐 Password Manager (Days 29–30)
A Tkinter GUI app that generates and stores passwords. Upgraded in Day 30 to use JSON storage with search functionality and robust error handling.

### 🃏 Flash Card App (Day 31)
A Tkinter-based language learning app that flips between the front (foreign word) and back (translation) of flash cards, tracks known words, and saves progress to CSV.

### 🎵 Habit Tracker (Day 35)
Integrates with the real **Pixela API** to create a user, set up a habit graph, and log/update/delete pixel entries — the first project using POST, PUT, and DELETE requests against a live external API.

---

## 📂 Folder Structure

```
02_Intermediate/
├── day-15_Coffee-Machine/
├── day-16_Object-Oriented-Programming/
│   └── 03-coffee-machine-in-oop/
├── day-17_Quiz-Project/
│   └── 02-quiz-game/
├── day-18_Turtle-and-GUI/
├── day-19_Instances-State-and-Higher-Order-Functions/
├── day-20_Snake-Game-Part-1/
├── day-21_Snake-Game-Part-2/
├── day-22_Pong-Game/
├── day-23_Turtle-Crossing-Game/
├── day-24_Files-Directories-Paths/
├── day-25_CSV-Files-and-Panda-Library/
├── day-26_Lists-and-Dictionary-Comprehensions/
├── day-27_GUI-with-Tkinter/
├── day-28_Tkinter-Dynamic-Typing/
├── day-29_Tkinter-Password-Manager/
├── day-30_Errors-Exceptions-and-JSON-Data/
├── day-31_Flash-Card-Project/
├── day-32_Send-Email-and-Manage-Dates/
├── day-33_API-Endpoints-and-API-Parameters/
├── day-34_API-Keys-Authentication-and-Environment-Variables/
├── day-35_Habit-Tracking-Project/
├── day-36_Web-Scraping-with-Beautiful-Soup/
├── day-37_Web-Development-with-Flask/
├── day-38_URL-Parsing-in-Flask/
├── day-39_Rendering-HTML-Static-files/
└── day-40_Templating-with-Jinja-in-Flask/
```

---

## 🚀 How to Run

Install the packages needed for a specific day (examples):

```bash
# GUI projects (Days 18–31)
pip install turtle  # usually built-in

# Data projects (Days 25–26)
pip install pandas

# API projects (Days 33–35)
pip install requests python-dotenv

# Web scraping (Day 36)
pip install beautifulsoup4 requests

# Flask projects (Days 37–40)
pip install flask
```

Each day folder has its own `README.md` with exact install and run instructions.

---

Happy coding! 🐍