from ..config import get_config
from ...constants.interfaces import *
from ...utils.format_period import format_period
import time


def get_title():
    size = get_config(FormConfig.SIZE)
    time_unit = format_period()[1]
    amount = format_period()[0]

    if time_unit == 'min':
        seconds = amount * size * 60

    elif time_unit == 'hour':
        seconds = amount * size * 60 * 60

    elif time_unit == 'day':
        seconds = amount * size * 24 * 60 * 60

    elif time_unit == 'mon':
        seconds = amount * size * 30 * 24 * 60 * 60

    elif time_unit == 'week':
        seconds = amount * size * 7 * 24 * 60 * 60

    elif time_unit == 'year':
        seconds = amount * size * 365 * 24 * 60 * 60

    days = int((seconds / 60) / 60 // 24)
    time_format = time.strftime("%Hh:%Mm", time.gmtime(seconds))

    return str(f'Last {days}d:{time_format}')
