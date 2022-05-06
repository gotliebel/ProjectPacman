from src.creatures import Enemies, Player
import src.settings as settings
import time
import pygame
from src.environment import env


class GamePlayFirstLevel(object):
    def __init__(self, screen, game_over, clock):
        self.game_over = game_over
        self.win = False
        self.clock = clock
        self.environment = env
        self.screen = screen
        self.player = Player(settings.WIDTH // 2, settings.HEIGHT // 2 + settings.CELL // 2, "images/player.png",
                             'images/red_heart.png', 0)
        self.enemies_group = pygame.sprite.Group()
        self.make_enemies()

    def make_enemies(self):
        for i in range(6):
            self.enemies_group.add(Enemies('images/slime.png', settings.WIDTH // 2, settings.HEIGHT // 2 - 40))

    def events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over = True

    def logic(self, player):
        hits_block = pygame.sprite.spritecollide(player, self.environment.group_dots, True)
        hits_enemy = pygame.sprite.spritecollide(player, self.enemies_group, False)
        if hits_enemy and player.lives == 0:
            player.dead = True
            for enemy in self.enemies_group:
                enemy.end_game = True
        elif hits_enemy:
            if player.lives == 3 or time.perf_counter() - player.hit_time >= 1:
                player.lives -= 1
                player.hit_time = time.perf_counter()
        player.score += len(hits_block)
        if not self.environment.group_dots:
            self.win = True
        if pygame.sprite.spritecollideany(player, self.environment.group_blocks):
            if player.difference_y < 0:
                player.rect.y -= player.difference_y
            elif player.difference_y > 0:
                player.rect.y -= player.difference_y
            elif player.difference_x > 0:
                player.rect.x -= player.difference_x
            else:
                player.rect.x -= player.difference_x
            player.difference_x = 0
            player.difference_y = 0

    def draw_result(self, phrase):
        self.screen.fill(settings.BLACK)
        text = pygame.font.SysFont('arial', 50)
        field = text.render(phrase, True, settings.GREEN)
        self.screen.blit(field,
                         (settings.WIDTH // 2 - field.get_width() / 2, settings.HEIGHT // 2 - field.get_height() / 2))

    def moment_frame(self, *args):
        self.player.update()
        self.screen.fill(settings.BLACK)
        self.enemies_group.update(*args)
        self.player.moment_image.set_colorkey((0, 0, 0))
        self.screen.blit(self.player.moment_image, self.player.rect)
        self.environment.group_dots.draw(self.screen)
        self.enemies_group.draw(self.screen)
        self.environment.group_blocks.draw(self.screen)

    def draw_moment_frame(self):
        self.moment_frame(self.player)
        text = pygame.font.SysFont('arial',
                                   self.player.moment_image.get_height())
        field = text.render("Score: " + str(self.player.score), True, settings.WHITE)
        self.screen.blit(field, (settings.WIDTH // 2 - field.get_width() / 2, 0))
        if self.win:
            self.draw_result("You won, congratulations!")
        if self.player.dead and self.player.animation_dead.moment_index == 11:
            self.draw_result("Score: " + str(self.player.score))
        pygame.display.flip()

    def run_loop(self):
        while not self.game_over:
            events = pygame.event.get()
            self.clock.tick(settings.FPS)
            self.logic(self.player)
            self.player.events_with_player(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, self.win, events)
            self.events(events)
            self.draw_moment_frame()


class GamePlayMultiplayer(GamePlayFirstLevel):
    def __init__(self, screen, game_over, clock):
        GamePlayFirstLevel.__init__(self, screen, game_over, clock)
        self.player = Player(int(settings.CELL * 2), int(settings.CELL * 1), 'images/player.png',
                             'images/red_heart.png', 3)
        self.second_player = Player(int(settings.WIDTH - settings.CELL * 2) + settings.SIZE * 4,
                                    int(settings.HEIGHT - settings.CELL * 2), 'images/player.png',
                                    'images/purple_heart.png', 3)

    def draw_moment_frame(self):
        GamePlayFirstLevel.moment_frame(self, self.player, self.second_player)
        text = pygame.font.SysFont('arial', self.player.moment_image.get_height() // 2)
        field = text.render("First Score: " + str(self.player.score), True, settings.WHITE)
        self.screen.blit(field, (settings.WIDTH // 2 - field.get_width() / 2, 10))
        text = pygame.font.SysFont('arial', self.second_player.moment_image.get_height() // 2)
        field = text.render("Second Score: " + str(self.second_player.score), True, settings.WHITE)
        self.screen.blit(field, (settings.WIDTH // 2 - field.get_width() / 2, 40))
        self.second_player.update()
        self.player.draw_lives(self.screen, 90)
        self.second_player.draw_lives(self.screen, -90)
        self.second_player.moment_image.set_colorkey((0, 0, 0))
        self.screen.blit(self.second_player.moment_image, self.second_player.rect)
        if self.win:
            if self.player.score > self.second_player.score:
                self.draw_result("First won, congratulations!")
            elif self.player.score < self.second_player.score:
                self.draw_result("Second won, congratulations!")
            else:
                self.draw_result("Draw, congratulations!")
        if self.player.dead and self.player.animation_dead.moment_index == 11:
            self.draw_result("First lost, congratulations!")
        elif self.second_player.dead and self.second_player.animation_dead.moment_index == 11:
            self.draw_result("Second lost, congratulations!")
        pygame.display.flip()

    def run_multiplayer_loop(self):
        while not self.game_over:
            events = pygame.event.get()
            self.clock.tick(settings.FPS)
            self.logic(self.player)
            self.logic(self.second_player)
            self.player.events_with_player(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, self.win, events)
            self.second_player.events_with_player(pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, self.win,
                                                  events)
            self.events(events)
            self.draw_moment_frame()
