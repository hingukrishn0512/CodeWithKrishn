import random

# Randomly choose the computer's move
computer = random.choice([1, -1, 0])

# User input
name = input("Enter your name: ")
your_choice = input("Enter your choice (stone, paper, scissor): ").lower()

# Mapping choices to numbers
values_dict = {"stone": 1, "paper": -1, "scissor": 0}

# Check if the user entered a valid choice
if(your_choice not in values_dict):
    print("enter valid number")
else:
    younum = values_dict[your_choice]

    # Display choices
    print(f"{name}'s choice: {your_choice.capitalize()}")
    print(f"Computer's choice: {['Stone', 'Paper', 'Scissors'][computer - 1]}")

    # Determine the winner
    if younum == computer:
        print("It's a tie!")
    elif younum == 1 and computer == 0:
        print(f"{name} wins! Stone beats Scissors.")
    elif younum == 1 and computer == -1:
        print(f"Computer wins! Paper beats Stone.")
    elif younum == 0 and computer == 1:
        print(f"Computer wins! Stone beats Scissors.")
    elif younum == 0 and computer == -1:
        print(f"{name} wins! Scissors beats Paper.")
    elif younum == -1 and computer == 1:
        print(f"{name} wins! Paper beats Stone.")
    elif younum == -1 and computer == 0:
        print("Computer wins! Scissors beats Paper.")
