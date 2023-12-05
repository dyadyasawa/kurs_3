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


def sort_and_choice_list(list_dict):
    """Сортирует входящий список по дате, и возврвщает 5 самых 'свежих' элементов"""

    sorted_list = sorted(list_dict, key=lambda item: item['date'], reverse=True)
    return sorted_list[0: 5]


def date_transformation(date):
    """Преобразует дату из входящего формата в формат дд.мм.гггг"""

    stage_1 = date.split("T")[0]
    stage_2 = stage_1.split("-")
    total_stage = ".".join(stage_2[::-1])
    return total_stage