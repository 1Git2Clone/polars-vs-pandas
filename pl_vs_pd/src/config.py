from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
CSV_FILENAME: Path = PROJECT_ROOT / "csv/foo.csv"
WARM_UP_RUN_COUNT: int = 2
