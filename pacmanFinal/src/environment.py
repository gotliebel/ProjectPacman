import pygame
import src.settings as settings

pygame.init()
screen = pygame.display.set_mode((int(settings.WIDTH), int(settings.HEIGHT)))


class Dot(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, first_x, first_y, second_x, second_y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.CELL, settings.CELL))
        self.surf = pygame.image.load(img)
        self.surf.set_colorkey((255, 255, 255))
        self.surf = pygame.transform.scale(self.surf, (settings.SIZE * 256, settings.SIZE * 32))
        self.image.blit(self.surf, (0, 0),
                        (first_x, first_y, second_x, second_y))
        self.rect = self.image.get_rect(center=(center_x, center_y))


class Block(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, first_x, first_y, second_x,
                 second_y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.CELL, settings.CELL))
        self.surf = pygame.image.load(img)
        self.surf.set_colorkey((255, 255, 255))
        self.surf = pygame.transform.scale(self.surf, (settings.SIZE * 256, settings.SIZE * 32))
        self.image.blit(self.surf, (0, 0),
                        (first_x, first_y, second_x, second_y))
        self.rect = self.image.get_rect(center=(center_x, center_y))

    def check_point(self, point):
        return self.rect.topleft[0] <= point[0] <= self.rect.bottomright[0] and \
               self.rect.topleft[1] <= point[1] <= self.rect.bottomright[1]


file = open("map/map.txt", 'r')
map_carta = list(file)


class Environment(object):
    def __init__(self):
        self.group_blocks = pygame.sprite.Group()
        self.group_dots = pygame.sprite.Group()
        self.create_self()

    def create_self(self):
        for i in range(settings.MAP_SKETCH_WIDTH):
            for j in range(settings.MAP_SKETCH_HEIGHT):
                if map_carta[i][j] == 'o':
                    self.group_dots.add(
                        Dot(i * settings.CELL, j * settings.CELL, settings.CELL, settings.CELL, settings.CELL,
                            settings.CELL,
                            'blocks/map16.png'))

                elif map_carta[i][j] == '.':
                    try:
                        self.group_dots.add(
                            Dot(i * settings.CELL, j * settings.CELL, 0, settings.CELL, settings.CELL, settings.CELL,
                                'blocks/map16.png'))
                    except:
                        pass

                elif map_carta[i][j] == '#':
                    down = 0
                    left = 0
                    right = 0
                    up = 0
                    if j < settings.MAP_SKETCH_HEIGHT - 1:
                        if '#' == map_carta[i][1 + j]:
                            down = 1
                    if i > 0:
                        if '#' == map_carta[i - 1][j]:
                            left = 1
                    else:
                        left = 1
                    if i < settings.MAP_SKETCH_WIDTH - 1:
                        if '#' == map_carta[1 + i][j]:
                            right = 1
                    else:
                        right = 1
                    if j > 0:
                        if '#' == map_carta[i][j - 1]:
                            up = 1
                    try:

                        self.group_blocks.add(Block(i * settings.CELL, j * settings.CELL, settings.CELL * (
                                down + 2 * (left + 2 * (right + 2 * up))), 0, settings.CELL,
                                                    settings.CELL, 'blocks/map16.png'))
                    except:
                        pass


env = Environment()
