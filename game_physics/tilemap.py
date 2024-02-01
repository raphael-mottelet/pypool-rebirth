import pygame
import json

class TileMap:

    def __init__(self, tile_size, map_file):
        # On initialise la carte avec la taille des tuiles et les données de la carte
        self.tile_size = tile_size
        self.map_data = self.load_map_data(map_file)
        self.width = len(self.map_data[0]) * tile_size
        self.height = len(self.map_data) * tile_size
        # On charge et redimensionne les images
        self.wall_image = pygame.transform.scale(pygame.image.load("assets/images/tilemap/wall.png"), (tile_size, tile_size))
        self.ground_image = pygame.transform.scale(pygame.image.load("assets/images/tilemap/ground.png"), (tile_size, tile_size))
        self.victorytile_image = pygame.transform.scale(pygame.image.load("assets/images/tilemap/victorytile.png"), (tile_size, tile_size))

    def load_map_data(self, map_file):
        # On charge les données de la carte à partir du fichier JSON qui contient notre map
        with open(map_file, 'r') as file:
            return json.load(file)

    def draw(self, surface):
        # Parcours de chaque tuile dans les données de la carte
        for row_index, row in enumerate(self.map_data):
            for col_index, tile_id in enumerate(row):
                # On Calcule des coordonnées x et y de la tuile en fonction de sa position dans la matrice
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                # On crée un rectangle représentant la tuile
                rect = pygame.Rect(x, y, self.tile_size, self.tile_size)

                if tile_id == 1:  # Murs (les 1 matrice), en gros si c'est le cas on charge l'asset correspondant, pareil pour les conditions suivantes
                    surface.blit(self.wall_image, rect)
                if tile_id == 0:  # Sol (les 0 de la matrice)
                    surface.blit(self.ground_image, rect)
                elif tile_id == 4:  # tuilde de la voctoire (4 sur la matrice)
                    surface.blit(self.victorytile_image, rect)

    def is_victory_tile(self, col, row):
        """
        Vérifie si la tuile à la position (col, row) est la tuile de victoire (avec le gros V vert).

        Paramètres:
        - col, row: indices de la tuile

        Retourne:
        - True si la tuile est la tuile de victoire, False sinon
        """
        if 0 <= col < len(self.map_data[0]) and 0 <= row < len(self.map_data):
            return self.map_data[row][col] == 4
        else:
            return False

    def is_wall(self, col, row):
        """
        Vérifie si la tuile à la position (col, row) est un mur.

        Parametres:
        - col, row: indices de la tuile

        Retourne:
        - True si la tuile est un mur, False sinon
        """
        # on vérifie que les lignes et les colonnes sont dans la limite de la carte
        if 0 <= col < len(self.map_data[0]) and 0 <= row < len(self.map_data):
            # Si la valeur dans map_data à la position (col, row) est 1, c'est un mur
            return self.map_data[row][col] == 1
        else:
            # En dehors des limites de la carte, considérons cela comme un mur
            return True