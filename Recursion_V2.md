# CS1350 Computer Science II: Introduction to Recursion

## Lecture Outline
1. **Introduction with Factorial** 
2. **Anatomy of Recursion** 
3. **Implementation and Call Stack**
4. **Additional Examples**
5. **Algorithm Design and Analysis** 
6. **Theory of Recursion**
7. **Advanced Topics: Divide & Conquer, Dynamic Programming**

## Part 1: Introduction to Recursion via Factorial

### What is Recursion?

**Recursion** is a problem-solving technique where a function calls itself to solve smaller instances of the same problem.

> "To understand recursion, you must first understand recursion." - Computer Science Joke

### The Factorial Example

Let's start with a mathematical concept you already know: factorial.

**Mathematical Definition:**
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 4! = 4 × 3 × 2 × 1 = 24
- 3! = 3 × 2 × 1 = 6

**But notice something interesting:**
- 5! = 5 × 4!
- 4! = 4 × 3!
- 3! = 3 × 2!

**This gives us a recursive definition:**
```
n! = n × (n-1)!  for n > 0
0! = 1           (by definition)
```

### Iterative vs Recursive Implementation

**Iterative Approach** (what you're familiar with):
```python
def factorial_iterative(n):
    """Calculate factorial using iteration"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Recursive Approach** (the new way):
```python
def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:  # Base case
        return 1
    else:                  # Recursive step
        return n * factorial_recursive(n - 1)
```

### Tracing the Recursion

Let's trace `factorial_recursive(4)`:
```
factorial_recursive(4)
├── 4 * factorial_recursive(3)
    ├── 3 * factorial_recursive(2)
        ├── 2 * factorial_recursive(1)
            ├── returns 1
        ├── returns 2 * 1 = 2
    ├── returns 3 * 2 = 6
├── returns 4 * 6 = 24
```

## Part 2: Anatomy of Recursion

### The Two Essential Components

Every recursive function **MUST** have these two parts:

#### 1. Base Case(s)
- The condition that stops the recursion
- Without it, you get infinite recursion (*stack overflow*!)
- Usually the simplest possible input

```python
if n == 0 or n == 1:  # Base case for factorial
    return 1
```

#### 2. Recursive Step
- The function calling itself with a **smaller/simpler** input
- Must make progress toward the base case
- Contains the problem decomposition logic

```python
return n * factorial_recursive(n - 1)  # Recursive step
```

### The Recursive Thinking Pattern

1. **Identify the simplest case** (base case)
2. **Express the problem in terms of smaller subproblems**
3. **Combine solutions** of subproblems to solve the original

### Common Pitfalls

```python
# BAD: No base case - infinite recursion!
def bad_factorial(n):
    return n * bad_factorial(n - 1)

# BAD: Doesn't progress toward base case
def another_bad_factorial(n):
    if n == 0:
        return 1
    return n * another_bad_factorial(n)  # n doesn't decrease!
```

| Part             | Purpose                                      | Factorial example                     |
|------------------|----------------------------------------------|---------------------------------------|
| Base case        | Stops the recursion (no recursive call)     | `if n == 0: return 1`                |
| Recursive case   | Makes progress toward the base case          | `return n * factorial(n-1)`          |

### Practice Exercises

#### Exercise 2.1: Beginner - Sum of Natural Numbers
**Problem:** Write a recursive function to calculate the sum of first n natural numbers.

```python
def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    # TODO: Implement this
    # Hint: What's the base case? When n = 0 or n = 1?
    # Hint: How can you express sum(n) in terms of sum(n-1)?
    pass

# Test cases:
# sum_natural(5) should return 15
# sum_natural(10) should return 55
# sum_natural(1) should return 1
```

#### Exercise 2.2: Intermediate - Count Digits
**Problem:** Write a recursive function that counts the number of digits in a positive integer.

```python
def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """
    # TODO: Implement this
    # Hint: How many digits does n // 10 have?
    # Hint: What's the base case? Single digit number?
    pass

# Test cases:
# count_digits(1234) should return 4
# count_digits(987654321) should return 9
# count_digits(5) should return 1
```


#### Exercise 2.3: Advanced - Palindrome Checker
**Problem:** Write a recursive function to check if a string is a palindrome (reads same forwards and backwards).

```python
def is_palindrome(s):
    """
    Check if string s is a palindrome recursively.
    Ignore case and consider only alphanumeric characters.
    Example: is_palindrome("A man a plan a canal Panama") = True
    Example: is_palindrome("race a car") = False
    """
    # TODO: Implement this
    # Hint: Compare first and last characters
    # Hint: What happens to the middle?
    # Hint: What are the base cases? (empty string, single char)
    pass

# Test cases:
# is_palindrome("racecar") should return True
# is_palindrome("hello") should return False
# is_palindrome("a") should return True
```

## Part 3: Implementation - Visualizing the Call Stack

### Understanding the Call Stack

When a function calls another function (including itself), Python uses a **call stack** to keep track of:
- Local variables
- Parameters
- Return addresses

### Step-by-Step Stack Visualization

Let's trace `factorial_recursive(4)` showing the stack:

```
Step 1: Initial call
┌─────────────────────┐
│ factorial(4)        │ ← Active
│ n = 4              │
│ waiting for...     │
└─────────────────────┘

Step 2: First recursive call
┌─────────────────────┐
│ factorial(3)        │ ← Active
│ n = 3              │
│ waiting for...     │
├─────────────────────┤
│ factorial(4)        │
│ n = 4              │
│ waiting at line 5  │
└─────────────────────┘

Step 3: Second recursive call
┌─────────────────────┐
│ factorial(2)        │ ← Active
│ n = 2              │
│ waiting for...     │
├─────────────────────┤
│ factorial(3)        │
│ n = 3              │
│ waiting at line 5  │
├─────────────────────┤
│ factorial(4)        │
│ n = 4              │
│ waiting at line 5  │
└─────────────────────┘

Step 4: Third recursive call
┌─────────────────────┐
│ factorial(1)        │ ← Active
│ n = 1              │
│ returns 1          │
├─────────────────────┤
│ factorial(2)        │
│ n = 2              │
│ waiting at line 5  │
├─────────────────────┤
│ factorial(3)        │
│ n = 3              │
│ waiting at line 5  │
├─────────────────────┤
│ factorial(4)        │
│ n = 4              │
│ waiting at line 5  │
└─────────────────────┘
```

### Stack Unwinding

Now the stack "unwinds" as functions return:

```
Step 5: factorial(1) returns 1
┌─────────────────────┐
│ factorial(2)        │ ← Active
│ n = 2              │
│ computes: 2 * 1 = 2│
├─────────────────────┤
│ factorial(3)        │
│ factorial(4)        │
└─────────────────────┘

Step 6: factorial(2) returns 2
┌─────────────────────┐
│ factorial(3)        │ ← Active
│ n = 3              │
│ computes: 3 * 2 = 6│
├─────────────────────┤
│ factorial(4)        │
└─────────────────────┘

Step 7: factorial(3) returns 6
┌─────────────────────┐
│ factorial(4)        │ ← Active
│ n = 4              │
│ computes: 4 * 6 = 24│
└─────────────────────┘

Step 8: factorial(4) returns 24
Stack is now empty!
Result: 24
```

### Debugging Recursive Functions

```python
def factorial_debug(n, depth=0):
    """Factorial with debug output to visualize recursion"""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    
    if n == 0 or n == 1:
        print(f"{indent}Base case reached! Returning 1")
        return 1
    else:
        print(f"{indent}Need to compute {n} * factorial({n-1})")
        result = n * factorial_debug(n - 1, depth + 1)
        print(f"{indent}factorial({n}) = {n} * {result // n} = {result}")
        return result

# Try it!
factorial_debug(4)
```

## Part 4: More Examples of Recursion

### Example 1: Fibonacci Sequence

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

**Mathematical Definition:**
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
```

**Recursive Implementation:**
```python
def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

**Trace for fibonacci(5):**
```
                    fib(5)
                   /      \
                fib(4)    fib(3)
               /    \      /    \
           fib(3)  fib(2) fib(2) fib(1)
           /   \    /  \   /  \
       fib(2) fib(1) fib(1) fib(0)
       /   \
    fib(1) fib(0)
```

Note: This has exponential time complexity! We'll address this later.

### Example 2: Binary Tree Traversal

Trees are naturally recursive structures!

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    """Traverse binary tree in order (left, root, right)"""
    if node is None:  # Base case
        return
    
    inorder_traversal(node.left)   # Visit left subtree
    print(node.value, end=' ')      # Process current node
    inorder_traversal(node.right)  # Visit right subtree

# Example tree:
#       5
#      / \
#     3   8
#    / \   \
#   1   4   9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(9)

inorder_traversal(root)  # Output: 1 3 4 5 8 9
```

### Example 3: N-Queens Problem

The N-Queen problem asks: *How can we place N queens on an N×N chessboard so that none attack each other?*

This is solved recursively via **backtracking**:

* Place a queen in a row.
* Recursively attempt to place queens in remaining rows.
* Backtrack if necessary.

This is one of the best examples of recursion for solving constraint-satisfaction problems.

```python
def solve_n_queens(n):
    """Solve the N-Queens problem using backtracking"""
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def is_safe(board, row, col):
        """Check if placing queen at (row, col) is safe"""
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def solve(row):
        """Recursively place queens row by row"""
        if row == n:  # Base case: all queens placed
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(n):  # Try each column
            if is_safe(board, row, col):
                board[row][col] = 'Q'  # Place queen
                solve(row + 1)         # Recurse to next row
                board[row][col] = '.'  # Backtrack
    
    solve(0)
    return solutions

# Example: 4-Queens
solutions = solve_n_queens(4)
print(f"Found {len(solutions)} solutions for 4-Queens")
```

### Practice Exercises 

#### Exercise 4.1: Beginner - Power Function
**Problem:** Implement a recursive function to calculate x^n (x to the power n).

```python
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

# Test cases:
# power(2, 5) should return 32
# power(3, 0) should return 1
# power(5, 3) should return 125
```

#### Exercise 4.2: Intermediate - Generate All Binary Strings
**Problem:** Generate all binary strings of length n.

```python
def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    Example: generate_binary_strings(2) = ['00', '01', '10', '11']
    Example: generate_binary_strings(3) = ['000', '001', '010', '011', '100', '101', '110', '111']
    """
    # TODO: Implement this
    # Hint: For each position, you can place either '0' or '1'
    # Hint: Use a helper function that builds strings character by character
    pass

# Test cases:
# generate_binary_strings(2) should return ['00', '01', '10', '11']
# generate_binary_strings(1) should return ['0', '1']
```

#### Exercise 4.3: Advanced - Subset Sum Problem
**Problem:** Given a list of integers and a target sum, determine if there exists a subset that adds up to the target.

```python
def subset_sum(nums, target):
    """
    Check if any subset of nums adds up to target.
    Example: subset_sum([3, 34, 4, 12, 5, 2], 9) = True (3 + 4 + 2 = 9)
    Example: subset_sum([3, 34, 4, 12, 5, 2], 30) = False
    """
    # TODO: Implement this
    # Hint: For each number, you have two choices: include it or exclude it
    # Hint: Use index to track position in array
    pass

# Test cases:
# subset_sum([3, 34, 4, 12, 5, 2], 9) should return True
# subset_sum([1, 2, 3, 4], 10) should return True
# subset_sum([1, 2, 3], 7) should return False
```

## Part 5: Design and Analysis of Recursive Algorithms 

### Designing Recursive Algorithms

**Step-by-Step Process:**

1. **Identify the recursive structure**
   - Can the problem be broken into similar subproblems?
   - Is there a natural hierarchy or tree structure?

2. **Define the base case(s)**
   - What's the simplest input?
   - When should recursion stop?

3. **Define the recursive step**
   - How to break down the problem?
   - How to combine subproblem solutions?

4. **Verify progress toward base case**
   - Does each recursive call get closer to the base case?
   - Will it always terminate?

### Time Complexity Analysis

#### Factorial: O(n)
```python
T(n) = T(n-1) + O(1)
T(0) = O(1)
Solution: T(n) = O(n)
```

#### Fibonacci (naive): O(2^n)
```python
T(n) = T(n-1) + T(n-2) + O(1)
T(0) = T(1) = O(1)
Solution: T(n) = O(2^n)  # Exponential!
```

#### Binary Tree Traversal: O(n)
```python
T(n) = T(left) + T(right) + O(1)
# For n nodes total
Solution: T(n) = O(n)
```

### Space Complexity

Recursion uses stack space!
- **Factorial:** O(n) - maximum depth of recursion
- **Fibonacci:** O(n) - maximum stack depth
- **Tree Traversal:** O(h) where h is tree height

### When to Use Recursion

**Good for:**
- Tree/graph traversal
- Divide-and-conquer problems
- Backtracking algorithms
- Problems with recursive mathematical definitions

**Avoid when:**
- Simple iterative solution exists
- Stack space is limited
- Performance is critical (function call overhead)

### Practice Exercises 

#### Exercise 5.1: Beginner - Analyze Recursive Sum
**Problem:** Analyze the time and space complexity of this recursive function.

```python
def recursive_sum(arr, n):
    """
    Sum first n elements of array arr recursively.
    """
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Questions to answer:
# 1. Write the recurrence relation for time complexity
# 2. What is the time complexity? O(?)
# 3. What is the space complexity? O(?)
# 4. Draw the recursion tree for recursive_sum([1,2,3,4], 4)
```

**Solution Guide:**
```python
"""
Analysis of recursive_sum:

1. Recurrence Relation:
   T(n) = T(n-1) + O(1)
   T(0) = O(1)

2. Time Complexity: O(n)
   - Makes n recursive calls
   - Each call does O(1) work
   - Total: n * O(1) = O(n)

3. Space Complexity: O(n)
   - Maximum stack depth is n
   - Each frame uses O(1) space
   - Total: n * O(1) = O(n)

4. Recursion Tree:
   recursive_sum([1,2,3,4], 4)
   ├── 4 + recursive_sum([1,2,3,4], 3)
       ├── 3 + recursive_sum([1,2,3,4], 2)
           ├── 2 + recursive_sum([1,2,3,4], 1)
               ├── 1 + recursive_sum([1,2,3,4], 0)
                   └── 0 (base case)
"""
```

#### Exercise 5.2: Intermediate - Design and Analyze Binary Search
**Problem:** Implement recursive binary search and analyze its complexity.

```python
def binary_search(arr, target, left, right):
    """
    Search for target in sorted array arr[left:right+1].
    Return index if found, -1 otherwise.
    """
    # TODO: Implement recursive binary search
    # TODO: Analyze time complexity
    # TODO: Analyze space complexity
    pass

# Requirements:
# 1. Implement the function
# 2. Write the recurrence relation
# 3. Prove time complexity is O(log n)
# 4. Compare space complexity with iterative version
```

#### Exercise 5.3: Advanced - Design Optimal Recursive Algorithm
**Problem:** The "Minimum Edit Distance" problem - find minimum operations to transform string s1 into s2.

```python
def edit_distance(s1, s2):
    """
    Find minimum edit distance between s1 and s2.
    Operations allowed: insert, delete, replace
    
    Example: edit_distance("cat", "cut") = 1 (replace 'a' with 'u')
    Example: edit_distance("sunday", "saturday") = 3
    """
    # TODO: Design recursive solution
    # TODO: Identify overlapping subproblems
    # TODO: Optimize with memoization
    # TODO: Analyze time complexity (both versions)
    pass

# Tasks:
# 1. Write naive recursive solution
# 2. Identify why it's inefficient
# 3. Add memoization
# 4. Compare complexities
```
## Part 6: Theory of Recursion - The Foundation of Computation

### Recursion and Computability

**Fundamental Insight:** Recursion lies at the heart of what it means for something to be computable!

### Why Recursion Matters in Computability Theory

1. **Universal Computing Model**: Any function that can be computed by any computer can be expressed recursively
2. **Mathematical Foundation**: Provides rigorous definition of "algorithm"
3. **Theoretical Limits**: Helps identify what can and cannot be computed

### Recursive Functions - Stephen Kleene's Contribution

**Stephen Kleene (1909-1994)** formalized the notion of computability through recursive functions.

#### Primitive Recursive Functions

Built from basic functions using:

**Base Functions:**
1. **Zero function:** Z(n) = 0
2. **Successor function:** S(n) = n + 1
3. **Projection function:** P_i(x₁, ..., xₙ) = xᵢ

**Operations:**
1. **Composition:** h(x) = f(g₁(x), ..., gₙ(x))
2. **Primitive recursion:**
   - h(0, y) = f(y)
   - h(S(x), y) = g(x, h(x, y), y)

**Example - Addition as Primitive Recursive:**
```
add(0, y) = y
add(S(x), y) = S(add(x, y))
```
With these you can define addition, multiplication, exponentiation, factorial, etc.

**All primitive recursive functions are total** (always halt).

#### General Recursive Functions
To get functions that can search for something, Kleene added the **minimization operator** (μ-operator):

μy [ f(x, y) = 0 ]  = the smallest y such that f(x,y)=0 (if it exists)

This lets us define functions that may loop forever on some inputs → **partial recursive functions**.

**Ackermann Function** - Not primitive recursive!
```text
A(0, y) = y + 1
A(x+1, 0) = A(x, 1)
A(x+1, y+1) = A(x, A(x+1, y))
```

- A(4, 2) is already 2↑↑↑2↑↑↑2 in Knuth up-arrow notation — roughly 19,729 digits.  
- A(5, 2) is incomprehensibly larger.

```python
def ackermann(m, n):
    """Ackermann function - grows faster than any primitive recursive function"""
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Warning: Even ackermann(4, 2) has 19,729 digits!
```

### Church-Turing Thesis

**The Big Claim:** The class of functions computable by:
- Turing machines
- Lambda calculus (Church)
- Recursive functions (Kleene)
- Any modern programming language

...are all **exactly the same**!

The Church-Turing thesis is the foundation of theoretical computer science.

In other words: **recursion (in the mathematical sense) captures exactly what algorithms can do**.

### Recursive Enumerability

A set S is **recursively enumerable** if there exists a recursive function that:
- Lists all elements of S (possibly with repetition)
- May run forever if S is infinite

Example: The set of all valid Python programs is recursively enumerable.

Recursive vs. Recursively Enumerable Sets

- A set is **recursive** (decidable) if there is an algorithm that always says yes/no in finite time.
- A set is **recursively enumerable** if we can list all its members (but maybe never halt on non-members).

The halting problem is r.e. but not recursive → there are limits to what recursion can decide.

## Part 7: Advanced Topics - Divide & Conquer and Dynamic Programming

### Divide and Conquer

**Strategy:** Recursively break problem into smaller subproblems, solve independently, combine results.

**Classic Example - Merge Sort:**
```python
def merge_sort(arr):
    """Sort array using divide and conquer"""
    if len(arr) <= 1:  # Base case
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Divide & recurse
    right = merge_sort(arr[mid:])   # Divide & recurse
    
    # Conquer: merge sorted halves
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

Time Complexity: O(n log n)

### Dynamic Programming

**Problem:** Recursive solutions often recalculate the same subproblems.

**Solution:** Memoization - store results of subproblems!

**Fibonacci with Memoization:**
```python
def fibonacci_memo(n, memo={}):
    """Efficient Fibonacci using memoization"""
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]

# Now O(n) instead of O(2^n)!
```

**Bottom-up Dynamic Programming:**
```python
def fibonacci_dp(n):
    """Fibonacci using bottom-up DP"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```
## Summary and Key Takeaways

### What We've Learned

1. **Recursion Basics**
   - Functions calling themselves
   - Base case + recursive step
   - Stack mechanism

2. **Design Principles**
   - Break problems into subproblems
   - Ensure progress toward base case
   - Combine subproblem solutions

3. **Applications**
   - Mathematical functions (factorial, Fibonacci)
   - Tree/graph algorithms
   - Backtracking (N-Queens)
   - Divide & conquer (merge sort)

4. **Theoretical Significance**
   - Foundation of computability
   - Recursive functions = computable functions
   - Church-Turing thesis

5. **Optimization Techniques**
   - Memoization for overlapping subproblems
   - Dynamic programming as alternative

### Common Recursion Patterns

```python
# Linear Recursion (single recursive call)
def linear(n):
    if base_case:
        return base_value
    return process(n) + linear(n-1)

# Binary Recursion (two recursive calls)
def binary(n):
    if base_case:
        return base_value
    return binary(left) + binary(right)

# Tail Recursion (recursive call is last operation)
def tail_recursive(n, accumulator=0):
    if base_case:
        return accumulator
    return tail_recursive(n-1, accumulator + n)
```

### Practice Problems

1. **Easy:** Write recursive function to calculate sum of digits
2. **Medium:** Implement recursive binary search
3. **Hard:** Solve Tower of Hanoi problem
4. **Challenge:** Implement recursive sudoku solver

### Remember

> "The power of recursion evidently lies in the possibility of defining an infinite set of objects by a finite statement."
> - Niklaus Wirth

Recursion is not just a programming technique—it's a fundamental way of thinking about computation itself!

## Questions for Reflection

1. When would you choose recursion over iteration?
2. How does the call stack limit recursive solutions?
3. Can every iterative solution be written recursively? Vice versa?
4. Why is tail recursion special in some languages?
5. How does recursion relate to mathematical induction?
