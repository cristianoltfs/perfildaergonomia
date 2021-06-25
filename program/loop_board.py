import pygame as pg
import draw_window as dw
import read_cards as rc
import sortition_cards as sc

def loop_main(FPS, screen, WHITE):
    clock = pg.time.Clock()
    run = True
    cards = rc.read_cards()
    board = pg.image.load('resources/images/tabuleiro.png')

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        sc.sortition_cards(cards)

        dw.draw_window(screen, board, WHITE)
        
    pg.quit()