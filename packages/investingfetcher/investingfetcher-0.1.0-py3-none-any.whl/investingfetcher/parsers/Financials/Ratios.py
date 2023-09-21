from pandas import DataFrame

from investingfetcher.parsers.Parser import Parser


class RatiosParser(Parser):

    def parse(self) -> DataFrame:
        elms = self.page.find_all('tr', {'class': 'child'})
        data_rows = [row for e in elms if len((row := e.text.strip().split('\n'))) == 3]
        df = DataFrame(data_rows).T
        columns = df.iloc[0].values
        return df.rename(
            columns={i: column for i, column in enumerate(columns)},
            index={1: "company", 2: "index"}
        ).drop(index=0)
