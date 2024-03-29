import random

couleurs = ["BLANC", "BLEU", "ROUGE", "VERT", "JAUNE", "ORANGE", "BRUN"]

def generer_couleur():
    return random.sample(couleurs, 4)

def reset_jeu():
    return [""] * 4, 0

def gagne():
    print("C'EST GAGNE")
    return reset_jeu()

def perdu():
    print("NUL")
    return reset_jeu()

def get_guess():
    guess = input(f"Entrez votre supposition {couleurs}: ")
    return guess.upper()

def game():
    choixCpu = generer_couleur()
    print(choixCpu)

    choixJoueur, essais = reset_jeu()

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
            choixJoueur, essais = gagne()
    perdu()

# Pour lancer le jeu, il suffit d'appeler la fonction game
game()
