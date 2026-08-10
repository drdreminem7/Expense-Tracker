# CLI Expense Tracker

A simple command-line expense tracker built with Python.

This project allows you to add, list, delete, save, load, and export expenses using a terminal-based menu. It uses JSON for persistent storage, CSV for export, and includes automated tests with `pytest`.

## Features

- Add expenses
- List expenses
- Delete expenses
- View monthly totals
- Save expenses to JSON
- Load expenses from JSON
- Export expenses to CSV
- Input validation
- Error handling
- Automated tests with `pytest`

## Project Structure

```text
expense-tracker/
├── main.py
├── storage.py
├── models.py
├── utils.py
├── expenses.json
├── expenses.csv
├── requirements.txt
├── pytest.ini
├── tests/
│   ├── test_models.py
│   ├── test_storage.py
│   └── test_utils.py
└── README.md
```

## Requirements

- Python 3.12+
- pytest

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

From the project root, run:

```bash
python main.py
```

## Example Menu

```text
Expense Tracker

1. Add Expense
2. List Expenses
3. Delete Expense
4. Monthly Total
5. Export to CSV
6. Exit
```

## Expense Format

Each expense contains:

```text
date
category
amount
description
```

Example:

```text
2026-08-10 | Food | 15.50 | Lunch
```

## Data Persistence

Expenses are saved in:

```text
expenses.json
```

This means expenses remain available after closing and reopening the program.

## CSV Export

The app can export expenses to:

```text
expenses.csv
```

CSV columns:

```text
amount, category, description, date
```

## Run Tests

Run all tests with:

```bash
pytest
```

Expected result:

```text
12 passed
```

## What I Practiced

This project practices:

- Python functions
- Classes and objects
- Lists and dictionaries
- File handling
- JSON persistence
- CSV export
- Input validation
- Exception handling
- Modular code structure
- Automated testing with pytest
- Mocking user input with monkeypatch

## Status

The project is functional and includes tests.

Possible future improvements:

- Category totals
- Better table formatting
- Edit expense feature
- Search/filter expenses
- Better date handling
- Command-line arguments
- Package the app as an installable CLI tool
