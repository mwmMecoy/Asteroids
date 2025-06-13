from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Asteroids can also have a rotation if needed

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20, 50)

        new_velocity1 = self.velocity.rotate(angle)
        new_velocity2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 / 1.2