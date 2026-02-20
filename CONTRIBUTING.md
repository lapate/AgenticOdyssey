# Contributing to AgenticOdyssey

Thank you for your interest in contributing to the AgenticOdyssey workshop! This document provides guidelines for contributing labs, demos, and documentation.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Adding a New Lab](#adding-a-new-lab)
- [Adding a New Demo](#adding-a-new-demo)
- [Content Standards](#content-standards)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). By participating, you agree to uphold this code.

---

## How to Contribute

1. **Fork** the repository and create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-contribution
   ```

2. Make your changes following the guidelines below.

3. **Test** your code and verify all instructions work end-to-end.

4. Open a **Pull Request** with a clear description of your changes.

---

## Adding a New Lab

Each lab lives in `labs/labXX-short-name/` and must include:

```
labs/labXX-short-name/
├── README.md          # Lab instructions (required)
├── requirements.txt   # Lab-specific Python dependencies (if needed)
├── solution/          # Complete solution code
│   └── *.py
└── starter/           # Starter code with TODOs (optional)
    └── *.py
```

### Lab README Template

Your `labs/labXX/README.md` should follow the structure in the existing labs:

- **Overview** — What participants will build/learn
- **Learning Objectives** — 3–5 measurable outcomes
- **Prerequisites** — What's needed before starting
- **Step-by-step instructions** — Clear, numbered steps
- **Expected Output** — Screenshots or sample output
- **Next Steps** — What to explore after completing the lab

---

## Adding a New Demo

Each demo lives in `demos/demoXX-short-name/` and must include:

```
demos/demoXX-short-name/
├── README.md          # Demo description and run instructions (required)
├── requirements.txt   # Demo-specific Python dependencies (if needed)
└── *.py               # Demo source files
```

---

## Content Standards

- **Python version:** Target Python 3.10+
- **Code style:** Follow [PEP 8](https://pep8.org/); use `black` for formatting
- **Dependencies:** Pin exact versions in `requirements.txt`
- **Secrets:** Never commit API keys or secrets. Use `.env` files and `.env.example` templates
- **Error handling:** Include meaningful error messages that guide participants
- **Comments:** Add inline comments to explain non-obvious agentic patterns

---

## Pull Request Process

1. Ensure your branch is up to date with `main`
2. Verify all code examples run successfully end-to-end
3. Update the main `README.md` table if you added a new lab or demo
4. Request a review from a workshop maintainer
5. PRs require at least **1 approving review** before merging
