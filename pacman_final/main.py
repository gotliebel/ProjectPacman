import pygame
from game import GamePlay
from menu import Menu

WIDTH = 1080
HEIGHT = 920
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MIDNIGHTBLUE = (25, 25, 112)


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PackMan")
    clock = pygame.time.Clock()
    game = GamePlay()
    menu = Menu(True, False)
    menu.append_option('Start', lambda run: not run)
    menu.append_option('Quit', lambda run, game_over: (not run, not game_over))
    while menu.run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                menu.run = False
                game.game_over = True
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    menu.switch(-1)
                elif e.key == pygame.K_s:
                    menu.switch(1)
                elif e.key == pygame.K_SPACE:
                    menu.select()
                elif e.key == pygame.K_RETURN:
                    menu.select()
            game.game_over = menu.game_over
        screen.fill(MIDNIGHTBLUE)
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
    while not game.game_over:
        clock.tick(FPS)
        game.logic()
        game.events()
        game.moment_frame(screen)
    pygame.quit()


if __name__ == '__main__':
    main()
