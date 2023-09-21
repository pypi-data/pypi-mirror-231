from pandas import DataFrame

from investingfetcher.parsers.Parser import Parser


class EarningParser(Parser):
    def parse(self) -> DataFrame:
        unfiltered_cols = 6
        elms = self.page.find_all('tr')
        data_rows = [row for e in elms if len((row := e.text.strip().split('\n'))) == unfiltered_cols]
        cleaned_rows = [[cell.replace('\xa0', '') for cell in r] for r in data_rows]
        return DataFrame(cleaned_rows[1:], columns=cleaned_rows[0])
