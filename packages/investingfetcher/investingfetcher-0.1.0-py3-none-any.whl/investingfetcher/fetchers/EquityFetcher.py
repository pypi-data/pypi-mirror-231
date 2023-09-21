import asyncio

import pandas as pd

from investingfetcher.equity import Equity
from investingfetcher.fetchers import NewsFetcher
from investingfetcher.fetchers import FinancialFetcher


class LazyEquityFetcher:
    def __init__(self,  path_to_api_file_key: str, as_single_df: bool = False, as_single_dict: bool = True):
        self.api_key = get_api_key(path_to_api_file_key)
        self.as_single_df = as_single_df
        self.as_single_dict = as_single_dict

    def __getitem__(self, item: Equity):
        loop = asyncio.get_event_loop()
        tasks = asyncio.gather(
            FinancialFetcher(item.value, self.api_key).fetch(),
            NewsFetcher(item.value, self.api_key).fetch()
        )
        financials, news = loop.run_until_complete(tasks)
        if not (self.as_single_dict and self.as_single_dict):
            return pd.DataFrame()
        if self.as_single_df:
            dfs = ['earnings', 'cash-flow', 'ratios', 'balance-sheet']
            merged_df = news['news']
            for df in dfs:
                row_count = financials[df].shape[0]
                financials[df].insert(0, 'Symbol', [item.value] * row_count, True)
                merged_df = merged_df.merge(financials[df], on='Symbol')
            return merged_df
        if self.as_single_dict:
            return financials | news


def get_api_key(path: str):
    try:
        with open(path, 'r') as f:
            file = f.read()
            lines = file.split('\n')
            key, value = lines[0].strip().split('=')
            if key == 'api_key' and value:
                return value.strip()
            else:
                raise ValueError
    except Exception:
        raise "Something is wrong. It possible due to the non-existed / empty file "