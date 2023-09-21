from typing import Dict

import pandas as pd

from investingfetcher.fetchers.Fetcher import Fetcher
from investingfetcher.parsers.Financials.BalanceSheet import BalanceSheetParser
from investingfetcher.parsers.Financials.CashFlow import CashFlowParser
from investingfetcher.parsers.Financials.Earnings import EarningParser
from investingfetcher.parsers.Financials.Ratios import RatiosParser


class FinancialFetcher(Fetcher):

    async def fetch(self) -> Dict[str, pd.DataFrame]:
        base_url = 'https://www.investing.com/equities/'
        sections = {
            'balance-sheet': BalanceSheetParser,
            'cash-flow': CashFlowParser,
            'ratios': RatiosParser,
            'earnings': EarningParser
        }

        urls = {f'{base_url}{self.stock_symbol}-{section}': (parser, section) for section, parser in sections.items()}
        pages = await self.fetch_all_async(list(urls.keys()))
        return {section: parser(page).parse() for page, (section, parser) in zip(pages, sections.items())}




