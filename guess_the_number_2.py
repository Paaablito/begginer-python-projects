import random
from re import L 

def guess(x):

    feedback=""
    guessed_number = random.randint(1,x)
    while feedback != 'c':

        feedback = input(f"Is the number: {guessed_number} too low(L), too high(H) or correct(C)?: ")
        if feedback == "l" or feedback == "L":
            guessed_number += 1
        elif feedback == "h" or feedback == "H":
            guessed_number -= 1
        else:
            break
        
    print(f"You were thinking about the number {guessed_number}")


guess(10)