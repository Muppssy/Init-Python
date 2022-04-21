def occ():
    a = int(input("entrez la valeur recherchée"))
    c = 0
    l = [1, 5, 7, 8, 8, 6, 9, 2, 2]
    for i in l:
        if(i == a):
            c = c+1
    print("le nombre d'ocurence de ", a, " est : ", c)


occ()
