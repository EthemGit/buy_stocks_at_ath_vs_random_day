import yfinance as yf
import pandas as pd

def download_sp500_data(start_date="1950-01-01"):
    """
    Downloads S&P 500 data from yfinance.
    """
    ticker = "^GSPC"
    print(f"Downloading data for {ticker}...")
    df = yf.download(ticker, start=start_date, progress=False)
        
    return df

def clean_sp500_df(df):
    """
    Clean the df from yfinance up: delete OHLV from OHLCV, i.e. only keep closing price.
    Resets index: date stops being index, instead regular column.
    """
    df = df["Close"]  # keep only closing price
    df = df.reset_index()  # date no longer the index
    df.columns = ["date", "close"]  # rename columns (one of them being the date)
    return df

def add_ath_column(df):
    df["is_ath"] = df["close"] == df["close"].cummax()
    return df

def add_1y_return_column(df):
    df["1y_return"] = (((df['close'].shift(-252)) / df["close"]) - 1) * 100
    df.fillna("NaN (Not enough time passed)", inplace=True)
    return df
