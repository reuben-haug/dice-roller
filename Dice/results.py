# Function to save the results to a JSON file
def save_results(all_results, total):
    try:
        with open('dice_rolls.json', 'w') as f:
            json.dump({'all_results': all_results, 'total': total}, f)
    except IOError:
        print("Error: Unable to save results.")

# Function to load the results from a JSON file
def load_results():
    try:
        with open('dice_rolls.json', 'r') as f:
            data = json.load(f)
        return data['all_results'], data['total']
    except IOError:
        print("Error: Unable to load results.")
    except json.JSONDecodeError:
        print("Error: Data in file is not in the expected format.")