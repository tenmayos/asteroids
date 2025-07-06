import pygame
import random
import circleshape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.d, self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            random_angle = random.uniform(20, 50)
            rotation_a = self.velocity.rotate(random_angle)
            rotation_b = self.velocity.rotate(-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.x, self.y, self.radius)
            asteroid2 = Asteroid(self.x, self.y, self.radius)
            asteroid1.velocity = rotation_a * 1.2
            asteroid2.velocity = rotation_b * 1.2
