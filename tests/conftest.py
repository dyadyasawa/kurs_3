
import pytest
from functions import utils
from config import LOAD_DATA_PATH


@pytest.fixture()
def start_list():
    return utils.load_data(f"../{LOAD_DATA_PATH}")


@pytest.fixture()
def blank_list_dict():
    return [{}, {'state': 'CANCELED', 'name': 'noname'}, {'state': 'EXECUTED'}]


@pytest.fixture()
def date_list():
    return [{'date': 26}, {'date': 11}, {'date': 74}, {'date': 5}, {'date': 252}, {'date': 0}, {'date': 1}]


@pytest.fixture()
def date_format():
    return "2019-08-26T10:50:58.294041"