import matplotlib.pyplot as plt
import os

def plot_returns_distribution(df, save_filename="plots/1y_return_dist.png"):
    """
    Plots two overlapping histograms with average returns in the legend.
    """
    # 1. Prepare data
    data = df.dropna(subset=['1y_return'])
    
    all_days_returns = data['1y_return']
    ath_days_returns = data[data['is_ath'] == True]['1y_return']

    # 2. Calculate Averages
    avg_all = all_days_returns.mean()
    avg_ath = ath_days_returns.mean()

    # 3. Create the Plot
    plt.figure(figsize=(10, 6))

    # Plot 'All Days'
    # We add the average to the label string here
    plt.hist(all_days_returns, bins=50, alpha=0.5, 
             label=f'All Days (Avg: {avg_all:.2f}%)', 
             density=True, color='grey')

    # Plot 'ATH Days'
    plt.hist(ath_days_returns, bins=50, alpha=0.5, 
             label=f'ATH Days (Avg: {avg_ath:.2f}%)', 
             density=True, color='blue')

    # 4. Add Vertical Lines for the Averages (Optional visual aid)
    plt.axvline(avg_all, color='grey', linestyle='dashed', linewidth=1)
    plt.axvline(avg_ath, color='blue', linestyle='dashed', linewidth=1)

    # 5. Add Decoration
    plt.title('Distribution of 1-Year Returns: Buying at ATH vs Random')
    plt.xlabel('1-Year Return (%)')
    plt.ylabel('Probability Density')
    plt.legend() # This will now show the labels we defined above
    plt.grid(True, alpha=0.3)
    
    # Draw a solid black line at 0% for reference
    plt.axvline(0, color='black', linewidth=1.5)

    # 6. Save the plot
    os.makedirs(os.path.dirname(save_filename), exist_ok=True)
    plt.savefig(save_filename)
    print(f"Plot saved successfully to {save_filename}")

    # Show it
    plt.show()
    