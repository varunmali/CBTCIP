import random

# Define functions for hand gestures with descriptive names
def select_rock():
    """Returns the string 'rock'"""
    return "rock"

def select_paper():
    """Returns the string 'paper'"""
    return "paper"

def select_scissors():
    """Returns the string 'scissors'"""
    return "scissors"

# Function to generate the computer's choice
def get_computer_choice():
    """Randomly selects one of the hand gestures for the computer"""
    gestures = [select_rock, select_paper, select_scissors]
    return random.choice(gestures)()

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's choice and the computer's choice.
    Returns a string describing the outcome.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win! Rock crushes scissors."
        else:
            return "You lose! Paper covers rock."
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win! Paper covers rock."
        else:
            return "You lose! Scissors cut paper."
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win! Scissors cut paper."
        else:
            return "You lose! Rock crushes scissors."
    else:
        return "Invalid input."

# Mapping single-letter choices to functions
choice_map = {
    "r": select_rock,
    "p": select_paper,
    "s": select_scissors
}

# Function to get the user's choice with validation
def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors.
    Accepts single-letter inputs and validates the choice.
    Returns the corresponding full string for the choice.
    """
    while True:
        user_input = input("Choose rock (r), paper (p), or scissors (s) (or 'q' to quit): ").lower()
        if user_input in choice_map:
            return choice_map[user_input]()  # Call the mapped function
        elif user_input == 'q':
            print("Thanks for playing! See you again :)")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Main game loop
def play_game():
    """Main game loop that allows the user to play multiple rounds"""
    user_score = 0
    computer_score = 0

    while True:
        # Get the user's choice
        user_choice = get_user_choice()

        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner and display the result
        result = determine_winner(user_choice, computer_choice)
        print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
        print(result)

        # Update the score based on the result
        if "You win!" in result:
            user_score += 1
        elif "You lose!" in result:
            computer_score += 1

        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final Score -> You: {}, Computer: {}. See you again :)".format(user_score, computer_score))
            break

# Start the game
play_game()
