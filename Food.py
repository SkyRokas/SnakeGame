import pygame
import random
from Items import *


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))
