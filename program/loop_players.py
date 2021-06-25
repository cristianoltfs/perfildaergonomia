import pygame as pg
import draw_window as dw

def loop_players(FPS, screen, WHITE):
    
    print("players")
    
    clock = pg.time.Clock()
    run = True
    board = pg.image.load('resources/images/tabuleiro.png')

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        dw.draw_window(screen, board, WHITE)
        
    pg.quit()