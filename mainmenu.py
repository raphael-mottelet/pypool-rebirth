import pygame
import gameconstants

def main_menu(screen):
    clock = pygame.time.Clock()
    selected_option = 0  # Ajout d'une variable pour suivre l'option sélectionnée

        # Ici on charge le logo
    logo = pygame.image.load("assets/images/menu/logo.png") #La on charge notre logo
    logo = pygame.transform.scale(logo, (gameconstants.LOGO_WIDTH, gameconstants.LOGO_HEIGHT)) #ici on importe les constantes qui définissent la largeur et la hauteur de notre logo
    logo_rect = logo.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 100))

    while True:
        screen.fill(gameconstants.BG)
        screen.blit(logo, logo_rect)
        # Dessinez le texte du menu
        font = pygame.font.Font(None, 36)

        # Dessinez les options du menu
        menu_options = ["Jouer", "Options", "Quitter"] #attention, si les mots ne correspondent pas exactement à ceux des conditions if juste en dessous pour valider une seletion, l'action n'est pas détectée.
        for i, option in enumerate(menu_options):
            text_color = (255, 255, 255) # couleur du texte dans le menu 
            if i == selected_option:
                text_color = (255, 0, 0)  # Couleur différente pour l'option sélectionnée (ici du rouge)
            text = font.render(option, True, text_color)
            text_rect = text.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 300 + i * 50)) # Cette ligne définis la position du texte dans le menu
            screen.blit(text, text_rect)

        pygame.display.update() #on update pour afficher tout ça

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z: #Si on utilise la touche haut ou Z, alors on sélectionne vers le haut
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s: #Si on utilise la touche bas ou S, alors on sélectionne vers le BAS
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN: #si on utilise la touche entrée pour selectionner une option dans le menu
                    if menu_options[selected_option] == "Jouer":
                        return  # On quitte la boucle pour commencer le jeu
                    elif menu_options[selected_option] == "Options":
                        # Ici on apelle la fonction des options du menu
                        pass
                    elif menu_options[selected_option] == "Quitter": #ici on quitte juste le jeux directement depuis le menu
                        pygame.quit()
                        quit()

        clock.tick(gameconstants.FPS)

