# tdd_python_template

This repository contains:
1. A [structure](#template-project-structure) for a Test-Driven Development Python project.

## Template Project Structure
```bash
├── project
│   ├── __init__.py
│   └── module_1.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── pytest.ini
    └── test_module_1
        ├── __init__.py
        └── test_something.py
```

## Usage

Run automated tests:

```pytest -v -s
# Prints output from pytest
```