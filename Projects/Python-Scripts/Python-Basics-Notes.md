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

## 1. Modules & Types

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

## 2. REPL (Read-Eval-Print Loop)

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


## 3. Variables & Data Types
**Concept:** Storing information for later use in your program.

**Syntax:**
```python
variable_name = value
```

**Key Data Types:**
- **String (str):** Text. `name = "Alice"`
- **Integer (int):** Whole numbers. `port = 443`
- **Boolean (bool):** True or False. `is_vulnerable = True`

> <img width="1366" height="768" alt="Screenshot 2025-08-26 073824" src="https://github.com/user-attachments/assets/d1b20662-9327-4e30-af87-f44e85896b9c" />
*Create a script that gets a target IP and port from the user.*

## 4. Basic Input/Output
**Concept:** Interacting with the user through the console.

**Syntax:**
```python
output = print("Message")  # Output to the screen
input = input("Prompt: ")  # Get input from the user
```
> <img width="1366" height="768" alt="Screenshot 2025-08-26 074044" src="https://github.com/user-attachments/assets/dbb05fb1-d925-45a9-a75b-09080c9ee1ce" />
*   **`variables_io.py`** | The Variables and Input/Output Lab  
    *Create a script that gets a target IP and port from the user.*

## 5. Conditionals (if, elif, else)
**Concept:** Making decisions in your code based on conditions.

**Syntax:**
```python
if condition:
    # do something
elif other_condition:
    # do something else
else:
    # do if all other conditions are False
```
> <img width="1366" height="768" alt="Screenshot 2025-08-26 074224" src="https://github.com/user-attachments/assets/7da2959f-24c8-4911-ae6b-ba67b64ae920" />
*   **`conditional_access.py`** | The Conditional Access Check Lab  
    *Simulate a login with `if/elif/else` to grant different access levels.*

    
## 6. Loops (for, while)
**Concept:** Repeating a block of code multiple times.

**Syntax:**
```python
# For Loop: iterate a set number of times or over a list
for item in sequence:
    # do something with item

# While Loop: repeat as long as a condition is True
while condition:
    # do something
```
<img width="1366" height="768" alt="Screenshot 2025-08-26 074354" src="https://github.com/user-attachments/assets/3a8b693f-89ff-4566-a38f-95b030297f8a" />
*   **`log_scanner.py`** | The Log Line Scanner Loop Lab  
    *Use a `for` loop to iterate through a list of log lines and find failures.*

## 7. Functions (def)
**Concept:** Creating reusable blocks of code to avoid repetition.

**Syntax:**
```python
def function_name(parameter):
    # do something
    return result
```

## 8. Working with Files (open(), read(), write())
**Concept:** Reading from and writing to files on the disk. Critical for handling logs, configs, and output.

**Syntax (The Safe Way - using with):**
```python
# Reading a file
with open('filename.txt', 'r') as file:
    content = file.read()

# Writing to a file (WARNING: Overwrites existing file!)
with open('filename.txt', 'w') as file:
    file.write("Hello World")

# Appending to a file (SAFER: Adds to the end)
with open('filename.txt', 'a') as file:
    file.write("Hello World\n")
```
> <img width="1366" height="768" alt="Screenshot 2025-08-26 074727" src="https://github.com/user-attachments/assets/020dec3a-47d7-4f3a-a134-2a14e7153cf8" />
*   **`file_operations.py`** | The File Write-Read Operation Lab  
    *Use `open()`, `write()`, and `read()` to save and load scan results.*

## Technical Environment

- **Language:** Python 3.x
- **Execution Methods:** File execution (`python filename.py`) and REPL
- **Tools:** PIP package manager, standard code editor
 
