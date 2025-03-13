"""
🔹 asyncio and await in Python
Python’s asyncio library allows for asynchronous programming,
 enabling you to run multiple tasks concurrently without using multiple threads or processes.

1️⃣ Synchronous vs Asynchronous Execution
🔸 Synchronous (Blocking Execution) → Each task waits for the previous one to finish.
🔸 Asynchronous (Non-Blocking Execution) → Tasks can pause and resume while waiting (e.g., waiting for I/O).

2️⃣ Key Concepts
async def → Defines an asynchronous function (coroutine).
await → Pauses execution of a coroutine until the awaited task is done.
asyncio.run() → Runs an async function.
asyncio.create_task() → Runs multiple tasks concurrently.
# """
# if __name__ == "__main__":
#     # 🔹 Synchronous (Slow)
#     import time
#
#     def sync_task(name):
#         print(f"Starting {name}...")
#         time.sleep(3)  # Simulates a delay
#         print(f"Finished {name}!")
#
#     def execute():
#         sync_task("Task 1")
#         sync_task("Task 2")
#
#     execute() # ⏳ Takes 6 seconds (each task runs one after another).

if __name__ == "__main__":
    import asyncio


    async def async_task(name):
        print(f"Starting {name}...")
        await asyncio.sleep(3)  # Simulates a delay (non-blocking)
        print(f"Finished {name}!")


    async def main():
        task1 = asyncio.create_task(async_task("Task 1"))
        task2 = asyncio.create_task(async_task("Task 2"))

        await task1  # Waits for task1 to complete
        await task2  # Waits for task2 to complete


    asyncio.run(main())  # Run the async event loop


    """
    4️⃣ When to Use asyncio?
✅ I/O-bound tasks (e.g., API calls, file handling, databases).
✅ Multiple tasks that can run independently (e.g., fetching multiple web pages).
❌ Not for CPU-heavy tasks (use multiprocessing instead).
    """



