name = input("What's Your name? ")
print(f"Welcome to the game, {name}!")

print("You are in the middle of the forest. You need to reach the city.")
direction = input("You come to a crossroad, choose left or right? (type left or right) ")

if direction == "left":
    answer = input("You come to a car, do You want to drive or go by foot? (type drive or foot) ")
    if answer == "drive":
        print("You droved to the nearest city and reached Your destination!")
    elif answer == "foot":
        print("The path is too long for You to finish on foot! Game over!")
    else:
        print("There is no such path!")
elif direction == "right":
    answer = input("You come to an old house, do You want to enter or skip and go further? (type enter or further) ")
    if answer == "enter":
        print("The spooky house is full of zombies. Game over!")
    elif answer == "further":
        answer = input("You come to a bus station, do You want to take the bus or go by foot? (type bus or foot) ")
        if answer == "bus":
            print("You came to the nearest city and reached Your destination!")
        elif answer == "foot":
            print("The path is too long for You to finish on foot! Game over!")
        else:
            print("There is no such path!")
    else:
        print("There is no such path!")
else:
    print("There is no such path!")
