import random

jackpot = random.randint(1, 100)

guess = int(input("Guess karo beta:"))

counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher!")

    else:
        print("Guess Lower!")

    guess = int(input("Phirse Guess karo beta:"))

    counter += 1
    
else:
    print("Guessed The Jackpot! You won in", counter, "guesses!")