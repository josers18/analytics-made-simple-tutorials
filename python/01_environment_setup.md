# Python Tutorial 1: Analytics Setup Without Tears

> **Official Companion Guide for [Analytics Made Simple: Python Setup Without Tears](https://analyticsmadesimple.com/tutorials/)**

A clean, reproducible Python environment is the foundation for reliable data analysis.

---

## 1. Creating an Isolated Virtual Environment

Never install third-party packages directly into your operating system's global Python environment.

```bash
# 1. Create a dedicated virtual environment
python3 -m venv .venv

# 2. Activate the virtual environment
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell:
# .\.venv\Scripts\Activate.ps1

# 3. Verify activation
which python
```

## 2. Installing Core Analytics Packages

```bash
pip install --upgrade pip
pip install pandas numpy sqlalchemy duckdb pyarrow jupyterlab matplotlib
```

## 3. Freezing Dependencies
```bash
pip freeze > requirements.txt
```
