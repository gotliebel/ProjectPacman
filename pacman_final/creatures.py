import time

from animation import Animation
from environment import *
import random
import math

WIDTH = 1080
HEIGHT = 920


class AbstractCreatures(pygame.sprite.Sprite):
    difference_x = 0
    difference_y = 0

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.const_image = pygame.image.load(image).convert()
        self.rect = self.const_image.get_rect()


class Player(AbstractCreatures):
    def __init__(self, x, y, image_filename):
        AbstractCreatures.__init__(self, image_filename)
        self.dead = False
        self.lives = 0
        self.moment_image = pygame.image.load(image_filename).convert()
        self.animation_dead = Animation(pygame.image.load("explosion.png"), 30, 30)
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

    def events_with_player(self, button_up, button_left, button_down, button_right, win, events):
        for event in events:
            if win:
                self.moment_image = self.const_image
                self.difference_y = 0
                self.difference_x = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == button_right:
                    self.move_right()
                elif event.key == button_left:
                    self.move_left()
                elif event.key == button_up:
                    self.move_up()
                elif event.key == button_down:
                    self.move_down()
            if event.type == pygame.KEYUP:
                if event.key == button_right:
                    self.stop_move_right()
                elif event.key == button_left:
                    self.stop_move_left()
                elif event.key == button_up:
                    self.stop_move_up()
                elif event.key == button_down:
                    self.stop_move_down()

    def update(self):
        if not self.dead:
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
        else:
            if self.animation_dead.moment_index == 10:
                self.animation_dead.moment_index = 11
            if self.animation_dead.moment_index < 11:
                self.animation_dead.update(30, 30)
            self.moment_image = self.animation_dead.moment_image

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


class Enemies(AbstractCreatures):
    def __init__(self, image, move_x, move_y, x, y):
        AbstractCreatures.__init__(self, image)
        self.end_game = False
        self.change_dir_time = time.perf_counter()
        self.difference_y = move_y
        self.difference_x = move_x
        self.image = self.const_image
        self.image.set_colorkey((0, 0, 0))
        if move_x >= 0 and move_y == 0:
            self.direction = 'right'
        if move_x < 0 and move_y == 0:
            self.direction = 'left'
        if move_y >= 0 and move_x == 0:
            self.direction = 'down'
        if move_y < 0 and move_x == 0:
            self.direction = 'up'
        self.possible_directions = ['right', 'left', 'up', 'down']
        self.rect.center = (x, y)

    def update(self, *args):
        self.make_directions()
        self.change_direction()
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if not self.end_game:
            if self.direction == 'right':
                self.move_right()
            elif self.direction == 'left':
                self.move_left()
            elif self.direction == 'down':
                self.move_down()
            elif self.direction == 'up':
                self.move_up()
        else:
            self.difference_x = 0
            self.difference_y = 0
        self.distance_to_pacman_change_speed(*args)
        self.rect.x += self.difference_x
        self.rect.y += self.difference_y

    def make_directions(self):
        self.possible_directions = ['right', 'left', 'up', 'down']
        for block in environment_blocks:
            if (block.check_point((self.rect.topright[0] + 7, self.rect.topright[1])) or block.check_point((self.rect.bottomright[0] + 7, self.rect.bottomright[1]))) and 'right' in self.possible_directions:
                self.possible_directions.remove('right')
            if (block.check_point((self.rect.topleft[0] - 7, self.rect.topleft[1])) or block.check_point((self.rect.bottomleft[0] - 7, self.rect.bottomleft[1]))) and 'left' in self.possible_directions:
                self.possible_directions.remove('left')
            if (block.check_point((self.rect.topleft[0], self.rect.topleft[1] - 7)) or block.check_point((self.rect.topright[0], self.rect.topright[1] - 7))) and 'up' in self.possible_directions:
                self.possible_directions.remove('up')
            if (block.check_point((self.rect.bottomleft[0], self.rect.bottomleft[1] + 7)) or block.check_point((self.rect.bottomright[0], self.rect.bottomright[1] + 7))) and 'down' in self.possible_directions:
                self.possible_directions.remove('down')

    def change_direction(self):
        if not self.possible_directions:
            self.direction = 'up'
        elif time.perf_counter() - self.change_dir_time > 0.1 or (self.direction not in self.possible_directions):
            if self.direction == 'right':
                if 'left' in self.possible_directions:
                    self.possible_directions.remove('left')
            elif self.direction == 'left':
                if 'right' in self.possible_directions:
                    self.possible_directions.remove('right')
            elif self.direction == 'up':
                if 'down' in self.possible_directions:
                    self.possible_directions.remove('down')
            elif self.direction == 'down':
                if 'up' in self.possible_directions:
                    self.possible_directions.remove('up')
            self.direction = random.choice(self.possible_directions)
            self.change_dir_time = time.perf_counter()

    def distance_to_pacman_change_speed(self, *args):
        for player in args:
            distance_to_player = math.sqrt((self.rect.center[0] - player.rect.center[0]) ** 2 + (self.rect.center[1] - player.rect.center[1]) ** 2)
            if distance_to_player < 128:
                self.difference_x *= 1.5
                self.difference_y *= 1.5

    def move_right(self):
        self.image = self.const_image
        self.difference_y = 0
        self.difference_x = 2

    def move_left(self):
        self.image = pygame.transform.flip(self.const_image, True, False)
        self.difference_y = 0
        self.difference_x = -2

    def move_up(self):
        self.difference_x = 0
        self.difference_y = -2

    def move_down(self):
        self.difference_x = 0
        self.difference_y = 2


class PlayerWithLives(Player):
    def __init__(self, x, y, image_filename, heart_filename):
        Player.__init__(self, x, y, image_filename)
        self.hit_time = 0
        self.lives = 3
        self.heart = pygame.image.load(heart_filename).convert()
        self.heart.set_colorkey((0, 0, 0))

    def draw_lives(self, screen, height):
        for i in range(self.lives):
            screen.blit(self.heart, self.heart.get_rect(center=(WIDTH // 2 - 30 + 30 * i, HEIGHT - height)))




