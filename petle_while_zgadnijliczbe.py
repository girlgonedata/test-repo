print("Hello stranger!\nI'm thinking of a number between 1 and 100... Can you guess it?")
print("\nTry to guess it in as few attempts as possible...or die trying!\n")

import random

the_number = random.randint(1,100)
guess = int(input("The number is...  "))
tries = 0

#The guessing part

while guess != the_number:
    if guess > the_number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Keep guessing...  "))
    tries += 1

#When the user succeeds

print(f"Congratulations! The number was {the_number}! It took {tries} tries!")
