from Vec2 import Vec2
from Particle import Particle
import pygame

class Circle(Particle):  # Circle inherits from Particle
    def __init__(self, radius=100, **kwargs):
        self.radius = radius
        super().__init__(**kwargs)

    def draw(self, screen):
        pygame.draw.circle(screen, [0,0,0], self.pos.int(), self.radius)
    