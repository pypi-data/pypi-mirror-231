import asyncio
from abc import ABC, abstractmethod
from typing import List, Dict

import aiohttp
import pandas as pd
from aiohttp import ClientSession, ClientTimeout


class Fetcher(ABC):

    def __init__(self, stock_symbol: str, api_key: str):
        self.stock_symbol = stock_symbol
        self.api_key = api_key

    async def fetch_async(self, session: ClientSession, url: str):
        params = {
            'url': url,
            'apikey': self.api_key,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            async with session.get(url, params=params, headers=headers) as response:
                if not response.ok:
                    print(f"Failed to fetch {url}. Status: {response.status}. Reason: {await response.text()}")
                    return None
                return await response.content.read()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    async def fetch_all_async(self, urls: List[str]):
        timeout = ClientTimeout(total=10)
        conn = aiohttp.TCPConnector(limit_per_host=40)
        async with aiohttp.ClientSession(timeout=timeout, connector=conn) as session:
            tasks = [self.fetch_async(session, url) for url in urls]
            return [response for response in await asyncio.gather(*tasks) if response]

    def fetch_all(self, urls):
        return asyncio.run(self.fetch_all_async(urls))

    @abstractmethod
    def fetch(self) -> Dict[str, pd.DataFrame]:
        raise NotImplementedError('Make some implementations')
