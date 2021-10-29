import random

print("*** Let the Guess A Number game begin! ***")
print("You need to specify a number, which")
print("will be used to set number boundaries for the game.")

max_range = input("Type a number greater than zero: ")

if max_range.isdigit():
    max_range = int(max_range)
else:
    print("Type a number next time!")
    quit()

rand = random.randrange(1, max_range)
guesses = 0

while True:
    user_number = input("Guess the number: ")
    guesses += 1

    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("Type a number next time!")
        continue

    if user_number == rand:
        print("Correct!")
        break
    else:
        if user_number > rand:
            print("Your guess is above the right number!")
        elif user_number < rand:
            print("Your guess is below the right number!")

print("You got it in", guesses, "guesses!")
