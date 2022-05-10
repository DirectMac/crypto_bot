from ..config import get_config
from ...constants.interfaces import *
from ...utils.format_period import format_period
import time


def get_title():
    size = get_config(FormConfig.SIZE)
    name_time = format_period()[1]
    amount = format_period()[0]

    if name_time == 'min':
        seconds = amount * size * 60

    elif name_time == 'hour':
        seconds = amount * size * 60 * 60

    elif name_time == 'day':
        seconds = amount * size * 24 * 60 * 60

    elif name_time == 'mon':
        seconds = amount * size * 30 * 24 * 60 * 60

    elif name_time == 'week':
        seconds = amount * size * 7 * 24 * 60 * 60

    elif name_time == 'year':
        seconds = amount * size * 365 * 24 * 60 * 60

    days = int((seconds / 60) / 60 // 24)
    time_format = time.strftime("%Hh:%Mm", time.gmtime(seconds))

    return str(f'Last {days}d:{time_format}')
