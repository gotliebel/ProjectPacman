import pygame

WIDTH = 1080
HEIGHT = 920


class Animation(object):
    def __init__(self, img, width, height):
        self.clock_counter = 1
        self.sprite_image = img
        self.image_list = []
        self.fill_image_list(width, height)
        self.moment_index = 0
        self.moment_image = pygame.Surface([width, height])
        self.moment_image.blit(img, (0, 0), (0, 0, width, height))

    def fill_image_list(self, width, height):
        for x in range(0, self.sprite_image.get_width(), width):
            for y in range(0, self.sprite_image.get_height(), height):
                image = pygame.Surface([width, height])
                image.blit(self.sprite_image, (0, 0), (x, y, width, height))
                self.image_list.append(image)

    def update(self, width, height):
        checker_time = range(0, 60, 8)
        if self.clock_counter == 60:
            self.clock_counter = 1
        else:
            self.clock_counter += 1
        if self.clock_counter in checker_time:
            self.moment_index += 1
            if self.moment_index == len(self.image_list):
                self.moment_index = 0
            self.moment_image = pygame.Surface([width, height])
            self.moment_image.blit(self.image_list[self.moment_index], (0, 0))
