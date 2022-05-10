from .input_checker import *
from ..constants.interfaces import *


def prepare_data(function_to_decorate):
    def wrapper(arg):
        if arg is FormConfig.SIZE:
            for item in function_to_decorate(arg):
                return check_size(item[arg])

        elif arg is FormConfig.CURRENCIES:
            for item in function_to_decorate(arg):
                return check_currencies(item[arg])

        elif arg is FormConfig.PERIOD:
            for item in function_to_decorate(arg):
                return check_period(item[arg])

        elif arg is FormConfig.INDEX:
            for item in function_to_decorate(arg):
                return check_index(item[arg])
    return wrapper
