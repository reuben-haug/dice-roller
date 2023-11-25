# Function to roll the dice and print the results
def roll_dice(dice, sides, rolls):
    all_results = []    # List to store all the results
    total = 0   # Variable to store the total sum of all rolls
    for _ in range(rolls):
        # Roll the dice and print the results
        results = [random.randint(1, sides) for _ in range(dice)]
        print(f'You rolled: {results}')
        total += sum(results)
        all_results.append(results)
    print(f'The total sum of all rolls is: {total}')
    return all_results, total