def selec(l):
    # recherche du mini
    for i in range(len(l)-1):
        ind_val_mini = i
    # Recherche des valeurs non trié
        for j in range(i+1, len(l)):
            if l[j] < l[ind_val_mini]:
                ind_val_mini = j
    #Echange des valeurs 

        l[ind_val_mini], l[i] = l[i], l[ind_val_mini]


l = [8, 5, 1, 7, 69, 5, 4, 2, 58, 6, 87, 1, 12, 65, 74, 89, 65, 4]


print(l)

selec(l)

print(l)
