# 📈 PyInvestingDataFetcher

A simple Python library to fetch equity data from investing.com.

Disclaimer: I created this library for fun and learning. I'm not sure about the proper ways to utilize this data. Maybe it's useful for someone out there! 🤷‍♂️ Also, I haven't checked the terms of service of investing.com closely, so using this might not align with their policies. Please ensure you're in compliance before using! 🚫
📜 Table of Contents

📜 Table of Contents

1. Installation
2. Usage
3. Configuration
4. Contributing
5. License

# 🛠 Installation

To install the library, just do:
```sh

pip install PyInvestingDataFetcher

```

# 🚀 Usage

Fetching data is a breeze with PyInvestingDataFetcher. Here's how:

```python
from investingfetcher.equity import Equity
from investingfetcher.fetchers import LazyEquityFetcher

if __name__ == "__main__":
    fetcher = LazyEquityFetcher('api_key.config', as_single_df=True)
    res = fetcher[Equity.tesla]

```

Replace Equity.tesla with your desired equity name and see the magic! 🎩✨
# ⚙ Configuration

Remember to set up your api_key.config with the necessary keys and configurations to access investing.com data.
api_key.config should look like this:
```sh
api_key=[your_api_key_here]
```
