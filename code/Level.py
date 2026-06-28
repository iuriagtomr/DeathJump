import pygame
import random

from code.Player import Player
from code.Obstacle import Obstacle
from code import Const


class Level:

    def __init__(self, window):
        self.window = window

        self.background = pygame.image.load("./assets/background.png").convert()

        self.player = Player()

        self.obstacles = [
            Obstacle(600),
            Obstacle(900),
            Obstacle(1200)
        ]

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)

    def run(self):

        pygame.mixer_music.stop()

        clock = pygame.time.Clock()

        running = True

        while running:

            clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # Fundo
            self.window.blit(self.background, (0, 0))

            self.player.update()
            self.player.draw(self.window)

            # Score
            self.score += 1

            texto = self.font.render(f"Score: {self.score//10}", True, (255, 255, 255))
            self.window.blit(texto, (20, 20))

            for obstacle in self.obstacles:

                obstacle.update()

                if obstacle.rect.right < 0:
                    obstacle.rect.x = random.randint(700, 1000)
                    self.score += 100

                obstacle.draw(self.window)

                # Colisão
                if self.player.rect.colliderect(obstacle.rect):
                    running = False
                    break

            pygame.display.flip()

        # Saiu do loop da fase
        self.game_over()
        return

    def game_over(self):

        # Salva o maior score obtido
        if self.score // 10 > Const.HIGH_SCORE:
            Const.HIGH_SCORE = self.score // 10

        fonte = pygame.font.SysFont("Arial", 45)

        texto = fonte.render("MORREU!", True, (255, 0, 0))
        score = fonte.render(f"Score: {self.score//10}", True, (255, 255, 255))

        self.window.blit(texto, (170, 110))
        self.window.blit(score, (170, 170))

        pygame.display.flip()

        pygame.time.delay(2500)