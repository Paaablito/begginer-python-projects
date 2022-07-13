import random

def randd(x):

    random_number = random.randint(1,x)

    while True:
        y = int(input("Podaj liczbe: "))
        if y > random_number:
            print("Nie trafiles, liczba jest za duza")
        if y < random_number:
            print("Nie trafiles, liczba jest za mala ")
        elif y == random_number:
            print(f"Gratulacje, trafiles :) Szukana liczba: {random_number}")
            break

randd(10)
