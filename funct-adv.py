#  Use Case: Sorting a List of Tuples
students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
students.sort(key=lambda x: x[1])  # Sort by age
print(students)  # ✅ [('Bob', 22), ('Charlie', 23), ('Alice', 25)]
"""
2️⃣ map(), filter(), and reduce()
🔹 map(function, iterable)
Applies a function to each element in an iterable.
"""
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # ✅ [1, 4, 9, 16]

"""
🔹 filter(function, iterable)
Filters elements based on a condition.
"""
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # ✅ [2, 4, 6]

"""
🔹 reduce(function, iterable)
Performs cumulative computations.
"""
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # ✅ 24 (1*2*3*4)

"""
3️⃣ Closures & Function Factories
A closure is a function that remembers variables from its enclosing scope even when executed outside that scope.
"""
def multiplier(n):
    def inner(x):
        return x * n
    return inner  # ✅ Returns a function

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # ✅ 10
print(triple(5))  # ✅ 15
# 🔹 Class-Based Decorators

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

@Decorator
def say_hello():
    print("Hello!")

say_hello()

# 5️⃣ Higher-Order Functions
# A higher-order function is a function that takes another function as an argument or returns a function.



def apply_function(func, value):
    return func(value)
#
# if __name__ == "__main__":
#     result = apply_function(lambda x: x**2, 5)
#     print(result)  # ✅ 25

#6️⃣ Memoization (functools.lru_cache)
#lru_cache caches function results to avoid redundant calculations.

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

# 5️⃣ String Interning (sys.intern())
# Python reuses immutable strings to save memory (interning).
import sys

s1 = sys.intern("hello_world")
s2 = sys.intern("hello_world")

print(s1 is s2)  # ✅ True (Same Memory Location)

# ✔ Shallow Copy (copy.copy()) – Creates a new object but references original elements.
# ✔ Deep Copy (copy.deepcopy()) – Recursively copies all objects.