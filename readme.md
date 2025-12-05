# doclean — Minimal Project Cleaner for Python Projects

`doclean` is a tiny command-line tool that removes build artifacts, cache folders, and other temporary files based on patterns you define in your project’s `pyproject.toml`.

It is designed to be **simple**, **safe**, and **predictable**, following familar configuration style used by common tools.

## Why Another Clean Tool?
doclean aims to be:
* Minimal — no frameworks, no plugins
* Safe — prevents destructive deletions
* Config-driven — controlled entirely via pyproject.toml
* Predictable — does exactly what you configure, no more

## ⭐ Features
- Reads cleanup patterns from `[tool.doclean]` in `pyproject.toml`
- Supports:
  - Wildcards (`*`)
  - Recursive globs (`**/pattern`)
  - Directories and files
- Safety checks:
  - Prevents deleting project root
  - Refuses paths outside the project directory
  - Rejects symlinks
  - Skips missing paths
- Searches **upward** to find the nearest `pyproject.toml`
- Optional `--dry` mode to preview deletions
- Zero dependencies

---

## 📦 Installation (development)

```bash
git clone git@github.com:Thaerious/doclean.git
python3 -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

## Details

### Safety Rules
Before deleting anything, doclean validates each expanded path:
* Never deletes the project root
* Rejects paths outside the project directory
* Skips missing paths
* Only validated, safe paths are removed.

### Example pyproject.toml
```bash
[tool.doclean]
paths = [
    "build",
    "dist",
    "**/__pycache__",
    ".pytest_cache"
]
```