import polars as pl
import pandas as pd

from config import CSV_FILENAME


def polars_csv_head() -> pl.DataFrame:
    return pl.read_csv(CSV_FILENAME).head()


def pandas_csv_head() -> pd.DataFrame:
    return pd.read_csv(CSV_FILENAME).head()
