"""
1️⃣ Lists, Tuples, Sets, Dicts – When to Use What?
Data Structure	Ordered?	Mutable?	Duplicates?	Lookup Time	Best Use Case
List ([])	✅ Yes	✅ Yes	✅ Yes	O(n) (search)	When order matters & elements need modification
Tuple (())	✅ Yes	❌ No	✅ Yes	O(n) (search)	Read-only collections (safer & faster than lists)
Set ({})	❌ No	✅ Yes	❌ No	O(1) (lookup)	Fast lookups & removing duplicates
Dict ({key: value})	❌ No	✅ Yes	❌ No (keys)	O(1) (lookup)	Key-value mapping with fast access
✔ Use lists for sequential storage, tuples for immutable data, sets for uniqueness, and dicts for key-value mapping.
"""
# 🔹 Using sorted() (Timsort – O(n log n))

# 🔹 Sorting with a Custom Comparator (functools.cmp_to_key)
from functools import cmp_to_key

def custom_sort(a, b):
    return a - b  # Ascending order

arr = [5, 2, 8, 1]
sorted_arr = sorted(arr, key=cmp_to_key(custom_sort))

#  Sorting with Heaps (heapq)
# ✔ Heap sort keeps the smallest element at the top (min-heap).

import heapq

arr = [5, 2, 8, 1]
heapq.heapify(arr)  # ✅ Converts list into a heap
smallest = heapq.heappop(arr)  # ✅ Removes the smallest element (1)

#  Use sorted() for general sorting, heapq for priority-based retrieval.

# 🔹 Binary Search (bisect module) – O(log n)
import bisect

arr = [1, 3, 4, 7, 9]
index = bisect.bisect_left(arr, 4)  # ✅ Finds position of 4
# Use bisect when working with sorted lists to speed up searches.

