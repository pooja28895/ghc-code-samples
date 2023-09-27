"""Basic Multiprocessing Example"""
import multiprocessing
import time


def heavy_computation(number):
    print(f"Starting intensive operation on {number}")
    time.sleep(2)
    print(f"Finished intensive operation on {number}")


def compute_using_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(heavy_computation, numbers)


if __name__ == "__main__":
    numbers = [x for x in range(4)]

    start_time = time.time()
    compute_using_multiprocessing(numbers)
    duration = time.time() - start_time
    print(f"Total Duration {duration} seconds")