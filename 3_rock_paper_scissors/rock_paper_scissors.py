import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type 'rock', 'paper', 'scissors' or 'q' to quit game: ")
    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand = random.randint(0, 2)
    comp_guess = options[rand]
    print(f"Computer guess is {comp_guess}")

    if user_input == "rock" and comp_guess == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and comp_guess == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and comp_guess == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        comp_wins += 1

print("You won", user_wins, "times!")
print("The computer won", comp_wins, "times!")
print("Good bye!")
