import pygame
import random
from circleshape import *
from constants import *

#class constructor
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    #method to handle small, medium and large asteroids
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x ,self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x ,self.position.y , new_radius)
        asteroid1.velocity = vector_1 * 1.2
        asteroid2.velocity = vector_2
        return [asteroid1, asteroid2]