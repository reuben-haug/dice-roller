# Dice Rolling Simulator 🎲

This is a simple dice rolling simulator written in Python. It allows the user to specify the number of dice, the number of sides on the dice, and the number of times to roll the dice. The results of each roll are printed to the console and saved to a JSON file.

## Features

- User input for number of dice, sides, and rolls
- Dice rolling with random results
- Saving results to a JSON file
- Loading results from a JSON file

## Usage

1. Run `main.py`.
2. When prompted, enter the number of dice you want to roll, the number of sides on the dice, and the number of times to roll the dice.
3. The results of each roll will be printed to the console.
4. The results will also be saved to a file named `dice_rolls.json`.
5. A histogram of the dice roll results will be displayed using matplotlib. This graph shows the distribution of the dice roll results.

## Requirements

- Python 3
- matplotlib

## Future Improvements

- Add error handling for user input
- Implement unit tests
- Store results in a database
- Plot results with matplotlib
- Switch to using the `dice` library for more robust dice rolling functionality