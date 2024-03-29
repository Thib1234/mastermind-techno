choixMaitreDeJeu = []
choixJoueur = []
choixLevel = []

couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]
level = ["T'es null", "Facil", "Moyen", "Difficile", "Connard"]

print("choisisez votre difficulté")
print(level)

print("Le Maitre de Jeu doit choisir une combinaison de 4 couleurs différentes parmi les suivantes : ")
print(couleurs)

for i in  range(0, 4):
    print("\nChoisissez la couleur",i+1,":")
    choixMaitreDeJeu.append(input())
    
#def verifCombinaison(choixJoueur):