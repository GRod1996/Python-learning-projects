def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """
    # TODO: Implement this
    # Hint: x^n = x * x^(n-1)
    # Hint: What's x^0?
    if n == 0:
        return 1
    return x * power(x, n - 1)


print(power(2, 5))
print(power(3, 0))
print(power(5, 3))

# Test cases:
# power(2, 5) should return 32
# power(3, 0) should return 1
# power(5, 3) should return 125


### Exercise 1.1 (Beginner): A Second Name for a Function


def shout(text):
    return text.upper() + "!"


# TODO: Make `yell` another name for the same function.
#       Assign the function itself - no parentheses.
yell = shout

print(yell("hello"))  # HELLO!
print(yell is shout)  # True


### Exercise 1.2 (Beginner): Pass a Function as an Argument


def apply(func, value):
    """Call func on value and return the result."""
    return func(value)


# TODO 1: Use apply to call the built-in len on "hello".
length = apply(len, "hello")
print(length)  # 5

# TODO 2: Use apply to call str.upper on "hello".
loud = apply(str.upper, "hello")
print(loud)  # HELLO


### Exercise 1.3 (Intermediate): Pick a Function from a Dictionary


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# TODO 1: Add one more entry so that "-" maps to subtract.
OPERATIONS = {"+": add, "-": subtract}


def calculate(symbol, a, b):
    # TODO 2: Look up the function for symbol in OPERATIONS,
    #         call it with a and b, and return the result.
    calculate = OPERATIONS[symbol]
    return calculate(a, b)


print(calculate("+", 8, 2))  # 10
print(calculate("-", 8, 2))  # 6


### Exercise 1.4 (Intermediate): Run a List of Functions


def double(x):
    return x * 2


def add_ten(x):
    return x + 10


steps = [double, add_ten, double]
value = 5

# TODO: Loop over steps. Each time, call the function on value
#       and store the result back in value. (Two lines.)
for step in steps:
    value = step(value)
print(value)  # 40

### Exercise 2.1 (Beginner): Double Everything

numbers = [1, 2, 3, 4]

# TODO: Use map and a lambda to double every number.
#       Wrap the result in list(...).
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # [2, 4, 6, 8]

### Exercise 2.2 (Beginner): Same Result, Comprehension Style

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))
print(squares)  # [1, 4, 9, 16]


# TODO: Build the same list with a list comprehension (no map, no lambda).
def is_square(x):
    return x * x


squares_comp = list(map(is_square, numbers))
print(squares_comp)  # [1, 4, 9, 16]
