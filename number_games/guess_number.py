# Guess the Number Game
# The user has to guess a number chosen by the program

import random

print("GUESS THE NUMBER GAME\n")

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🎉 Congratulations! You guessed it right.")
else:
    print("❌ Wrong guess.")
    print("The correct number was:", secret_number)
