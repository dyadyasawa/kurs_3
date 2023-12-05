
from random import randint
from functions import utils


def test_load_data(start_list):
    assert type(start_list) == list
    assert type(start_list[randint(0, len(start_list))]) == dict


def test_selection_list(blank_list_dict):
    assert len(utils.selection_list(blank_list_dict)) == 1


def test_sort_and_choice_list(date_list):
    assert utils.sort_and_choice_list(date_list)[0]['date'] == 252
    assert len(utils.sort_and_choice_list(date_list)) == 5


def test_date_transformation(date_format):
    assert utils.date_transformation(date_format) == '26.08.2019'


def test_account_number_transformation(account_number):
    assert utils.account_number_transformation(account_number[0])[-5] == ' '
    assert utils.account_number_transformation(account_number[1]) == "Внесение наличных средств"
    assert utils.account_number_transformation(account_number[2])[:4] == 'Счет'
