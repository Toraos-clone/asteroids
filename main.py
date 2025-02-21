# all my imports required for this project
import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroid import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # sets the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    pygame.font.init()  # Initialize the font module
    game_font = pygame.font.Font(None, 74)  # None uses default font, 74 is size

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # updates all of the update fields with 1 call
        updatable.update(dt)

        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                #display to the pygame screen as well
                game_over_text = game_font.render("Game Over!", True, (255, 0, 0))
                # Position it in center of screen
                text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                # Draw it
                screen.blit(game_over_text, text_rect)
                pygame.display.flip()  # Update the display
                # Wait for a moment so player can see the text
                pygame.time.wait(5000)  # Wait 5 seconds
                sys.exit("Game Over!")
                running = False
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
