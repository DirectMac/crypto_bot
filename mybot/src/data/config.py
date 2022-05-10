import json
from ..utils.prepare_data import prepare_data


@prepare_data
def get_config(config):
    with open('mybot/config.json', 'r') as file:
        data_config = json.load(file)
    return data_config, config
