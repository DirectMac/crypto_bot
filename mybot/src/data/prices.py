from ..utils.input_checker import *
import requests
import sys


class Prices:
    prices_url = 'https://api.huobi.pro/market/history/kline?period={}&size={}&symbol={}usdt'

    def fetch_prices(self, currency, period, size, index):
        result = []
        fetched_prices = requests.get(
            self.prices_url.format(period, size, currency)).json()
        try:
            for item in fetched_prices['data']:
                result.append(item[index])
        except KeyError:
            print("Error: Related to currency or config")
            sys.exit()

        return result
