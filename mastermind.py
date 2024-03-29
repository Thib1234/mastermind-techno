# yaouuuuu
choixMaitreDeJeu = []
choixJoueur = []


couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]
# collection du choix de niveau
level = ["1: T'es null", "2: Facile", "3: Moyen", "4: Difficile", "5: Connard"]
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

# choix des couleur avec une boucle, pour agmenter le nombre de couleur en fonction des difficulter
print("Le Maitre de Jeu doit choisir une combinaison de 4 couleurs différentes parmi les suivantes : ")
print(couleurs)

while lvl < (choixLevel+1):
    
    lvl += 1
    pass
