import matplotlib.pyplot as plt
import os

def plot_returns_distribution(df, save_filename="plots/1y_return_dist.png"):
    """
    Plots two overlapping histograms and saves the result to a file.
    """
    # ... (Keep the data preparation logic the same) ...
    data = df.dropna(subset=['1y_return'])
    all_days_returns = data['1y_return']
    ath_days_returns = data[data['is_ath'] == True]['1y_return']

    # Create the Plot
    plt.figure(figsize=(10, 6))
    
    # ... (Keep the histogram logic the same) ...
    plt.hist(all_days_returns, bins=50, alpha=0.5, label='All Days', density=True, color='grey')
    plt.hist(ath_days_returns, bins=50, alpha=0.5, label='ATH Days', density=True, color='blue')

    # Add Decoration
    plt.title('Distribution of 1-Year Returns: Buying at ATH vs Random')
    plt.xlabel('1-Year Return (%)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axvline(0, color='black', linestyle='--', linewidth=1)

    # --- Save the plot ---
    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_filename), exist_ok=True)
    plt.savefig(save_filename)
    print(f"Plot saved successfully to {save_filename}")

    # Show it (optional, can comment out if you want it to run silently)
    plt.show()