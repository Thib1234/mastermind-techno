choixMaitreDeJeu = []
choixJoueur = []


couleurs = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]
level = ["1: T'es null", "2: Facile", "3: Moyen", "4: Difficile", "5: Connard"]

lvl = 0

print("choisisez votre difficulté")
print(level)
choixLevel =  int(input('chiffre2: '))


print("Le Maitre de Jeu doit choisir une combinaison de 4 couleurs différentes parmi les suivantes : ")
print(couleurs)

while lvl < (choixLevel+1):
    
    lvl += 1
    pass

for i in  range(0, 4):
    print("\nChoisissez la couleur",i+1,":")
    choixMaitreDeJeu.append(input())
    
#def verifCombinaison(choixJoueur):