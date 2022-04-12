from game import *
from MeNu import *

WIDTH = 1080
HEIGHT = 920
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
    menu = Menu(True, False)
    menu.append_option('FirstLevel', lambda run_first_level, run: (not run_first_level, not run))
    menu.append_option('Multiplayer', lambda run_first_level, run: (not run_first_level if run_first_level else run_first_level, not run))
    menu.append_option('Quit', lambda run_first_level, run, game_over: (not run_first_level, not run, not game_over))
    game_over = False
    while menu.run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                menu.run = False
                game_over = True
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
            game_over = menu.game_over
        screen.fill(MIDNIGHTBLUE)
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
    if menu.run_first_level:
        game = GamePlayFirstLevel(screen, game_over)
        while not game.game_over:
            
            events = pygame.event.get()
            clock.tick(FPS)
            game.logic(game.player)
            game.player.events_with_player(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, game.win, events)
            game.events(events)
            game.draw_moment_frame()
    else:
        game = GamePlaySecondLevel(screen, game_over)
        while not game.game_over:
            events = pygame.event.get()
            clock.tick(FPS)
            game.logic(game.player)
            game.logic(game.second_player)
            game.events(events)
            game.player.events_with_player(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, game.win, events)
            game.second_player.events_with_player(pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, game.win, events)
            game.draw_moment_frame()
    pygame.quit()

if __name__ == '__main__':
    main()
