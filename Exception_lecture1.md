# CS1350 Computer Science II Error Handling and Exceptions

## Week 10 Session 2

**What We'll Learn Today:**

- Why exceptions are better than error codes
- Python's exception hierarchy
- How to handle errors gracefully
- Writing robust, production-ready code
- Creating custom exceptions
- Best practices for error handling

# UNIT 1: Introduction to Errors and Exceptions

## Lecture: Why Exceptions Matter

### The Problem with Traditional Error Handling

**Without Exceptions (C-style):**

```python
# Imagine if Python used error codes instead of exceptions
def divide(a, b):
    if b == 0:
        return None, -1  # -1 is error code
    return a / b, 0      # 0 means success

# Using it becomes messy:
result, error_code = divide(10, 0)
if error_code == -1:
    print("Error: Division by zero")
else:
    print(f"Result: {result}")
```

**Problems with error codes:**

1. Easy to ignore (forget to check)
2. Clutters normal code flow
3. No standard error codes
4. Hard to propagate errors up
5. Mixing return values with error indicators

### The Exception Solution

**With Exceptions (Python-style):**

```python
def divide(a, b):
    return a / b  # Clean and simple!

# Caller decides how to handle errors
try:
    result = divide(10, 0)
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero")
```

### Types of Errors in Python

**1. Syntax Errors (Parse-time):**

```python
# These happen before code runs
# if x = 5:  # SyntaxError - caught before execution
```

**2. Exceptions (Runtime):**

```python
# These happen during execution
x = 10 / 0  # ZeroDivisionError - happens at runtime
```

### Exception Objects

Exceptions are objects that carry information:

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Type: {type(e)}")           # <class 'ZeroDivisionError'>
    print(f"Message: {e}")               # division by zero
    print(f"Arguments: {e.args}")        # ('division by zero',)
```

## Instructor Demo: Error Comparison

```python
# Let's compare error handling approaches
print("🔍 COMPARING ERROR HANDLING APPROACHES")
print("=" * 50)

# Approach 1: No error handling (crashes)
def unsafe_file_reader(filename):
    """Reads file without any error handling."""
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

# Approach 2: Check everything (tedious)
def paranoid_file_reader(filename):
    """Checks everything manually."""
    import os

    if not isinstance(filename, str):
        return None, "Filename must be string"

    if not os.path.exists(filename):
        return None, "File doesn't exist"

    if not os.access(filename, os.R_OK):
        return None, "No read permission"

    try:
        with open(filename, 'r') as f:
            return f.read(), None
    except:
        return None, "Unknown error"

# Approach 3: Exception handling (clean and robust)
def smart_file_reader(filename):
    """Uses exceptions for clean error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")
        return None
    except PermissionError:
        print(f"❌ No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Test all approaches
test_files = [
    "exists.txt",      # Normal file
    "missing.txt",     # Doesn't exist
    123,              # Wrong type
]

print("\nTesting different approaches:\n")

for filename in test_files:
    print(f"Reading: {filename}")

    # Paranoid approach
    content, error = paranoid_file_reader(filename)
    if error:
        print(f"  Paranoid: {error}")

    # Smart approach
    content = smart_file_reader(filename)
    if content:
        print(f"  Smart: Success!")

    print()
```

## ✏️ Student Practice: Basic Exception Handling

```python
def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)

    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        # Add try-except block here
        pass  # Replace with your code

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        # Add appropriate exception handling
        pass  # Replace with your code

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        # Try int first, then float, handle ValueError
        pass  # Replace with your code

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")

# Run the practice
practice_1_basic_exceptions()
```

# UNIT 2: Python's Exception Hierarchy

## Lecture: The Exception Family Tree

### The BaseException Hierarchy

```
BaseException
 ├── SystemExit           # sys.exit()
 ├── KeyboardInterrupt    # Ctrl+C
 ├── GeneratorExit        # Generator cleanup
 └── Exception            # All regular exceptions
      ├── StopIteration
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── TypeError
      ├── ValueError
      ├── OSError (IOError, EnvironmentError)
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── RuntimeError
      ├── AttributeError
      └── ... many more
```

### Why Hierarchy Matters

**Catching at different levels:**

```python
# Specific - catches only one type
try:
    x = my_list[10]
except IndexError:
    print("Index out of range")

# General - catches IndexError AND KeyError
try:
    x = my_list[10]
except LookupError:  # Parent of IndexError and KeyError
    print("Lookup failed")

# Too general (usually bad!)
try:
    x = my_list[10]
except Exception:  # Catches almost everything
    print("Something went wrong")
```

### Common Exception Categories

**1. Value/Type Errors:**

```python
int("hello")     # ValueError: invalid literal
"2" + 2         # TypeError: can't concatenate str and int
```

**2. Lookup Errors:**

```python
lst = [1, 2, 3]
lst[10]         # IndexError: list index out of range

dict = {"a": 1}
dict["b"]       # KeyError: 'b'
```

**3. File/IO Errors:**

```python
open("missing.txt")  # FileNotFoundError
open("/root/file")   # PermissionError (usually)
```

**4. Attribute/Name Errors:**

```python
x = 5
x.append(3)     # AttributeError: 'int' has no attribute 'append'
print(undefined) # NameError: name 'undefined' is not defined
```

## Instructor Demo: Exception Hierarchy Explorer

```python
# Let's explore the exception hierarchy
print("🌳 EXCEPTION HIERARCHY EXPLORER")
print("=" * 50)

def show_exception_info(exception_class):
    """Display information about an exception class."""
    print(f"\n📦 {exception_class.__name__}")
    print(f"   Base classes: {[c.__name__ for c in exception_class.__mro__[1:]]}")

    # Find direct subclasses
    subclasses = exception_class.__subclasses__()
    if subclasses:
        print(f"   Direct children: {[c.__name__ for c in subclasses[:5]]}")
        if len(subclasses) > 5:
            print(f"   ... and {len(subclasses)-5} more")

# Explore major exception branches
show_exception_info(BaseException)
show_exception_info(Exception)
show_exception_info(ArithmeticError)
show_exception_info(LookupError)
show_exception_info(OSError)

print("\n" + "="*50)
print("DEMONSTRATING EXCEPTION CATCHING")
print("="*50)

def demonstrate_catching_levels():
    """Show how different catch levels work."""

    test_operations = [
        ("10 / 0", lambda: 10 / 0),
        ("[1,2][5]", lambda: [1,2][5]),
        ("int('abc')", lambda: int('abc')),
        ("open('/fake')", lambda: open('/fake/file.txt'))
    ]

    for description, operation in test_operations:
        print(f"\nTrying: {description}")

        # Try with specific exception
        try:
            operation()
        except ZeroDivisionError:
            print("  ✓ Caught as ZeroDivisionError")
        except IndexError:
            print("  ✓ Caught as IndexError")
        except ValueError:
            print("  ✓ Caught as ValueError")
        except FileNotFoundError:
            print("  ✓ Caught as FileNotFoundError")
        except Exception as e:
            print(f"  ✓ Caught as general Exception: {type(e).__name__}")

demonstrate_catching_levels()

# Show exception inheritance check
print("\n" + "="*50)
print("INHERITANCE RELATIONSHIPS")
print("="*50)

exceptions_to_check = [
    (IndexError, LookupError),
    (KeyError, LookupError),
    (FileNotFoundError, OSError),
    (ZeroDivisionError, ArithmeticError),
    (ValueError, Exception),
    (KeyboardInterrupt, Exception)  # This one is False!
]

for child, parent in exceptions_to_check:
    is_subclass = issubclass(child, parent)
    symbol = "✓" if is_subclass else "✗"
    print(f"{symbol} {child.__name__} is {'a' if is_subclass else 'NOT a'} {parent.__name__}")
```

## Student Practice: Exception Hierarchy

```python
def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except:  # TODO: Replace with appropriate parent exception
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        # TODO: Fix the order of exception handlers
        try:
            return int(value)
        except:  # Add specific exceptions in correct order
            pass

        return str(value)

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")

# Run the practice
practice_2_exception_hierarchy()
```

# UNIT 3: The Try-Except-Else-Finally Pattern

## Lecture: Complete Exception Handling

### The Full Pattern

```python
try:
    # Code that might raise exceptions
    risky_operation()
except SpecificError as e:
    # Handle specific error
    handle_specific_error(e)
except (ErrorA, ErrorB) as e:
    # Handle multiple errors the same way
    handle_multiple_errors(e)
except Exception as e:
    # Catch-all for unexpected errors
    log_unexpected_error(e)
else:
    # Runs only if NO exception occurred
    success_operation()
finally:
    # ALWAYS runs, even if return/break/continue
    cleanup_operation()
```

### The else Clause

**When to use else:**

```python
# BAD - processing in try block unnecessarily
try:
    file = open('data.txt')
    data = file.read()
    # Risky - what if processing fails?
    processed = data.upper().split()
    file.close()
except IOError:
    print("Can't read file")

# GOOD - only risky operation in try
try:
    file = open('data.txt')
except IOError:
    print("Can't read file")
else:
    # File opened successfully, now process
    data = file.read()
    processed = data.upper().split()
    file.close()
```

### The finally Clause

**Guaranteed cleanup:**

```python
# finally ALWAYS runs
def read_file(filename):
    file = None
    try:
        file = open(filename)
        return file.read()
    except IOError:
        return None
    finally:
        if file:
            print("Closing file...")
            file.close()  # Runs even with return!
```

### Exception Propagation

```python
def level_3():
    return 10 / 0  # Raises ZeroDivisionError

def level_2():
    return level_3()  # Doesn't handle, propagates up

def level_1():
    try:
        return level_2()
    except ZeroDivisionError:
        print("Caught at level 1!")
        return 0

# Exception bubbles up until caught
result = level_1()  # Prints: Caught at level 1!
```

## Instructor Demo: Database Transaction Pattern

```python
# Let's simulate a database transaction with proper cleanup
print("DATABASE TRANSACTION SIMULATOR")
print("=" * 50)

class DatabaseConnection:
    """Simulated database connection."""

    def __init__(self):
        self.connected = False
        self.in_transaction = False
        self.data = {}

    def connect(self):
        print("Connecting to database...")
        self.connected = True

    def disconnect(self):
        print("Disconnecting from database...")
        self.connected = False

    def begin_transaction(self):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print("Beginning transaction...")
        self.in_transaction = True
        self.backup = self.data.copy()

    def commit(self):
        if not self.in_transaction:
            raise RuntimeError("No active transaction")
        print("Committing transaction...")
        self.in_transaction = False
        self.backup = None

    def rollback(self):
        if not self.in_transaction:
            return
        print("Rolling back transaction...")
        self.data = self.backup
        self.in_transaction = False
        self.backup = None

    def insert(self, key, value):
        if not self.in_transaction:
            raise RuntimeError("No active transaction")
        if key in self.data:
            raise ValueError(f"Duplicate key: {key}")
        self.data[key] = value
        print(f"  📝 Inserted {key}: {value}")

def perform_transaction(db, operations):
    """
    Perform database transaction with proper error handling.
    """
    print(f"\nAttempting transaction with {len(operations)} operations")

    try:
        db.connect()
        db.begin_transaction()

        # Try all operations
        for key, value in operations:
            db.insert(key, value)

    except ValueError as e:
        print(f"Validation error: {e}")
        db.rollback()
        return False

    except RuntimeError as e:
        print(f"Runtime error: {e}")
        db.rollback()
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        db.rollback()
        return False

    else:
        # All operations succeeded
        print("All operations successful!")
        db.commit()
        return True

    finally:
        # Always disconnect
        if db.connected:
            db.disconnect()
        print(f"Final database state: {db.data}")

# Test transactions
db = DatabaseConnection()

# Successful transaction
good_operations = [
    ("user1", "Alice"),
    ("user2", "Bob"),
    ("user3", "Charlie")
]
perform_transaction(db, good_operations)

# Failed transaction (duplicate key)
bad_operations = [
    ("user4", "David"),
    ("user1", "Eve"),  # Duplicate!
    ("user5", "Frank")
]
perform_transaction(db, bad_operations)

print("\n" + "="*50)
print("EXCEPTION FLOW DEMONSTRATION")
print("="*50)

def demonstrate_flow(raise_error=False):
    """Show the flow through try-except-else-finally."""
    print(f"\n{'With' if raise_error else 'Without'} exception:")

    try:
        print("  1. In try block")
        if raise_error:
            raise ValueError("Test error")
        print("  2. End of try block")

    except ValueError as e:
        print(f"  3. In except block: {e}")

    else:
        print("  4. In else block (no exception)")

    finally:
        print("  5. In finally block (always runs)")

    print("  6. After entire try-except block")

demonstrate_flow(raise_error=False)
demonstrate_flow(raise_error=True)
```

## Student Practice: Complete Pattern

```python
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            # TODO: Open file
            pass
        except FileNotFoundError:
            # TODO: Handle missing file
            pass
        except PermissionError:
            # TODO: Handle permission issues
            pass
        else:
            # TODO: Process file content (only if opened successfully)
            pass
        finally:
            # TODO: Ensure file is closed
            pass

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            # TODO: Implement with possible RuntimeError
            pass

        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            pass

        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            pass

    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource

# Run the practice
practice_3_complete_pattern()
```

