import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW
from code import Const


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu_img.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        menu_option = 0

        pygame.mixer_music.load('./assets/menu_sound.wav')
        pygame.mixer_music.play(-1)

        # Limpa qualquer evento antigo
        pygame.event.clear()

        while True:

            self.window.blit(self.surf, self.rect)

            self.menu_text(
                50,
                "Death",
                C_ORANGE,
                (WINDOW_WIDTH / 2, 70)
            )

            self.menu_text(
                50,
                "Jump",
                C_ORANGE,
                (WINDOW_WIDTH / 2, 120)
            )

            self.menu_text(
                18,
                "Pressione ENTER",
                C_WHITE,
                (WINDOW_WIDTH / 2, 170)
            )

            self.menu_text(
                18,
                "Pressione ESPAÇO para pular",
                C_WHITE,
                (WINDOW_WIDTH / 2, 300)
            )

            self.menu_text(
                20,
                f"Recorde: {Const.HIGH_SCORE}",
                C_WHITE,
                (WINDOW_WIDTH / 2, 30)
            )

            for i in range(len(MENU_OPTION)):

                cor = C_YELLOW if i == menu_option else C_WHITE

                self.menu_text(
                    20,
                    MENU_OPTION[i],
                    cor,
                    (WINDOW_WIDTH / 2, 200 + 25 * i)
                )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size, text, text_color, text_center_pos):

        text_font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            text_size
        )

        text_surf = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)