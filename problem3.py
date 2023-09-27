import time
import aiofiles
import asyncio
import json
from pathlib import Path
import os

DIRECTORY = '/Users/ppatel462/Desktop/ghc presentation resources/github_repo/ghc-code-samples/large_data'

async def read_file_async(file):
    async with aiofiles.open(file, mode='r') as f:
        contents = await f.read()
    print(f"read {file}")

async def read_all_files_with_async(files):
    tasks = []
    for file in files:
        task = asyncio.create_task(read_file_async(file))
        tasks.append(task)
    await asyncio.gather(*tasks)

def read_file_sync(file):
    with open(file, 'r') as f:
        contents = f.read()
    print(f"read {file}")

def read_all_files_with_sync(files):
    for file in files:
        read_file_sync(file)

if __name__ == "__main__":
    # files = Path(DIRECTORY).glob('*.json')
    files = os.listdir(DIRECTORY)
    files = [os.path.join(DIRECTORY, file) for file in files]

    start_time = time.time()
    asyncio.run(read_all_files_with_async(files))
    duration_async = time.time() - start_time

    start_time = time.time()
    read_all_files_with_sync(files)
    duration_sync = time.time() - start_time

    print(f"Read using asyncio in {duration_async} seconds")
    print(f"Read synchronously in {duration_sync} seconds")