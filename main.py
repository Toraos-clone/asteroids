import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Fill the screen with black color
        screen.fill((0, 0, 0))  # RGB for black: (0, 0, 0)

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
