from ..constants.interfaces import *
from dataclasses import astuple


def check_currencies(currencies_list):
    allowable_currencies = FormCurrencies()
    forms = list(astuple(allowable_currencies))
    for item in currencies_list:
        if item not in forms:
            currencies_list.remove(item)
    return currencies_list


def check_period(symbol):
    allowable_period = FormPeriod()
    forms = list(astuple(allowable_period))
    if symbol in forms:
        return symbol
    return allowable_period.MIN5


def check_size(symbol):
    allowable_size = FormSize()
    try:
        if int(symbol) >= allowable_size.MAX:
            return allowable_size.MAX

        if int(symbol) <= allowable_size.MIN:
            return allowable_size.MIN
        return int(symbol)
    except:
        return 300


def check_index(symbol):
    allowable_index = FormIndex()
    forms = list(astuple(allowable_index))
    if symbol in forms:
        return symbol
    return allowable_index.CLOSE
