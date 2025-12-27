import pygame
import sys
from shot import Shot
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)

    AsteroidField()
    player = Player(x,y)

    while True:
        log_state() # Otomatik kontrol için gerekli

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            # ...her bir mermiyi kontrol et
            for shot in shots:
                # Çarpışma var mı?
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot") # Olayı kaydet
                    shot.kill()      # Mermiyi yok et
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        # Süre hesaplaması döngünün sonunda
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
