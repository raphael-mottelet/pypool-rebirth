import pygame
import gameconstants


pygame.init()

screen = pygame.display.set_mode((gameconstants.SCREEN_WIDTH, gameconstants.SCREEN_HEIGHT))
pygame.display.set_caption("PYRAMAZE")

#main game loop
run = True
while run:

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()