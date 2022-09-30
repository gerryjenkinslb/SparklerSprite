from sparkler import Sparkler, point_from_polar
import pygame
import math

YELLOW = (255, 255, 120)
BLUE = (200, 200, 255)
RED = (255, 100, 100)
GREEN = (120, 255, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# moving sparklers

class CirclingSparkler(Sparkler):
    # These sparklers move in circle with radius 
    # starting at start_angle from screen origin point
    # and moves around circle at speed radians change per tick
    def __init__(self, size, colors, origin, radius, 
                                         speed=2*math.pi/250, start_angle=0.0):
        """CirclingSparkler object constructor

                    Args:
                size (float): size of square area sides for sparkler effect
                colors (list of colors): List of colors to choose lines from
                screen origin: center of sparkler rotation in screen coordinates
                radius: how far out to circle
                speed: radians per tick to move in circle
                start_angle: the initial position on the circle of spin
                """
        super().__init__(size, colors)
        self.angle = start_angle
        self.speed = speed
        self.spin_radius = radius
        self.origin = origin

        # set initial screen coordinate center of sparkler
        self.rect.center = point_from_polar(self.origin, 
                                         self.spin_radius, self.angle)

    def update(self): # on each tick, rotate around
        self.angle += self.speed
        self.rect.center = point_from_polar(self.origin, 
                                         self.spin_radius, self.angle)
        super().update()


def example2():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill(BLACK)

    all_sprites_list = pygame.sprite.Group()

    # 3 sparklers each with different circle and colors. 
    # note #2 move anti-clockwise
    sparkler1 = CirclingSparkler(500, (RED, YELLOW, BLUE), (400, 500), 200)
    sparkler2 = CirclingSparkler(500, (RED, ), (500, 600), 150, 
                                                      speed=-2*math.pi/500)
    sparkler3 = CirclingSparkler(500, (BLUE, YELLOW,), (500, 500), 100, 
                        speed=2*math.pi/500, start_angle=2*math.pi/4)

    all_sprites_list.add((sparkler1, sparkler2, sparkler3,))

    clock = pygame.time.Clock()

    running = True

    i = 0
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
    example2()
