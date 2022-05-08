import pygame
import src.settings as settings

pygame.init()


class Menu:
    font_menu = pygame.font.SysFont('arial', 50)

    def __init__(self, run, game_over, screen):
        self.option_surfaces = []
        self.callbacks = []
        self.screen = screen
        self._current_option_index = 0
        self.run = run
        self.run_first_level = game_over
        self.game_over = game_over
        self.create_menu()

    def append_option(self, option, callback):
        self.option_surfaces.append(
            self.font_menu.render(option, True, (255, 255, 255)))
        self.callbacks.append(callback)

    def create_menu(self):
        self.append_option('FirstLevel', lambda run_first_level, run: (not run_first_level, not run))
        self.append_option('Multiplayer', lambda run_first_level, run: (not run_first_level if run_first_level else run_first_level, not run))
        self.append_option('Quit',
                           lambda run_first_level, run, game_over: (not run_first_level, not run, not game_over))

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self.option_surfaces) - 1))

    def select(self):
        if self._current_option_index == 2:
            self.run_first_level, self.run, self.game_over = [i for i in self.callbacks[self._current_option_index](
                self.run_first_level, self.run, self.game_over)]
        else:
            self.run_first_level, self.run = self.callbacks[self._current_option_index](self.run_first_level, self.run)

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, settings.LIME, option_rect)
            surf.blit(option, option_rect)
        pygame.display.flip()

    def menu_loop(self):
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                    self.game_over = True
                    break
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_w:
                        self.switch(-1)
                    elif e.key == pygame.K_s:
                        self.switch(1)
                    elif e.key == pygame.K_SPACE:
                        self.select()
                    elif e.key == pygame.K_RETURN:
                        self.select()
                    elif e.key == pygame.K_ESCAPE:
                        self.run = False
                        self.game_over = True
                        break
            self.screen.fill(settings.MIDNIGHTBLUE)
            self.draw(self.screen, 100, 100, 75)
