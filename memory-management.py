"""
 Python Memory Management
 python has an automatic memory management system that handles
 memory allocation and deallocation for objects. It includes
 1. Reference Counting
 2. Garbage Collection(GC)
 3. Memory pools & Allocators

"""
"""
1️⃣ Reference Counting (sys.getrefcount())
Python uses reference counting to track the number of references to an object.

When ref count = 0, Python frees the memory.
# """
# if __name__ == "__main__":
#     import sys
#     x =[1,2,3] # Create a list
#     print(sys.getrefcount(x))  # Count references (typically 2: one for `x` and one for `getrefcount` argument)

"""
2️⃣ Garbage Collection (gc Module)
Python automatically deletes unused objects using a garbage collector (GC).

🔹 Why is Garbage Collection Needed?
Reference counting alone fails in cyclic references (e.g., self-referencing objects).
GC detects unreachable cycles and removes them.
🔹 Example: Forcing Garbage Collection
"""
# if __name__ == "__main__":
#     import gc
#     gc.collect()  # Manually trigger garbage collection

"""
3️⃣ Memory Pools & Object Allocators
🔹 Small Object Optimization (pymalloc)
Python pre-allocates memory for frequently used objects (int, float, list, etc.).
Reduces overhead for small objects.
"""

# id() Function (Memory Address of an Object)

x = 10
print(id(x))  # Memory address of `x`

"""
4️⃣ Memory Optimization Tips
Tip	Why?
Use generators (yield) instead of lists : 	Saves memory by avoiding large in-memory lists
Use del to remove unused objects	: Helps free memory sooner
Use gc.collect() carefully	: Only for force cleanup (rarely needed)
Avoid creating large objects unnecessarily	: Helps reduce memory usage

"""
"""
🚀 Summary
🔹 Python automatically manages memory (Reference Counting + GC).
🔹 Garbage Collector removes cyclic references.
🔹 Optimized memory pools (pymalloc) speed up object creation.
🔹 Use yield, del, and efficient data structures for memory-efficient code.
"""