# Function to get user input for number of dice, sides, and rolls
def get_user_input():
    while True:
        try:
            # Prompt user for number of dice, sides, and rolls
            dice = int(input("How many dice do you want to roll at once? "))
            sides = int(input("How many sides does the dice have? "))
            rolls = int(input("How many times do you want to roll the dice? "))
            # Check if the user input is valid
            if dice < 1 or sides < 1 or rolls < 1:
                print("Invalid input. The number of dice, sides, and rolls must be at least 1.")
                continue
            # Return the user input if valid
            return dice, sides, rolls
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")