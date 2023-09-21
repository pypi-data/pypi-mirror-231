from pandas import DataFrame
from datetime import datetime

from investingfetcher.parsers.Parser import Parser


class CashFlowParser(Parser):
    def parse(self) -> DataFrame:
        elms = self.page.find_all('tr')
        data_rows = [row for e in elms if len((row := e.text.strip().split('\n'))) == 5]

        periods = self.page.find('tr', {'id': "header_row"}).text.strip().split('\n')[1:]
        periods = [datetime.strptime(d, '%Y%d/%m') for d in periods]

        df = DataFrame(data_rows).T
        column_names = df.iloc[0].values
        return df.drop(index=0).rename(
            columns={i: column_name for i, column_name in enumerate(column_names)},
            index={i + 1: date for i, date in enumerate(periods)}
        )
