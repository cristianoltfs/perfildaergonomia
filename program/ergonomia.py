import pygame as pg
pg.init()

import loop_main as lm

from classes.jogador import Jogador
j1 = Jogador()

print(j1)

pg.display.set_caption("Perfil da Ergonomia")

icon = pg.image.load('resources/images/tabuleiro.png')
pg.display.set_icon(icon)

background = pg.image.load('resources/images/tabuleiro.png')

WIDTH, HEIGHT = 1366, 768
screen = pg.display.set_mode((WIDTH, HEIGHT))

WHITE =(255, 255, 255)
FPS = 30

if __name__ == "__main__":
    lm.loop_main(FPS, screen, background, WHITE)