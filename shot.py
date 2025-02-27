from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        self.radius = SHOT_RADIUS
        super().__init__(x, y, self.radius)
        
    
    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)