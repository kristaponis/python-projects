print("Hello, welcome to Quiz Game!")
print("The Quiz has 5 questions.")

check = True
score = 0

while check:
    play = input("Do You want to play? ").lower()
    if play == "yes":
        print("Good, let's continue!")
        check = False
        break
    elif play == "no":
        print("No? Then come back again later!")
        quit()
    else:
        print("Please enter yes or no")

print("Please give answers yes or no.")
print()

answer1 = input("Question 1. Is Python a programing language? ").lower()
if answer1 == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("Question 2. Is Python a compiled language? ").lower()
if answer2 == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("Question 3. Does Python have automatic garbage collection? ").lower()
if answer3 == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("Question 4. Is Python a weakly typed (loosely typed) language? ").lower()
if answer4 == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("Question 5. Was Python first released in 1991? ").lower()
if answer5 == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

if score == 0:
    print("You answered " + str(score) + " questions out of 5! Oh my, try harder next time!")
elif score == 1:
    print("You answered " + str(score) + " question out of 5! Hmm, only one correct answer..")
elif score == 2:
    print("You answered " + str(score) + " questions out of 5! Not bad, but try harder!")
elif score == 3:
    print("You answered " + str(score) + " questions out of 5! Good job! Average score!")
elif score == 4:
    print("You answered " + str(score) + " questions out of 5! Almost perfect!")
elif score == 5:
    print("You answered " + str(score) + " questions out of 5! Perfect! Well done!")
