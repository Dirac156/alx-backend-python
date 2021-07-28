#!/usr/bin/env python3
""" measure coroutine """
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ measure time execution of the function wait_n"""
    start_time = time.time()
    await wait_n(n, max_delay)
    elapsed_time = time.time() - start_time
    return elapsed_time / n
