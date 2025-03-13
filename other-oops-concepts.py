"""
2️⃣ Abstract Base Classes (ABC) vs Duck Typing
🔹 ABC (Strict Interface Enforcement)
Abstract Base Classes enforce method implementation in derived classes.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Must be implemented by subclasses


class Dog(Animal):
    def make_sound(self):
        return "Bark!"


dog = Dog()
print(dog.make_sound())  # ✅ Output: Bark!

"""
🔹 Duck Typing (Flexible, No Enforcement)
"If it looks like a duck and quacks like a duck, it must be a duck."
"""
class Dog:
    def make_sound(self):
        return "Bark!"

class Cat:
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    return animal.make_sound()  # ✅ No strict type check

print(animal_sound(Dog()))  # ✅ Bark!
print(animal_sound(Cat()))  # ✅ Meow!

"""
3️⃣ Metaclasses & Custom Class Creation (type)
Metaclasses control how classes themselves are created.
"""
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: "Hello from metaclass!"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())  # ✅ Output: Hello from metaclass!


# 4️⃣ Property Decorators (@property, @setter, @deleter)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name

    @name.deleter
    def name(self):  # Deleter
        del self._name

p = Person("Alice")
p.name = "Bob"
print(p.name)  # ✅ Bob

# 5️⃣ Operator Overloading (__add__, __eq__, __hash__)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):  # Overloading +
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):  # Overloading ==
        return self.x == other.x and self.y == other.y

p1, p2 = Point(2, 3), Point(4, 5)
print((p1 + p2).__dict__)  # ✅ {'x': 6, 'y': 8}

# 6️⃣ Method Resolution Order (MRO) & super()
# MRO defines the order in which methods are inherited.
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B" + super().show()

class C(A):
    def show(self):
        return "C" + super().show()

class D(B, C):
    pass

print(D().show())  # ✅ Output: BCA (Method Resolution Order)
print(D.mro())  # ✅ [D, B, C, A, object]

"""
 SOLID Principles ensure maintainability & scalability.
✔ Abstract Base Classes enforce structure, while Duck Typing keeps things flexible.
✔ Metaclasses define class creation rules dynamically.
✔ Property Decorators manage attribute access in an elegant way.
✔ Operator Overloading customizes object behavior with arithmetic operators.
✔ MRO determines inheritance order and super() ensures correct method calls.
"""

"""
Yes, two objects can be added if the class defines the __add__ method (operator overloading).
"""