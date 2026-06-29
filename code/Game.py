import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):

        menu = Menu(self.window)

        while True:

            option = menu.run()

            if option == "Novo jogo":
                level = Level(self.window)
                level.run()

            elif option == "SAIR":
                pygame.quit()
                quit()