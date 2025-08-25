# Python Fundamentals - Core Concepts

## Overview
Essential Python concepts covering first program execution, code documentation, module systems, and interactive development. Based on "Python for Everybody" curriculum.

## First Program Execution

Create file `hello.py` with code:

```python
print("Hello World")  # print is a function (to be explored later)
```

Execute via terminal command:
```bash
python hello.py
```

Output: Hello World printed on screen

> <img width="1366" height="768" alt="Screenshot 2025-08-25 081916" src="https://github.com/user-attachments/assets/eb1e8b1a-7c82-4c94-9f23-deaca836001b" />


## Code Documentation

**Single-line comments:**
```python
# Explanatory notes
```

**Multi-line comments:**
```python
"""
Documentation spanning 
multiple lines
"""
```

## Modules & Types

**Built-in Modules:** Pre-installed utilities (math, os, sys)

**External Modules:** Install via PIP:
```bash
pip install package_name
```

**Implementation:**
```python
import module_name
```
> <img width="1366" height="768" alt="Screenshot 2025-08-25 082144" src="https://github.com/user-attachments/assets/a59731e3-afbc-463e-9040-9b3225753884" />

*The Installing and using requests pyjokes module | pip install pyjokes.*

## REPL (Read-Eval-Print Loop)

Interactive Python environment accessed by typing `python` in terminal

Immediate code execution:
```python
>>> 5 + 3
8
>>> 2 ** 4
16
```
> <img width="1366" height="768" alt="Screenshot 2025-08-25 081254" src="https://github.com/user-attachments/assets/219abf63-bf6e-4e13-9b47-0fe6f03e7cb2" />
*The Using REPL to print multiplication table of 5.*

## Technical Environment

- **Language:** Python 3.x
- **Execution Methods:** File execution (`python filename.py`) and REPL
- **Tools:** PIP package manager, standard code editor
