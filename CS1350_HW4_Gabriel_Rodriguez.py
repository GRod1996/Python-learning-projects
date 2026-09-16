# Unit 3.1 (Beginner)
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for product in inventory:
    print(product)
total_items = sum(inventory.values())
print("Total items:", total_items)
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
print()

# Unit 3.1 (Intermidiate)
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

for product in sorted(prices):
    print(product)
for product, price in sorted(prices.items(), key=lambda item: item[1]):
    print(f"{product}: ${price}")
most_expensive = max(prices.items(), key=lambda item: item[1])
print("Most expensive:", most_expensive[0], "- $", most_expensive[1])
print()

# Unit 3.1 (Advanced)
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

average = sum(temps.values()) / len(temps.values())
print("Average temperature:", average)
hottest_day, coldest_day = None, None
for day, temp in temps.items():
    if hottest_day is None or temp > temps[hottest_day]:
        hottest_day = day
    if coldest_day is None or temp < temps[coldest_day]:
        coldest_day = day
print("Hottest day:", hottest_day, "-", temps[hottest_day])
print("Coldest day:", coldest_day, "-", temps[coldest_day])
above_average_count = sum(1 for temp in temps.values() if temp > average)
print("Days above average:", above_average_count)
print()

# Unit 3.2 (Beginner)
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}
print("Laptop price:", products["laptop"]["price"])
for product, details in products.items():
    print(f"{product}: {details['stock']} in stock")
print()

# Unit 3.2 (Intermidiate)
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print(country_capitals)
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}
products["tablet"] = {"price": 449, "stock": 30}
print(products)
for product in list(products.keys()):
    if products[product]["stock"] < 20:
        del products[product]
print(products)
print()

# Unit 3.2 (Advanced)
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}
for department, employees in company.items():
    for name, salary in employees.items():
        print(f"{department} - {name}: {salary}")
for department, employees in company.items():
    average_salary = sum(employees.values()) / len(employees)
    print(f"{department} average salary: {average_salary}")
highest_name, highest_salary, highest_dept = None, None, None
for department, employees in company.items():
    for name, salary in employees.items():
        if highest_salary is None or salary > highest_salary:
            highest_name, highest_salary, highest_dept = name, salary, department
print(f"Highest paid: {highest_name} ({highest_dept}) - {highest_salary}")
print()

# Unit 3.3 (Beginner)
cubes = {}
for n in range(1, 6):
    cubes[n] = n**3
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}

celsius_temps = {}
for day, temp in temps.items():
    celsius_temps[day] = (temp - 32) * 5/9
for day, temp in celsius_temps.items():
    print(f"{day}: {temp:.2f}")
print()

# Unit 3.3 (Intermidiate)
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)

def to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
print(letter_grades)

student_ids = {"Alice": 101, "Bob": 102}
id_to_name = {student_id: name for name, student_id in student_ids.items()}
print(id_to_name)
print()

# Unit 3.3 (Advanced)
sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

sales_by_region = {}
for region, person, amount in sales:
    sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(sales_by_region)

sales_by_person = {}
for region, person, amount in sales:
    sales_by_person[person] = sales_by_person.get(person, 0) + amount
print(sales_by_person)

sales_by_region_person = {}
for region, person, amount in sales:
    if region not in sales_by_region_person:
        sales_by_region_person[region] = {}
    sales_by_region_person[region][person] = sales_by_region_person[region].get(person, 0) + amount
print(sales_by_region_person)
print()

# Set (Beginner)
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)
print("Number of elements:", len(unique_numbers))
# Number 3 creates an empty dictionary and not an empty set, in order to create a empty set you have to use the command "set()".
print()

# Set (Intermidiate)
text = "mississippi"
unique_chars = set(text)
print(unique_chars)
print("Number of unique letters:", len(unique_chars))

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]

unique_emails = list(set(emails))
print(unique_emails)
print()
# Number 3 needs to be immutable like a tuple in order to be hashable.

# Set (Advanced)
import timeit

# 1. Compare time to check membership in a set vs a list
numbers_list = list(range(1_000_000))
numbers_set = set(range(1_000_000))

list_time = timeit.timeit(lambda: 999999 in numbers_list, number=1000)
set_time = timeit.timeit(lambda: 999999 in numbers_set, number=1000)

print(f"List lookup time: {list_time:.6f} seconds")
print(f"Set lookup time: {set_time:.6f} seconds")
print()

# 2. Create a frozenset and use it as a dictionary key
group_a = frozenset([1, 2, 3])
group_b = frozenset([4, 5, 6])

group_totals = {
    group_a: 100,
    group_b: 250
}
print(group_totals[group_a])
print(group_totals[frozenset([1, 2, 3])])
print()

# 3. Extract unique nodes from a list of edges
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
nodes = {node for edge in edges for node in edge}
print(nodes)  # {1, 2, 3, 4}
nodes = set()
for edge in edges:
    for node in edge:
        nodes.add(node)