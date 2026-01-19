import yfinance as yf
import pandas as pd
import os

DATA_PATH = "data/sp500_data.csv"

def download_sp500_data(start_date="1950-01-01"):
    """
    Checks if data exists locally. If yes, load it.
    If no, download from yfinance and save it to CSV.
    """
    # Check if the file already exists
    if os.path.exists(DATA_PATH):
        print(f"Loading data from local file: {DATA_PATH}...")
        # parse_dates tells pandas to treat the 'date' column as actual dates, not strings
        # index_col=0 sets the first column (date) as the index, which matches yfinance format
        df = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)
        return df
    
    # does not exist -> download the data
    ticker = "^GSPC"
    print(f"Downloading data for {ticker}...")
    df: pd.DataFrame = yf.download(ticker, start=start_date, progress=False)

    # Save the raw data so we don't have to download again
    # We save it immediately to the data folder
    df.to_csv(DATA_PATH)
    print(f"Data saved to {DATA_PATH}")
        
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
    return df


def generate_stats_report(df):
    """
    Calculates key statistics and returns a formatted string summary.
    """
    # Filter valid data
    df_valid = df.dropna(subset=["1y_return"])
    
    ath_data = df_valid[df_valid["is_ath"] == True]["1y_return"]
    all_data = df_valid["1y_return"]
    
    # Calculate stats
    avg_ath = ath_data.mean()
    avg_all = all_data.mean()
    median_ath = ath_data.median()
    median_all = all_data.median()
    win_rate_ath = (ath_data > 0).mean() * 100
    win_rate_all = (all_data > 0).mean() * 100
    
    # Calculate the "Edge" (How much better/worse is ATH?)
    edge_mean = avg_ath - avg_all
    
    report = f"""
    =============================================
    ANALYSIS SUMMARY: BUYING S&P 500 AT ATH
    =============================================
    1. EXPECTED RETURN (AVERAGE)
       - Buying Randomly: {avg_all:.2f}%
       - Buying at ATH:   {avg_ath:.2f}%
       - Difference:      {edge_mean:+.2f}% 
       -> Conclusion: Buying at ATH yields {'BETTER' if edge_mean > 0 else 'WORSE'} average returns.

    2. MEDIAN RETURN (Typical Outcome)
       - Buying Randomly: {median_all:.2f}%
       - Buying at ATH:   {median_ath:.2f}%

    3. WIN RATE (Chance of making money)
       - Buying Randomly: {win_rate_all:.2f}%
       - Buying at ATH:   {win_rate_ath:.2f}%
    =============================================
    """
    return report
