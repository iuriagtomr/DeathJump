import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("./assets/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 220

        self.velocity_y = 0
        self.gravity = 0.7
        self.jump_force = -12

        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False

    def update(self):

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # chão
        if self.rect.y >= 220:
            self.rect.y = 220
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, window):
        window.blit(self.image, self.rect)