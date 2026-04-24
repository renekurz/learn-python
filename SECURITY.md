# Security Policy

## Supported Versions

This is a learning repository, not a production application. However, code quality and safety still matter — especially in sections that deal with authentication, databases, and APIs.

The following sections are actively maintained:

| Section | Status |
|---------|--------|
| 01_Beginner | ✅ Maintained |
| 02_Intermediate | ✅ Maintained |
| 03_Advanced | ✅ Maintained |
| 04_FastAPI | ✅ Maintained |

## Reporting a Vulnerability

If you discover a security issue in this repository — for example:

- Hardcoded secrets, API keys, or passwords accidentally committed
- Vulnerable dependency versions (e.g. in FastAPI, Flask, or SQLAlchemy examples)
- Insecure code patterns that could mislead learners into bad practices
- Authentication or JWT implementation flaws in the example projects

**Please do not open a public issue.** Instead, report it privately by emailing the maintainer directly via the contact listed on the [GitHub profile](https://github.com/renekurz).

### What to include in your report

- The file(s) and line number(s) affected
- A description of the vulnerability and its potential impact
- If applicable, a suggested fix or safer alternative

### Response timeline

- You can expect an acknowledgement within **48 hours**
- A fix or mitigation will be prioritised and applied as soon as possible
- You will be credited in the fix commit unless you prefer to remain anonymous

## Security Best Practices for Learners

Some examples in this repo (particularly in `03_Advanced` and `04_FastAPI`) demonstrate authentication, environment variables, and database access. A few reminders:

- **Never commit real API keys or secrets.** Always use environment variables or a `.env` file, and make sure `.env` is listed in `.gitignore`.
- **Do not reuse passwords** from these examples in any real project.
- The JWT and authentication examples are for learning purposes. Before deploying anything to production, review the [OWASP Top 10](https://owasp.org/www-project-top-ten/) and consult up-to-date security resources.

## Scope

This repository contains educational code only. It is not deployed as a live service. Security reports related to GitHub itself or third-party services used in examples (e.g. Pixela API) are out of scope.
