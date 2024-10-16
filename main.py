import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        game_over = True

if __name__ == "__main__":
    main()