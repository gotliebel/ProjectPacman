import pygame

WIDTH = 1080
HEIGHT = 920


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))

    def check_point(self, point):
        return self.rect.topleft[0] <= point[0] <= self.rect.bottomright[0] and self.rect.topleft[1] <= point[1] <= self.rect.bottomright[1]
environment_blocks = []
environment_blocks.append(Block(4, 168, 'verticalline.png'))
environment_blocks.append(Block(4, 752, 'verticalline.png'))
environment_blocks.append(Block(148, 4, 'horizontalline.png'))
environment_blocks.append(Block(752, 4, 'horizontalline.png'))
environment_blocks.append(Block(420, 4, 'horizontalline.png'))
environment_blocks.append(Block(920, 4, 'horizontalline.png'))
environment_blocks.append(Block(1076, 170, 'verticalline.png'))
environment_blocks.append(Block(1076, 752, 'verticalline.png'))
environment_blocks.append(Block(148, 916, 'horizontalline.png'))
environment_blocks.append(Block(752, 916, 'horizontalline.png'))
environment_blocks.append(Block(420, 916, 'horizontalline.png'))
environment_blocks.append(Block(920, 916, 'horizontalline.png'))
environment_blocks.append(Block(98, 98, 'square100x100.png'))
environment_blocks.append(Block(98, 238, 'square100x100.png'))
environment_blocks.append(Block(98, 822, 'square100x100.png'))
environment_blocks.append(Block(982, 98, 'square100x100.png'))
environment_blocks.append(Block(982, 822, 'square100x100.png'))
environment_blocks.append(Block(98, 682, 'square100x100.png'))
environment_blocks.append(Block(982, 238, 'square100x100.png'))
environment_blocks.append(Block(982, 682, 'square100x100.png'))
environment_blocks.append(Block(288, 98, 'rectangle100x200.png'))
environment_blocks.append(Block(792, 98, 'rectangle100x200.png'))
environment_blocks.append(Block(288, 822, 'rectangle100x200.png'))
environment_blocks.append(Block(792, 822, 'rectangle100x200.png'))
environment_blocks.append(Block(540, 74, 'rectanglecolored.png'))
environment_blocks.append(Block(540, 846, 'rectanglecolored.png'))
environment_blocks.append(Block(74, 384, 'rectangleleft.png'))
environment_blocks.append(Block(74, 536, 'rectangleleft.png'))
environment_blocks.append(Block(1006, 384, 'rectangleright.png'))
environment_blocks.append(Block(1006, 536, 'rectangleright.png'))
environment_blocks.append(Block(213, 314, 'rectanglerightdown.png'))
environment_blocks.append(Block(213, 606, 'rectanglerightup.png'))
environment_blocks.append(Block(349, 536, 'rectangleleftbig.png'))
environment_blocks.append(Block(731, 536, 'rectanglerightbig.png'))
environment_blocks.append(Block(867, 314, 'rectangleleftdown.png'))
environment_blocks.append(Block(867, 606, 'rectangleleftup.png'))
environment_blocks.append(Block(349, 384, 'rectangleleftbig.png'))
environment_blocks.append(Block(731, 384, 'rectanglerightbig.png'))
environment_blocks.append(Block(540, 238, 'rectangledown.png'))
environment_blocks.append(Block(540, 616, 'halfrectangledown.png'))
environment_blocks.append(Block(540, 304, 'halfrectangleup.png'))
environment_blocks.append(Block(540, 460, 'center.png'))
environment_blocks.append(Block(540, 682, 'rectangleup.png'))