def bobEpargne():
    n = int(input(" entrer un nombre entre 1 et 50"))
    a = 200
    b = 0.02
    c = a*b

    for i in range(n):
        a = a + c
        c = a * b
        print("solde du compte a n +", i+1, ":", a)

bobEpargne()
 