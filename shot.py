import pygame
from constants import SHOT_RADIUS
from CircleShape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt
