from animation import Animation
import pygame

WIDTH = 1080
HEIGHT = 920


class AbstractCreatures(pygame.sprite.Sprite):
    difference_x = 0
    difference_y = 0

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.const_image = pygame.image.load(image).convert()
        self.const_image.set_colorkey((0, 0, 0))
        self.rect = self.const_image.get_rect()


class Player(AbstractCreatures):
    def __init__(self, x, y, image_filename):
        AbstractCreatures.__init__(self, image_filename)
        self.moment_image = pygame.image.load(image_filename).convert()
        self.animation_rotate_image = pygame.image.load("walk.png")
        self.animation_move_right = Animation(self.animation_rotate_image, 32,
                                              32)
        self.animation_move_left = Animation(
            pygame.transform.rotate(self.animation_rotate_image, 180), 32, 32)
        self.animation_move_up = Animation(
            pygame.transform.rotate(self.animation_rotate_image, 90), 32, 32)
        self.animation_move_down = Animation(
            pygame.transform.rotate(self.animation_rotate_image, 270), 32, 32)
        self.moment_image.set_colorkey((0, 0, 0))
        self.rect.center = (x, y)
        self.score = 0

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.difference_x > 0:
            self.animation_move_right.update(32, 32)
            self.moment_image = self.animation_move_right.moment_image
        if self.difference_x < 0:
            self.animation_move_left.update(32, 32)
            self.moment_image = self.animation_move_left.moment_image
        if self.difference_y < 0:
            self.animation_move_up.update(32, 32)
            self.moment_image = self.animation_move_up.moment_image
        if self.difference_y > 0:
            self.animation_move_down.update(32, 32)
            self.moment_image = self.animation_move_down.moment_image
        self.rect.x += self.difference_x
        self.rect.y += self.difference_y

    def move_right(self):
        self.moment_image = self.const_image
        self.difference_y = 0
        self.difference_x = 3

    def move_left(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 180)
        self.difference_y = 0
        self.difference_x = -3

    def move_up(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 90)
        self.difference_x = 0
        self.difference_y = -3

    def move_down(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 270)
        self.difference_x = 0
        self.difference_y = 3

    def stop_move_right(self):
        self.moment_image = self.const_image
        self.difference_x = 0

    def stop_move_left(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 180)
        self.difference_x = 0

    def stop_move_up(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 90)
        self.difference_y = 0

    def stop_move_down(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 270)
        self.difference_y = 0
