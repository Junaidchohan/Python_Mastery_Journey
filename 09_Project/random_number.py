import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or type Quit: ")

    if userChoice.lower() == "quit":
        break

    if not userChoice.isdigit():
        print("Please enter a valid number.")
        continue

    userChoice = int(userChoice)

    if userChoice == target:
        print("Success: Correct Guess!")
        break
    elif userChoice < target:
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")

print("----------- Game Over -------------")