import sys
sys.path.append("..")  # cette ligne nous permet de faire des imports en dehors du repertoire
import pygame
import gameconstants
from game_physics.map_generator import generer_labyrinthe
from game_menus.gameoptions import handle_options

def main_menu(screen):
    clock = pygame.time.Clock()
    selected_option = 0  # variable qui permet de suivre les choix d'options en incrémentant en fonction du choix sélectionné
    in_options = False  # Variable pour suivre si l'utilisateur est dans le sous-menu "Options"
    lignes = 19
    colonnes = 20

    # Ici on charge le logo
    logo = pygame.image.load("assets/images/menu/logo.png")  # La on charge notre logo
    logo = pygame.transform.scale(logo, (gameconstants.LOGO_WIDTH, gameconstants.LOGO_HEIGHT))  # ici on importe les constantes qui définissent la largeur et la hauteur de notre logo
    logo_rect = logo.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 100))

    while True:
        screen.fill(gameconstants.BG)
        screen.blit(logo, logo_rect)
        # Ici on dessine le texte du menu
        font = pygame.font.Font(None, 36)

        # On dessine les options du menu
        menu_options = ["Jouer", "Options", "Quitter"]  # attention, si les mots ne correspondent pas exactement à ceux des conditions if juste en dessous pour valider une sélection, l'action n'est pas détectée.
        for i, option in enumerate(menu_options):
            text_color = (255, 255, 255)  # couleur du texte dans le menu
            if i == selected_option:
                text_color = (255, 0, 0)  # Couleur différente pour l'option sélectionnée (ici du rouge)
            text = font.render(option, True, text_color)
            text_rect = text.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 300 + i * 50))  # Cette ligne définis la position du texte dans le menu
            screen.blit(text, text_rect)

        pygame.display.update()  # on update pour afficher tout ça

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z:  # Si on utilise la touche haut ou Z, alors on sélectionne vers le haut
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:  # Si on utilise la touche bas ou S, alors on sélectionne vers le BAS
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:  # si on utilise la touche entrée pour sélectionner une option dans le menu
                    if menu_options[selected_option] == "Jouer":
                        return  # On quitte la boucle pour commencer le jeu

                    elif menu_options[selected_option] == "Quitter":  # ici on quitte juste le jeux directement depuis le menu
                        pygame.quit()
                        quit()
                    elif selected_option == 1:  # Si "Options" est sélectionné
                        in_options = True
                        selected_option = 0
                        handle_options(screen, in_options, selected_option, lignes, colonnes) # Appeler la fonction de gestion des options depuis gameoptions.py
                

                    elif selected_option == 1 and in_options:  # Si "Options" est sélectionné et l'utilisateur est dans le sous-menu "Options"
                        if event.key == pygame.K_RETURN:  # si on utilise la touche entrée pour sélectionner une option dans le sous-menu "Options"
                            if selected_option == 0:  # Si "Générer Map" est sélectionné
                                generer_labyrinthe(lignes, colonnes)  # Appeler la fonction de génération de map
                                in_options = False
                            elif selected_option == 1:  # Si "Sélectionner Map" est sélectionné
                                # Ajoutez le code pour sélectionner une map ici
                                pass
                elif event.key == pygame.K_ESCAPE:  # Si la touche échappe est pressée, revenez en arrière
                    if in_options:
                        in_options = False
                        selected_option = 0
                elif event.key == pygame.K_RIGHT and in_options:  # Si l'utilisateur est dans le sous-menu "Options" et la touche droite est pressée
                    selected_option = 0
                elif event.key == pygame.K_LEFT and not in_options:  # Si l'utilisateur n'est pas dans le sous-menu "Options" et la touche gauche est pressée
                    selected_option = 1

        clock.tick(gameconstants.FPS)
