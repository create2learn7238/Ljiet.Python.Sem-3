# Python Data Structures - Comprehensive Guide

This repository contains a comprehensive collection of Jupyter notebooks covering Python's immutable and mutable data structures, along with functional programming concepts. Perfect for beginners and intermediate learners who want to master Python's core data handling capabilities.

## 📚 Notebooks Overview

### 1. [Ch-3] Immutable Data Structure (`Ch-3 Immutable Data Structure.ipynb`)
**Focus: Strings and Tuples**

#### Strings 📝
- **Accessing characters** using positive/negative indexing
- **Slicing operations** with step parameters
- **Mathematical operations**: Concatenation (`+`) and Repetition (`*`)
- **String comparisons** (lexicographical)
- **Important methods**: 
  - `join()`, `format()`, `strip()` family
  - Case conversion: `upper()`, `lower()`, `swapcase()`, `title()`
  - Character type checking: `isalnum()`, `isalpha()`, `isdigit()`, `isspace()`
  - Search: `find()`, `count()`, `replace()`
  - `split()` and `translate()` with `maketrans()`
- **Practical programs**:
  - Palindrome checker
  - Character frequency counters
  - Password validation
  - String shifting operations

#### Tuples 🔒
- **Creation**: With/without parentheses, single element tuples
- **Accessing elements**: Indexing and slicing
- **Operations**: Concatenation, repetition
- **Methods**: `count()`, `index()`
- **Tuple packing and unpacking**
- **Looping through tuples**
- **Conversion**: `sorted()`, `reversed()`, `enumerate()`

---

### 2. [Ch-4] Mutable Data Structure (`Ch-4 Mutable DS.ipynb`)
**Focus: Lists**

#### Lists 📋
- **Creation**: Direct, `list()`, `eval()`, `split()`
- **Mutability demonstration**: Modifying elements
- **Accessing**: Indexing, slicing with step
- **Operations**: Concatenation (`+`), Repetition (`*`)
- **Membership operators**: `in`, `not in`
- **Nested lists and matrix operations**
- **List methods**:
  - Adding: `append()`, `insert()`, `extend()`
  - Removing: `remove()`, `pop()`, `clear()`
  - Reordering: `reverse()`, `sort()` (with key functions)
  - Copying: Aliasing vs. shallow copy

---

### 3. Advanced Mutable Structures (`Mutable Ds 2.ipynb`)
**Focus: List operations, Dictionary**

#### Lists Advanced 🚀
- **Comparison operators** between lists
- **Aliasing and cloning** (understanding references)
- **Nested list manipulation**
- **List comprehension** with conditions
- **Practical problems**:
  - Circular shift on lists
  - Element frequency analysis
  - Finding special elements that balance list sums
  - String length filtering
  - Matrix transpose operations

#### Dictionaries 📖
- **Creation**: Key-value pairs
- **Accessing and updating** elements
- **Deleting**: `del`, `clear()`
- **Dictionary comprehension**
- **Important methods**: `copy()`, `len()`

---

### 4. Functional Programming & Sets (`Mutable Ds 3.ipynb`)
**Focus: Sets, Lambda, Map, Reduce, Filter**

#### Sets 🔄
- **Creation**: `set()`, from strings
- **Operations**: `add()`, `update()`, `remove()`, `discard()`, `pop()`
- **Set comprehension**
- **Frozenset** (immutable version)

#### Functional Programming 🧠
- **Lambda functions**: Anonymous functions for quick operations
- **map()**: Apply function to all sequence elements
- **filter()**: Filter elements based on condition
- **reduce()**: Reduce sequence to single value
- **Combined applications**:
  - Capitalizing list elements
  - Separating positive/negative numbers
  - Custom sorting with key functions

## 🎯 Key Takeaways

| Feature | Immutable | Mutable |
|---------|-----------|---------|
| Strings | ✅ Cannot modify after creation | ❌ |
| Tuples | ✅ Cannot modify after creation | ❌ |
| Lists | ❌ | ✅ Can add/remove/modify |
| Sets | ❌ | ✅ (except frozenset) |
| Dicts | ❌ | ✅ |

## 🛠️ Prerequisites

- Python 3.x
- Jupyter Notebook / JupyterLab
- Basic Python syntax knowledge

## 🚀 How to Use

1. Clone the repository
2. Install Jupyter if not already installed:
   ```bash
   pip install jupyter
