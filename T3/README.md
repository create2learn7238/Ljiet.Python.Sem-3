
# 🐍 Python Learning Portfolio

A comprehensive collection of Python practice files, projects, and learning materials covering fundamental to intermediate concepts. This repository serves as a personal learning journey through Python programming, with practical examples and mini-projects.

---

## 📚 Contents Overview

### Core Python Concepts
- **Object-Oriented Programming** - Classes, objects, inheritance, and exception handling
- **File Operations** - Reading/writing files, file manipulation, and data processing
- **Modules & Libraries** - Working with built-in and custom modules
- **Data Structures** - Lists, dictionaries, and their methods
- **Functions** - Function definitions, parameters, and return values

---

## 📁 Repository Structure

### Learning Modules
| File | Description |
|------|-------------|
| `U-6 working with files.ipynb` | Comprehensive file operations including read/write, line counting, word replacement, and file comparisons |
| `U-7 Modules and directories.ipynb` | Module creation, imports, directory operations, and datetime usage |
| `U-8 OOp and Exception Handling.ipynb` | Class creation, ATM simulation, pizza ordering system, and exception handling |

### Custom Modules
- `calc.py` - Basic calculator functions (add, subtract, multiply, divide, floor, power, modulo)
- `myfunc.py` - String and list manipulation functions

### Sample Projects & Exercises
- **ATM Simulation** - PIN creation, balance checking, withdrawal system
- **Pizza Ordering System** - Customizable pizza orders with price calculation
- **Student Management** - Student records, report cards
- **File Analysis Tools** - Word count, line comparison, comment removal from code files

### Practice Files
Multiple text files for testing file operations:
- `ai.txt` - Creative content about AI
- `demo.txt`, `test.txt` - Test files for file operations
- `student name.txt` - Student data
- `f1.txt`, `f2.txt`, `f3.txt` - Multi-file operations practice
- `code.txt` - Python code examples with comments

---

## 🚀 Key Features Demonstrated

### File Handling
- Reading/writing different file modes (r, w, a, r+, w+, a+)
- Line-by-line processing
- Word and character counting
- File comparison and merging
- Comment removal from code files
- Text replacement operations

### OOP Concepts
- Class creation and instantiation
- Methods and attributes
- Real-world simulations (ATM, Pizza ordering)
- Inheritance and encapsulation

### Exception Handling
- Try-except blocks
- Custom exception raising
- Error management in user inputs
- File operation error handling

### Modules
- Custom module creation
- Import techniques (import, from-import, aliasing)
- Module functions and attributes
- Directory operations with OS module

---

## 💡 Sample Code Snippets

### ATM Class Example
```python
class atm:
    def __init__(self):
        self.bal=10000
    def createpin(self):
        pin = int(input("Enter 4 digit pin :"))
        if len(str(pin))==4:
            self.pin=pin
        else:
            print("Invalid enter 4 digit only")
    def checkbal(self):
        epin=int(input("Enter your Pin :"))
        if self.pin==epin:
            print(self.bal)
