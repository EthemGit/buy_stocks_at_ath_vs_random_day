import pandas as pd

def print_row_and_252_days_later(df: pd.DataFrame, index: int):
    """
    Given a dataframe and an index, this prints the row for that index and
     the row 252 trading days later.
    """
    # prevent accessing indices that don't exist
    if index >= len(df):
        print(f"Start index {index} is out of range. DataFrame has {len(df)} rows.")
        return
    # 252 days later has to be in-bound too
    end_idx = index + 252
    if end_idx >= len(df):
        print(f"End-Index (index+252) {end_idx} is out of range. DataFrame has {len(df)} rows.")
        return

    specific_rows = df.iloc[[index, index+252]]
    print(specific_rows)


def print_rows_range(df: pd.DataFrame, start_idx: int, n_rows: int) -> None:
    """
    Prints a range of rows from a DataFrame starting at start_idx for n_rows.

    Parameters:
    - start_idx: int, the starting row index (0-based)
    - n_rows: int, number of rows to print

    Returns:
    - None (prints directly)
    """
    # compute end index (make sure it doesn't exceed df length)
    end_idx = start_idx + n_rows
    if start_idx >= len(df):
        print(f"Start index {start_idx} is out of range. DataFrame has {len(df)} rows.")
        return

    if end_idx > len(df):
        print(f"End index {end_idx} exceeds DataFrame length ({len(df)}). Printing until the last row.")
        end_idx = len(df)

    # Print the slice of rows
    print(df.iloc[start_idx:end_idx])

def print_statistics(df):
    """
    Prints some interesting statics. Currently
    - # of trading days
    - # of days at ATH
    - percentage of how many days were ATH
    """
    print("\n--- ATH Statistics ---")
    total_days = len(df)
    ath_days = df['is_ath'].sum() # True counts as 1, False as 0
    print(f"Total trading days: {total_days}")
    print(f"Days at All Time High: {ath_days}")
    print(f"Percentage of time at ATH: {(ath_days/total_days)*100:.2f}%")