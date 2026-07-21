import pygame
import sys

from logger import log_state, log_event
from shot import Shot
def main():
    pygame.init()
    from logger import log_state
    from constants import SCREEN_WIDTH, SCREEN_HEIGHT
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    print (f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = updatable
    asteroid_spawn = AsteroidField()
    player = Player((SCREEN_WIDTH/2) , (SCREEN_HEIGHT/2) )
    



    while True :
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for unit in drawable:
            unit.draw(screen)
        updatable.update(dt)
        for astrd in asteroids:
            if astrd.collides_with(player):
                log_event("player_hit")
                print ("Game Over")
                sys.exit()
            for bullet in shots:
                if astrd.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    astrd.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds
    
    




if __name__ == "__main__":
    main()


