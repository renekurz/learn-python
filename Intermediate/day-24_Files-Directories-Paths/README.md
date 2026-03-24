# 🐍 Day 24 – Files, Directories & Paths

Welcome to **Day 24** of the Python learning journey!
Today focuses on working with **files**, **directories**, and **file paths** in Python. You will learn how to read, write, and manage files, and apply these concepts in practical mini-projects.

This day also enhances a previous project by adding **persistent high score storage**.

---

## 📚 Topics Covered

- Reading from files
- Writing and appending to files
- File paths and directory structures
- Managing persistent program data
- Working with nested folders
- Automating document generation

---

## 📂 Files Overview

### 📁 `01-add-highscore-to-snake-game/`

Adds **file persistence** to the Snake Game by saving and loading the high score.

| File             | Description                                           |
| ---------------- | ----------------------------------------------------- |
| `main.py`        | Main Snake Game loop with high score integration      |
| `snake.py`       | Snake movement and growth logic                       |
| `food.py`        | Food spawning logic                                   |
| `scoreboard.py`  | Scoreboard updated to read/write high score from file |
| `high_score.txt` | File storing the persistent high score                |

---

### 📁 `02-open-read-write-files/`

Basic practice for working with files.

| File                  | Description                                   |
| --------------------- | --------------------------------------------- |
| `main.py`             | Demonstrates reading and writing file content |
| `my_file.txt`         | Example file used for reading practice        |
| `new_file.txt`        | Example file created programmatically         |
| `my_writing_file.txt` | Example file for writing/appending text       |

---

### 📁 `03-mail-merge-challenge/`

Automates generating personalized letters using file input/output.

| File / Folder                       | Description                                  |
| ----------------------------------- | -------------------------------------------- |
| `main.py`                           | Mail merge automation logic                  |
| `Input/Names/invited_names.txt`     | List of names used for generating letters    |
| `Input/Letters/starting_letter.txt` | Template letter with placeholder             |
| `Output/ReadyToSend/`               | Generated personalized letters output folder |

_(Generated example letters are included as sample outputs.)_

---

## 🎯 Learning Goal

By the end of Day 24, you should be able to:

- Read and write files in Python
- Work with nested directory structures
- Store persistent data for applications
- Automate document generation tasks
- Manage file paths correctly in projects

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash id="q3b0yq"
python3 filename.py
```

Example:

```bash id="b0a7my"
cd day-24_Files-Directories-Paths/03-mail-merge-challenge
python3 main.py
```

---

## 🧠 Practical Applications

These concepts are widely used in real-world programming:

- Saving game progress or settings
- Generating reports automatically
- Processing large datasets
- Automating administrative tasks
- Building file-based workflows

Try enhancing the projects by:

- Allowing custom file paths via user input
- Adding error handling for missing files
- Generating PDFs instead of text files
- Integrating with APIs for dynamic data

---

Happy coding! 📁💻
