"""
🔹 Generator, Iterable, and Iterator in Python
These concepts are key to lazy evaluation and efficient memory usage in Python.
"""
"""
What is an Iterable?
An iterable is any object that can be looped over (e.g., lists, tuples, strings).

🔹 An iterable must have __iter__() method.
🔹 Calling iter(iterable) returns an iterator.
"""

# if __name__ =='__main__':
#     numbers = [1, 2, 3]  # List (iterable)
#     for num in numbers:
#         print(num)  # Loops through elements

"""
3️⃣ What is an Iterator?
An iterator is an object that produces values one at a time using next().
It does not store all values in memory.

# ✅ Has __iter__() and __next__() methods.
# """
# if __name__ == "__main__":
#     # Example: Creating an Iterator from an Iterable
#     numbers = [1,2,3]
#     it = iter(numbers) # Get iterator
#     print(next(it))# 1
#     print(next(it)) # 2
#     print(next(it))  # 3
#     print(next(it))  # Raises StopIteration (End of elements)

"""
What is a Generator?
A generator is a special type of iterator created using a function with yield.

Unlike normal functions, generators do not return values immediately.
They pause execution at yield and resume when next() is called.

✅ Memory Efficient: Doesn’t store all values at once.
✅ Lazy Evaluation: Computes values only when needed.

"""
if __name__ == "__main__":
    def my_generator():
        yield 1
        yield 2
        yield 3


    gen = my_generator()  # Create generator

    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    # print(next(gen))  # Raises StopIteration


