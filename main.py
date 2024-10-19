import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
        
        for obj in asteroids:
            for objs in shots:
                if obj.collision(objs):
                    obj.split()
                    pygame.sprite.Sprite.kill(objs)
        
        for shot in shots:
            shot.update(dt)  
            shot.draw(screen)
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()