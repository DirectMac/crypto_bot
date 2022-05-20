from .prices import Prices
from ..constants.interfaces import FormConfig
from .config import get_config


class Brain(Prices):

    def count_currency(self, currency):
        period = get_config(FormConfig.PERIOD)
        size = get_config(FormConfig.SIZE)
        index = get_config(FormConfig.INDEX)
        data = super().fetch_prices(currency, period, size, index)
        current = data[0]
        high = max(data)
        low = min(data)
        procent_down = (high - current) / ((high + current) / 2) * 100
        procent_up = (current - low) / ((current + low) / 2) * 100

        if procent_up >= procent_down:
            procent = float(f'{procent_up:.2f}')
            procent = f'[green]+{procent}'
        else:
            procent = float(f'{procent_down:.3f}')
            procent = f'[red]-{procent}'

        return {
            currency: [current, high, low, procent]
        }
