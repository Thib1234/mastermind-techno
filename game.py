import random
couleurs = ["BLANC", "BLEU", "ROUGE", "VERT", "JAUNE", "ORANGE", "BRUN"]
choixJoueur = [""] * 4  # Initialisez la liste avec des chaînes vides

essais = 0
def generer_couleur():
    return random.sample(couleurs, 4)
def gagne():
    print("C'EST GAGNE")
    choixJoueur = [""] * 4
def perdu():
    print("NUL")
    choixJoueur = [""] * 4

choixCpu = generer_couleur()
print(choixCpu)

def get_guess():
    guess = input(f"Entrez votre supposition {couleurs}: ")
    return guess.upper()

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