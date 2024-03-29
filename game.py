import random
colors = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Brun"]

essais = 0
def generate_code():
    return random.sample(colors, 4)

def get_guess():
    guess = input(f"Entrez votre supposition {colors}: ")
    return guess.upper()

print(get_guess())

while essais <= 10:
    get_guess()