def myPass():
    m = input("Entrer votre mot de passe")
    mdp = "mdp123"
    count = 2

    while m != mdp and count > 0:
        count = count-1

        print("il vous reste", count, " essai")
        m = input("Entrer votre mot de passe")

    if m != mdp:
        print("Vous n'avez plus d'essai")

    if m == mdp:
            print("welcome")
            
myPass()