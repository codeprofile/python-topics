"""
__slots__: Memory Optimization in python objects
By default, Python stores object attributes in a dictionary(__dict__)
which makes attribute access flexible but memory-intensive.
Using __Slots__ removes the need for __dict__, making object instances more memory-efficient.
"""


# 🔹 Example Without __slots__ (Normal Class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# if __name__ == "__main__":
#     p = Person("Laxmi",28)
#     print(p.__dict__)
# 📌 Downside: Each instance stores attributes in a dictionary, which takes extra memory.

# 🔹 Optimizing with __slots__
class Person1:
    __slots__ = ("name", "age")  # Restricts attributes to only these names

    def __init__(self, name, age):
        self.name = name
        self.age = age


# if __name__ == "__main__":
#     p = Person1("Laxmi", 28)
#     # print(p.__dict__)  # ❌ AttributeError: 'Person' object has no attribute '__dict__'
#     """
#     ✅ Benefits of __slots__:
#     🚀 Reduces memory usage (No __dict__)
#     🔐 Prevents adding new attributes dynamically (p.address = "NYC" → ❌ AttributeError)
#     """

"""
2️⃣ dataclass: Simplifying Class Creation
A dataclass automatically generates methods like __init__(), __repr__(), and __eq__() for you, reducing boilerplate code.
"""


# 🔹 Example Without dataclass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# if __name__ == "__main__":
#     p = Person("Alice", 25)
#     print(p)  # Person(name=Alice, age=25)
#     # Downside: Manually writing __init__() and __repr__().

# 🔹 Simplifying with dataclass

from dataclasses import dataclass

# You can combine both for performance & memory optimization.
@dataclass(slots=True)
class Person:
    name: str
    age: int

if __name__ == "__main__":
    p = Person("Alice", 25)
    print(p)  # ✅ Person(name='Alice', age=25)
    """
    ✅ Benefits of dataclass:

🚀 Automatically generates __init__(), __repr__(), __eq__()
📝 Supports default values & type hints
    """
    """
    ✅ Best of both worlds:

    Memory-efficient (__slots__)
    Auto-generated methods (dataclass)
    """

"""
 "A dataclass in Python is a decorator (@dataclass)
  that automatically generates boilerplate methods like __init__(), __repr__(), and __eq__() for classes. 
  It makes defining simple data-holding classes easier and more readable."
"""