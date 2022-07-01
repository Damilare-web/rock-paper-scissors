import random

print(
    "Winning Rules of the Rock Paper Scissors game as follows: \n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n"
)

while True:
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    user_input = input(
        "Enter a choice (R for Rock, P for Paper, S for Scissors): ")
    user_input = user_input.upper()
    if user_input not in possible_actions:
        print("Invalid input. Please enter one of the following: R, P, S")
        continue
    actions_dict = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors",
    }
    print(
        f"\nPlayer ({actions_dict[user_input]}) : CPU ({actions_dict[computer_action]})\n")

    if user_input == computer_action:
        print("It's a tie!\nYou'll have to try again!\n")
        continue
    elif user_input == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! Computer wins!")
    elif user_input == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! Computer wins!")
    elif user_input == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! Computer wins!")
    else:
        print("Invalid input! Please try again.")
        continue

    if input("\nDo you want to play again? (Y/N): ").upper() != "Y":
        break