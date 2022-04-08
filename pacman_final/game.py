from creatures import *
from dots import *
from MeNu import *
import time

WIDTH = 1080
HEIGHT = 920
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class GamePlayFirstLevel(object):
    def __init__(self, screen, game_over):
        self.game_over = game_over
        self.win = False
        self.environment = pygame.sprite.Group()
        for block in environment_blocks:
            self.environment.add(block)
        self.screen = screen
        self.player = Player(30, 30, "player.png")
        self.dots = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.make_enemies()
        for dot in dots_array:
            self.dots.add(dot)

    def make_enemies(self):
        for i in range(8):
            self.enemies_group.add(Enemies('slime.png', 0, 0, WIDTH // 2, HEIGHT // 2))

    def events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over = True

    def logic(self, player):
        hits_block = pygame.sprite.spritecollide(player, self.dots, True)
        hits_enemy = pygame.sprite.spritecollide(player, self.enemies_group, False)
        if hits_enemy and player.lives == 0:
            player.dead = True
            for enemy in self.enemies_group:
                enemy.end_game = True
        elif hits_enemy:
            if player.lives == 3 or time.perf_counter() - player.hit_time >= 1:
                player.lives -= 1
                player.hit_time = time.perf_counter()
        if hits_block:
            player.score += 1
        if not self.dots:
            self.win = True
        if pygame.sprite.spritecollideany(player, self.environment):
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
        screen.fill(BLACK)
        text = pygame.font.SysFont('arial', 50)
        field = text.render(phrase, True, GREEN)
        self.screen.blit(field, (WIDTH / 2 - field.get_width() / 2, HEIGHT / 2 - field.get_height() / 2))

    def moment_frame(self, *args):
        self.player.update()
        self.screen.fill(BLACK)
        self.enemies_group.update(*args)
        self.player.moment_image.set_colorkey((0, 0, 0))
        self.screen.blit(self.player.moment_image, self.player.rect)
        self.dots.draw(screen)
        self.enemies_group.draw(self.screen)
        self.environment.draw(self.screen)

    def draw_moment_frame(self):
        self.moment_frame(self.player)
        text = pygame.font.SysFont('arial',
                                   self.player.moment_image.get_height())
        field = text.render("Score: " + str(self.player.score), True, WHITE)
        self.screen.blit(field, (WIDTH / 2 - field.get_width() / 2, 0))
        if self.win:
            self.draw_result("You won, congratulations!")
        if self.player.dead and self.player.animation_dead.moment_index == 11:
            self.draw_result("Score: " + str(self.player.score))
        pygame.display.flip()


class GamePlaySecondLevel(GamePlayFirstLevel):
    def __init__(self, screen, game_over):
        GamePlayFirstLevel.__init__(self, screen, game_over)
        self.player = PlayerWithLives(30, 30, 'player.png', 'red_heart.png')
        self.second_player = PlayerWithLives(WIDTH - 30, HEIGHT - 30, 'player.png', 'purple_heart.png')

    def draw_moment_frame(self):
        GamePlayFirstLevel.moment_frame(self, self.player, self.second_player)
        text = pygame.font.SysFont('arial', self.player.moment_image.get_height() // 2)
        field = text.render("First Score: " + str(self.player.score), True, WHITE)
        self.screen.blit(field, (WIDTH / 2 - field.get_width() / 2, 10))
        text = pygame.font.SysFont('arial', self.second_player.moment_image.get_height() // 2)
        field = text.render("Second Score: " + str(self.second_player.score), True, WHITE)
        self.screen.blit(field, (WIDTH / 2 - field.get_width() / 2, 40))
        self.second_player.update()
        self.player.draw_lives(self.screen, 90)
        self.second_player.draw_lives(self.screen, 45)
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



