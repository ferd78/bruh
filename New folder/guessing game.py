import random

user_input = int(input("Please enter a number between 1 - 100: "))
randomint = random.randint(1,100)

while randomint != user_input:
    if randomint > user_input:
        print("Your guess was too high, Please try again!")
        user_input = int(input("Please enter a number between 1 - 100: "))
    elif randomint < user_input:
        print("Your guess was too low, Please try again!")
        user_input = int(input("Please enter a number between 1 - 100: "))
    else:
        print("Congratulations! You are correct!")
    break


