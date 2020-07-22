import random as r

random_number = r.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

guess = -1

while guess != random_number:
    guess = input("Guess the number: ")
    guess = int(guess)

    if guess > random_number:
        print("Too high, try again")
    elif guess < random_number:
        print("Too low, try again")
    else:
        print("You guessed !")
print("Bip boup, shutting down...")
