"""Find factorials of all numbers up 5000"""

import multiprocessing
import time


def factorial(number):
    op = 1
    for i in range(1,number+1):
        op *= i
    # print(f"{number}! = {op}")


def get_factorials_using_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(factorial, numbers)

def get_factorials_synchronously(numbers):
    for number in numbers:
        factorial(number)

if __name__ == "__main__":
    numbers = [i for i in range(1,5000)]

    start_time = time.time()
    get_factorials_using_multiprocessing(numbers)
    duration_multithreading = time.time() - start_time

    start_time = time.time()
    get_factorials_synchronously(numbers)
    duration_sync = time.time() - start_time

    print(f"Synchronous Duration:  {duration_sync} seconds")
    print(f"Multiprocessing Duration:  {duration_multithreading} seconds")

# Output from previous runs:
# Synchronous Duration:  13.20751690864563 seconds
# Multiprocessing Duration:  1.9648630619049072 seconds