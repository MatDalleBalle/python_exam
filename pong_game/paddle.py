import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        self.rect.y -= self.speed
    
    def move_down(self, boundary):
        if self.rect.bottom + self.speed <= boundary:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        