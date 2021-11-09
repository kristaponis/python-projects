import random
from hangman_art import *

word_list = ["lithuania", "latvia", "estonia", "poland", "sweden", "belarus"]
guessed_letters = []
remaining_guesses = 6
mistakes = 0
word_index = random.randint(0, len(word_list) - 1)
word = word_list[word_index].upper()

def game_status():
    if mistakes == 0:
        no_mistake()
    elif mistakes == 1:
        mistake_one()
    elif mistakes == 2:
        mistake_two()
    elif mistakes == 3:
        mistake_three()
    elif mistakes == 4:
        mistake_four()
    elif mistakes == 5:
        mistake_five()
    elif mistakes == 6:
        game_over()
    
    print("Your word: ", end="")
    for ltr in guessed_letters:
        print(f"{ltr} ", end="")
    print(f"\nGuesses left: {remaining_guesses}")

for i in range(len(word)):
        guessed_letters.append("-")

while True:
    game_status()
    user_letter = input("Enter a letter: ")
    if not user_letter:
        print("Input not valid! Try again!")
    else:
        letter = user_letter[0].upper()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_letters[i] = letter
            if "-" not in guessed_letters:
                break
        else:
            print("There is no such letter in this word!")
            print("Try again!")
            remaining_guesses -= 1
            mistakes += 1
            if mistakes == 6:
                break

if mistakes == 6:
    game_status()
    print(f"You Lost!")
    print(f"The word was {word}!")
else:
    print("You Won!")
    