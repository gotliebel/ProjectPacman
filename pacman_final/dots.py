import pygame


class Dot(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, color, (width / 2, height / 2),
                           height / 2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
