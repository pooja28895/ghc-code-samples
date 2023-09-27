"""Download 1000 Web Pages"""

import asyncio
import time
import aiohttp
import requests


async def fetch_webpage(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} words from {url}")

def fetch_webpage_sync(session, url):
    with session.get(url) as response:
        print(f"Read {len(response.content)} words from {url}")

async def fetch_all_pages_with_aync(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_webpage(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)


def fetch_all_pages_synchronously(urls):
    with requests.Session() as session:
        for url in urls:
            fetch_webpage_sync(session, url)

if __name__ == "__main__":
    urls = [
        "https://pooja28895.github.io/dummy-webpage-1/",
        "https://pooja28895.github.io/dummy-webpage-1/",
    ] * 500

    start_time = time.time()
    asyncio.run(fetch_all_pages_with_aync(urls))
    duration_async = time.time() - start_time

    start_time = time.time()
    fetch_all_pages_synchronously(urls)
    duration_sync = time.time() - start_time

    print(f"Time taken to fetch {len(urls)} using asyncio: {duration_async}")
    print(f"Time taken to fetch {len(urls)} using synchronously: {duration_sync}")

# Results from a previous run:
# Time taken to fetch 1000 using asyncio: 2.6749320030212402
# Time taken to fetch 1000 using synchronously: 189.28802919387817