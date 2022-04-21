int def leaEpargne():
    solde = 200
    a = int(input("age"))
    for i in range(a):
        solde = solde + i * 2
        print("année:", i, "solde:", solde)
leaEpargne()
