import pygame
from constants import *
import player as player_module
import asteroid as asteroid_module
import asteroidfield
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()
    dt = 0  

    player_module.Player.containers = (updatables, drawables)
    player = player_module.Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    

    Shot.containers = (shots, updatables, drawables)
    asteroid_module.Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables,)
    asteroid_field = asteroidfield.AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()
                    
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
