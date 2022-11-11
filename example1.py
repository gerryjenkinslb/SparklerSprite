from sparkler import Sparkler
import pygame

YELLOW = (255, 255, 80)
BLUE = (180, 180, 255)
RED = (255, 200, 200)
GREEN = (120, 255, 120)
BLACK = (0, 0, 0)

    
def example1():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    screen.fill(BLACK)

    all_sprites_list = pygame.sprite.Group()

    # create sprite, center on screen, and add to sprite list
    sparkler = Sparkler(800, colors=(RED, YELLOW, BLUE))
    sparkler.rect.center = screen.get_rect().center 
    all_sprites_list.add(sparkler)

    clock = pygame.time.Clock()

    # simple game loop with exit on window close
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

