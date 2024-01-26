import pygame
import gameconstants

def game_menu(screen, game_screen):
    clock = pygame.time.Clock()
    selected_option = 0

    menu_surface = pygame.Surface((gameconstants.SCREEN_WIDTH // 2, gameconstants.SCREEN_HEIGHT // 2), pygame.SRCALPHA)
    menu_surface.fill((0, 0, 0, 128))  # Ajustez l'alpha selon votre préférence

    while True:
        screen.blit(game_screen, (0, 0))  # Afficher le fond du jeu

        # Afficher le menu avec transparence
        screen.blit(menu_surface, (gameconstants.SCREEN_WIDTH // 4, gameconstants.SCREEN_HEIGHT // 4))

        font = pygame.font.Font(None, 36)

        menu_options = ["Reprendre", "Quitter"]
        for i, option in enumerate(menu_options):
            text_color = (255, 255, 255)
            if i == selected_option:
                text_color = (255, 0, 0)
            text = font.render(option, True, text_color)
            text_rect = text.get_rect(center=(gameconstants.SCREEN_WIDTH // 2, 200 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Reprendre":
                        return  # Quitter le menu pour reprendre le jeu
                    elif menu_options[selected_option] == "Quitter":
                        pygame.quit()
                        quit()

        clock.tick(gameconstants.FPS)
