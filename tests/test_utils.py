
from random import randint
from functions import utils


def test_load_data(start_list):
    assert type(start_list) == list
    assert type(start_list[randint(0, len(start_list))]) == dict


def test_selection_list(blank_list_dict):
    assert len(utils.selection_list(blank_list_dict)) == 1