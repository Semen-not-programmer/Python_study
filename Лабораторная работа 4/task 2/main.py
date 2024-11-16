import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f_1:
        data = [i for i in csv.DictReader(f_1)]

    with open(OUTPUT_FILENAME, 'w') as f_2:
        i = json.dumps(data, indent=4)
        f_2.write(i)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
