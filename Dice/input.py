import dice

# Function to get user input for number of dice, sides, and rolls
def get_user_input():
    while True:
        try:
            # Prompt user for number of dice, sides, and rolls
            num_dice = int(input("How many dice do you want to roll at once? "))
            sides = int(input("How many sides does the dice have? "))
            rolls = int(input("How many times do you want to roll the dice? "))
            # Check if the user input is valid
            if num_dice < 1 or sides < 1 or rolls < 1:
                print("Invalid input. The number of dice, sides, and rolls must be at least 1.")
                continue
            # Roll the dice using the dice library
            for _ in range(rolls):
                result = dice.roll(f'{num_dice}d{sides}')
                print(f'You rolled {result}')
            return num_dice, sides, rolls
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")