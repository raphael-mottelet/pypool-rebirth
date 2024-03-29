import sys
sys.path.append("..") #cette ligne nous permet de faire des imports en dehors du repertoire
import pygame
import gameconstants
from game_character.gamecharacter import scale_img
from game_physics.gamephysics import is_collision
from game_physics.tilemap import TileMap
from game_menus.mainmenu import main_menu
from game_menus.gamemenu import game_menu
from game_menus.levelfinished import Level_finished
from game_character.initialize_player import initialize_player
from game_menus.gameoptions import *


pygame.init()

screen = pygame.display.set_mode((gameconstants.SCREEN_WIDTH, gameconstants.SCREEN_HEIGHT))
pygame.display.set_caption("PYRAMAZE")
main_menu(screen)

tile_map = TileMap(gameconstants.TILE_SIZE, "gamelevels/tilemap_data.json") #on importe notre tilemap, avec ses données en json

clock = pygame.time.Clock()

moving_left = False
moving_right = False
moving_up = False
moving_down = False



# On charge la  feuille de sprite pour l'animation au repos (mais l'animation est cassée)
idle_sprite_sheet = pygame.image.load("assets/images/characters/player/Punk_idle.png").convert_alpha()
idle_frame_width = idle_sprite_sheet.get_width() // gameconstants.NUM_IDLE_FRAMES # On Extrait les frames de la feuille de sprite pour l'animation au repos et le nombre de frame depuis la constante NUM_IDLE_FRAMES
idle_frame_height = idle_sprite_sheet.get_height()

#liste sensé importer les différentes frame pour l'animation (mais l'animation ne marche pas, probablement une erreur dans la fonction update de gamecharacter.py)
idle_animation_list = []
for i in range(gameconstants.NUM_IDLE_FRAMES):
    idle_frame = idle_sprite_sheet.subsurface((i * idle_frame_width, 0, idle_frame_width, idle_frame_height))
    idle_frame = scale_img(idle_frame, gameconstants.SCALE)
    idle_animation_list.append(idle_frame)

# On charger la feuille de sprite pour l'animation en mouvement (ouf celle la marche)
sprite_sheet = pygame.image.load("assets/images/characters/player/Punk_run.png").convert_alpha()

# On Extrait les frames de la feuille de sprite pour l'animation en mouvement, et on définis le nombre de frame grace à la constante  MOUVEMENTS_LAT_FRAMES (ici 6 frames)
frame_width = sprite_sheet.get_width() // gameconstants.MOUVEMENTS_LAT_FRAMES
frame_height = sprite_sheet.get_height()


animation_list = [] #on fait défiler dans un tableaux nos différentes frames
for i in range(gameconstants.MOUVEMENTS_LAT_FRAMES):
    frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
    frame = scale_img(frame, gameconstants.SCALE) #on importe scale img qui définis la taille de notre image de personnage
    animation_list.append(frame)

player = initialize_player(animation_list, idle_animation_list) #position initiale de notre box personnage, et import des différentes animations. On importe tout depuis notre fichier initialize player qui servira plus tard à générer des positions aléatoires du joeur.
run = True

while run:

    
    clock.tick(gameconstants.FPS)
    screen.fill(gameconstants.BG)
    
    tile_map.draw(screen) #cette condition est mise ici, de manière à ce que notre personnage soit au premier plan et non caché par la tilemap.
  #on calcule les mouvements du joueur avec une suite de conditions if

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

    # Créer un nouveau rectangle pour la nouvelle position du joueur
    new_player_rect = player.rect.move(dx, dy)

    if tile_map.is_victory_tile(player.rect.x // gameconstants.TILE_SIZE, player.rect.y // gameconstants.TILE_SIZE):
        Level_finished(screen)

    # Vérifier la collision en fonction du nouveau rectangle
    if not is_collision(tile_map, new_player_rect.x, new_player_rect.y, new_player_rect.width, new_player_rect.height):
        player.rect = new_player_rect
    else:
        # En cas de collision, on n'éffectue aucun déplacement en méttant les déplacements x et y à 0
        dx = 0 #petit problème dans cette partie du code, crée un bug qui empeche le joueur de se déplacer après quelques colisions
        dy = 0

    player.mouvements(dx, dy, tile_map)  # mouvements du joueur sur l'axe X et Y
    player.update()  # on update l'état du joueur
    player.draw(screen)  # on dessine notre joueur (carré rouge)

    # ici on gere les evenements, par exemple si on quitte la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # ici on prend les input pour dé
        # placer notre joueur quand on appuie sur la touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Q (gauche)
                moving_left = True
            if event.key == pygame.K_d:  # D (droite)
                moving_right = True
            if event.key == pygame.K_z:  # Z (haut)
                moving_up = True
            if event.key == pygame.K_s:  # S (bas)
                moving_down = True
            if event.key == pygame.K_ESCAPE:
                game_menu(screen)  # Afficher le menu pause

        # ici on prend les input pour arrêter de déplacer notre joueur quand il relache la touche
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:  # Q (gauche)
                moving_left = False
            if event.key == pygame.K_d:  # D (droite)
                moving_right = False
            if event.key == pygame.K_z:  # Z (haut)
                moving_up = False
            if event.key == pygame.K_s:  # S (bas)
                moving_down = False

    pygame.display.update()

pygame.quit()