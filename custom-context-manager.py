"""
Context Manager in Python (With Statement)
A context manger in python is an object that manages resources
automatically. ensuring proper setup and cleanup.

🔹 Why Use Context Managers?
✅ Ensures cleanup (e.g., closing files, releasing locks)
✅ Prevents resource leaks
✅ Improves readability
"""
"""
1️⃣ Example: Context Manager for Files (with open())
"""
# Without a context manager, we must manually close the file:
file = open("data.txt", "w")
file.write("Hello, World!")
file.close()  # Must close manually

# With a context manager (with statement):
with open("data.txt", "w") as file:
    file.write("Hello, World!")  # File closes automatically after the block

"""
2️⃣ Creating a Custom Context Manager (__enter__() & __exit__())
"""


class CustomContext:
    def __enter__(self):
        print("Entering Context")
        return self  # Returns an object inside `with` block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Existing Context")


# if __name__ == "__main__":
#     # Using the custom context manager
#     with CustomContext(): #✅ Automatically runs __enter__() and __exit__().
#         print("Inside Context")

"""
3️⃣ Using contextlib for Simpler Context Managers
Instead of a class, you can use the contextlib.contextmanager decorator:
"""
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Entering Context")
    yield  # Code inside `with` runs here
    print("Existing Context")


if __name__ == "__main__":
    with my_context():
        print("Inside Context")

"""
🚀 Summary
Context managers ensure proper resource management.
with statement handles setup and cleanup automatically.
Custom context managers can be created using __enter__() and __exit__().
Use contextlib.contextmanager for simpler context management.
"""
