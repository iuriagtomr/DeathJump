import pygame

class Obstacle:

    def __init__(self, x):
        self.image = pygame.image.load("./assets/obstacle.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = 230

        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

    def draw(self, window):
        window.blit(self.image, self.rect)