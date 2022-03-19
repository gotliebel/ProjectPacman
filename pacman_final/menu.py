import pygame

pygame.init()

WIDTH = 1080
HEIGHT = 920
font_menu = pygame.font.SysFont('arial', 50)
BLACK = (0, 0, 0)
MIDNIGHTBLUE = (25, 25, 112)
LIME = (0, 255, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Menu:
    def __init__(self, run, game_over):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
        self.run = run
        self.game_over = game_over

    def append_option(self, option, callback):
        self._option_surfaces.append(
            font_menu.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0,
                                         min(self._current_option_index + direction,
                                             len(self._option_surfaces) - 1))

    def select(self):
        if self._current_option_index == 1:
            self.run, self.game_over = [i for i in self._callbacks[self._current_option_index](self.run, self.game_over)]
        else:
            self.run = self._callbacks[self._current_option_index](self.run)

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, LIME, option_rect)
            surf.blit(option, option_rect)
