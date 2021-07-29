#!/usr/bin/env python3
""" Measure time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure execution time"""
    start_time = time.perf_counter()
    allTask = [async_comprehension for i in range(4)]
    await asyncio.gather(*allTask)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
