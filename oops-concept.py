"""
Python follows an Object-Oriented Programming (OOP) paradigm,
which helps organize code into reusable objects and follows principles like Encapsulation, Inheritance, and Polymorphism.
"""
# Encapsulation , Abstarction , Inheritance,Polymorphism

# 2️⃣ Encapsulation (Data Hiding)
"""
Encapsulation restricts direct access to data 
by using private (__) and protected (_) attributes.
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):  # Public method to access private attribute
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✅ Output: 1500
print(account.__balance)  # ❌ Error! Attribute is private

#3️⃣ Inheritance (Code Reusability)
"""
Inheritance allows a child class to inherit properties and methods from a parent class.
"""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):  # 🚗 Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Calls the parent class constructor
        self.model = model

    def show_info(self):
        return f"{self.show_brand()}, Model: {self.model}"

car = Car("Toyota", "Corolla")
print(car.show_info())  # ✅ Output: Brand: Toyota, Model: Corolla

"""
🔹 Types of Inheritance:

Single Inheritance – One parent, one child class.
Multiple Inheritance – A child inherits from multiple parent classes.
Multilevel Inheritance – A child class inherits from another child class.
Hierarchical Inheritance – Multiple child classes inherit from a single parent.
"""

# 4️⃣ Polymorphism (Same Interface, Different Implementation)
# Polymorphism allows different classes to use the same method name but with different behaviors.

class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # ✅ Bark! Meow!

# ✅ Method Overriding (Polymorphism with Inheritance)

class Parent:
    def show(self):
        return "Parent method"

class Child(Parent):
    def show(self):  # Overriding parent method
        return "Child method"

obj = Child()
print(obj.show())  # ✅ Output: Child method

# 5️⃣ Abstraction (Hiding Implementation Details)
"""abstraction allows defining abstract methods in a base class that must be implemented in derived classes."""
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def sound(self):
        pass  # Must be implemented by subclasses


class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
print(dog.sound())  # ✅ Output: Woof!

"""
6️⃣ Special (Dunder) Methods in OOP
Python has special methods (dunder methods) to customize object behavior.
"""
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):  # String representation
        return f"{self.title} - ${self.price}"

    def __add__(self, other):  # Overloading `+` operator
        return self.price + other.price

b1 = Book("Python 101", 50)
b2 = Book("Advanced Python", 70)
print(b1)  # ✅ Python 101 - $50
print(b1 + b2)  # ✅ 120

# 7️⃣ Class vs. Static Methods
# Instance Method (self) – Works on object instance.
class Person:
    def greet(self):  # Instance method
        return "Hello!"

# Class Method (@classmethod) – Works on class level.
class Employee:
    count = 0  # Class attribute

    @classmethod
    def increment(cls):
        cls.count += 1

Employee.increment()
print(Employee.count)  # ✅ 1

# Static Method (@staticmethod) – No self or cls, independent utility method.
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 5))  # ✅ 8


"""
 Encapsulation – Restricts access to class members using private/protected attributes.
✔ Inheritance – Child classes inherit methods and attributes from parent classes.
✔ Polymorphism – Different classes use the same method name with different implementations.
✔ Abstraction – Defines abstract methods that subclasses must implement.
✔ Dunder Methods – Special methods for customizing behavior (__str__, __add__, etc.).
✔ Class & Static Methods – Work with class-level attributes and utility methods.
"""

