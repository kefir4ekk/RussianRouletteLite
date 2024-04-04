import time
import os
import random

print("Hi traveler, this is a game Guess the Number! But it will be Russian Roulette")
print("The rules are simple: If you guess, everything will be fine and if you don't guess, your system will be turned off (because this is the lite version of this game)")
guess = int(input("- "))
guess1 = random.randint(1,3)
i = 5

if guess == guess1:
    print("You won!")
else:
    print("You lose. System will be turned off in ")
    b = 'True'
    while b == 'True':
        print(i, "seconds")
        time.sleep(1)
        i = i - 1
        if i == 0:
            print("System turned off hahaha")
            os.system('shutdown /s /t 1')
            break