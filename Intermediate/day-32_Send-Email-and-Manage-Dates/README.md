# 🐍 Day 32 – Sending Emails & Managing Dates

Welcome to **Day 32** of the Python learning journey!
Today focuses on automating real-world tasks using Python, including **sending emails**, working with **dates and times**, and building automation scripts like a **Birthday Wisher**.

---

## 📚 Topics Covered

- Sending emails using SMTP
- Working with environment variables (`.env`)
- Using the `datetime` module
- Automating recurring tasks
- Reading CSV data for automation
- Building real-world automation scripts

---

## 📂 Files Overview

### 📄 Core Scripts

| File                                            | Description                                              |
| ----------------------------------------------- | -------------------------------------------------------- |
| `01-sending-emails.py`                          | Basic example of sending emails using Python             |
| `02-datetime-module.py`                         | Introduction to working with dates and times             |
| `03-motivational-quotes-on-monday-via-email.py` | Sends motivational quotes automatically on specific days |
| `quotes.txt`                                    | Collection of quotes used for email automation           |

---

### 📁 `04-birthday-wisher/`

| File / Folder                                  | Description                                        |
| ---------------------------------------------- | -------------------------------------------------- |
| `main.py`                                      | Main automation script for sending birthday emails |
| `birthdays.csv`                                | Dataset containing names, emails, and birthdays    |
| `letter_templates/`                            | Folder containing customizable email templates     |
| `letter_1.txt`, `letter_2.txt`, `letter_3.txt` | Template variations for birthday emails            |

---

### 🔐 `.env` File

Used to securely store sensitive information like email credentials.

Example structure:

```
EMAIL=
PASSWORD=
```

_(Never commit real credentials to GitHub!)_

---

## 🎯 Learning Goal

By the end of Day 32, you should be able to:

- Send emails programmatically
- Work with environment variables securely
- Use datetime for scheduling logic
- Automate real-world repetitive tasks
- Combine file handling with automation

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash id="7gk2w1"
python3 filename.py
```

Example:

```bash id="f2k9pl"
cd day-32_Send-Email-and-Manage-Dates/04-birthday-wisher
python3 main.py
```

---

## 🧠 Main Project

The **Birthday Wisher** automation:

- Checks today’s date
- Matches it with birthdays in a CSV file
- Selects a random email template
- Sends a personalized email automatically

Try enhancing it by:

- Adding multiple email providers
- Scheduling with cron jobs
- Adding attachments
- Logging sent emails
- Creating a GUI for managing birthdays

---

Happy coding! 📧🎉💻
