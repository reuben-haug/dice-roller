# Function to plot the results
def plot_results(all_results, sides):
    plt.hist([roll for rolls in all_results for roll in rolls], bins=range(1, sides+2), edgecolor='black', align='left')
    plt.xlabel('Dice Roll')
    plt.ylabel('Frequency')
    plt.title('Frequency of Each Dice Roll')
    plt.savefig('dice_roll_histogram.png')