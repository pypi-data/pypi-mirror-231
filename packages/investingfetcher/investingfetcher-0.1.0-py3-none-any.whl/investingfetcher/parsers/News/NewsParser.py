from datetime import datetime
from dateutil import parser as dateparser
from investingfetcher.parsers.Parser import Parser


class NewsParser(Parser):

    def __init__(self, page, symbol):
        super().__init__(page)
        self.symbol = symbol

    def parse(self):
        return [self.__extract_dates(), self.__extract_news_text(), self.symbol]

    def __extract_dates(self):
        elms = self.page.find_all('div', {'class': 'contentSectionDetails'})
        date_str = elms[1].text if elms and len(
            elms) >= 2 else str(datetime.now())
        arr = date_str.split('\n')
        if len(arr) > 1:
            return dateparser.parse(arr[1].replace('Published ', ''))
        else:
            return dateparser.parse(arr[0].replace('Published ', ''))

    def __extract_news_text(self):
        page = self.page.find('div', {'class': 'articlePage'})
        useless_text = 'Position added successfully to: \n'
        if page:
            elms = page.find_all('p')
            return ' '.join([elem.text for elem in elms]).replace(useless_text, '')
        return ''
