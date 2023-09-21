from typing import List

from investingfetcher.parsers.Parser import Parser


class NewsLinkParser(Parser):
    def parse(self) -> List[str]:
        articles = self.page.find_all('article')

        def link_is_okay(article):
            return article and article.find('a') and article.find('a').get('href') != '/'

        return [article.find('a', {'data-test': 'article-title-link'}).get('href') for article in articles if
                link_is_okay(article)]
