import pygame

def draw_window(screen, background, WHITE):
    screen.fill(WHITE)
    screen.blit(background,(0, 0))
    pygame.display.update()