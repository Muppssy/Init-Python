

number = random.randint(0, 20)
number1 = -1
essai = 0

while (number1 != number):

    essai = essai + 1

    number1 = int(input(" Entre un nombre"))

    if number1 < number:
        print("c'est plus.")

    if number1 > number:
        print("c'est moins.")

    if number1 == number:
        print("Bien Joué!!")
        print("Vous avez fini le jeu en", essai, "tentative !")

    else:
        print("Recommencer")
