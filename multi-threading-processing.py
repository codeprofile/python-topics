# Latest Stable Python version is 3.13.2
# 3.14 is in beta version (still under development)

# Enhancement in 3.13
"""
Free-Threaded Build Mode : This mode allows python to operate
without the Global Interpreter Lock (GIL), enabling improved concurrency
in multi-threaded applications


Free-Threaded Build Mode in python 3.13 refers to an experimental mode
where Python runs without the Global Interpreter Lock (GIL). This allows
true multi-threading, meaning multiple threads can execute python
code simultaneously without being blocked by the GIL

What is the GIL ?
The Global Interpreter Lock (GIL) is a mechanim in CPython that
restricts execution to one thread at a time , even on multi-core processors.
This limits python's ability to utilize multiple CPU cores effectively for parallael
execution

"""
import threading
import time


# Define a function that simulates a CPU-bound task
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


# Run with multiple threads

def run_threads(num_threads=4, iterations=10_000_000):
    threads = []

    start_time = time.time()

    for _ in range(num_threads):
        t = threading.Thread(target=cpu_task, args=(iterations,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(f"Execution Time: {time.time() - start_time:.2f} seconds")


# Run the test
# if __name__ == "__main__":
#     print("Testing Multi-Threading Performance")
#     run_threads()

"""
Expected behavior:

On a standard Python build (with GIL) → Threads will run one after another.
On free-threaded Python (without GIL) → Threads should run simultaneously, utilizing multiple cores effectively.
"""
import multiprocessing
import time


def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def run_processes(num_processes=4, iterations=10_000_000):
    processes = []
    start_time = time.time()

    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_task, args=(iterations,))
        p.start()  # it runs independently of the main program.
        processes.append(p)

    for p in processes:
        # blocks the main program until the thread finishes execution.
        p.join()  # is a method used in Python threading to ensure that the main program waits for a thread to complete before moving forward.

    print(f"Execution Time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    print("Testing Multiprocessing Performance")
    run_processes()

"""
1️⃣ Multitasking
🔹 Definition:
Multitasking refers to running multiple tasks (processes or threads) simultaneously. It can be achieved using:

Process-based multitasking (multiple programs running at the same time)
Thread-based multitasking (multiple threads within a program)
🔹 Example:
Process-Based Multitasking → Running a web browser, music player, and file download at the same time.
Thread-Based Multitasking → A browser loading multiple tabs at once.


2️⃣ Multithreading
🔹 Definition:
Multithreading is a type of multitasking where multiple threads run within the same process, sharing memory.

🔹 Key Features:
✅ Threads share the same memory space (faster communication than processes).
✅ Good for I/O-bound tasks (e.g., file reading, network requests).
❌ Limited by the Global Interpreter Lock (GIL) in standard Python, so it does not improve CPU-bound tasks.
"""

"""
4️⃣ Multiprocessing (Better for CPU Tasks)
If you need true parallel execution, use multiprocessing instead of threading.
🔹 Unlike threads, processes run in separate memory spaces, so they can fully utilize multiple CPU cores.
5️⃣ When to Use What?
Task Type	Use Multithreading	Use Multiprocessing
I/O-bound tasks (file reading, web scraping, network requests)	✅ Yes	❌ No
CPU-bound tasks (image processing, ML training, number crunching)	❌ No (GIL issue)	✅ Yes
Need shared memory?	✅ Yes	❌ No
Need true parallel execution?	❌ No (GIL limits it)	✅ Yes

Multitasking = Running multiple tasks (processes or threads).
Multithreading = Running multiple threads within a single process (good for I/O-bound tasks).
Multiprocessing = Running multiple processes (good for CPU-bound tasks, bypasses the GIL).
"""
"""

concurrent Library in Python
The concurrent library in Python provides high-level tools for managing parallel and concurrent execution using threads and processes. It has two key modules:

concurrent.futures – A simpler and more efficient way to manage threads and processes.
concurrent.queue – A thread-safe queue for managing shared data between threads.
"""

"""
1️⃣ concurrent.futures (High-Level Threading & Multiprocessing)
This module provides two key classes:

ThreadPoolExecutor – Runs functions asynchronously using threads.
ProcessPoolExecutor – Runs functions asynchronously using separate processes.
"""
"""
🔹 Using ThreadPoolExecutor (For I/O-bound tasks)
ThreadPoolExecutor is useful when tasks involve waiting (e.g., web scraping, API requests, file reading).
"""

import concurrent.futures
import time


def task(n):
    print(f"Task {n} starting...")
    time.sleep(2)
    print(f"Task {n} completed!")
    return n * 2


# Create a thread pool with 3 workers
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))  # Run tasks concurrently

# if __name__ == "__main__":
#     print(list(results))  # Output: [0, 2, 4, 6, 8]

"""
🔹 Using ProcessPoolExecutor (For CPU-bound tasks)
For heavy computations, ProcessPoolExecutor uses multiple processes to fully utilize CPU cores.
"""
"""
2️⃣ queue.Queue (Thread-Safe Queues)
The queue.Queue module is useful when multiple threads need to share data safely.
"""

import queue
import threading
import time

# Create a shared queue
q = queue.Queue()


def producer():
    for i in range(5):
        time.sleep(1)
        q.put(i)
        print(f"Produced: {i}")


def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed: {item}")
        time.sleep(1)


# Start producer and consumer threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t1.join()  # Ensure producer finishes before consumer starts

t2.start()
t2.join()

"""
🚀 When to Use What?
Use Case	Best Choice
Web scraping, file I/O, API calls	ThreadPoolExecutor
Image processing, machine learning, heavy computations	ProcessPoolExecutor
Thread-safe data sharing	queue.Queue
"""

"""
🔹 Global Interpreter Lock (GIL) in Python
The Global Interpreter Lock (GIL) is a mutex (lock) in CPython that allows only one thread to execute Python bytecode at a time, even in multi-threaded programs.

🔹 Why Does Python Have a GIL?
Python uses automatic memory management with a garbage collector (reference counting).
To prevent race conditions when multiple threads modify memory, CPython locks execution to one thread at a time
"""

"""
1️⃣ Impact of GIL
Task Type	Affected by GIL?	Alternative
I/O-bound tasks (e.g., web scraping, file I/O, API calls)	❌ No	Use threading (ThreadPoolExecutor)
CPU-bound tasks (e.g., image processing, ML, number crunching)	✅ Yes (GIL slows down threads)	Use multiprocessing (ProcessPoolExecutor)
"""

from multiprocessing import Pool


def square(n):
    return n ** 2


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a pool with 3 worker processes
    with Pool(processes=3) as pool:
        result = pool.map(square, numbers)  # Apply `square` function to each number

    print(result)  # Output: [1, 4, 9, 16, 25]
