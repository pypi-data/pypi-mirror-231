from itertools import chain
from typing import List, Dict

import pandas as pd

from investingfetcher.fetchers.Fetcher import Fetcher
from investingfetcher.parsers.News.LinkParsers import NewsLinkParser
from investingfetcher.parsers.News.NewsParser import NewsParser


class NewsFetcher(Fetcher):
    def __init__(self, stock_symbol: str, api_key: str, max_pages: int = 2):
        super().__init__(stock_symbol, api_key)
        self.base_url = 'https://www.investing.com/equities/'
        self.news_base_url = 'https://www.investing.com'

        self.equities_news_url = [self.base_url + self.stock_symbol + '-news' + f'/{page}' for page in
                                  range(1, max_pages)]

    async def fetch(self) -> Dict[str, pd.DataFrame]:
        link_pages: List[bytes] = await self.fetch_all_async(self.equities_news_url)
        relative_links: chain = chain(
            *[article_links for page in link_pages if (article_links := NewsLinkParser(page).parse())]
        )
        absolute_links = [self.news_base_url + link for link in relative_links]
        pages = await self.fetch_all_async(absolute_links)
        return {'news': pd.DataFrame([NewsParser(page, self.stock_symbol).parse() for page in pages],
                                     columns=['Creation datetime', 'Content', 'Symbol'])}
