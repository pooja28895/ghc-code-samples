"""Basic Multithreading Example"""
import concurrent.futures
import time


def do_something_long(number):
    print(f"Starting long operation on {number}")
    time.sleep(number)
    print(f"Finished long operation on {number}")


def use_multithreading(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(do_something_long, numbers)


if __name__ == "__main__":
    numbers = [x for x in range(5)]
    start_time = time.time()
    use_multithreading(numbers)
    duration = time.time() - start_time
    print(f"Total duration: {duration} seconds")
