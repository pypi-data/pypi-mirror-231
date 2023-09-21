from pandas import DataFrame

from investingfetcher.parsers.Parser import Parser


class DividendParser(Parser):
    def parse(self) -> DataFrame:
        unfiltered_cols = 7
        unused_cols = ['Type']

        elms = self.page.find_all('tr')
        data_rows = [row for e in elms if len((row := e.text.strip().split('\n'))) == unfiltered_cols]
        cleaned_rows = [[cell for cell in r if cell] for r in data_rows]
        headers = [e.text for e in self.page.find_all('th', {'class': 'pointer'}) if e.text not in unused_cols]
        return DataFrame(cleaned_rows, columns=headers)
