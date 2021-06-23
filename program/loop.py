import pygame
import draw_window as dw

def loop(FPS, screen, background, WHITE):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        dw.draw_window(screen, background, WHITE)
        
    pygame.quit()