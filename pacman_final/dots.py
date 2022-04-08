import pygame

WIDTH = 1080
HEIGHT = 920
LIGHTBLUE = (0, 255, 255)


class Dot(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, color, (width / 2, height / 2),
                           height / 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


dots_array = []
for i in range(28, 408, WIDTH // 40):
    if i != 28 + WIDTH // 40 * 5:
        dots_array.append(Dot(10, 10, i, 28, LIGHTBLUE))
for i in range(672, 1052, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 28, LIGHTBLUE))
for i in range(28, 408, WIDTH // 40):
    if i != 28 + WIDTH // 40 * 5:
        dots_array.append(Dot(10, 10, i, 892, LIGHTBLUE))
for i in range(672, 1050, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 892, LIGHTBLUE))
for i in range(5, 1080, WIDTH // 40):
    if i != 5 + WIDTH // 40 * 18 and i != 5 + WIDTH // 40 * 19 and i != 5 + WIDTH // 40 * 20 and i != 5 + WIDTH // 40 * 21 and i != 5 + WIDTH // 40 * 22 and i != 5 + WIDTH // 40 * 34:
        dots_array.append(Dot(10, 10, i, 460, LIGHTBLUE))
for i in range(55, 1080, WIDTH // 40):
    if i != 55 + WIDTH // 40 * 4 and i != 55 + WIDTH // 40 * 32 and i != 55 + WIDTH // 40 * 37:
        dots_array.append(Dot(10, 10, i, 168, LIGHTBLUE))
for i in range(55, 1080, WIDTH // 40):
    if i != 55 + WIDTH // 40 * 4 and i != 55 + WIDTH // 40 * 32 and i != 55 + WIDTH // 40 * 37:
        dots_array.append(Dot(10, 10, i, 752, LIGHTBLUE))
for i in range(290, 490, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 310, LIGHTBLUE))
for i in range(290, 490, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 610, LIGHTBLUE))
for i in range(617, 820, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 310, LIGHTBLUE))
for i in range(617, 820, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 610, LIGHTBLUE))
for i in range(28, 148, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 310, LIGHTBLUE))
for i in range(28, 148, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 610, LIGHTBLUE))
for i in range(927, 1080, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 310, LIGHTBLUE))
for i in range(927, 1080, WIDTH // 40):
    dots_array.append(Dot(10, 10, i, 610, LIGHTBLUE))
dots_array.append(Dot(10, 10, 510, 400, LIGHTBLUE))
dots_array.append(Dot(10, 10, 537, 400, LIGHTBLUE))
dots_array.append(Dot(10, 10, 564, 400, LIGHTBLUE))
dots_array.append(Dot(10, 10, 510, 520, LIGHTBLUE))
dots_array.append(Dot(10, 10, 537, 520, LIGHTBLUE))
dots_array.append(Dot(10, 10, 564, 520, LIGHTBLUE))
# #по вертикали
for i in range(28, 280, WIDTH // 40):
    dots_array.append(Dot(10, 10, 28, i, LIGHTBLUE))
for i in range(612, 870, WIDTH // 40):
    dots_array.append(Dot(10, 10, 28, i, LIGHTBLUE))
for i in range(28, HEIGHT, WIDTH // 40):
    dots_array.append(Dot(10, 10, 168, i, LIGHTBLUE))
for i in range(28, 148, WIDTH // 40):
    dots_array.append((Dot(10, 10, 408, i, LIGHTBLUE)))
for i in range(28, 148, WIDTH // 40):
    dots_array.append((Dot(10, 10, 672, i, LIGHTBLUE)))
for i in range(772, 900, WIDTH // 40):
    dots_array.append((Dot(10, 10, 408, i, LIGHTBLUE)))
for i in range(772, 900, WIDTH // 40):
    dots_array.append((Dot(10, 10, 672, i, LIGHTBLUE)))
for i in range(28, HEIGHT, WIDTH // 40):
    dots_array.append(Dot(10, 10, 912, i, LIGHTBLUE))
for i in range(28, 280, WIDTH // 40):
    dots_array.append(Dot(10, 10, 1052, i, LIGHTBLUE))
for i in range(612, HEIGHT - 20, WIDTH // 40):
    dots_array.append(Dot(10, 10, 1052, i, LIGHTBLUE))
for i in range(195, 310, WIDTH // 40):
    dots_array.append(Dot(10, 10, 258, i, LIGHTBLUE))
for i in range(610, 732, WIDTH // 40):
    dots_array.append(Dot(10, 10, 258, i, LIGHTBLUE))
for i in range(195, 310, WIDTH // 40):
    dots_array.append(Dot(10, 10, 822, i, LIGHTBLUE))
for i in range(610, 732, WIDTH // 40):
    dots_array.append(Dot(10, 10, 822, i, LIGHTBLUE))
for i in range(310, 632, WIDTH // 40):
    dots_array.append(Dot(10, 10, 480, i, LIGHTBLUE))
for i in range(310, 632, WIDTH // 40):
    dots_array.append(Dot(10, 10, 600, i, LIGHTBLUE))
