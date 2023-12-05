
import pytest
from functions import utils
from config import LOAD_DATA_PATH


@pytest.fixture()
def start_list():
    return utils.load_data(f"../{LOAD_DATA_PATH}")