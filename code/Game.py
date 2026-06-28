import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu
from code.Level import Level   # novo import


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            option = menu.run()      # guarda a opção escolhida

            if option == "Novo jogo":
                pygame.mixer_music.stop()

                level = Level(self.window)
                level.run()

            elif option == "SAIR":
                pygame.quit()
                quit()