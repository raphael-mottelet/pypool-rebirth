import math
import pygame
import gameconstants

class Character(): #classe qui va définir le personnage
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, gameconstants.STATIC_RED, self.rect)

    def move(self, dx, dy):
        # ici on contrôle notre vitesse
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy
