# loops
# Ask: roll the dice?
# If user enter y
#   generate two numbers
#   print them
# if user enter n
#   print thankyou message
# else
#   print invalid choice
import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice")
