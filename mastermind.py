import random
choixMaitreDeJeu = [0, 0, 0, 0]
choixJoueur = [""] * 4
playAgain = True
couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]
essais = 0

def generer_couleur():
    return random.sample(couleurs, 4)
def gagne():
    print("C'EST GAGNE")
    choixJoueur = [""] * 4
def perdu():
    print("NUL")
    choixJoueur = [""] * 4
def get_guess():
    guess = input(f"Entrez votre supposition {couleurs}: ")
    return guess.upper()

# collection du choix de niveau
level = ["1: T'es nul", "2: Facile", "3: Moyen", "4: Difficile", "5: Connard"]
lvl = 0

print("choisisez votre difficulté")
print(level)
choixLevel =  int(input('chiffre2: '))

# nombre d'essai a degrémenter dans la boucle que vous avez crée de votre coder
match choixLevel:
    case 1:
        essais = -1
    case 2:
        essais = 20
    case 3:
        essais = 15
    case 4:
        essais = 10
    case 5:
        essais = 5

# choix des couleur avec une boucle, pour agmenter le nombre de couleur en fonction des difficulterplayAgain = True
validationMode = True

while validationMode:

    modeDeJeu = int(input("Choisissez le mode de jeu (1 pour Mode CPU, 2 pour Mode Maître de Jeu) : "))
    if modeDeJeu in [1, 2]:
        validationMode = False
    else:
        print("Veuillez choisir 1 ou 2.")

if modeDeJeu == 1:
    choixCpu = generer_couleur()

    while essais <= 10:
        for i in range(len(choixCpu)):
            choixJoueur[i] = get_guess()
        for j in range(len(choixCpu)):
            if choixCpu[j] == choixJoueur[j]:
                print(f"L'élément {j} est indentique et au bon endroit : {choixCpu[j]} et {choixJoueur[j]}")
            else:
                print(f"L'élément {j} est différent dans les deux tableaux : {choixCpu[j]} ")
        essais += 1
        if choixJoueur == choixCpu:
            gagne()
    perdu()
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