import pygame
import gameconstants
from gamecharacter import Character

pygame.init()

screen = pygame.display.set_mode((gameconstants.SCREEN_WIDTH, gameconstants.SCREEN_HEIGHT))
pygame.display.set_caption("PYRAMAZE")

#on créer une clock pour maintenir le framerate
clock = pygame.time.Clock()

#on définis les variables de mouvements pour le joueur 
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#on crée notre joueur
player = Character(100, 100)

#boucle principale qui maintien notre fenêtre
run = True
while run:

  #ici on contrôle le framerate
  clock.tick(gameconstants.FPS)

  screen.fill(gameconstants.BG)

  #on calcule les mouvements du joueur avec une suite de conditions if
  dx = 0
  dy = 0
  if moving_right:
    dx = gameconstants.SPEED
  if moving_left:
    dx = -gameconstants.SPEED
  if moving_up:
    dy = -gameconstants.SPEED
  if moving_down:
    dy = gameconstants.SPEED

  #on bouge notre joueur sur un axe X et YS
  player.move(dx, dy)

  #draw player on screen
  player.draw(screen)

  #ici on gere les evenements, par exemple si on quitte la fenetre
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #ici on prend les input pour déplacer notre joueur quand on appuie sur la touche
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:  # Q (gauche)
        moving_left = True
      if event.key == pygame.K_d:  #D (droite)
        moving_right = True
      if event.key == pygame.K_z:  # Z (haut)
        moving_up = True
      if event.key == pygame.K_s:  #S (bas)
        moving_down = True

    #ici on prend les input pour arréter de déplacer notre joueur quand il relache la touche
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_q: # Q (gauche)
        moving_left = False
      if event.key == pygame.K_d: #D (droite)
        moving_right = False
      if event.key == pygame.K_z: # Z (haut)
        moving_up = False
      if event.key == pygame.K_s: #S (bas)
        moving_down = False

  pygame.display.update()

pygame.quit()
