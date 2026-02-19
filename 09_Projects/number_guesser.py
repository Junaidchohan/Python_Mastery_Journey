import random

"""
Number Guessing Game

The program:
1. Asks the user to enter the maximum range.
2. Generates a random number.
3. Keeps asking the user to guess until correct.
4. Shows how many attempts were taken.
"""

# ---------------------------------
# Step 1: Ask for maximum range
# ---------------------------------

top_of_range = input("Enter a maximum number: ")

# Check if input is a valid number
if not top_of_range.isdigit():
    print("Please enter a valid positive number next time.")
    quit()

top_of_range = int(top_of_range)

# Ensure number is greater than 0
if top_of_range <= 0:
    print("Number must be greater than 0.")
    quit()


# ---------------------------------
# Step 2: Generate random number
# ---------------------------------

random_number = random.randint(1, top_of_range)

# Counter to track number of guesses
guesses = 0


# ---------------------------------
# Step 3: Start guessing loop
# ---------------------------------

while True:
    guesses += 1

    user_guess = input("Make a guess: ")

    # Validate user input
    if not user_guess.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_guess)

    # Compare guess with random number
    if user_guess == random_number:
        print("Correct! You guessed the number.")
        break
    elif user_guess > random_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")


# ---------------------------------
# Step 4: Final result
# ---------------------------------

print("You guessed the number in", guesses, "attempts.")
