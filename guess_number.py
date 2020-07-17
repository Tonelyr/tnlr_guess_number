# Guess the number app

import random
from random import seed
from random import randint

random.seed(1) 

for number in range(1): 
    random_number = random.randint(0,20)
    #print(random_number)

user_guess = print(input("Guess the number: "))

while user_guess != random_number:
    print(input("Wrong number, try again: "))

if input == random_number:
    print("You guessed the number !")





