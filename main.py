# Import the functions we wrote in the src folder
from src.analysis import *
from src.helpers import *
from src.visualization import plot_returns_distribution

def main():
    # 1. Load Data (Cached)
    df = download_sp500_data()
    
    # 2. Process
    df = clean_sp500_df(df)
    df = add_ath_column(df)
    df = add_1y_return_column(df)

    # 3. Generate and Print Text Report
    report = generate_stats_report(df)
    print(report)

    # 4. Generate and Save Plot
    plot_returns_distribution(df)


    

# This block ensures the code only runs if you execute this file directly
if __name__ == "__main__":
    main()
