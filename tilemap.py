import pygame
import gameconstants
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

                if tile_id == 1:  # Wall
                    surface.blit(self.wall_image, rect)
                elif tile_id == 0:  # Ground
                    surface.blit(self.ground_image, rect)
