"""
🔹 Dunder (Magic) Methods in Python
Dunder (double underscore) methods, also called magic methods,
are special methods with double underscores (__) before and after their names.
They allow built-in behavior customization for classes, such as object representation, arithmetic operations, and iteration.

1️⃣ Basic Dunder Methods
Dunder Method	Purpose
__init__	Constructor (initializes objects)
__str__	User-friendly string representation (str(obj))
__repr__	Debugging string representation (repr(obj))
__len__	Defines behavior for len(obj)
__getitem__	Enables indexing (obj[key])
__setitem__	Enables setting values (obj[key] = value)
__delitem__	Enables deletion (del obj[key])
__call__	Makes an instance callable (obj())

"""


# 2️⃣ Constructor & String Representations
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def __str__(self):  # User-friendly representation
        return f"Person: {self.name}, Age: {self.age}"

    def __repr__(self):  # Debugging representation
        return f"Person('{self.name}', {self.age})"


p = Person("Alice", 30)
print(str(p))  # ✅ "Person: Alice, Age: 30"
print(repr(p))  # ✅ "Person('Alice', 30)"


# 3️⃣ Arithmetic Operators (+, -, *, /)

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):  # Overloads `+`
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # Overloads `-`
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1, v2 = Vector(3, 4), Vector(1, 2)
print(v1 + v2)  # ✅ Vector(4, 6)
print(v1 - v2)  # ✅ Vector(2, 2)

#4️⃣ Comparison Methods (==, !=, <, >, etc.)

class Car:
    def __init__(self, speed):
        self.speed = speed

    def __eq__(self, other):  # Overloads `==`
        return self.speed == other.speed

    def __lt__(self, other):  # Overloads `<`
        return self.speed < other.speed

car1, car2 = Car(100), Car(120)
print(car1 == car2)  # ✅ False
print(car1 < car2)   # ✅ True

# Length & Indexing(len(), obj[index])
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):  # Overloads `len(obj)`
        return len(self.members)

    def __getitem__(self, index):  # Enables indexing
        return self.members[index]

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))     # ✅ 3
print(team[1])       # ✅ "Bob"

# 6️⃣ Callable Objects (obj())
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):  # Makes object callable
        return value * self.factor

double = Multiplier(2)
print(double(10))  # ✅ 20

# 7️⃣ Context Managers (with Statement)

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):  # Setup
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):  # Cleanup
        self.file.close()

with FileManager("test.txt") as file:
    file.write("Hello, World!")

