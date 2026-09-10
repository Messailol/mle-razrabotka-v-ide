from pathlib import Path

import pandas as pd

from src.reporter import DataFrameReporter


def main():
    data_path = Path(__file__).parent / "data" / "payments.csv"
    data = pd.read_csv(data_path)

    reporter = DataFrameReporter(include_all=True)
    reporter.show_report(data, "Отчёт по payments.csv")


if __name__ == "__main__":
    main()
