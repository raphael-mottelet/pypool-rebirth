import pygame
import gameconstants

#Grossièrement, ce code est la même chose à peut de choses près que le fichier
def Level_finished(screen):
    clock = pygame.time.Clock()
    selected_option = 0

    while True:
        screen.fill(gameconstants.BG)

        font = pygame.font.Font(None, 36)

        menu_options = ["Niveau {} validé !","Recommencer", "Quitter"]
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
                if event.key == pygame.K_UP or event.key == pygame.K_z: #Si on utilise la touche haut ou Z, alors on sélectionne vers le haut
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s: #Si on utilise la touche bas ou S, alors on sélectionne vers le BAS
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Recommencer":
                        return "restart"  # Indicate that the game needs to be restarted
                    elif menu_options[selected_option] == "Quitter":
                        pygame.quit()
                        quit()

        clock.tick(gameconstants.FPS)