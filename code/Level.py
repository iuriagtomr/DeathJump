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
        self.level = 1
        self.next_level = 100

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

            # Jogador
            self.player.update()
            self.player.draw(self.window)

            # Pontuação
            self.score += 1
            pontos = self.score // 10

            texto = self.font.render(
                f"Score: {pontos}",
                True,
                (255, 255, 255)
            )
            self.window.blit(texto, (20, 20))

            # Nível atual
            texto_nivel = self.font.render(
                f"Nível: {self.level}",
                True,
                (255, 255, 0)
            )
            self.window.blit(texto_nivel, (20, 55))

            # Passagem de nível a cada 100 pontos
            if pontos >= self.next_level:

                self.level += 1
                self.next_level += 100

                # aumenta velocidade dos obstáculos
                for obstacle in self.obstacles:
                    obstacle.speed += 1

                self.level_up()

            # Obstáculos
            for obstacle in self.obstacles:

                obstacle.update()

                if obstacle.rect.right < 0:
                    # Encontra o obstáculo mais à frente
                    maior_x = max(obs.rect.x for obs in self.obstacles)

                    # Reposiciona mantendo uma distância segura
                    obstacle.rect.x = maior_x + random.randint(280, 450)

                    self.score += 100

                obstacle.draw(self.window)

                # Colisão
                if self.player.rect.colliderect(obstacle.rect):
                    running = False
                    break

            pygame.display.flip()

        self.game_over()

        # Espera o jogador soltar todas as teclas
        while any(pygame.key.get_pressed()):
            pygame.event.pump()

        pygame.event.clear()

    def level_up(self):

        fonte = pygame.font.SysFont("Arial", 45)

        texto = fonte.render(
            f"NÍVEL {self.level}",
            True,
            (0, 255, 0)
        )

        clock = pygame.time.Clock()

        inicio = pygame.time.get_ticks()

        while pygame.time.get_ticks() - inicio < 1500:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.blit(self.background, (0, 0))
            self.window.blit(texto, (150, 140))

            pygame.display.flip()

            clock.tick(60)

    def game_over(self):

        # Atualiza recorde
        if self.score // 10 > Const.HIGH_SCORE:
            Const.HIGH_SCORE = self.score // 10

        fonte = pygame.font.SysFont("Arial", 45)

        texto = fonte.render(
            "MORREU!",
            True,
            (255, 0, 0)
        )

        score = fonte.render(
            f"Score: {self.score // 10}",
            True,
            (255, 255, 255)
        )

        clock = pygame.time.Clock()

        inicio = pygame.time.get_ticks()

        while pygame.time.get_ticks() - inicio < 2500:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.blit(self.background, (0, 0))
            self.window.blit(texto, (170, 110))
            self.window.blit(score, (170, 170))

            pygame.display.flip()

            clock.tick(60)