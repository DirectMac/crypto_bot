from ..utils.input_checker import *
import requests
import sys


class Prices:

    link_to_prices = 'https://api.huobi.pro/market/history/kline?period={}&size={}&symbol={}usdt'

    def get_prices(self, currency, period, size, index):

        get_prices = requests.get(
            self.link_to_prices.format(period, size, currency)).json()

        prices = []

        try:
            for i in get_prices['data']:
                prices.append(i[index])

        except KeyError:
            print("Error: Related to currency or config")
            sys.exit()

        return prices
