import time

from typing import Callable


def bench(func: Callable[[], object]) -> int:
    start: int = time.perf_counter_ns()
    print(func())
    end: int = time.perf_counter_ns()
    total_time: int = end - start
    print(f"{func.__name__.capitalize()}: {total_time:,}ns.")

    return total_time


def output_quicker_perf(df_lib: str, *, faster_ns: int, slower_ns: int) -> str:
    return f"{df_lib} is {slower_ns / faster_ns} times faster than Pandas."
