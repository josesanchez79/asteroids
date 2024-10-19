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

    #here we initialize pygame
    pygame.init()

    #screen and clock init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #creating objects 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    #setting player start position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
    #delta time variable
    dt = 0
    
    #this while is an infinite loop to keep the game running
    while True:

        #for loop to close the game when clicking on the "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #updating all updatable group
        for obj in updatable:
            obj.update(dt)

        #check if asteroids have collided with player
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
        
        #check if asteroids have collided with shots
        for obj in asteroids:
            for objs in shots:
                if obj.collision(objs):
                    obj.split()
                    pygame.sprite.Sprite.kill(objs)
        
        #for loop to shoot
        for shot in shots:
            shot.update(dt)  
            shot.draw(screen)
        
        #fills screen with black color
        screen.fill("black")

        #loops drawable to draw objects on screen
        for obj in drawable:
            obj.draw(screen)

        #updates screen
        pygame.display.flip()

        #set to have screen at max 60fps
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()