choixMaitreDeJeu = [0, 0, 0, 0]
choixJoueur = []
playAgain = True
couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]

# collection du choix de niveau
level = ["1: T'es nul", "2: Facile", "3: Moyen", "4: Difficile", "5: Connard"]
lvl = 0

print("choisisez votre difficulté")
print(level)
choixLevel =  int(input('chiffre2: '))

# nombre d'essai a degrémenter dans la boucle que vous avez crée de votre coder
match choixLevel:
    case 1:
        nombreEssai = -1
    case 2:
        nombreEssai = 20
    case 3:
        nombreEssai = 15
    case 4:
        nombreEssai = 10
    case 5:
        nombreEssai = 5

# choix des couleur avec une boucle, pour agmenter le nombre de couleur en fonction des difficulterplayAgain = True

print("Sélectionner un mode de jeu.\n1. Versus CPU\n2. Versus Player")
modeDeJeu = int(input())
if modeDeJeu == 1:
    pass # Mode CPU
elif modeDeJeu == 2:
    print("Le Maitre de Jeu doit choisir une combinaison de 4 couleurs différentes parmi les suivantes : ")
    print(couleurs)

    for i in  range(0, 4):
        while choixMaitreDeJeu[i] == 0:
            print("\nChoisissez la couleur",i+1,":")
            choix = input().capitalize()
            if choix not in choixMaitreDeJeu and choix in couleurs:
                choixMaitreDeJeu[i] = choix
            else:
                print("Veuillez choisir une couleur unique.")
    
#def verifCombinaison(choixJoueur):rouge