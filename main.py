
from config import LOAD_DATA_PATH
from functions import utils

start_list = utils.load_data(LOAD_DATA_PATH)
executed_list = utils.selection_list(start_list)
sorted_list = utils.sort_and_choice_list(executed_list)

utils.output_result(sorted_list)
