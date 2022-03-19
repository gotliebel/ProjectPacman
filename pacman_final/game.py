import pygame
import creatures
from dots import *

WIDTH = 1080
HEIGHT = 920
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


f1 = Field(WIDTH // 2 + 150, HEIGHT // 2 + 100, 'rectangle.png')


class GamePlay(object):
    def __init__(self):
        self.game_over = False
        self.win = False
        self.player = creatures.Player(WIDTH / 2, HEIGHT / 2, "player.png")
        self.dots = pygame.sprite.Group()
        self.environment = pygame.sprite.Group()
        self.environment.add(f1)
        for i in range(0, WIDTH - 1, WIDTH // 40):
            self.dots.add(Dot(10, 10, i, 150, (0, 255, 255)))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over = True
            if self.win:
                self.player.moment_image = self.player.const_image
                self.player.difference_y = 0
                self.player.difference_x = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.move_right()
                elif event.key == pygame.K_a:
                    self.player.move_left()
                elif event.key == pygame.K_w:
                    self.player.move_up()
                elif event.key == pygame.K_s:
                    self.player.move_down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.stop_move_right()
                elif event.key == pygame.K_a:
                    self.player.stop_move_left()
                elif event.key == pygame.K_w:
                    self.player.stop_move_up()
                elif event.key == pygame.K_s:
                    self.player.stop_move_down()

    def logic(self):
        hits = pygame.sprite.spritecollide(self.player, self.dots, True)
        if hits:
            self.player.score += 1
        if not self.dots:
            self.win = True
        if pygame.sprite.spritecollideany(self.player, self.environment):
            if self.player.difference_y < 0:
                self.player.rect.y -= self.player.difference_y
            elif self.player.difference_y > 0:
                self.player.rect.y -= self.player.difference_y

            elif self.player.difference_x > 0:
                self.player.rect.x -= self.player.difference_x
            else:
                self.player.rect.x -= self.player.difference_x
            self.player.difference_x = 0
            self.player.difference_y = 0

    def moment_frame(self, screen):
        self.player.update()
        self.player.moment_image.set_colorkey(BLACK)
        screen.fill(BLACK)
        screen.blit(f1.image, f1.rect)
        self.dots.draw(screen)
        text = pygame.font.SysFont('arial',
                                   self.player.moment_image.get_height())
        field = text.render("Score: " + str(self.player.score), True, WHITE)
        screen.blit(field, (WIDTH / 2 - field.get_width() / 2, 0))
        screen.blit(self.player.moment_image, self.player.rect)
        if self.win:
            screen.fill(BLACK)
            text = pygame.font.SysFont('arial', 50)
            field = text.render("You won, congratulations!", True, WHITE)
            screen.blit(field, (WIDTH / 2 - field.get_width() / 2,
                                HEIGHT / 2 - field.get_height() / 2))
        pygame.display.flip()
