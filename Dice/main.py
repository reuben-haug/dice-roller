# Import necessary modules
from input import get_user_input
from roll import roll_dice
from results import save_results, load_results
from plot import plot_results

# Main function
def main():
    dice, sides, rolls = get_user_input()   # Get user input
    all_results, total = roll_dice(dice, sides, rolls)  # Roll the dice
    save_results(all_results, total)    # Save the results to a JSON file
    plot_results(all_results, sides)    # Plot the results
    loaded_results, loaded_total = load_results()   # Load the results
    if loaded_results is not None and loaded_total is not None:
        print(f'Loaded results: {loaded_results}')
        print(f'Loaded total: {loaded_total}')

if __name__ == '__main__':
    main()