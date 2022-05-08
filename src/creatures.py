import time
import pygame
from src.animation import Animation
from src.environment import env
import random
import math
import src.settings as settings


class AbstractCreatures(pygame.sprite.Sprite):
    difference_x = 0
    difference_y = 0

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.const_image = pygame.image.load(image).convert()
        self.rect = self.const_image.get_rect()


class Player(AbstractCreatures):
    def __init__(self, x, y, image_filename, heart_filename, lives):
        AbstractCreatures.__init__(self, image_filename)
        self.dead = False
        self.hit_time = 0
        self.lives = lives
        self.heart = pygame.image.load(heart_filename).convert()
        self.heart.set_colorkey((0, 0, 0))
        self.moment_image = pygame.image.load(image_filename).convert()
        self.animation_dead = Animation(pygame.image.load("images/explosion.png"), 32, 32)
        self.animation_rotate_image = pygame.image.load("images/walk.png")
        self.animation_move_right = Animation(self.animation_rotate_image, 32, 32)
        self.animation_move_left = Animation(pygame.transform.rotate(self.animation_rotate_image, 180), 32, 32)
        self.animation_move_up = Animation(pygame.transform.rotate(self.animation_rotate_image, 90), 32, 32)
        self.animation_move_down = Animation(pygame.transform.rotate(self.animation_rotate_image, 270), 32, 32)
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
            if self.rect.left > int(settings.WIDTH):
                self.rect.right = 0
            elif self.rect.right < 0:
                self.rect.left = int(settings.WIDTH)
            elif self.rect.bottom < 0:
                self.rect.top = int(settings.HEIGHT)
            elif self.rect.top > int(settings.HEIGHT):
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
                self.animation_dead.update(32, 32)
            self.moment_image = self.animation_dead.moment_image

    def draw_lives(self, screen, width):
        for i in range(self.lives):
            screen.blit(self.heart,
                        self.heart.get_rect(center=(settings.WIDTH // 2 - width - 30 + 30 * i, settings.HEIGHT - 39)))

    def move_right(self):
        self.moment_image = self.const_image
        self.difference_y = 0
        self.difference_x = 4

    def move_left(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 180)
        self.difference_y = 0
        self.difference_x = -4

    def move_up(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 90)
        self.difference_x = 0
        self.difference_y = -4

    def move_down(self):
        self.moment_image = pygame.transform.rotate(self.const_image, 270)
        self.difference_x = 0
        self.difference_y = 4

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
    def __init__(self, image, x, y):
        AbstractCreatures.__init__(self, image)
        self.end_game = False
        self.change_dir_time = time.perf_counter()
        self.difference_y = 0
        self.difference_x = 0
        self.image = self.const_image
        self.image.set_colorkey((0, 0, 0))
        self.direction = ''
        self.possible_directions = ['right', 'left', 'up', 'down']
        self.rect.center = (x, y)

    def update(self, *args):
        self.make_directions()
        self.change_direction(*args)
        if self.rect.left > settings.WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = settings.WIDTH
        elif self.rect.bottom < 0:
            self.rect.top = settings.HEIGHT
        elif self.rect.top > settings.HEIGHT:
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

    def distance_to_player(self, player):
        return math.sqrt(
            (self.rect.center[0] - player.rect.center[0]) ** 2 + (self.rect.center[1] - player.rect.center[1]) ** 2)

    def make_directions(self):
        self.possible_directions = ['right', 'left', 'up', 'down']
        for block in env.group_blocks:
            if (block.check_point((self.rect.topright[0] + 7, self.rect.topright[1])) or block.check_point(
                    (self.rect.bottomright[0] + 7, self.rect.bottomright[1]))) and 'right' in self.possible_directions:
                self.possible_directions.remove('right')
            if (block.check_point((self.rect.topleft[0] - 7, self.rect.topleft[1])) or block.check_point(
                    (self.rect.bottomleft[0] - 7, self.rect.bottomleft[1]))) and 'left' in self.possible_directions:
                self.possible_directions.remove('left')
            if (block.check_point((self.rect.topleft[0], self.rect.topleft[1] - 7)) or block.check_point(
                    (self.rect.topright[0], self.rect.topright[1] - 7))) and 'up' in self.possible_directions:
                self.possible_directions.remove('up')
            if (block.check_point((self.rect.bottomleft[0], self.rect.bottomleft[1] + 7)) or block.check_point(
                    (self.rect.bottomright[0], self.rect.bottomright[1] + 7))) and 'down' in self.possible_directions:
                self.possible_directions.remove('down')
        if self.direction == 'right' and 'left' in self.possible_directions:
            self.possible_directions.remove('left')
        elif self.direction == 'left' and 'right' in self.possible_directions:
            self.possible_directions.remove('right')
        elif self.direction == 'up' and 'down' in self.possible_directions:
            self.possible_directions.remove('down')
        elif self.direction == 'down' and 'up' in self.possible_directions:
            self.possible_directions.remove('up')

    def follow_packman(self, min_distance, min_distance_player):
        self.rect.x += 2
        if self.distance_to_player(min_distance_player) < min_distance and 'right' in self.possible_directions:
            self.direction = 'right'
        self.rect.x -= 2
        self.rect.x -= 2
        if self.distance_to_player(min_distance_player) < min_distance and 'left' in self.possible_directions:
            self.direction = 'left'
        self.rect.x += 2
        self.rect.y += 2
        if self.distance_to_player(min_distance_player) < min_distance and 'down' in self.possible_directions:
            self.direction = 'down'
        self.rect.y -= 2
        self.rect.y -= 2
        if self.distance_to_player(min_distance_player) < min_distance and 'up' in self.possible_directions:
            self.direction = 'up'
        self.rect.y += 2

    def change_direction(self, *args):
        if not self.possible_directions:
            self.direction = 'up'
        elif time.perf_counter() - self.change_dir_time > 0.1 or (self.direction not in self.possible_directions):
            min_distance = self.distance_to_player(args[0])
            min_distance_player = args[0]
            for player in args:
                moment_distance = self.distance_to_player(player)
                if self.distance_to_player(player) < min_distance:
                    min_distance = moment_distance
                    min_distance_player = player
            if len(self.possible_directions) != 1 or (
                    len(self.possible_directions) == 1 and self.possible_directions[0] != self.direction):
                self.change_dir_time = time.perf_counter()
            self.direction = random.choice(self.possible_directions)
            if min_distance < 96:
                self.follow_packman(min_distance, min_distance_player)

    def distance_to_pacman_change_speed(self, *args):
        for player in args:
            distance_to_player = self.distance_to_player(player)
            if distance_to_player < 96:
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
