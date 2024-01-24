import pygame
import gameconstants
from gamecharacter import Character


pygame.init()

screen = pygame.display.set_mode((gameconstants.SCREEN_WIDTH, gameconstants.SCREEN_HEIGHT))
pygame.display.set_caption("PYRAMAZE")

#on set des coordonnées pour tester notre character
x = 100
y = 100
player = Character(x, y)

#boucle principale
run = True
while run:

  player.draw(screen)

  #gère les évènements
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()