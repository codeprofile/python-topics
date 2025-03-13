"""
🔹 Exceptions in Python
Exceptions in Python occur when an error disrupts the normal flow of a program. You can handle exceptions using try-except, finally, and raise
"""

class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print(e)
