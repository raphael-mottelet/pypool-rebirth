import sys
sys.path.append("..") #cette ligne nous permet de faire des imports en dehors du repertoire
import pygame
import gameconstants
from game_physics.map_generator import generer_labyrinthe
def handle_options(screen, in_options, selected_option):
    clock = pygame.time.Clock()


    #ce fichier est grossierement un gros copié collé des autres menus, la différence resulte juste en les imports de la génération de map.

    while in_options:
        screen.fill(gameconstants.BG)

        font = pygame.font.Font(None, 36)
        sub_options = ["Générer Map", "Sélectionner Map"]

        for i, sub_option in enumerate(sub_options):
            text_color = (255, 255, 255)
            if i == selected_option:
                text_color = (255, 0, 0)
            text = font.render(sub_option, True, text_color)
            text_rect = text.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 300 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z:
                    selected_option = (selected_option - 1) % len(sub_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected_option = (selected_option + 1) % len(sub_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Si "Générer Map" est sélectionné
                        generer_labyrinthe()  # Appeler la fonction de génération de map
                    elif selected_option == 1:  # Si "Sélectionner Map" est sélectionné
                        # Ajoutez le code pour sélectionner une map ici
                        pass
                elif event.key == pygame.K_ESCAPE:
                    return  # Revenir au menu principal

        clock.tick(gameconstants.FPS)
