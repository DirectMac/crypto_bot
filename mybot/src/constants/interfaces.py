from dataclasses import dataclass


@dataclass
class FormConfig:
    CURRENCIES: str = 'CURRENCIES'
    PERIOD: str = 'PERIOD'
    SIZE: str = 'SIZE'
    INDEX: str = 'INDEX'
    INVALID = None


@dataclass
class FormCurrencies:
    BTC: str = 'btc'
    DOGE: str = 'doge'
    ETH: str = 'eth'
    WAXP: str = 'waxp'
    LTC: str = 'ltc'
    XRP: str = 'xrp'
    INVALID = None


@dataclass
class FormPeriod:
    MIN1: str = '1min'
    MIN5: str = '5min'
    MIN15: str = '15min'
    MIN30: str = '30min'
    MIN60: str = '60min'
    HOUR4: str = '4hour'
    DAY1: str = '1day'
    MON1: str = '1mon'
    WEEK1: str = '1week'
    YEAR1: str = '1year'
    INVALID = None


class FormSize:
    MIN: int = 1
    MAX: int = 2000
    INVALID = None


@dataclass
class FormIndex:
    CLOSE: str = 'close'
    OPEN: str = 'open'
    LOW: str = 'low'
    HIGH: str = 'high'
    INVALID = None
