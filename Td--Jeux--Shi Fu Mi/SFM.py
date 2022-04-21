
import random
from turtle import bgcolor

# On lance la parti
#-------------------------------#

# Paramètre couleurs de texte
#-------------------------------#


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    INFO = '\033[0;36m'  # BLUE
    OTHER = '\033[0;35m'  # PURPLE
    RESET = '\033[0m'  # RESET COLOR


i = ["Pardon!!!", "Je ne peux rien batir ici.",
     "Aaalouette!!, Gentille Alouette!", "Encore du travail?", "Oui Messire!", "Oui MonSeigneur!"]

response = input("!=== COMMENCER UNE PARTI? ===!")
choice = -1
while choice != response and response != choice:

    if response == "oui":
        print(bcolors.WARNING + "on continue!" + bcolors.RESET)
        break

    elif response == "non":
        print(bcolors.FAIL + "on s'arrête!" + bcolors.RESET)
        break

    else:
        for answer in range(len(i)):
            print(random.choice(i))
            response = input(
                bcolors.FAIL + "TU VAS!!! la commencer ta parti?" + bcolors.RESET)


# On détermine le nombre de round
#-------------------------------#

init_round = int(input("Combien de round voulez vous jouer?"))
nb_round = 0

while init_round != nb_round:
    nb_round = init_round * 1
    print(bcolors.INFO + "Vous jouer pour", nb_round, "round." + bcolors.RESET)


# Choix du joueur
#-------------------------------#

choice_user = input(" choissisez entre Pierre, Feuille, Ciseaux ||")
if choice_user == "Pierre" or choice_user == "Feuille" or choice_user == "Ciseaux":
    print(bcolors.OK + "Vous avez choisi", choice_user, ".||")


# Choix de l'ordinateur Kenny
#-------------------------------#
ordi_choice = ["Pierre", "Feuille", "Ciseaux"]
ordi_select = random.choice(ordi_choice)
print(bcolors.OTHER + "Kenny à choisi", ordi_select, "." + bcolors.RESET)


# Début de l'algoritme
# On affiche toute les possibilité.
#--------------------------------#

if choice_user == ordi_select:
    print("Egalité")
elif choice_user == "Pierre" and ordi_choice == "Ciseaux":
    print("Kenny a perdu")
elif choice_user == "Feuille" and ordi_choice == "Pierre":
    print("Kenny loose")
elif choice_user == "Ciseaux" and ordi_choice == "Feuillle":
    print("Kenny")
