# gamecamera.py

import pygame
import gameconstants

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)

    def apply(self, target_rect):
        return target_rect.move(-self.camera_rect.x, -self.camera_rect.y)

    def update(self, target_rect):
        _, _, w, h = self.camera_rect

        x = -target_rect.x + gameconstants.SCREEN_WIDTH // 2
        y = -target_rect.y + gameconstants.SCREEN_HEIGHT // 2

        x = min(0, x)
        y = min(0, y)
        x = max(-(w - gameconstants.SCREEN_WIDTH), x)
        y = max(-(h - gameconstants.SCREEN_HEIGHT), y)

        self.camera_rect = pygame.Rect(x, y, w, h)

    def reset(self):
        self.camera_rect.topleft = (0, 0)
