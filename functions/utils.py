import json


def load_data(load_path):
    """Преобразует json-файл в список словарей"""

    with open(load_path, "r", encoding="UTF8") as file:
        list_dict = json.load(file)
    return list_dict