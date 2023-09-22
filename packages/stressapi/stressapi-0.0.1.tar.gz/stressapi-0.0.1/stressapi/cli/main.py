import time
from threading import Lock
from typing import Optional
import click
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
import requests


lock = Lock()


def request(url: str) -> None:
    try:
        response = requests.get(url)
        # print(response.status_code)
    except Exception as error:
        print(str(error))


@click.command()
@click.argument('url')
@click.option('--workers', type=int, default=1, help='Number of workers')
@click.option('--threads', type=int, default=1, help='Number of threads')
@click.option('--count', type=int, default=100, help='request count')
def stressapi(url: str, workers: int, threads: int, count: int):
    """Stress test a URL."""
    thread_pool = ThreadPoolExecutor(max_workers=threads)

    max_num = count

    started_at = time.time()

    for _ in range(max_num):
        thread_pool.submit(request, url)
    thread_pool.shutdown(wait=True)

    ended_at = time.time()

    pay_time = (ended_at-started_at)
    print(f'pay_time: {round(pay_time,3)}s')
    print(f'RPS: {max_num/pay_time}')


if __name__ == '__main__':
    stressapi()
