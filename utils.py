import datetime
import pandas as pd
import yfinance as yf

from typing import Tuple, List


def get_tickers() -> List:
    wiki_table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    wiki_df = wiki_table[0]

    return wiki_df['Symbol'].to_list()


def get_start_end_date(date: str, train_years: int) -> Tuple[str, str]:
    date_formatted = datetime.datetime.strptime(date, '%Y-%m-%d')
    start_date = date_formatted - datetime.timedelta(days=train_years * 365)
    start_date_str = start_date.strftime('%Y-%m-%d')

    return start_date_str, date


def get_train_data(date: str, train_years: int) -> pd.DataFrame:
    start_date, end_date = get_start_end_date(date, train_years)
    tickers = get_tickers()

    return yf.download(tickers, start_date, end_date)['Adj Close']
