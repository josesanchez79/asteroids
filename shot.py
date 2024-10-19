import pygame

from circleshape import CircleShape
from constants import *

#class constructor
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    #draw method for shots
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    #update method
    def update(self, dt):
        self.position += (self.velocity * dt)