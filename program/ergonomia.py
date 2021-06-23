import loop_main as lm
import pygame as pg
pg.init()

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