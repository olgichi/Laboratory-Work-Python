"""Конвертер из CSV в JSON формат"""
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f_csv:
        data_csv = [line for line in csv.DictReader(f_csv)]
    with open(OUTPUT_FILENAME, "w") as f_json:
        json.dump(data_csv, f_json,indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
