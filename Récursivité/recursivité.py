# -----------------------------------------#
# def som(n):
#     if n == 1:
#         s = 1
#     else:
#         s = n+som(n-1)
#     return s


# print(som(5))
# -----------------------------------------#
# def puissance(a, n):
#     if n == 0:
#         s = 1
#     else:
#         s = a*puissance(a, n-1)
#     return s

# print(puissance(10, 4))

# ---------------------------------------#
# def sommeL(l):
#     if len(l) == 0:
#         return 0
#     else:
#         return l[0] + sommeL(l[1:])


# liste = [1, 1, 1, 2, 2, 3]
# print(sommeL(liste))

# ---------------------------------------#
# Epargne de bob - Récursivité

# def epargnB(n):
#     if n == 0:
#         return 200
#     else:
#         return 1.02 * epargnB(n-1)


# print(epargnB(5))


# -----------------------------------------#
#//Récursivité - Epargne de Léa\\#

# def epargnL(L):
#     if L == 0:
#         return 200
#     else:
#         return 2*L+epargnL(L-1)


# print(epargnL(5))

# ------------------------------------------#
#//triangle rectangle\\#

# def rect(a):

#     if a == 1:
#         return "*"
#     else:
#         return rect(a+1) + "\n" + a*"*"

# print(rect(5))

# --------------------------------------------#
#//Récursivité - Somme\\#


# l = [1, 2, 3, 4, 5, 6]


# def somme(liste):

#     if len(liste) == 0:
#         return 0
#     else:
#         return liste[0]+somme(liste[1:])


# print(somme(l))
#--------------------------------------------#
#//Récursivité - Occurence\\#

# l = [1, 5, 7, 8, 8, 6, 5, 9, 2, 2, 5, 3, 3]


# def occ(liste, elt):
#     if liste == []:
#         return 0
#     if liste[0] == elt:
#         return 1+occ(liste[1:], elt)
#     else:
#         return occ(liste[1:], elt)


# print(occ(l, int(input("Entrer une valeur"))))

#--------------------------------------------#
#// Récursivité - Le Maxi \\#

# l = [1, 5, 4, 7, 87, 9, 6, 5, 4]


# def maxi(liste):

#     if liste == []:
#         return 0

#     elif liste[0] > maxi(liste[1:]):
#         return liste[0]

#     else:
#         return maxi(liste[1:])

# print(maxi(l))
#--------------------------------------------#
#//Récursivité - Le Mini\\#

# l = [1, 5, 4, 7, 87, 9, 6, 5, 4]

# def mini(liste):

#     if len(liste) == 1:
#         return liste[0]

#     elif liste[0] < mini(liste[1:]):
#         return liste[0]

#     else:
#         return mini(liste[1:])

# print(mini(l))

#--------------------------------------------#
#//Récursivité - La Moyenne\\#
l = [1, 2, 3, 4, 5, 6]

def moyenne(result):

    moyenne()
