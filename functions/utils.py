import json


def load_data(load_path):
    """Преобразует json-файл в список словарей"""

    with open(load_path, "r", encoding="UTF8") as file:
        list_dict = json.load(file)
    return list_dict


def selection_list(list_dict):
    """Создает новый список словарей, удаляя пустые, и отбирая по заданному значению из входящего """

    result_list = []
    for item in list_dict:
        if item == {}:
            continue
        elif item['state'] == 'EXECUTED':
            result_list.append(item)
    return result_list