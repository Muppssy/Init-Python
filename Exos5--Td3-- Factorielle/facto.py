import random

number = random.randint(0, 100)
number1 = int(input("Devinez un nombre : "))
compteur = 5

while number != number1:
    compteur = compteur-1

    if number > number1:
        print("c'est plus, il vous reste" ,compteur)
        number1 = int(input("Devinez un nombre : "))
    if number < number1:
        print("c'est moins, c'est moins il vous reste" ,compteur)
        number1 = int(input("Devinez un nombre : "))
    if number == number1:
        print("c'est gagner")
   