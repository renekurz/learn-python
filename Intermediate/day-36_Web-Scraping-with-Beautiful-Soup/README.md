# 🐍 Day 36 – Web Scraping with BeautifulSoup

Welcome to **Day 36** of the Python learning journey!
Today focuses on **Web Scraping**, using the **BeautifulSoup** library to extract and work with HTML data.

You will learn how to parse both **local HTML files** and **live websites**.

---

## 📚 Topics Covered

- What web scraping is
- Understanding HTML structure (tags, attributes)
- Using `requests` to fetch web pages
- Parsing HTML with **BeautifulSoup**
- Finding elements using tags and selectors
- Extracting text and attributes

---

## 📂 Files Overview

### 📄 Core Scripts

| File                                 | Description                                                 |
| ------------------------------------ | ----------------------------------------------------------- |
| `01-parsing-html-and-making-soup.py` | Loads and parses a local HTML file using BeautifulSoup      |
| `02-scraping-a-live-website.py`      | Fetches and scrapes data from a live website using requests |

---

### 📁 Additional Files

| File           | Description                                             |
| -------------- | ------------------------------------------------------- |
| `website.html` | Local HTML file used for practicing parsing and queries |

---

## 🎯 Learning Goal

By the end of Day 36, you should be able to:

- Parse HTML documents with BeautifulSoup
- Navigate and search HTML elements
- Extract data from both local files and live websites
- Understand how real websites are structured
- Build simple scraping scripts

---

## 🚀 How to Run

Install required packages:

```bash
pip install beautifulsoup4 requests
```

Run a script:

```bash
python3 01-parsing-html-and-making-soup.py
```

or

```bash
python3 02-scraping-a-live-website.py
```

---

## 🧠 Main Projects

### 📄 HTML Parsing Practice

- Works with a local HTML file (`website.html`)
- Finds elements like headings, links, and paragraphs
- Helps understand structure before scraping real sites

### 🌐 Live Website Scraper

- Sends a request to a real website
- Parses returned HTML
- Extracts specific data from the page

---

## 💡 Improvements & Ideas

Try extending the project by:

- Extracting links (`href`) and images (`src`)
- Saving results to a file (CSV or TXT)
- Using CSS selectors for more precise scraping
- Handling missing elements safely
- Scraping multiple pages

---

## ⚠️ Important Note

Always respect a website’s **terms of service** when scraping.
Avoid sending too many requests in a short time.

---

Happy coding! 🌐🕸️💻
