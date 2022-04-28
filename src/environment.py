import pygame
from src.dots import Dot

WIDTH = 1080
HEIGHT = 920
LIGHTBLUE = (0, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))

    def check_point(self, point):
        return self.rect.topleft[0] <= point[0] <= self.rect.bottomright[0] and self.rect.topleft[1] <= point[1] <= \
               self.rect.bottomright[1]


class Environment(object):
    def __init__(self):
        self.group_blocks = pygame.sprite.Group()
        self.group_dots = pygame.sprite.Group()
        self.create_self()

    def create_self(self):
        self.group_blocks.add(Block(4, 168, 'blocks/verticalline.png'))
        self.group_blocks.add(Block(4, 752, 'blocks/verticalline.png'))
        self.group_blocks.add(Block(148, 4, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(752, 4, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(420, 4, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(920, 4, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(1076, 168, 'blocks/verticalline.png'))
        self.group_blocks.add(Block(1076, 752, 'blocks/verticalline.png'))
        self.group_blocks.add(Block(148, 916, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(752, 916, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(420, 916, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(920, 916, 'blocks/horizontalline.png'))
        self.group_blocks.add(Block(98, 98, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(98, 238, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(98, 822, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(982, 98, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(982, 822, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(98, 682, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(982, 238, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(982, 682, 'blocks/square100x100.png'))
        self.group_blocks.add(Block(288, 98, 'blocks/rectangle100x200.png'))
        self.group_blocks.add(Block(792, 98, 'blocks/rectangle100x200.png'))
        self.group_blocks.add(Block(288, 822, 'blocks/rectangle100x200.png'))
        self.group_blocks.add(Block(792, 822, 'blocks/rectangle100x200.png'))
        self.group_blocks.add(Block(540, 74, 'blocks/rectanglecolored.png'))
        self.group_blocks.add(Block(540, 846, 'blocks/rectanglecolored.png'))
        self.group_blocks.add(Block(74, 384, 'blocks/rectangleleft.png'))
        self.group_blocks.add(Block(74, 536, 'blocks/rectangleleft.png'))
        self.group_blocks.add(Block(1006, 384, 'blocks/rectangleright.png'))
        self.group_blocks.add(Block(1006, 536, 'blocks/rectangleright.png'))
        self.group_blocks.add(Block(213, 314, 'blocks/rectanglerightdown.png'))
        self.group_blocks.add(Block(213, 606, 'blocks/rectanglerightup.png'))
        self.group_blocks.add(Block(349, 536, 'blocks/rectangleleftbig.png'))
        self.group_blocks.add(Block(731, 536, 'blocks/rectanglerightbig.png'))
        self.group_blocks.add(Block(867, 314, 'blocks/rectangleleftdown.png'))
        self.group_blocks.add(Block(867, 606, 'blocks/rectangleleftup.png'))
        self.group_blocks.add(Block(349, 384, 'blocks/rectangleleftbig.png'))
        self.group_blocks.add(Block(731, 384, 'blocks/rectanglerightbig.png'))
        self.group_blocks.add(Block(540, 238, 'blocks/rectangledown.png'))
        self.group_blocks.add(Block(540, 616, 'blocks/halfrectangledown.png'))
        self.group_blocks.add(Block(540, 304, 'blocks/halfrectangleup.png'))
        self.group_blocks.add(Block(540, 460, 'blocks/center.png'))
        self.group_blocks.add(Block(540, 682, 'blocks/rectangleup.png'))
        for i in range(28, 388, WIDTH // 40):
            if i != 28 + WIDTH // 40 * 5:
                self.group_dots.add(Dot(10, 10, i, 28, LIGHTBLUE))
        for i in range(672, 1052, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 28, LIGHTBLUE))
        for i in range(28, 388, WIDTH // 40):
            if i != 28 + WIDTH // 40 * 5:
                self.group_dots.add(Dot(10, 10, i, 892, LIGHTBLUE))
        for i in range(699, 1050, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 892, LIGHTBLUE))
        for i in range(5, 1080, WIDTH // 40):
            if i != 5 + WIDTH // 40 * 33 and i != 5 + WIDTH // 40 * 17 and i != 5 + WIDTH // 40 * 18 and i != 5 + WIDTH // 40 * 19 and i != 5 + WIDTH // 40 * 20 and i != 5 + WIDTH // 40 * 21 and i != 5 + WIDTH // 40 * 22 and i != 5 + WIDTH // 40 * 34:
                self.group_dots.add(Dot(10, 10, i, 460, LIGHTBLUE))
        for i in range(55, 1080, WIDTH // 40):
            if i != 55 + WIDTH // 40 * 4 and i != 55 + WIDTH // 40 * 32 and i != 55 + WIDTH // 40 * 37:
                self.group_dots.add(Dot(10, 10, i, 168, LIGHTBLUE))
        for i in range(55, 1080, WIDTH // 40):
            if i != 55 + WIDTH // 40 * 4 and i != 55 + WIDTH // 40 * 32 and i != 55 + WIDTH // 40 * 37:
                self.group_dots.add(Dot(10, 10, i, 752, LIGHTBLUE))
        for i in range(290, 490, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 310, LIGHTBLUE))
        for i in range(290, 470, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 610, LIGHTBLUE))
        for i in range(617, 820, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 310, LIGHTBLUE))
        for i in range(617, 820, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 610, LIGHTBLUE))
        for i in range(28, 148, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 310, LIGHTBLUE))
        for i in range(55, 148, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 610, LIGHTBLUE))
        for i in range(927, 1080, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 310, LIGHTBLUE))
        for i in range(940, 1040, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, i, 610, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 510, 400, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 537, 400, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 564, 400, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 510, 520, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 537, 520, LIGHTBLUE))
        self.group_dots.add(Dot(10, 10, 564, 520, LIGHTBLUE))
        # #по вертикали
        for i in range(28, 280, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 28, i, LIGHTBLUE))
        for i in range(612, 870, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 28, i, LIGHTBLUE))
        for i in range(28, HEIGHT - 20, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 168, i, LIGHTBLUE))
        for i in range(28, 148, WIDTH // 40):
            self.group_dots.add((Dot(10, 10, 408, i, LIGHTBLUE)))
        for i in range(28, 148, WIDTH // 40):
            self.group_dots.add((Dot(10, 10, 672, i, LIGHTBLUE)))
        for i in range(780, 900, WIDTH // 40):
            self.group_dots.add((Dot(10, 10, 408, i, LIGHTBLUE)))
        for i in range(780, 900, WIDTH // 40):
            self.group_dots.add((Dot(10, 10, 672, i, LIGHTBLUE)))
        for i in range(55, HEIGHT - 40, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 912, i, LIGHTBLUE))
        for i in range(60, 280, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 1052, i, LIGHTBLUE))
        for i in range(612, HEIGHT - 20, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 1052, i, LIGHTBLUE))
        for i in range(195, 310, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 258, i, LIGHTBLUE))
        for i in range(610, 732, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 258, i, LIGHTBLUE))
        for i in range(195, 310, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 822, i, LIGHTBLUE))
        for i in range(610, 732, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 822, i, LIGHTBLUE))
        for i in range(310, 632, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 480, i, LIGHTBLUE))
        for i in range(310, 632, WIDTH // 40):
            self.group_dots.add(Dot(10, 10, 600, i, LIGHTBLUE))


env = Environment()