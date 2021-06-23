import pygame
import draw_window

def main(FPS, screen, background, WHITE):
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

        draw_window.draw_window(screen, background, WHITE)
        
    pygame.quit()