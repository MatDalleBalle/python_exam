import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else: 
            self.rect.y += self.speed

    def move(self, up=True, height=600):
        if up:
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.rect.top = 0
        else:
            self.rect.y += self.speed
            if self.rect.bottom > height:
                self.rect.bottom = height

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        