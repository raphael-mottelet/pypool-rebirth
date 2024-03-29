import pygame
import gameconstants

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (int(w * scale), int(h * scale)))

class Character():
   #On déclare notre méthode init 
    def __init__(self, x, y, animation_list, idle_animation):
        self.flip = False #on initialise flip en flase au début. Flip nous sert à retourner vers la gauche la même image (permet d'économiser de la place coté asset)
        self.animation_list = animation_list #attribu pour notre classe character (pour l'animation "run")
        self.idle_animation = idle_animation #attribu pour notre classe character (pour l'animation au repos)
        self.frame_index = 0
        self.idle_frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.idle_animation[0]  # On fait rentrer notre premiere frame dans le tableau pour l'animation au repos (ne marche pas)
        self.rect = pygame.Rect(0, 0, 40, 40) #Ici on définis la taille de notre box joueur. les deux derniers termes sont la largeur et la hauteur.
        self.rect.center = (x, y)
        self.animating = False  # On initialise notre animation sur false 
        self.idle_update_time = pygame.time.get_ticks()  # Nouvelle variable pour gérer l'animation au repos

        self.initial_x = x
        self.initial_y = y
        self.previous_rect = self.rect.copy()

    def draw(self, surface):
        # Ajustements pour la droite et la gauche
        if self.flip:  # Si le personnage va vers la gauche on ajuste sa position à gauche
            adjusted_position = (self.rect.x - gameconstants.DEPLACEMENT_POS_GAUCHE, self.rect.y)

        else:  # Si le personnage va vers la droite on ajuste sa position à droite
            adjusted_position = (self.rect.x - gameconstants.AJUSTEMENT_POS_DROIT, self.rect.y)

        # on ajuste avec une constante la position haut du personnage
        adjusted_position = (adjusted_position[0], adjusted_position[1] - gameconstants.AJUSTEMENT_POS_HAUT)

        # Utiliser self.flip pour décider si l'image doit être retournée ou non
        flipped_image = pygame.transform.flip(self.image, self.flip, False)

        # On dessine le personnage avec les ajustements de position, on draw la box rouge "STATIC_PLAYER_BOX" ou se trouve le sprite personnage
        surface.blit(flipped_image, adjusted_position)
        pygame.draw.rect(surface, gameconstants.STATIC_PLAYER_BOX, self.rect, 1)


    def mouvements(self, dx, dy, tile_map):

        screen_scroll = [0,0]
        if dx != 0 or dy != 0:
            dx = dx * (1 / 2) * gameconstants.SPEED  # On ajuste la vitesse pour le mouvement diagonal
            dy = dy * (1 / 2) * gameconstants.SPEED

            # Copie des coordonnées actuelles du joueur
            old_x, old_y = self.rect.x, self.rect.y

            # Met à jour les coordonnées du joueur
            self.rect.x += dx
            self.rect.y += dy

            # Vérifie s'il y a une collision avec les murs après la mise à jour des coordonnées
            if not self.is_collision_with_walls(tile_map):
                # Aucune collision, le joueur peut se déplacer
                pass
            else:
                # Collision détectée, annule le mouvement
                print("Collision detected. Player position not updated.")
                self.rect.x, self.rect.y = old_x, old_y

            # Partie qui permet d'orienter et d'inverser le sprite
            # On met à jour la valeur de flip en fonction de la direction du mouvement
            # pour pouvoir orienter une même frame du même fichier sur la gauche ou la droite
            if dx > 0:
                self.flip = False
            elif dx < 0:
                self.flip = True
            self.animating = True  # On définit l'animation à True lors du déplacement pour activer le défilement des frames du fichier
        else:
            self.animating = False  # On définit l'animation sur false et on arrête le mouvement
            self.idle_frame_index = 0  # On réinitialise idle_frame_index lors de l'arrêt du mouvement

    def is_collision_with_walls(self, tile_map): #nouvelle fonction qui règle les bugs de collision
        """
        Nouvelle fonction qui vérifie s'il y a une collision avec les murs à la nouvelle position du personnage.
        cette fonction règle le problème de collision

        Paramètres:
        - tile_map: instance de la classe TileMap

        Retourne:
        - True s'il y a collision, False sinon
        """
        # Convertis les coordonnées en indices de tuile
        tile_x = int(self.rect.x / tile_map.tile_size)
        tile_y = int(self.rect.y / tile_map.tile_size)

        # Vérifie les collisions avec les murs
        for row in range(tile_y, int((self.rect.y + self.rect.height) / tile_map.tile_size) + 1):
            for col in range(tile_x, int((self.rect.x + self.rect.width) / tile_map.tile_size) + 1):
                if tile_map.is_wall(col, row):
                    print(f"Collision with wall at ({col}, {row})")  # Ligne pour le débogage, affiche les collisions dans le terminal
                    return True  # Collision avec un mur

        return False  # Pas de collision


    def is_collision_victory(self, tile_map):
        """
        Vérifie s'il y a une collision avec la tuile de victoire à la nouvelle position du personnage.

        Paramètres:
        - tile_map: instance de la classe TileMap

        Retourne:
        - True s'il y a collision avec la tuile de victoire, False sinon
        """
        # Convertis les coordonnées en indices de tuile
        tile_x = int(self.rect.x / tile_map.tile_size)
        tile_y = int(self.rect.y / tile_map.tile_size)

        # Vérifie les collisions avec la tuile de victoire
        for row in range(tile_y, int((self.rect.y + self.rect.height) / tile_map.tile_size) + 1):
            for col in range(tile_x, int((self.rect.x + self.rect.width) / tile_map.tile_size) + 1):
                if tile_map.is_victory(col, row):  # Ajoutez une méthode is_victory à votre classe TileMap
                    print(f"Collision with victory tile at ({col}, {row})")  # Ligne pour le débogage, affiche les collisions dans le terminal
                    return True  # Collision avec la tuile de victoire

        return False  # Pas de collision avec la tuile de victoire


    def update(self):
            animation_cooldown = 70 #permet de modifier la vitesse de transition entre les animations, entre deux types de frame (mais pas visible car l'animation "IDLE" (au repos) est cassée)

            # Si le personnage est en mouvement
            if self.animating:
                if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                    self.image = self.animation_list[self.frame_index]
                    self.frame_index += 1
                    if self.frame_index >= len(self.animation_list):
                        self.frame_index = 0
                    self.update_time = pygame.time.get_ticks()

            # Si le personnage n'est pas en mouvement (mais l'animation est cassée donc ça marche pas, auccune frame ne défile)
            else:
                if pygame.time.get_ticks() - self.idle_update_time > animation_cooldown:
                    self.image = self.idle_animation[self.idle_frame_index]
                    self.idle_frame_index += 1
                    if self.idle_frame_index >= len(self.idle_animation):
                        self.idle_frame_index = 0
                    self.idle_update_time = pygame.time.get_ticks()




                """ ancinenne fonction mouvement qui posait des problèmes concernant les bugs de collision
    def mouvements(self, dx, dy):
        if dx != 0 or dy != 0:
            dx = dx * (1 / 2) * gameconstants.SPEED  # On ajuster la vitesse pour le mouvement diagonal
            dy = dy * (1 / 2) * gameconstants.SPEED

            self.rect.x += dx
            self.rect.y += dy

            # partie qui permet d'orienter et d'inverser le sprite
            # on met à jour la valeur de flip en fonction de la direction du mouvement pour pouvoir orienter une même frame du même fichier sur la gauche ou la droite
            if dx > 0:
                self.flip = False
            elif dx < 0:
                self.flip = True
            self.animating = True  # on définis l'animation à True lors du déplacement pour activer le défilement des frame du fichier
        else:
            self.animating = False  # On définis l'animation sur false et on arrete le mouvement
            self.idle_frame_index = 0  # On réinitialise idle_frame_index lors de l'arrêt du mouvement
"""