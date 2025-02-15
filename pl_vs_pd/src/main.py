import time

from config import WARM_UP_RUN_COUNT
from utils.bench import bench, output_quicker_perf
from utils.data_frame import pandas_csv_head, polars_csv_head


def main():
    # =========================================================================
    # Warm up runs
    # =========================================================================
    print(f"Doing `{WARM_UP_RUN_COUNT}` warm-up runs.")
    for i in range(1, WARM_UP_RUN_COUNT + 1):
        s = time.perf_counter_ns()
        print(f"Run {i}... ", end="", flush=True)
        polars_csv_head()
        pandas_csv_head()
        print(f"{time.perf_counter_ns() - s:,}ns. total.")
    print("Warm-up finished!")
    # =========================================================================

    pl_time: int = bench(polars_csv_head)
    pd_time: int = bench(pandas_csv_head)

    if pd_time > pl_time:
        print(output_quicker_perf("Polars", faster_ns=pl_time, slower_ns=pd_time))
    else:
        raise RuntimeError(
            output_quicker_perf("Pandas", faster_ns=pd_time, slower_ns=pl_time)
        )


if __name__ == "__main__":
    main()
