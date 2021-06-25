import pygame as pg
pg.init()

# import loop_main as lm
import loop_begin as lb

# from classes.jogador import Jogador
# j1 = Jogador()
# print(j1)

pg.display.set_caption("Perfil da Ergonomia")

icon = pg.image.load('resources/images/logo_reduzida.png')
pg.display.set_icon(icon)

background = pg.image.load('resources/images/fundo_jogo_2.png')

WIDTH, HEIGHT = 1366, 768
screen = pg.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BABYBLUE = (216, 227, 250)
BLACK = (0, 0, 0)
BLUE = (5, 17, 44)
DARKBLUE = (66, 191, 254)

BORDERWIDTH = 1

FPS = 30

if __name__ == "__main__":
    lb.loop_begin(FPS,
                  screen,
                  background,
                  WHITE,
                  BLACK,
                  BABYBLUE,
                  BLUE,
                  DARKBLUE,
                  BORDERWIDTH,
                  WIDTH)
    #lm.loop_main(FPS, screen, background, WHITE)