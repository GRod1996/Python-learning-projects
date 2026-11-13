# CS1350 Computer Science II — Advanced Functions in Python

## Fall 2026

## Lecture Outline

1. Functions as First-Class Objects
2. Higher-Order Functions
3. Generators and Generator Expressions
4. Advanced Parameter Handling
5. Type Hints and Function Annotations
6. Context Managers as Functions
7. Function Factories and Meta-Programming

# Part 1: Functions as First-Class Objects

## What Does "First-Class" Mean?

In Python, functions are **first-class citizens**, meaning they can be:

- Assigned to variables
- Passed as arguments to other functions
- Returned from functions
- Stored in data structures

This is fundamental to functional programming!

## 1.1 Functions Assigned to Variables

```python
# Functions are objects - they have a type and can be assigned
def greet(name):
    return f"Hello, {name}!"

# Assign function to variable (note: no parentheses!)
my_function = greet
print(type(my_function))  # <class 'function'>

# Call through the variable
result = my_function("Alice")
print(result)  # Hello, Alice!

# Both names refer to the same function object
print(greet is my_function)  # True
```

> `greet` is the function object itself; `greet("Alice")` *calls* it and gives you the return value. Mixing the two up is the most common mistake in this unit.

**Why is this useful?**

```python
# Dynamic function selection
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Select operation based on user input
operation = input("Choose operation (+ or *): ")
if operation == "+":
    func = add
else:
    func = multiply

result = func(10, 5)
print(f"Result: {result}")
```

## 1.2 Functions Passed as Arguments

```python
def apply_twice(func, arg):
    """Apply a function twice to an argument"""
    return func(func(arg))

def double(x):
    return x * 2

def square(x):
    return x ** 2

# Pass functions as arguments
print(apply_twice(double, 3))   # double(double(3)) = double(6) = 12
print(apply_twice(square, 2))   # square(square(2)) = square(4) = 16

# Real-world example: sorting with custom key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Carol", "grade": 78}
]

# Pass a function to extract the sort key
def get_grade(student):
    return student["grade"]

students.sort(key=get_grade)
print(students)  # Sorted by grade: Carol (78), Alice (85), Bob (92)
```

## 1.3 Functions as Return Values

```python
def make_multiplier(n):
    """Create and return a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier  # Return the function itself

# Create specialized functions
times_2 = make_multiplier(2)
times_5 = make_multiplier(5)

print(times_2(10))   # 20
print(times_5(10))   # 50

# More practical example: a function factory
def make_logger(prefix):
    """Create a logging function with a specific prefix"""
    def log_message(message):
        print(f"[{prefix}] {message}")
    return log_message

error_log = make_logger("ERROR")
info_log = make_logger("INFO")

error_log("File not found")   # [ERROR] File not found
info_log("Process started")   # [INFO] Process started
```

> `make_multiplier` and `make_logger` are **function factories**: functions that build and return other functions. They are not decorators. A decorator is a special kind of factory that takes a *function* and returns a replacement for it — see Part 7.

## 1.4 Functions Stored in Data Structures

```python
# Dictionary of functions (dispatch table)
math_operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None
}

# Use dictionary to select function
operation = 'multiply'
result = math_operations[operation](10, 5)
print(f"{operation}: {result}")  # multiply: 50

# List of functions (pipeline)
def uppercase(text):
    return text.upper()

def remove_spaces(text):
    return text.replace(" ", "")

def add_exclamation(text):
    return text + "!"

# Create a text processing pipeline
pipeline = [uppercase, remove_spaces, add_exclamation]

text = "hello world"
for func in pipeline:
    text = func(text)
print(text)  # HELLOWORLD!
```

(`lambda` creates a small unnamed function; it is covered properly in section 2.2.)

**Takeaway:** In Python, a function is an ordinary object whose type happens to define `__call__`. You can bind it to a name, pass it, return it, and store it exactly as you would an `int`, a `str`, or a `list`. What a function does *not* share with those types is their operators: you cannot add two functions or index into one.

## 1.5 Functional Programming Patterns

```python
# Closure: Function that remembers its environment
def counter():
    """Create a counter function with persistent state"""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Each counter maintains its own state
counter1 = counter()
counter2 = counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (independent counter)
print(counter1())  # 3
```

> **Why `nonlocal`?** Without it, `count += 1` makes Python treat `count` as a brand-new local variable of `increment`, and the line fails with `UnboundLocalError`. You only need `nonlocal` when the inner function *assigns* to the outer variable; just reading it (as `multiplier` reads `n` in 1.3) needs nothing.

```python
# Function composition
def compose(f, g):
    """Return a function that computes f(g(x))"""
    def composed(x):
        return f(g(x))
    return composed

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

# Create new function by composition
add_one_then_square = compose(square, add_one)
print(add_one_then_square(3))  # square(add_one(3)) = square(4) = 16
```

Note the order: `compose(f, g)` runs `g` first and `f` second, as in mathematics.

## Practice Exercises — Part 1

### Exercise 1.1 (Beginner): A Second Name for a Function

```python
def shout(text):
    return text.upper() + "!"

# TODO: Make `yell` another name for the same function.
#       Assign the function itself - no parentheses.
yell = None

print(yell("hello"))   # HELLO!
print(yell is shout)   # True
```

### Exercise 1.2 (Beginner): Pass a Function as an Argument

```python
def apply(func, value):
    """Call func on value and return the result."""
    return func(value)

# TODO 1: Use apply to call the built-in len on "hello".
length = None
print(length)   # 5

# TODO 2: Use apply to call str.upper on "hello".
loud = None
print(loud)     # HELLO
```

### Exercise 1.3 (Intermediate): Pick a Function from a Dictionary

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# TODO 1: Add one more entry so that "-" maps to subtract.
OPERATIONS = {
    "+": add,
}

def calculate(symbol, a, b):
    # TODO 2: Look up the function for symbol in OPERATIONS,
    #         call it with a and b, and return the result.
    pass

print(calculate("+", 8, 2))   # 10
print(calculate("-", 8, 2))   # 6
```

### Exercise 1.4 (Intermediate): Run a List of Functions

```python
def double(x):
    return x * 2

def add_ten(x):
    return x + 10

steps = [double, add_ten, double]
value = 5

# TODO: Loop over steps. Each time, call the function on value
#       and store the result back in value. (Two lines.)

print(value)   # 40
```

### Exercise 1.5 (Advanced): Your Own Function Factory

Look at `make_multiplier` in section 1.3 and write the same thing for addition.

```python
def make_adder(n):
    """Return a function that adds n to its argument."""
    # TODO: Define an inner function, then return it.
    pass

add_5 = make_adder(5)
add_100 = make_adder(100)
print(add_5(10))     # 15
print(add_100(10))   # 110
```

# Part 2: Higher-Order Functions

## What Are Higher-Order Functions?

Functions that either:

1. Take one or more functions as arguments, **or**
2. Return a function as their result

Python's built-in higher-order functions make code more concise and expressive.

## 2.1 Map, Filter, Reduce, Zip

- `map()`, `filter()`, and `zip()` do not return lists. 
- They return *iterators* that produce one item at a time and can be consumed only once. - That is why the examples wrap them in `list(...)` before printing.

### Map: Transform Each Element

```python
# map(function, iterable) - applies function to each element
numbers = [1, 2, 3, 4, 5]

# Traditional approach
squared = []
for n in numbers:
    squared.append(n ** 2)

# Using map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Map with multiple iterables
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(add, list1, list2))
print(sums)  # [11, 22, 33]
```

With several iterables, `map` stops as soon as the shortest one runs out.

### Filter: Select Elements

```python
# filter(predicate, iterable) - keeps elements where predicate is true
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional approach
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Practical example
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Carol", "grade": 78},
    {"name": "David", "grade": 95}
]

# Filter students with grade >= 90
honor_roll = list(filter(lambda s: s["grade"] >= 90, students))
print(honor_roll)
# [{'name': 'Bob', 'grade': 92}, {'name': 'David', 'grade': 95}]
```

### Reduce: Aggregate Elements

```python
from functools import reduce

# reduce(function, iterable[, initializer]) - accumulates result
numbers = [1, 2, 3, 4, 5]

# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum value
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# With initializer
# Sum with starting value of 100
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115

# Practical: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, nested, [])
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

**Notes on `reduce`:**

 - `reduce` on an **empty** iterable with no initializer raises `TypeError`. Pass an initializer whenever the input could be empty.
 - These examples show how `reduce` works; in real code prefer the dedicated tools: `sum(numbers)`, `max(numbers)`, `math.prod(numbers)`.
 - Flattening with `+` builds a new list at every step, so it gets slow on long inputs. `list(itertools.chain.from_iterable(nested))` or `[x for sub in nested for x in sub]` does the same job in one pass.

### Zip: Combine Iterables

`zip` does not take a function, so strictly speaking it is not a higher-order function. It is taught here because it is so often used together with `map` and `filter`.

```python
# zip(*iterables) - a lazy iterator of tuples built from parallel iterables
names = ["Alice", "Bob", "Carol"]
grades = [85, 92, 78]
subjects = ["Math", "Physics", "Chemistry"]

# Combine parallel lists
student_data = list(zip(names, grades, subjects))
print(student_data)
# [('Alice', 85, 'Math'), ('Bob', 92, 'Physics'), ('Carol', 78, 'Chemistry')]

# Unzip (transpose)
combined = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
names, grades = zip(*combined)
print(names)   # ('Alice', 'Bob', 'Carol')
print(grades)  # (85, 92, 78)

# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

**Gotcha:** 
- `zip` silently stops at the shortest input, so `list(zip([1, 2, 3], ["a", "b"]))` is `[(1, 'a'), (2, 'b')]` and the `3` is dropped without warning. 
- Write `zip(a, b, strict=True)` (Python 3.10+) to get a `ValueError` when the lengths differ. 
- Python 3.14 added the same `strict=True` option to `map`.

## 2.2 Lambda Functions

Anonymous functions for simple operations:

```python
# Lambda syntax: lambda arguments: expression

# Regular function
def add(x, y):
    return x + y

# Equivalent lambda (assigned to a name only so we can compare the two)
add_lambda = lambda x, y: x + y

print(add(5, 3))         # 8
print(add_lambda(5, 3))  # 8

# Lambdas are perfect for higher-order functions
numbers = [1, 2, 3, 4, 5]

# Without lambda (verbose)
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))

# With lambda (concise)
evens = list(filter(lambda n: n % 2 == 0, numbers))

# Lambda as a sort key
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
# Sort by grade (second element)
students.sort(key=lambda student: student[1])
print(students)  # [('Carol', 78), ('Alice', 85), ('Bob', 92)]
```

**Limits and style:**

- A lambda body is a **single expression**. No statements: no assignment, no `return`, no `for`/`while`, no `try`.
- PEP 8 advises against `name = lambda ...`. If a function deserves a name, write it with `def` — you get a real name in tracebacks and room for a docstring. Use lambdas where you would otherwise need a throwaway one-line function, such as a `key=` argument.

## 2.3 Comprehensions vs Functional Style

```python
numbers = range(1, 11)

# List comprehension (Pythonic)
squares_comp = [x**2 for x in numbers if x % 2 == 0]

# Functional style
squares_func = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

print(squares_comp)  # [4, 16, 36, 64, 100]
print(squares_func)  # [4, 16, 36, 64, 100]

# Performance comparison
import timeit

comp_time = timeit.timeit(
    '[x**2 for x in range(1000) if x % 2 == 0]',
    number=1000)
func_time = timeit.timeit(
    'list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1000))))',
    number=1000)

print(f"Comprehension: {comp_time:.4f}s")
print(f"Functional:    {func_time:.4f}s")
```

The comprehension usually wins here because the functional version pays for a `lambda` call on every element. When you already have a function to hand — especially a built-in such as `str.upper` or `int` — `map` is just as fast and sometimes faster. Exact timings vary by machine and Python version.

| Task | List comprehension | Functional style |
|---|---|---|
| Squares | `[x*x for x in nums]` | `list(map(lambda x: x*x, nums))` |
| Even squares | `[x*x for x in nums if x%2==0]` | `list(map(lambda x: x*x, filter(lambda x: x%2==0, nums)))` |
| First letters | `[w[0] for w in words]` | `list(map(lambda w: w[0], words))` |

(Without the outer `list(...)`, the right-hand column gives a lazy iterator, not a list.)

**Rule of thumb:**

- Simple transformations → comprehensions are clearer
- Complex pipelines, or when you already have a named function → `map` / `filter`

## 2.4 Callable Objects

Not just functions are callable!

```python
# Check if something is callable
print(callable(print))        # True - functions are callable
print(callable(lambda x: x))  # True - lambdas too
print(callable(42))           # False - integers aren't

# Classes are callable (calling one creates an instance)
print(callable(list))         # True
my_list = list([1, 2, 3])     # Calling the list class

# Objects can be made callable with __call__
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Make instance callable like a function"""
        return value * self.factor

# Create callable object
times_three = Multiplier(3)
print(callable(times_three))  # True
print(times_three(10))        # 30 - called like a function!

# Practical example: Stateful function object
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

Compare `Counter` with the closure version in section 1.5: both keep state between calls. A class is the better choice once you need several methods or want to inspect the state from outside (`counter.count`).

## Practice Exercises — Part 2

### Exercise 2.1 (Beginner): Double Everything

```python
numbers = [1, 2, 3, 4]

# TODO: Use map and a lambda to double every number.
#       Wrap the result in list(...).
doubled = None

print(doubled)   # [2, 4, 6, 8]
```
### Exercise 2.2 (Beginner): Same Result, Comprehension Style

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))
print(squares)        # [1, 4, 9, 16]

# TODO: Build the same list with a list comprehension (no map, no lambda).
squares_comp = None
print(squares_comp)   # [1, 4, 9, 16]
```

### Exercise 2.3 (Intermediate): Filter and Sort

```python
words = ["kiwi", "fig", "banana", "plum", "apple"]

# TODO 1: Use filter and a lambda to keep the words with more than 4 letters.
long_words = None
print(long_words)   # ['banana', 'apple']

# TODO 2: Use sorted() with key=lambda ... to order the words by length.
by_length = None
print(by_length)    # ['fig', 'kiwi', 'plum', 'apple', 'banana']
```
### Exercise 2.4 (Intermediate): Make an Object Callable

Look at `Multiplier` in section 2.4.

```python
class Adder:
    def __init__(self, amount):
        self.amount = amount

    # TODO: Write __call__(self, value) so that it returns value + self.amount.

add_ten = Adder(10)
print(add_ten(5))          # 15
print(callable(add_ten))   # True
```

### Exercise 2.5 (Advanced): Zip and Reduce

```python
from functools import reduce

names = ["Ann", "Ben", "Cy"]
scores = [80, 90, 70]

# TODO 1: Use zip to build a dictionary that maps each name to its score.
score_table = None
print(score_table)   # {'Ann': 80, 'Ben': 90, 'Cy': 70}

# TODO 2: Use reduce and a lambda to add up all the scores.
total = None
print(total)         # 240
```

# Part 3: Generators and Generator Expressions

## 3.1 Understanding Generators with Yield

Generators are functions that produce values **lazily** (on demand). Because only one value exists at a time, they are a memory-efficient way to work through long — or even endless — sequences.

**Regular function: builds and returns everything at once**

```python
def get_squares_list(n):
    """Return list of squares - uses O(n) memory"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result
```

**Generator: yields one value at a time**

```python
def get_squares_generator(n):
    """Yield squares one at a time - uses O(1) memory"""
    for i in range(n):
        yield i ** 2  # Pause and hand back a value
```

- Any function whose body contains `yield` is a **generator function**.
- Calling it does **not** run the body. It returns a *generator object*.
- Each `next()` runs the body up to the next `yield`, hands back that value, and pauses there with all local variables kept.
- When the body finishes, the generator raises `StopIteration`. A `for` loop handles that for you.

**Compare the two**

```python
squares_list = get_squares_list(5)
print(squares_list)  # [0, 1, 4, 9, 16] - all in memory

squares_gen = get_squares_generator(5)
print(squares_gen)   # <generator object get_squares_generator at 0x...>
```

**Iterate through the generator**

```python
for square in squares_gen:
    print(square, end=' ')  # 0 1 4 9 16
print()

# A generator can be consumed only ONCE
print(list(squares_gen))    # [] - already exhausted
```

To go through the values again, call the generator function again to get a fresh generator.

**Generator state example**

```python
def countdown(n):
    """Generator that counts down from n"""
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n  # Pause here and return n
        print(f"Resuming after yielding {n}")
        n -= 1
    print("Countdown complete!")

# Use the generator
gen = countdown(3)          # Nothing is printed yet!
print(next(gen))  # 3 - runs until first yield
print(next(gen))  # 2 - resumes from where it paused
print(next(gen))  # 1
# print(next(gen))  # prints the last two messages, then raises StopIteration
```

Full output of the three `next()` calls:

```
Starting countdown from 3
3
Resuming after yielding 3
2
Resuming after yielding 2
1
```

## 3.2 Generator Expressions

Comprehension syntax for generators.

**List comprehension — creates the full list**

```python
squares_list = [x**2 for x in range(1000000)]  # Uses lots of memory!
```

**Generator expression — creates a generator**

```python
squares_gen = (x**2 for x in range(1000000))   # Uses minimal memory!
```

**Memory comparison**

```python
import sys
print(f"List size: {sys.getsizeof(squares_list)} bytes")      # about 8.4 MB
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")  # about 200 bytes
```

> `sys.getsizeof` on a list counts only the list's own array of references, not the million integer objects it points to, so the real cost of the list is several times larger than the number printed. The generator's size stays the same no matter how many values it will produce. Exact numbers differ between Python versions.

**Chaining generators for efficiency**

```python
from itertools import islice

numbers = range(1, 1000000)
# Chain operations lazily - nothing is computed yet
result = (x**2 for x in numbers)
result = (x for x in result if x % 2 == 0)

# Take just the first five; only x = 1 .. 10 are ever squared
print(list(islice(result, 5)))  # [4, 16, 36, 64, 100]
```

> **Laziness only helps if the consumer stops early.** `list(result)[:5]` would look similar but does the opposite: `list()` first runs the *whole* pipeline — all 999,999 squares — and only then slices off five items. Use `itertools.islice(gen, n)` to take the first `n` items, or `next(gen)` for one.
>
> Also note that a filter such as `(x for x in result if x < 1000)` never stops by itself. It cannot know that no later value will pass, so it tests every remaining item. To stop at the first failure use `itertools.takewhile(lambda x: x < 1000, result)`.

## 3.3 Yield From

Delegate to another generator:

```python
def generator_a():
    yield 1
    yield 2

def generator_b():
    yield 3
    yield 4

# Without yield from (verbose)
def combined_verbose():
    for value in generator_a():
        yield value
    for value in generator_b():
        yield value

# With yield from (clean)
def combined_clean():
    yield from generator_a()
    yield from generator_b()

print(list(combined_clean()))  # [1, 2, 3, 4]

# Practical example: Flattening nested structures
def flatten(nested_list):
    """Recursively flatten nested lists"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate to recursive call
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]], 7]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7]
```

`yield from` works with any iterable, not only generators: `yield from [1, 2, 3]` is fine.

## 3.4 Sending Values to Generators

`yield` is also an *expression*. `gen.send(value)` resumes the generator, makes the paused `yield` evaluate to `value`, runs on to the next `yield`, and returns what that one yields.

```python
def doubler():
    """Generator that receives numbers and yields each one doubled"""
    print("Generator started")
    result = None
    while True:
        received = yield result  # Hand back the last result, wait for the next value
        print(f"Received: {received}")
        result = received * 2

# Use the interactive generator
gen = doubler()
next(gen)             # Prime it: run to the first yield (prints "Generator started")

print(gen.send(10))   # Received: 10, then 20
print(gen.send(5))    # Received: 5,  then 10
gen.close()           # Stop the generator cleanly
```

> **Rules for `send()`:**
>
> - A new generator must be **primed** with `next(gen)` (the same as `gen.send(None)`) before you can send it a real value, because at the start there is no paused `yield` to receive one.
> - Use **one** `yield` per loop for both directions, as above. With two separate `yield` expressions in the loop, every other `send()` lands on the "wrong" one and returns `None`.
> - Stop a generator with `gen.close()`. If you instead make the generator `return` or `break` in response to a sent value, that `send()` call raises `StopIteration` in the caller.

```python
# Practical: Running average calculator
def running_average():
    """Calculate running average of sent values"""
    total = 0
    count = 0
    average = 0

    while True:
        value = yield average
        if value is not None:
            total += value
            count += 1
            average = total / count

avg_gen = running_average()
next(avg_gen)  # Prime the generator

print(avg_gen.send(10))  # 10.0
print(avg_gen.send(20))  # 15.0
print(avg_gen.send(30))  # 20.0
```

> **Terminology:** generators used this way are often called *generator-based coroutines*. In modern Python the word "coroutine" normally means a function defined with `async def` and driven with `await`. That is a separate feature and is not covered in CS1350.

## Practice Exercises — Part 3

### Exercise 3.1 (Beginner): Add the Missing Line

```python
def count_up_to(n):
    """Yield 1, 2, 3, ... up to n."""
    i = 1
    while i <= n:
        # TODO: Hand back i with yield (one line).
        i += 1

print(list(count_up_to(3)))   # [1, 2, 3]

gen = count_up_to(2)
print(next(gen))              # 1
print(next(gen))              # 2
```
### Exercise 3.2 (Beginner): From List to Generator

```python
# TODO: Change this list comprehension into a generator expression.
#       (You only need to change two characters.)
squares = [x * x for x in range(5)]

print(next(squares))   # 0
print(next(squares))   # 1
print(list(squares))   # [4, 9, 16]  - only what is left
```

### Exercise 3.3 (Intermediate): Write a Generator

```python
def countdown(n):
    """Yield n, n-1, ... down to 1."""
    # TODO 1: Replace with your code. Use a while loop and yield.
    pass

print(list(countdown(3)))   # [3, 2, 1]

# TODO 2: Use a generator expression inside sum() to add up
#         the squares of the numbers from countdown(3).
total = None
print(total)                # 14
```
### Exercise 3.4 (Intermediate): yield from

```python
def morning():
    yield "wake up"
    yield "breakfast"

def evening():
    yield "dinner"
    yield "sleep"

def whole_day():
    """Yield everything from morning(), then everything from evening()."""
    # TODO: Replace with your code. Use yield from (two lines).
    pass

print(list(whole_day()))   # ['wake up', 'breakfast', 'dinner', 'sleep']
```

### Exercise 3.5 (Advanced): A Running Total with send()

This is the `running_average` example from section 3.4, made simpler.

```python
def running_total():
    """Receive numbers with send(); yield the total so far."""
    total = 0
    while True:
        value = yield total
        # TODO 1: Add value to total (one line).

gen = running_total()
# TODO 2: Prime the generator with next() before sending anything.

print(gen.send(5))    # 5
print(gen.send(10))   # 15
print(gen.send(1))    # 16
```

# Part 4: Advanced Parameter Handling

## 4.1 Python's Call Semantics

### Pass-by-Assignment (Object Reference Model)

Python is neither pass-by-value nor pass-by-reference in the C++ sense. It is **pass-by-assignment** (also called *pass by object reference* or *call by sharing*): the parameter name is bound to the very same object the caller passed, exactly as if you had written `parameter = argument`.

```python
# Immutable objects (int, str, tuple)
def modify_immutable(x):
    print(f"Inside function, id: {id(x)}")
    x = x + 1  # Creates NEW object and rebinds the local name x
    print(f"After modification, id: {id(x)}")
    return x

value = 10
print(f"Before call, id: {id(value)}")
result = modify_immutable(value)
print(f"After call, original: {value}, result: {result}")
# After call, original: 10, result: 11

# Mutable objects (list, dict, set)
def modify_mutable(lst):
    print(f"Inside function, id: {id(lst)}")
    lst.append(4)    # Modifies SAME object
    lst = [7, 8, 9]  # Rebinds the local name to a NEW list
    lst.append(10)   # Changes only the new list
    print(f"After reassignment, id: {id(lst)}")
    return lst

my_list = [1, 2, 3]
print(f"Before call, id: {id(my_list)}")
result = modify_mutable(my_list)
print(f"After call, original: {my_list}, result: {result}")
# Original is [1, 2, 3, 4], not [7, 8, 9, 10]!
```

- Immutables (`int`, `str`, `tuple`) *look like* pass-by-value, because nothing a function does can change the caller's object.
- Mutables (`list`, `dict`, `set`) *look like* pass-by-reference, because in-place changes are visible to the caller.
- The mechanism is identical in both cases. The two rules that matter: **mutating** an object is seen by everyone who holds it; **rebinding** a name (`x = ...`) affects only that name.

### Understanding Object References

```python
# Demonstration of reference behavior
def explain_references(obj):
    """Show how references work with different operations"""
    print(f"Parameter 'obj' references object at {id(obj)}")

    # These operations modify the existing object
    if isinstance(obj, list):
        obj.append("modified")  # Modifies original
        obj += ["extended"]     # Modifies original (in-place for lists)

    # This creates a new object
    obj = obj + ["new list"]    # Creates new object
    return obj

test_list = ["original"]
result = explain_references(test_list)
print(f"Original list: {test_list}")  # ['original', 'modified', 'extended']
print(f"Returned list: {result}")     # ['original', 'modified', 'extended', 'new list']
```

> `+=` changes a **list** in place, but for immutable types (`int`, `str`, `tuple`) it builds a new object and rebinds the name. So `obj += (1,)` inside a function never affects the caller's tuple.

## 4.2 *args and **kwargs

Flexible parameter handling.

**`*args`: collect extra positional arguments into a tuple**

```python
def sum_all(*args):
    """Sum any number of arguments"""
    print(f"args is a {type(args)}: {args}")
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

**`**kwargs`: collect extra keyword arguments into a dictionary**

```python
def print_info(**kwargs):
    """Print any keyword arguments"""
    print(f"kwargs is a {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
```

The names `args` and `kwargs` are only a convention; the `*` and `**` do the work.

**Combining regular parameters, `*args`, and `**kwargs`**

```python
def debug(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

debug(1, 2, 3, name="Ada", year=2026)
# args: (1, 2, 3)
# kwargs: {'name': 'Ada', 'year': 2026}
```

```python
def flexible_function(required, default="default", *args, **kwargs):
    """Demonstrate all parameter types"""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

flexible_function("must_provide", "custom", 1, 2, 3, key1="value1", key2="value2")
# Required: must_provide
# Default: custom
# Extra positional: (1, 2, 3)
# Extra keyword: {'key1': 'value1', 'key2': 'value2'}
```

**Unpacking in calls**

```python
coords = (10, 20)
print(*coords)  # same as print(10, 20)

options = {"sep": " | ", "end": "!!!\n"}
print("a", "b", "c", **options)  # a | b | c!!!
```

```python
# Unpacking with * and **
def greet(first, last, age):
    return f"{first} {last} is {age} years old"

# Unpack list/tuple as positional arguments
person_data = ["Alice", "Smith", 25]
print(greet(*person_data))  # Unpacks to greet("Alice", "Smith", 25)

# Unpack dictionary as keyword arguments
person_dict = {"first": "Bob", "last": "Jones", "age": 30}
print(greet(**person_dict))  # Unpacks to greet(first="Bob", last="Jones", age=30)

# Extended unpacking in assignments
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")
# First: 1, Middle: [2, 3, 4], Last: 5

# Merging dictionaries with unpacking
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2, "e": 5}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

Since Python 3.9 you can also merge with the `|` operator: `dict1 | dict2`. In both forms, when a key appears twice the right-most value wins.

## 4.3 Keyword-Only and Positional-Only Parameters

Two markers in a signature let you control *how* callers may pass each argument:

```python
def connect(host, /, port=5432, *, timeout=10, retries=3):
    return f"{host}:{port} timeout={timeout} retries={retries}"

print(connect("db.local"))                  # db.local:5432 timeout=10 retries=3
print(connect("db.local", 6000))            # port by position
print(connect("db.local", port=6000))       # port by keyword
print(connect("db.local", timeout=30))      # timeout MUST be passed by keyword

# connect(host="db.local")         # TypeError: host is positional-only
# connect("db.local", 6000, 30)    # TypeError: timeout is keyword-only
```

- Parameters **before `/`** are positional-only: callers cannot use the name.
- Parameters **after `*`** (or after `*args`) are keyword-only: callers must use the name.
- Everything in between can be passed either way.

Keyword-only parameters make calls self-documenting (`timeout=30` instead of a mystery `30`). The full order in a signature is: positional-only, `/`, regular, `*args` or a bare `*`, keyword-only, `**kwargs`.

## Practice Exercises — Part 4

### Exercise 4.1 (Beginner): Any Number of Arguments

```python
def total(*numbers):
    """Return the sum of all the arguments."""
    # TODO 1: Replace with your code (one line). Remember: numbers is a tuple.
    pass

print(total(1, 2, 3))   # 6
print(total())          # 0

prices = [5, 10, 15]
# TODO 2: Call total with the three prices by unpacking the list with *.
result = None
print(result)           # 30
```
### Exercise 4.2 (Beginner): Unpack a Dictionary into a Call

```python
def describe(name, age):
    return f"{name} is {age}"

person = {"name": "Ada", "age": 36}

# TODO: Call describe using the dictionary and the ** operator.
#       Do not type "Ada" or 36 yourself.
result = None
print(result)   # Ada is 36
```

### Exercise 4.3 (Intermediate): Keyword Arguments

```python
def make_profile(name, **info):
    """Return a dictionary holding every keyword argument plus "name"."""
    # TODO: Replace with your code. Remember: info is already a dictionary.
    pass

print(make_profile("Alice", major="CS", year=2))
# {'major': 'CS', 'year': 2, 'name': 'Alice'}
print(make_profile("Bob"))
# {'name': 'Bob'}
```
### Exercise 4.4 (Intermediate): Unpacking Without a Function

```python
scores = [55, 70, 80, 90, 100]

# TODO 1: In ONE assignment with a starred name, put the first score in
#         lowest, the last score in highest, and the rest in middle.

print(lowest, highest)   # 55 100
print(middle)            # [70, 80, 90]

defaults = {"color": "blue", "size": "M"}
custom = {"size": "L"}

# TODO 2: Merge the two dictionaries with ** so that custom wins.
settings = None
print(settings)          # {'color': 'blue', 'size': 'L'}
```

### Exercise 4.5 (Advanced): Fix the Bug

This function is supposed to empty the caller's shopping cart, but it does nothing. Change **one line** to fix it.

```python
def empty_cart(cart):
    cart = []   # BUG: this only rebinds the local name

my_cart = ["pen", "book"]
empty_cart(my_cart)
print(my_cart)   # should be []  (the buggy version prints ['pen', 'book'])
```

Hint: section 4.1 — *rebinding* a name does not affect the caller, *mutating* the object does. Lists have a `.clear()` method.

# Part 5: Type Hints and Function Annotations

## Basic Type Hints

```python
from collections.abc import Callable

# Basic type hints
def add(x: int, y: int) -> int:
    """Add two integers"""
    return x + y

# Complex types: built-in collections can be subscripted directly
def process_scores(scores: list[float]) -> dict[str, float]:
    """Calculate statistics from scores (scores must not be empty)"""
    return {
        "mean": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    }

# Optional parameters (can be None)
def greet(name: str, title: str | None = None) -> str:
    if title:
        return f"Hello, {title} {name}"
    return f"Hello, {name}"

# Union types (multiple possible types)
def process_id(user_id: int | str) -> str:
    """Accept either integer or string ID"""
    return f"User-{user_id}"

# Function type hints: Callable[[argument types], return type]
def apply_operation(
    data: list[int],
    operation: Callable[[int], int]
) -> list[int]:
    """Apply operation function to each element"""
    return [operation(x) for x in data]

# Using the typed function
result = apply_operation([1, 2, 3], lambda x: x * 2)
print(result)  # [2, 4, 6]
```

> **Type hints are not enforced when your program runs.** Python stores them and otherwise ignores them:
>
> ```python
> print(add("a", "b"))  # ab  - no error, even though the hints say int
> ```
>
> Hints are checked by separate tools — a static type checker such as **mypy** or **pyright**, or your IDE — which read your code *without running it* and report mismatches.

> **Older spelling you will see in existing code:** before Python 3.9/3.10 these hints had to be imported from `typing` and written `List[float]`, `Dict[str, float]`, `Optional[str]`, and `Union[int, str]`. Those forms still work, but `typing.List`, `typing.Dict`, and `typing.Tuple` are deprecated aliases. In new code write `list[float]`, `dict[str, float]`, `str | None`, and `int | str`, and import `Callable` from `collections.abc`.

## Function Annotations (Metadata)

```python
# At run time an annotation can be any expression, not just a type
def documented_function(
    x: "First parameter",
    y: "Second parameter"
) -> "The sum of x and y":
    return x + y

# Access annotations
print(documented_function.__annotations__)
# {'x': 'First parameter', 'y': 'Second parameter', 'return': 'The sum of x and y'}
```

> This shows that annotations are just data attached to the function. Do not write real code this way: type checkers expect annotations to be types and will reject these strings. Put descriptions in the docstring. (When you need a type *plus* extra metadata, the standard tool is `typing.Annotated`, e.g. `x: Annotated[int, "First parameter"]`.)
>
> To read annotations, `inspect.get_annotations(func)` is the recommended call. Since Python 3.14, annotations are evaluated lazily — only when something asks for them — so a hint may mention a class that is defined further down the file without being put in quotes.

### Validating Results with a Decorator Factory

```python
from functools import wraps

def validate_range(min_val: int, max_val: int):
    """Decorator factory: check that the function's result is in a range"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not (min_val <= result <= max_val):
                raise ValueError(f"Result {result} out of range [{min_val}, {max_val}]")
            return result
        return wrapper
    return decorator

@validate_range(0, 100)
def calculate_percentage(score: int, total: int) -> float:
    return (score / total) * 100

print(calculate_percentage(85, 100))  # 85.0
# calculate_percentage(150, 100)  # ValueError: Result 150.0 out of range [0, 100]
```

Note that `validate_range` does not read the annotations at all: the range comes from its own arguments. It is the same decorator-factory pattern as the `@retry` decorator from Week 14, and Part 7 looks at the pattern again.

## Newer Typing Syntax (Python 3.12+)

```python
# Type alias: a readable name for a complicated type
type Vector = list[float]

def scale(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]

print(scale([1.0, 2.5], 2))  # [2.0, 5.0]

# Generic function: "whatever type goes in the list is the type that comes out"
def first[T](items: list[T]) -> T:
    return items[0]

print(first([3, 1, 2]))      # 3   (a checker infers int)
print(first(["a", "b"]))     # a   (a checker infers str)
```

> Before 3.12 an alias was written `Vector: TypeAlias = list[float]` (with `from typing import TypeAlias`, added in Python 3.10) and generics needed `T = TypeVar("T")`. Both still run, but `TypeAlias` has been deprecated since 3.12 in favor of the `type` statement.

Type hints help IDEs, mypy, pyright, and future readers.

## Practice Exercises — Part 5

### Exercise 5.1 (Beginner): Add the Hints

Add type hints to the parameters and return values. Do not change the function bodies.

```python
def area(width, height):   # both are floats; returns a float
    return width * height

def greet(name):           # name is a string; returns a string
    return f"Hello, {name}!"

print(area.__annotations__)
# {'width': <class 'float'>, 'height': <class 'float'>, 'return': <class 'float'>}
print(greet.__annotations__)
# {'name': <class 'str'>, 'return': <class 'str'>}
```

### Exercise 5.2 (Intermediate): Hints for Collections and None

Add the hints. Do not change the function bodies.

```python
def average(scores):               # scores: a list of floats; returns a float
    return sum(scores) / len(scores)

def find_user(users, user_id):     # users: a dict from int to str; user_id: an int
    """Return the user's name, or None if the id is unknown."""
    return users.get(user_id)      # returns a str or None

print(average.__annotations__)
# {'scores': list[float], 'return': <class 'float'>}
print(find_user.__annotations__)
# {'users': dict[int, str], 'user_id': <class 'int'>, 'return': str | None}
```

### Exercise 5.3 (Advanced): A Function That Takes a Function

Look at `apply_operation` in Part 5 and write a similar function yourself, hints included.

```python
from collections.abc import Callable

# TODO: Write apply_to_all with two parameters:
#         numbers - a list of ints
#         func    - a function that takes an int and returns an int
#       It returns a new list of ints: func applied to every number.

print(apply_to_all([1, 2, 3], lambda x: x + 1))   # [2, 3, 4]
print(list(apply_to_all.__annotations__))         # ['numbers', 'func', 'return']
```

### Exercise 5.4 (Beginner): A Parameter That May Be None

Add the hints. Do not change the function body.

```python
def greet(name, title=None):   # name: a string; title: a string or None; returns a string
    if title:
        return f"Hello, {title} {name}"
    return f"Hello, {name}"

print(greet("Hopper", "Dr."))    # Hello, Dr. Hopper
print(greet.__annotations__)
# {'name': <class 'str'>, 'title': str | None, 'return': <class 'str'>}
```

### Exercise 5.5 (Intermediate): Hints Are Not Enforced

**Step 1:** before you run this, write down what you think it prints.

```python
def double(n: int) -> int:
    return n * 2

user_input = "5"   # text typed by a user is always a string
print(double(user_input))
```

**Step 2:** the hint says `int`, but Python did not stop the string. Change the last line so that `double` receives a real `int` and the program prints `10`. Do not change the function.

---

# Part 6: Context Managers as Functions

You met the `with` statement and class-based context managers (`__enter__` / `__exit__`) in Week 14. `contextlib.contextmanager` lets you write one as a single generator function instead.

## Using contextlib

```python
from contextlib import contextmanager
import time

# Create context manager with generator
@contextmanager
def timer(label):
    """Context manager to time code execution"""
    print(f"Starting {label}...")
    start = time.perf_counter()

    try:
        yield  # The body of the with-block runs here
    finally:
        end = time.perf_counter()
        print(f"{label} took {end - start:.4f} seconds")

# Use the context manager
with timer("Processing"):
    time.sleep(1)
    print("Doing work...")
# Starting Processing...
# Doing work...
# Processing took 1.00xx seconds
```

How the generator maps onto the `with` statement:

| Part of the generator | When it runs |
|---|---|
| Code before `yield` | On entering the `with` block (like `__enter__`) |
| The value after `yield` | Becomes the `as` variable |
| Code after `yield` | On leaving the block (like `__exit__`) |

> **Rules:**
>
> - The function must `yield` **exactly once**.
> - If the `with` body raises an exception, that exception is re-raised *inside the generator at the `yield` line*. Without `try` / `finally` around the `yield`, your cleanup code would be skipped — so always use it.
> - `time.perf_counter()` is the right clock for measuring elapsed time; `time.time()` can jump if the system clock is adjusted.

```python
# File handling context manager
@contextmanager
def managed_file(filename, mode):
    """Ensure file is properly closed"""
    print(f"Opening {filename}")
    file = open(filename, mode, encoding="utf-8")
    try:
        yield file  # 'file' becomes the 'as' variable
    finally:
        print(f"Closing {filename}")
        file.close()

with managed_file("demo_notes.txt", "w") as f:
    f.write("Hello from a context manager\n")
print(f.closed)  # True
# Opening demo_notes.txt
# Closing demo_notes.txt
# True
```

`open()` is already a context manager, so in real code you would simply write `with open(...) as f:`. `managed_file` is here to show the pattern for resources that do not come with one.

```python
# Temporary state context manager
@contextmanager
def temporary_attribute(obj, attr, value):
    """Temporarily change object attribute"""
    old_value = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)

class Settings:
    debug = False

settings = Settings()
with temporary_attribute(settings, "debug", True):
    print(settings.debug)  # True  - inside the block
print(settings.debug)      # False - restored afterwards
```

## Practice Exercises — Part 6

### Exercise 6.1 (Beginner): Fill in the Two Prints

```python
from contextlib import contextmanager

@contextmanager
def banner(title):
    # TODO 1: print "=== <title> ==="
    try:
        yield
    finally:
        # TODO 2: print "=== end ==="
        pass

with banner("Report"):
    print("line 1")
# === Report ===
# line 1
# === end ===
```

### Exercise 6.2 (Intermediate): Write One Yourself

Use Exercise 6.1 as your model.

```python
from contextlib import contextmanager

# TODO: Write a context manager tag(name) that prints <name> before the
#       block and </name> after it - even if the block raises an exception.

with tag("b"):
    print("hello")
# <b>
# hello
# </b>

try:
    with tag("i"):
        raise ValueError("boom")
except ValueError:
    print("error caught")
# <i>
# </i>
# error caught
```

### Exercise 6.3 (Advanced): A Temporary Setting

Look at `temporary_attribute` in Part 6. Do the same for a dictionary entry.

```python
from contextlib import contextmanager

@contextmanager
def temporary_setting(settings, key, value):
    """Set settings[key] to value inside the with-block, then put the old value back."""
    old_value = settings[key]
    # TODO: 1. store the new value
    #       2. try: yield
    #       3. finally: restore old_value

settings = {"volume": 3}
with temporary_setting(settings, "volume", 10):
    print(settings["volume"])   # 10
print(settings["volume"])       # 3
```

### Exercise 6.4 (Beginner): Use a Context Manager

The context manager is already written. You only have to use it.

```python
from contextlib import contextmanager

@contextmanager
def announce(label):
    print(f"Starting {label}")
    try:
        yield
    finally:
        print(f"Finished {label}")

# TODO: Write a with statement that uses announce("backup")
#       and runs print("copying files") inside it.

# Starting backup
# copying files
# Finished backup
```

### Exercise 6.5 (Intermediate): Hand a Value to the with-Block

```python
from contextlib import contextmanager

@contextmanager
def open_basket():
    items = []
    try:
        # TODO: Replace the next line. Yield items, so that it becomes
        #       the variable after `as`.
        pass
    finally:
        print(f"Collected {len(items)} items")

with open_basket() as basket:
    basket.append("apple")
    basket.append("pear")
# Collected 2 items
```

---

# Part 7: Function Factories and Meta-Programming

**Meta-programming** means writing code that creates or modifies other code. In this course that means functions that build functions (factories) and functions that wrap functions (decorators).

## Function Factories

**Create specialized functions dynamically**

```python
def make_power_function(exponent):
    """Factory for power functions"""
    def power(base):
        return base ** exponent
    power.__name__ = f"power_{exponent}"
    power.__doc__ = f"Raise to power {exponent}"
    return power

# Generate family of functions
square = make_power_function(2)
cube = make_power_function(3)
fourth_power = make_power_function(4)

print(square(5))        # 25
print(cube(3))          # 27
print(fourth_power(2))  # 16
print(cube.__name__)    # power_3
```

## Decorator Factories

A decorator is a function that takes a function and returns a replacement for it. The `@` line is shorthand:

```python
# @decorator            is the same as        def greet(...): ...
# def greet(...): ...                         greet = decorator(greet)
```

A **decorator factory** adds one more layer so the decorator can take settings: `@repeat(3)` first calls `repeat(3)`, which returns the actual decorator.

```python
from functools import wraps

def repeat(times):
    """Decorator factory - create decorator that repeats function call"""
    def decorator(func):
        @wraps(func)  # copy func's name and docstring onto wrapper
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"

print(greet("Alice"))  # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
print(greet.__name__)  # greet   (without @wraps this would print: wrapper)
```

> Always put `@wraps(func)` on the wrapper. Without it the decorated function loses its own name and docstring, which makes tracebacks, `help()`, and debugging confusing.
>
> `repeat` calls the function a fixed number of times and collects the results. Do not confuse it with the `@retry` decorator from Week 14, which calls the function again only when it *fails*. The three-level shape (factory → decorator → wrapper) is the same.

## Advanced: Function Generation from Specifications

```python
def create_validator(rules):
    """Create validation function from rules dictionary"""
    def validate(data):
        for field, rule in rules.items():
            if field not in data:
                return False, f"Missing field: {field}"
            if not rule(data[field]):
                return False, f"Invalid {field}: {data[field]}"
        return True, "Valid"
    return validate

# Define validation rules (check the type FIRST, then the value)
user_validator = create_validator({
    'age': lambda x: isinstance(x, int) and 0 < x < 150,
    'email': lambda x: isinstance(x, str) and '@' in x and '.' in x,
    'name': lambda x: isinstance(x, str) and len(x) > 0
})

# Test validation
test_user = {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'}
is_valid, message = user_validator(test_user)
print(f"Validation: {message}")  # Validation: Valid

bad_user = {'name': 'Bob', 'age': 25, 'email': None}
is_valid, message = user_validator(bad_user)
print(f"Validation: {message}")  # Validation: Invalid email: None
```

> **Why the `isinstance` checks matter:** a rule written as just `'@' in x and '.' in x` crashes with `TypeError` when the value is `None` or a number — the validator would blow up on exactly the bad data it is supposed to report. Test the type first; `and` stops at the first false condition.
>
> One more surprise: `bool` is a subclass of `int`, so `isinstance(True, int)` is `True` and the `age` rule accepts `True` as an age (it equals `1`). Use `type(x) is int` when you need to exclude booleans.

## Practice Exercises — Part 7

### Exercise 7.1 (Beginner): Finish the Factory

```python
def make_greeter(greeting):
    def greet(name):
        # TODO: Return "<greeting>, <name>!" (one line).
        pass
    return greet

hello = make_greeter("Hello")
hola = make_greeter("Hola")
print(hello("Ada"))   # Hello, Ada!
print(hola("Ada"))    # Hola, Ada!
```

### Exercise 7.2 (Intermediate): Write a Factory

```python
def make_tax_calculator(rate):
    """Return a function that takes a price and returns the price
    with tax added, rounded to 2 decimal places."""
    # TODO: Define an inner function, then return it.
    #       Price with tax is: price * (1 + rate)
    pass

with_state_tax = make_tax_calculator(0.08)
with_city_tax = make_tax_calculator(0.10)
print(with_state_tax(50))   # 54.0
print(with_city_tax(50))    # 55.0
```

### Exercise 7.3 (Advanced): Finish the Decorator

```python
from functools import wraps

def announce(func):
    """Decorator: print 'Calling <function name>' before every call."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO 1: print "Calling " followed by func.__name__
        # TODO 2: call func with the same arguments and return its result
        pass
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))
# Calling add
# 5
print(add.__name__)   # add
```

### Exercise 7.4 (Beginner): Use a Factory

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# TODO: Use make_multiplier to create the two functions below.
triple = None
times_ten = None

print(triple(4))      # 12
print(times_ten(4))   # 40
```

### Exercise 7.5 (Intermediate): Two Ways to Apply a Decorator

The decorator is already written. You only have to apply it.

```python
from functools import wraps

def exclaim(func):
    """Decorator: add '!!!' to the end of whatever func returns."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

# TODO 1: Decorate hello with exclaim by adding ONE line with the @ syntax.
def hello(name):
    return f"Hello, {name}"

def goodbye(name):
    return f"Goodbye, {name}"

# TODO 2: Decorate goodbye WITHOUT the @ syntax, with one assignment.

print(hello("Ada"))     # Hello, Ada!!!
print(goodbye("Ada"))   # Goodbye, Ada!!!
```

---

# Summary and Key Takeaways

## What We've Learned

1. **First-Class Functions**
   - Functions as values, arguments, and return values
   - Foundation of functional programming in Python
2. **Higher-Order Functions**
   - `map`, `filter`, `reduce` for data transformation (all lazy except `reduce`)
   - Lambda functions for short, single-expression functions
   - Callable objects for stateful functions
3. **Generators**
   - Memory-efficient iteration with `yield`
   - Generator expressions for lazy evaluation
   - Two-way communication with `send()`
4. **Advanced Parameters**
   - Python's pass-by-assignment model: mutate vs. rebind
   - `*args` and `**kwargs` for flexibility; `/` and `*` to control how arguments are passed
   - Unpacking operators
5. **Type Hints**
   - Static type checking support (not enforced at run time)
   - Self-documenting code
   - Run-time introspection
6. **Context Managers**
   - Resource management with generator functions
   - Clean setup/teardown patterns
7. **Function Factories**
   - Dynamic function generation
   - Decorators and decorator factories

| Concept | Why it matters |
|---|---|
| First-class functions | Enables functional programming in Python |
| `map` / `filter` / `reduce` / `lambda` | Clean data transformations |
| Generators | Memory-efficient processing of huge or infinite data |
| `*args` / `**kwargs`, keyword-only and positional-only parameters | Write flexible, clear APIs |
| Type hints | Catch bugs early with a type checker; better IDE support |
| Decorators & factories | DRY, reusable behavior (caching, logging, validation…) |

## Best Practices

```python
# 1. Use appropriate functional tools
# Good: Clear and efficient
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 2. Choose generators for large datasets
# Good: Memory efficient - nothing is computed until you iterate
def process(x):
    return x * 2

huge_list = range(1_000_000)
large_data = (process(x) for x in huge_list)

# 3. Type hints for clarity
def calculate(values: list[float]) -> dict[str, float]:
    return {"total": sum(values)}

# 4. Leverage closures for state
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# 5. Use @wraps in every decorator you write
```

## When to Use These Techniques

- **First-class functions:** Callbacks, event handlers, strategy pattern
- **Higher-order functions:** Data transformation pipelines
- **Generators:** Large datasets, infinite sequences, streaming data
- **Type hints:** API design, team projects, documentation
- **Context managers:** Resource management, temporary state
- **Function factories:** Configuration-driven behavior, decorators, validation rules

## Practice Exercise Index

| Part | Beginner | Intermediate | Advanced | More practice (Beginner) | More practice (Intermediate) |
|---|---|---|---|---|---|
| 1. First-class functions | 1.1 A second name for a function | 1.2 Pick a function from a dictionary | 1.3 Your own function factory | 1.4 Pass a function as an argument | 1.5 Run a list of functions |
| 2. Higher-order functions | 2.1 Double everything | 2.2 Filter and sort | 2.3 Zip and reduce | 2.4 Same result, comprehension style | 2.5 Make an object callable |
| 3. Generators | 3.1 Add the missing line | 3.2 Write a generator | 3.3 A running total with `send()` | 3.4 From list to generator | 3.5 `yield from` |
| 4. Parameters | 4.1 Any number of arguments | 4.2 Keyword arguments | 4.3 Fix the bug | 4.4 Unpack a dictionary into a call | 4.5 Unpacking without a function |
| 5. Type hints | 5.1 Add the hints | 5.2 Hints for collections and `None` | 5.3 A function that takes a function | 5.4 A parameter that may be `None` | 5.5 Hints are not enforced |
| 6. Context managers | 6.1 Fill in the two prints | 6.2 Write one yourself | 6.3 A temporary setting | 6.4 Use a context manager | 6.5 Hand a value to the with-block |
| 7. Factories | 7.1 Finish the factory | 7.2 Write a factory | 7.3 Finish the decorator | 7.4 Use a factory | 7.5 Two ways to apply a decorator |

## Questions for Reflection

1. When should you choose functional style over imperative?
2. How do generators improve memory efficiency?
3. Why does Python use pass-by-assignment?
4. When are type hints most valuable?
5. How can function factories reduce code duplication?