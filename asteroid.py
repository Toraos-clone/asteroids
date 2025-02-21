from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        # if it's already the smallest size just destroy
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # otherwise create an angle to have the parts split to
        random_angle = random.uniform(20, 50)
        # splits and goes off on opposite angles
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2= self.velocity.rotate(-random_angle)
        # determines the new size
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # creates the split asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        #sets the velocity which should be sped up a little bit
        asteroid_1.velocity = (velocity_1 * 1.2)
        asteroid_2.velocity = (velocity_2 * 1.2)



    
