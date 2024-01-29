import random
import json

# Fonction pour générer un labyrinthe avec la méthode du labyrinthe parfait
def generer_labyrinthe(lignes, colonnes):
    # Initialiser le labyrinthe avec des murs
    labyrinthe = [[1 for _ in range(colonnes)] for _ in range(lignes)]
    pile = []

    # Fonction pour vérifier si une case est valide
    def est_valide(x, y):
        return 0 <= x < colonnes and 0 <= y < lignes and labyrinthe[y][x] == 1

    # Fonction pour obtenir les cases voisines
    def obtenir_voisins(x, y):
        voisins = [(x, y - 2), (x, y + 2), (x - 2, y), (x + 2, y)]
        random.shuffle(voisins)
        return [(nx, ny) for nx, ny in voisins if est_valide(nx, ny)]

    # Fonction pour creuser un passage entre deux cases
    def creuser_passage(x, y):
        labyrinthe[y][x] = 0

    pile.append((1, 1))  # Commencer depuis une position aléatoire

    while pile:
        x, y = pile[-1]
        voisins = obtenir_voisins(x, y)

        if voisins:
            nx, ny = voisins[0]
            creuser_passage(nx, ny)
            pile.append((nx, ny))
        else:
            pile.pop()

    return labyrinthe

# Fonction pour sauvegarder le labyrinthe dans un fichier JSON
def sauvegarder_labyrinthe(labyrinthe, numero_map):
    fichier_json = f'labyrinthe_{numero_map}.json'
    with open(fichier_json, 'w') as fichier:
        json.dump(labyrinthe, fichier)
    print(f'Le labyrinthe a été sauvegardé dans {fichier_json}.')

if __name__ == "__main__":
    lignes_labyrinthe = 15
    colonnes_labyrinthe = 15

    numero_map = 1  # Initialiser le numéro de la première map

    for _ in range(5):  # ici nous avons choisis de générer au maximum 5 map 
        labyrinthe_genere = generer_labyrinthe(lignes_labyrinthe, colonnes_labyrinthe)
        sauvegarder_labyrinthe(labyrinthe_genere, numero_map)
        numero_map += 1  # Incrémenter le numéro de la map
