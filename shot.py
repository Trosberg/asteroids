import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.color = (255, 255, 255)  # white bullet

    def update(self, dt):
        self.position += self.velocity * dt

        # Remove the shot if it leaves the screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)
