"""
A decorator in Python is a function
that modifies another function or class without changing its actual code. It allows for code reusability and cleaner syntax.
"""

# #  Decorator with Arguments
#
# if __name__ == "__main__":
#     def repeat(n):
#         def decorator(func):
#             def wrapper(*args, **kwargs):
#                 for _ in range(n):
#                     func(*args, **kwargs)
#
#             return wrapper
#
#         return decorator
#
#     @repeat(3)  # 👈 Runs `say_hi()` 3 times
#     def say_hi():
#         print("Hi!")
#
#     say_hi()

"""
3️⃣ Using functools.wraps (Preserving Metadata)
By default, decorators override function metadata (__name__, __doc__). Use functools.wraps to preserve them.
"""

# if __name__ == "__main__":
#     from functools import wraps
#
#
#     def my_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("Running decorated function")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#
#     @my_decorator
#     def greet():
#         """Returns a greeting message."""
#         return "Hello!"
#
#
#     print(greet.__name__)  # ✅ Outputs 'greet' instead of 'wrapper'
#     print(greet.__doc__)  # ✅ Preserves docstring

# ✅ Logging Function Calls
#
# if __name__ == "__main__":
#     def log_calls(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#
#     @log_calls
#     def add(a, b):
#         return a + b
#
#
#     print(add(3, 4))

"""
5️⃣ Class Decorators
Decorators can also be used on classes.
"""
def add_greeting(cls):
    cls.greet = lambda self: f"Hello from {self.__class__.__name__}!"
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())  # ✅ Output: Hello from Person!

"""
🚀 Summary
✔ Decorators modify functions/classes without changing their definition.
✔ Use @decorator_name instead of manually wrapping a function.
✔ Use functools.wraps to preserve function metadata.
✔ Great for logging, access control, memoization, and profiling.
"""