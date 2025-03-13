"""
🔹 Creating a Custom Iterable and Iterator in Python
Yes! You can create a custom iterable and iterator
 by implementing the __iter__() and __next__() methods
 in a class.

 1️⃣ Creating a Custom Iterable
An iterable class must implement __iter__(), which returns an iterator.
An iterator class must implement __next__(), which returns the next value.
"""

# if __name__ == "__main__":
#     class RangeIterator:
#         def __init__(self, max_value):
#             self.current = 1  # Start from 1
#             self.max = max_value
#
#         def __iter__(self):
#             return self  # An iterator must return itself
#
#         def __next__(self):
#             if self.current > self.max:
#                 raise StopIteration  # Stop when max is reached
#             val = self.current
#             self.current += 1  # Increment counter
#             return val  # Return the next value
#
#
#     class CustomRange:
#         def __init__(self, max_value):
#             self.max = max_value
#
#         def __iter__(self):
#             return RangeIterator(self.max) # Return an iterator instance
#
#
#     # ✅ Using the custom iterable
#     my_range = CustomRange(5)  # Create an iterable object
#
#     for num in my_range:
#         print(num)  # Output: 1, 2, 3, 4, 5

"""
2️⃣ Creating an Iterable Without a Separate Iterator Class
Instead of creating two separate classes, you can make the same class both iterable and an iterator.

Example: Implementing Both __iter__() & __next__() in One Class
"""
# class MyRange:
#     def __init__(self, max_value):
#         self.current = 1
#         self.max = max_value
#
#     def __iter__(self):
#         return self  # The same class is both an iterable and an iterator
#
#     def __next__(self):
#         if self.current > self.max:
#             raise StopIteration  # Stop iteration
#         val = self.current
#         self.current += 1
#         return val
#
#
# # ✅ Using the custom iterable
# for num in MyRange(5):
#     print(num)  # Output: 1, 2, 3, 4, 5

"""
3️⃣ Making It More Pythonic with a Generator
Instead of manually implementing __iter__() and __next__(), a generator does it automatically.

Example: Generator-Based Iterable
"""
if __name__ == "__main__":
    class MyRange:
        def __init__(self,max_value):
            self.max = max_value

        def __iter__(self):
            for num in range(1, self.max + 1):
                yield num  # Yield instead of `__next__()`


    # ✅ Using the generator-based iterable
    for num in MyRange(5):
        print(num)  # Output: 1, 2, 3, 4, 5

"""
🚀 Summary
Approach	Description	Best Use Case
Custom Iterator Class	Separate __iter__() & __next__() classes	Fine control over iteration logic
Single-Class Iterator	Implements both __iter__() & __next__()	When modification of the object is okay
Generator (yield)	Uses yield in __iter__()	When simplicity & performance matter
"""


