from rich.live import Live
from rich.table import Table as _Table
from ...constants.interfaces import *
from ..brain import Brain
from ..config import get_config
from .title import get_title
import time


class Table(Brain):

    currency_array = []

    def __del__(self):
        self.currency_array.clear()

    def screen_table(self):
        def generate_table():
            table = _Table(title=get_title())
            table.add_column('Currency')
            table.add_column('Procent')
            table.add_column('Current $')
            table.add_column('High $')
            table.add_column('Low $')

            for data_to_table in self.currency_array:
                for key, data in data_to_table.items():
                    table.add_row(key.upper(),
                                  f'{data[3]}',
                                  f'{data[0]}',
                                  f'{data[1]}',
                                  f'{data[2]}'
                                  )
            return table

        with Live(generate_table(), refresh_per_second=10) as live:
            while True:
                try:
                    currency = get_config(FormConfig.CURRENCIES)
                    for i in currency:
                        self.currency_array.append(super().result(i))
                    live.update(generate_table())
                    self.currency_array.clear()
                    time.sleep(0.2)
                except KeyboardInterrupt:
                    break
