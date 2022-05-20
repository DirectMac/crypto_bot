from dataclasses import dataclass
from typing import Final


@dataclass
class FormConfig:
    CURRENCIES: Final = 'CURRENCIES'
    PERIOD: Final = 'PERIOD'
    SIZE: Final = 'SIZE'
    INDEX: Final = 'INDEX'
    INVALID = None


@dataclass
class FormCurrencies:
    BTC: Final = 'btc'
    DOGE: Final = 'doge'
    ETH: Final = 'eth'
    WAXP: Final = 'waxp'
    LTC: Final = 'ltc'
    XRP: Final = 'xrp'
    INVALID = None


@dataclass
class FormPeriod:
    MIN1: Final = '1min'
    MIN5: Final = '5min'
    MIN15: Final = '15min'
    MIN30: Final = '30min'
    MIN60: Final = '60min'
    HOUR4: Final = '4hour'
    DAY1: Final = '1day'
    MON1: Final = '1mon'
    WEEK1: Final = '1week'
    YEAR1: Final = '1year'
    INVALID = None


@dataclass
class FormSize:
    MIN: Final = 1
    MAX: Final = 2000
    INVALID = None


@dataclass
class FormIndex:
    CLOSE: Final = 'close'
    OPEN: Final = 'open'
    LOW: Final = 'low'
    HIGH: Final = 'high'
    INVALID = None
