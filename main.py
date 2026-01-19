# Import the functions we wrote in the src folder
from src.analysis import *
from src.helpers import *

def main():
    # Step 1: Get the data
    df = download_sp500_data()

    # Step 2: Clean the df
    df = clean_sp500_df(df)

    # Step 3: Get new ATH column
    df = add_ath_column(df)

    # Step 4: Get new 1y_return column
    df = add_1y_return_column(df)

    print_statistics(df)
    

# This block ensures the code only runs if you execute this file directly
if __name__ == "__main__":
    main()
