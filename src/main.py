# pip install git+https://github.com/SorbonneParis1Ufr02FinancePythonM1-M2/helpers.git@master

import os

from helpers.helpers_serialize import dict_to_serialized_file


def main():
    config = {
        "portfolio": {"GE": 0.5, "JPM": 0.2, "MSFT": 0.2, "PG": 0.1},
        "field_to_keep": "Adj Close",
        "begin_date": "2015-01-02",
        "end_date": "2018-03-27",
        "new_fields": ["Date", "Ticker", "Value"],
    }

    os.makedirs("output", exist_ok=True)
    path = os.path.join(os.getcwd(), "output", "output.toml")
    print(path)
    dict_to_serialized_file(config, path)
    print("OK")


if __name__ == "__main__":
    main()
