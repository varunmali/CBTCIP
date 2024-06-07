import random

# Define functions for hand gestures (descriptive names)
def select_rock():
  return "rock"

def select_paper():
  return "paper"

def select_scissors():
  return "scissors"

# Function to generate computer's choice with clear variable name
def get_opponent_choice():
  choices = [select_rock, select_paper, select_scissors]
  return random.choice(choices)()

# Function to determine winner with clear explanations
def determine_victor(user_choice, opponent_choice):
  if user_choice == opponent_choice:
    return "It's a tie!"
  elif user_choice == "rock":
    if opponent_choice == "scissors":
      return "You win! Rock crushes scissors."
    else:
      return "You lose! Paper covers rock."
  elif user_choice == "paper":
    if opponent_choice == "rock":
      return "You win! Paper covers rock."
    else:
      return "You lose! Scissors cut paper."
  else:
    if opponent_choice == "paper":
      return "You win! Scissors cut paper."
    else:
      return "You lose! Rock crushes scissors."
  
# Function to handle user input and validation
def get_user_choice():
  while True:
    user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
    if user_choice in ["rock", "paper", "scissors"]:
      return user_choice
    elif user_choice == 'q':
      exit()
    else:
      print("Invalid choice. Please try again.")
