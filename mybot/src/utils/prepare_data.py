from .input_checker import *
from ..constants.interfaces import *


def prepare_data(function_to_decorate):
    def wrapper(arg):
        for item in function_to_decorate(arg):
            if arg is FormConfig.SIZE:
                return check_size(item[arg])
            elif arg is FormConfig.CURRENCIES:
                return check_currencies(item[arg])
            elif arg is FormConfig.PERIOD:
                return check_period(item[arg])
            elif arg is FormConfig.INDEX:
                return check_index(item[arg])
    return wrapper
