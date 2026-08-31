import sys

# Unit 1.1 (Begginer)
my_info = {"name": "Gabriel Rodriguez", "age": 30, "major": "Cybersecurity"}
for value in my_info.values():
    print(value)

# Unit 1.1 (Intermidiate)
menu = {"chicken fingers": 7.99, "fries": 2.99, "wings": 16.99, "soup": 4.99}
user_input = (
    input(
        "\nWhat would you like for the menu? Please select one item at a time. We have chicken fingers, fries, wings, and soup. \n"
    )
    .strip()
    .lower()
)
if user_input not in menu:
    print("\nPlease choose a valid selection.")
else:
    print(f"\nThe {user_input}'s price is ${menu[user_input]}")

# Exsecise number 2
course_credits = {"CS1350": 3, "CS1500": 4, "CYS1200": 3, "MATH1100": 3}
print(course_credits["CS1500"])

# Unit 1.1 (Advanced)
weekly_temps = dict(
    Monday=72, Tuesday=75, Wednesday=68, Thursday=70, Friday=74, Saturday=78, Sunday=76
)
print(weekly_temps["Wednesday"])

# Unit 1.2 (Beginner)
pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"], pet["age"])
print(pet.get("color", "unknown"))  # Unit 1.2 (Intermidiate)

# Exsercise 2
grades = {"CS1350": 85, "MATH1030": 72, "CYS2100": 58}
grade = grades.get("CYS2100", 0)
if grade >= 60:
    print("PASSED")
else:
    print("FAILED")

# Unit 1.2 (Advanced)
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}
product_name = input("\nEnter a product name: \n").strip().lower()
price = products.get(product_name)
if price is not None:
    print(f"The price is ${price}")
else:
    print("Product not available")

# Unit 1.3 (Beginner)
inventory = {}
inventory["sedan"] = 15
inventory["suv"] = 10
inventory["truck"] = 7
print("These are the vehicles available at the moment: ", inventory)

# Unit 1.3 (Advanced)
scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
print(scores.pop("Team A"))
print(scores)

# Unit 2.1 (Beginner)
"Student_name"  # valid (strings are immutable therefore are hashable)
[1, 2, 3]  # invalid (lists are mutable therefore not hashable)
100  # valid (intergers are immutable therefore hashable)
("x", "y")  # valid (tuples containing immutable values are hashable)
{"a": 1}  # invalid (dictionaries are mutable therefore not hashable)
frozenset({1, 2})  # valid (frozensets are immutable therefore hashable)

# Unit 2.1 (Intermediate)
locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

# Exsercise 2 (It will only print the last value for the key)
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))

# Exsercise 3 (It gave me a hash value for my name, however, the number stayed the same)
print("===Hash Values===")
print(f"hash('Gabriel') = {hash('Gabriel')}")
print(f"hash(100) = {hash(100)}")

# Unit 2.1 (Advanced)
high_scores = {
    ("Gabriel", "Batman"): 4978,
    ("Keishla", "Animal Crossing"): 3750,
    ("Oto", "Minecraft"): 1000,
}
print(high_scores[("Gabriel", "Batman")])

# Exsercise 2
import time

my_list = list(range(100000))
my_dictionary = {x: x for x in range(100000)}
target = 99999
# List time
start = time.perf_counter()
target in my_list
list_time = time.perf_counter() - start
# Dict time
start = time.perf_counter()
target in my_dictionary
dictionary_time = time.perf_counter() - start
print("List time:", list_time)
print("Dictionary time:", dictionary_time)

# Compare
if list_time < dictionary_time:
    difference = list_time / dictionary_time
    print("The list was faster.")
    print("It was", difference, "times faster.")
else:
    difference = dictionary_time / list_time
    print("The dictionary was faster.")
    print("It was", difference, "times faster.")

# Unit 2.2 (Beginner)
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(f"Days: {temps.keys()}")
print(f"Temperatures: {temps.values()}")
print(f"Number of Days: {(len(temps))}")

# Unit 2.2 (Intermidiate)
print("Highest temp:", max(temps.values()))
print("Lowest temp:", min(temps.values()))
if "Friday" in temps:
    print("Friday is in the directory.")
else:
    print("Friday is not in the directory.")
temps.setdefault("Thursday", 70)
days = temps.keys()
print("Before:", days)
temps["Friday"] = 73
print("After:", days)

# Unit 2.2 (Advanced) ***
prices = {"laptop": 999, "phone": 699, "tablet": 499, "watch": 299}
total_value = sum(prices.values())
average = total_value / len(prices)
print("This is the total value: $", total_value)
print("This is the average: $", average)
most_expensive = max(prices, key=prices.get)
least_expensive = min(prices, key=prices.get)
print("The most expensive item:", most_expensive, "$", prices[most_expensive])
print("The least expensive item:", least_expensive, "$", prices[least_expensive])
keys_view = prices.keys()
keys_list = list(prices.keys())
print("Memory used by keys:", sys.getsizeof(keys_view), "bytes")
print("Memory used by list:", sys.getsizeof(keys_list), "bytes")
prices.update({"headphones": 199, "keyboard": 89, "mouse": 49})
print("All products:")
for product, price in prices.items():
    print(product, "$", price)

# Unit 2.3 (Beginner)
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for color in colors.items():
    print(f"The {color[0]} is {color[1]}")
# list(colors.items()) will print each pair as a tuple inside a list. [('apple','red'), ('banana', 'yellow'), ('grape','purple')]

# Unit 2.3 (Intermidiate)
drink_price = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for item, price in drink_price.items():
    drink_price[item] = price * 1.10
    print(f"The price for {item}: is ${price:.2f}")
counter = 0
for item, price in drink_price.items():
    if price > 4:
        counter = counter + 1
print(counter)

x = 10
y = 20
x, y = y, x
print(x, y)

list = [1, 2, 3, 4, 5]
first, *middle, last = list
print(f"first={first}, middle={middle}, last={last}")

# Unit 2.3 (Advanced)
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
name, score = max(scores.items(), key=lambda highscore: highscore[1])
print(f"{name} has scored the highest with {score}")
