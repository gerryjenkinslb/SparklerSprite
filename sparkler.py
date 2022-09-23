# PyGmame sparkler sprite

import pygame
import numpy as np
from random import randrange, random, choice, sample, randint
from math import pi, sin, cos

# create n gamma samples 0.0 to 1.0 for length of sparks
# with a high prob near zero tapering off fast
# see
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.gamma.html

G_SHAPE, G_SCALE = 1, .5
LEN_SAMPLES = tuple(
    v / 4 for v in np.random.gamma(G_SHAPE, G_SCALE, 2000) if v < 4)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def point_from_polar(origin, length, angle):
    x = origin[0] + length * sin(angle)
    y = origin[1] + length * cos(angle)
    return x,y


class Sparkler(pygame.sprite.DirtySprite):
    def __init__(self, size, colors=(WHITE,)):
        """Sparkler object constructor

            Args:
        size (float): size of square area sides for sparkler effect
        colors (list of colors): List of colors to choose lines from
        """

        super().__init__()

        self.radius = size / 2
        self.colors = colors
        self.image = pygame.Surface([size, size], pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(0, 0, size, size)


    # fireworks sparkler changes so fast, we create all of it every clock tick
    def update(self):
        self.dirty = 1
        self.image.fill((0,0,0,0,))
        n_spikes = randrange(50, 300)
        for _ in range(n_spikes):
            spark_len = choice(LEN_SAMPLES) * self.radius
            spark_angle = 2 * pi * random()

            # pick start inside a radiaus 1/10th total sparkler
            start_len = choice(LEN_SAMPLES) * self.radius / 10
            start_angle = 2 * pi * random()

            # convert angle and len to (x,y) tuples
            start_pt = point_from_polar((self.radius, self.radius),
                                         start_len, start_angle)
            end_pt = point_from_polar((self.radius, self.radius),
                                         spark_len, spark_angle)
            pygame.draw.line(self.image, choice(self.colors), start_pt, end_pt,
                             choice((1, 2, 3)))

            # 30% a percent of lines with secondary sparks at end from 1 to 10
            if random() < .30:  # 5% of time
                for d in sample(LEN_SAMPLES, randint(1, 10)):  # num sparks
                    d = d * self.radius / 3
                    a = 2 * pi * random()  # angle
                    e = point_from_polar(end_pt, d, a)
                    pygame.draw.line(self.image, choice(self.colors), end_pt, e,
                                     choice((1, 2, 3)))

YELLOW = (255, 255, 120)
BLUE = (220, 220, 255)
RED = (255, 220, 220)
GREEN = (120, 255, 120)

def example1():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill(BLACK)

    all_sprites_list = pygame.sprite.Group()

    sparkler = Sparkler(800, colors=(RED, YELLOW, BLUE))
    sparkler.rect.x = 0
    sparkler.rect.y = 0

    all_sprites_list.add(sparkler)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites_list.update()
        screen.fill(BLACK)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    example1()
