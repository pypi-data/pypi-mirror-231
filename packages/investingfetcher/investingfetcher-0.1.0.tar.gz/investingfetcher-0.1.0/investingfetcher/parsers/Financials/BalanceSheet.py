from pandas import DataFrame
from investingfetcher.parsers.Parser import Parser


class BalanceSheetParser(Parser):

    def parse(self) -> DataFrame:
        unfiltered_cols = 5
        elms = self.page.find_all('tr')
        data_rows = [row for e in elms if len((row := e.text.strip().split('\n'))) == unfiltered_cols]
        df = DataFrame(data_rows).T
        return df.drop(index=[0]).rename(columns=dict((enumerate(df.iloc[0].values))))
