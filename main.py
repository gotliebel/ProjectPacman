import src.game as GAME
import pygame
import src.menu as MENU
import src.settings as settings


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("PackMan")
    clock = pygame.time.Clock()
    menu = MENU.Menu(True, False, screen)
    menu.menu_loop()
    if menu.run_first_level:
        game = GAME.GamePlayFirstLevel(screen, menu.game_over, clock)
        game.run_loop()
    else:
        game = GAME.GamePlayMultiplayer(screen, menu.game_over, clock)
        game.run_multiplayer_loop()
    pygame.quit()


if __name__ == '__main__':
    main()
