import pygame
import draw_window as dw
import read_cards as rc
import sortition_cards as sc

def loop_main(FPS, screen, background, WHITE):
    clock = pygame.time.Clock()
    run = True
    cards = rc.read_cards()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        sc.sortition_cards(cards)

        dw.draw_window(screen, background, WHITE)
        
    pygame.quit()