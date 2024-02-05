print("Mam na myśli pewną liczbę od 1 do 100... Czy potrafisz odgadnąć, jaką?")

import random

the_number = random.randint(1,100)
guess = int(input("Ta liczba to... "))
tries = 1

#Zgadywanie

while guess != the_number:
    if guess > the_number:
        print("Za duża!")
    else:
        print("Za mała!")

    guess = int(input("Ta liczba to... "))
    tries += 1

#Gdy uda się odgadnąć

print(f"GRATULACJE! Ta liczba to {the_number}! Odgadłeś za {tries} razem!")
