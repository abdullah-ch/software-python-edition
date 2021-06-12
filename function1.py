# Guess the Number
# Python Random Module
import random

# Number of Variables
attempts = 0

# Choose a random number
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# While the player's guesses is less then 6
while attempts < 6:
    guess = input("Take a guess: ")
    guess = int(guess)

    attempts += 1

    # If the player's guess is too low
    if guess < number:
        print("Higher")

    # If the player's guess is too high
    if guess > number:
        print("Lower")

    # If the player won, stop the loop
    if guess == number:
        break

# If the player won
if guess == number:
    attempts = str(attempts)
    print(f"Good job! You guessed my number in {attempts} guesses!")

# If the player lost
if guess != number:
    number = str(number)
    print(f"Nope. The number I was thinking of was {number}")
