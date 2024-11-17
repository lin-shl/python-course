import json


INPUT_FILE = "input.json"


def task() -> float:
    # Чтение данных из файла
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)

    # Суммирование произведений
    sum_ = sum(i['score'] * i['weight'] for i in data)

    # Округление
    return round(sum_, 3)


print(task())
