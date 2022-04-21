def puissance():
    t = 0
    b = 1
    while t != n:
        b = b*x
        t = t + 1
        print(b)

    return b


x = int(input(" Entrer une première valeur"))
n = int(input("Entrer une seconde valeur"))

puissance()
