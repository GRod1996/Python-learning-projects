"""
class Library:
    def __init__(self):
        self.books = {}
        pass

    def add_book(self, isbn, title, author, copies):
        if isbn in self.books:
            self.books[isbn]["copies"] = self.books[isbn]["copies"] + copies
        else:
            self.books[isbn] = {"title": title, "author": author, "copies": copies}
        pass

    def checkout(self, isbn):
        if isbn not in self.books:
            return False
        if self.books[isbn]["copies"] == 0:
            return False
        self.books[isbn]["copies"] = self.books[isbn]["copies"] - 1
        return True
        pass

    def by_author(self, author):
        titles = []
        for isbn in self.books:
            book = self.books[isbn]
            if book["author"].strip().lower() == author.strip().lower():
                titles.append(book["title"])
        titles.sort()
        return titles
        pass

    def inventory_value(self, prices):
        total = 0
        for isbn in prices:
            if isbn in self.books:
                total = total + self.books[isbn]["copies"] * prices[isbn]
        return total
        pass

    def low_stock(self, threshold):
        result = {}
        for isbn in self.books:
            if self.books[isbn]["copies"] < threshold:
                result[isbn] = self.books[isbn]["copies"]
        return result
        pass

# Test cases
lib = Library()
lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)
lib.add_book("111", "Python Basics", "Jane Doe", 1)

print(lib.checkout("222"))
print(lib.checkout("222"))
print(lib.checkout("999"))
print(lib.by_author("Jane Doe"))
print(lib.inventory_value({"111": 20.0, "333": 30.0, "999": 5.0}))
print(lib.low_stock(3))
"""
#Excercise 2
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def get_hours(self):
        return self.total_seconds // 3600

    def get_minutes(self):
        return (self.total_seconds % 3600) // 60

    def get_seconds(self):
        return self.total_seconds % 60

    def __str__(self):
        return f"{self.get_hours()}:{self.get_minutes():02}:{self.get_seconds():02}"

    def __repr__(self):
        return f"Duration({self.get_hours()}, {self.get_minutes()}, {self.get_seconds()})"

    def __len__(self):
        return self.total_seconds

    def __getitem__(self, unit):
        if unit == "hours":
            return self.get_hours()
        if unit == "minutes":
            return self.get_minutes()
        if unit == "seconds":
            return self.get_seconds()
        raise KeyError(unit)

    def __bool__(self):
        return self.total_seconds > 0

    def __add__(self, other):
        return Duration(0, 0, self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        result = self.total_seconds - other.total_seconds
        if result < 0:
            raise ValueError("Negative duration")
        return Duration(0, 0, result)

    def __mul__(self, number):
        return Duration(0, 0, self.total_seconds * number)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds


a = Duration(1, 5, 9)
b = Duration(0, 59, 51)

print(a)
print(b)
print(repr(a))

print(len(a))
print(a["minutes"])
print(bool(Duration()))

c = a + b
print(c)
print(a - b)
print(b * 2)

print(a == Duration(0, 65, 9))
print(b < a)

try:
    print(b - a)
except ValueError as e:
    print("Caught:", e)

try:
    print(a["days"])
except KeyError:
    print("Caught: bad unit")