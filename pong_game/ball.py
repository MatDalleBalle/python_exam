import pygame
import random

class Ball:
    def __init__(self, x, y, size, speed):
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.speed_x = random.choice([-speed, speed])
        self.speed_y = random.choice([-speed, speed])

    def update(self, width, height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-abs(self.speed_x), abs(self.speed_x)])

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        