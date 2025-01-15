import pygame
from constants import *
import random
import math


class AsteroidShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.kind = random.randint(1, ASTEROID_KINDS)
        self.points = self.generate_asteroid_points(self.radius)

    def generate_asteroid_points(self, radius):
        points = []
        for i in range(10):
            angle = i * math.pi * 2 / 10
            x = radius * math.cos(angle) + random.uniform(-radius/5, radius/5)
            y = radius * math.sin(angle) + random.uniform(-radius/5, radius/5)
            points.append((x, y))
        return points

    def draw(self, screen):
        color = ("green", "blue", "red")[self.kind - 1]
        offset_points = [(self.position.x + x, self.position.y + y) for x, y in self.points]
        pygame.draw.polygon(screen, color, offset_points, 1)

    def update(self, dt):
        self.position += self.velocity * dt

    def is_colliding(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

