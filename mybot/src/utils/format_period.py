from ..constants.interfaces import *
from ..data.config import get_config


def format_period():
    title_period = get_config(FormConfig.PERIOD)
    try:
        time_period = int(title_period[:2])
        return [time_period, title_period[2:]]
    except:
        time_period = int(title_period[0])
        return [time_period, title_period[1:]]
