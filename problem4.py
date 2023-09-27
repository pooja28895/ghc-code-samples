import multiprocessing
import concurrent.futures
import threading
import time

def multiply_by_4(number):
        print(f"4 multiplied by {number} = {number * 4}")

def compute_synchronously(numbers):
    for number in numbers:
        multiply_by_4(number)

def compute_using_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(multiply_by_4, numbers)

def compute_using_multithreading(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(multiply_by_4, numbers)

if __name__ == "__main__":
    numbers = numbers = [x for x in range(11)]

    start_time = time.time()
    compute_synchronously(numbers)
    duration_sync = time.time() - start_time

    start_time = time.time()
    compute_using_multiprocessing(numbers)
    duration_multiprocessing = time.time() - start_time

    start_time = time.time()
    compute_using_multithreading(numbers)
    duration_multithreading = time.time() - start_time

    print(f"Time taken synchronously: {duration_sync}")
    print(f"Time taken using multiprocessing: {duration_multiprocessing}")
    print(f"Time taken using multithreading: {duration_multithreading}")
