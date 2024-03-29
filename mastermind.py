choixMaitreDeJeu = [0, 0, 0, 0]
choixJoueur = []
couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]

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
            