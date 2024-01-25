FPS = 60 #images par secondes du jeux
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800


STATIC_PLAYER_BOX = (255, 0, 0) #on définis la couleur de notre box de référence pour le personnage
STATIC_TILE_GRID = (0, 255, 0)  # Remplacez cela par la couleur que vous souhaitez utiliser
BG = (40, 25, 25) #on définis la couleur du background

MOUVEMENTS_LAT_FRAMES = 6  # On ajuste le nombre de frame à display en fonction du nombre compris dans le .png (ici 6 frames)
NUM_IDLE_FRAMES = 4 # ici on ajuste par rapport au nombre de frame du fichier .png pour l'animation de repos (mais l'animation de repos ne marche pas)
SCALE = 2  # On ajuste la taille de nos frame
TILE_SIZE = 40* SCALE # on set la taille de nos tuiles en fonction de la taille totale

SPEED = 3  #on ajuste la vitesse du personnage
AJUSTEMENT_POS_DROIT = 5 # On ajuste le positionement de notre personnage par rapport à la box de référence (à droite)
DEPLACEMENT_POS_GAUCHE= 52 # On ajuste le positionement de notre personnage par rapport à la box de référence (à gauche)
AJUSTEMENT_POS_HAUT = 45 # On ajuste le positionement de notre personnage par rapport à la box de référence (en haut)