# Contributing to learn-python 🐍

Thank you for your interest in contributing! This is a beginner-friendly Python learning repository, and contributions of all kinds are welcome — whether you're fixing a typo, improving an explanation, adding an exercise, or suggesting a new mini-project.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Coding & Style Guidelines](#coding--style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

---

## Code of Conduct

This project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold a welcoming and respectful environment for everyone, regardless of experience level.

---

## How Can I Contribute?

### 🐛 Bug Fixes
Found a broken example, a logic error in an exercise, or code that doesn't run? Please open an issue or submit a fix directly via a pull request.

### 📝 Improve Explanations
If an explanation in a `README.md` is unclear, too terse, or contains a mistake, feel free to improve it. This repo is aimed at beginners, so clarity matters more than brevity.

### ➕ Add Exercises or Examples
You can propose additional exercises or code examples for any existing day. Keep them consistent with the topic and difficulty of that day's content.

### 🆕 Suggest New Content
Have an idea for a new day, mini-project, or section? Open an issue first to discuss it before investing time in building it out.

### 🧹 Refactor or Improve Code Quality
Improvements to readability, Pythonic style, or adding type hints and docstrings are welcome, especially for the Intermediate and Advanced sections.

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/learn-python.git
   cd learn-python
   ```
3. **Create a branch** for your change:
   ```bash
   git checkout -b fix/day-07-hangman-logic
   # or
   git checkout -b feat/day-14-add-extra-exercise
   ```
4. Make your changes, then **commit and push**:
   ```bash
   git add .
   git commit -m "fix(day-07): correct hangman lives decrement logic"
   git push origin your-branch-name
   ```
5. Open a **Pull Request** against the `main` branch.

---

## Repository Structure

```
learn-python/
├── 01_Beginner/        # Days 1–14: core syntax, logic, mini-games
├── 02_Intermediate/    # Days 15–40: OOP, GUIs, APIs, Flask intro
├── 03_Advanced/        # Days 41–46: Flask forms, databases, auth
└── 04_FastAPI/         # Days 47–55: FastAPI, SQLAlchemy, JWT, testing
```

Each day lives in its own folder following the naming pattern:

```
day-XX_Topic-Name/
├── main.py          # (or equivalent entry point)
├── README.md        # topic overview, key concepts, run instructions
└── ...              # additional files as needed
```

When adding or editing content, please follow this existing structure and keep each day self-contained.

---

## Coding & Style Guidelines

- **Python version:** Python 3.10+
- **Style:** Follow [PEP 8](https://peps.python.org/pep-0008/). Keep lines under 100 characters.
- **Naming:** Use `snake_case` for variables and functions, `PascalCase` for classes.
- **Comments:** Write comments that explain *why*, not just *what*. Since this is a learning repo, a little more explanation is always appreciated.
- **Docstrings:** Add docstrings to all functions and classes, especially in the Intermediate and Advanced sections.
- **No magic numbers:** Use named constants instead of bare literals where it makes the code clearer.
- **Keep it beginner-friendly:** Avoid complex one-liners or advanced patterns in the Beginner section. Clarity over cleverness.
- **Dependencies:** If your contribution requires a new package, mention it clearly in the day's `README.md` with the install command.

### Example — preferred style

```python
# Good
def calculate_tip(bill_amount: float, tip_percentage: int) -> float:
    """Calculate the tip amount for a given bill.

    Args:
        bill_amount: The total bill in the local currency.
        tip_percentage: The desired tip as a whole number (e.g. 15 for 15%).

    Returns:
        The tip amount rounded to two decimal places.
    """
    return round(bill_amount * tip_percentage / 100, 2)
```

---

## Commit Messages

Use the following format for commit messages:

```
type(scope): short description
```

| Type     | When to use                                      |
|----------|--------------------------------------------------|
| `fix`    | A bug fix or correction                          |
| `feat`   | A new exercise, example, or day                  |
| `docs`   | Changes to README or other documentation         |
| `style`  | Formatting, whitespace, no logic change          |
| `refactor` | Code restructure without changing behaviour   |
| `test`   | Adding or updating tests (FastAPI section)       |
| `chore`  | Repo maintenance (gitignore, config, etc.)       |

**Examples:**
```
fix(day-11): correct dealer bust condition in Blackjack
feat(day-35): add retry logic example for Pixela API
docs(day-49): clarify SQLAlchemy session lifecycle
```

---

## Pull Request Process

1. Make sure your branch is up to date with `main` before opening a PR.
2. Fill in the PR description: explain *what* you changed and *why*.
3. Keep PRs focused — one fix or feature per PR is much easier to review than a large catch-all change.
4. Ensure all existing code in the files you touched still runs correctly.
5. If you're adding a new day or section, include a `README.md` for it.
6. A maintainer will review your PR and may request changes or ask questions before merging.

---

## Reporting Issues

If you find a bug, unclear explanation, or have a question, please [open an issue](https://github.com/renekurz/learn-python/issues) with:

- The day/folder where the problem is (e.g. `02_Intermediate/day-25_CSV-Files-and-Pandas`)
- A clear description of the problem
- Steps to reproduce it (if applicable)
- What you expected to happen vs. what actually happened

---

Happy coding, and thank you for helping make this resource better for everyone learning Python! 🚀
