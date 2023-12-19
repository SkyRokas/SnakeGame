import pygame
import random
from Items import *


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.body_image = pygame.image.load("snake_body.png")
        self.head_image = pygame.image.load("snake_head.png")
        self.head_image = pygame.transform.scale(self.head_image, (GRID_SIZE, GRID_SIZE))
        self.body_image = pygame.transform.scale(self.body_image, (GRID_SIZE, GRID_SIZE))
        self.images = {
            UP: pygame.transform.rotate(self.head_image, -90),
            DOWN: pygame.transform.rotate(self.head_image, 90),
            LEFT: self.head_image,
            RIGHT: pygame.transform.flip(self.head_image, True, False)
        }
        self.paused = False

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        if not self.paused:
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.paused = False

    def render(self, surface):
        for i, p in enumerate(self.positions):
            if i == 0:
                head_image = self.images.get(self.direction,
                                             self.images[(0, -1)])
                surface.blit(head_image, (p[0], p[1]))
            else:
                surface.blit(self.body_image, (p[0], p[1]))
