# Implement a guessing game where the computer generates a random
# number between 1 and 100, and the user has to guess the number.

import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"enter a number between {low}-{high}: "))
    guesses += 1
    if guess < number:
        print(f"{guess} is low")
    elif guess > number:
        print(f"{guess} is high")
    else:
        print(f"{guess} is true")
        break
print(f"this take {guesses} try")
