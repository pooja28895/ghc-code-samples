"""Basic Asyncio Example"""
import asyncio
import time

async def do_something_long(number):
    print(f"Starting long operation on {number}")
    await asyncio.sleep(number)
    print(f"Finished long operation on {number}")

async def use_async_io(numbers):  
    tasks = [do_something_long(number) for number in numbers]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    numbers = [4,3,2,1]
    start_time = time.time()
    asyncio.run(use_async_io(numbers))
    duration = time.time() - start_time
    print(f"total duration: {duration} seconds")