import main
import pygame
pygame.init()

pygame.display.set_caption("Perfil da Ergonomia")

icon = pygame.image.load('resources/images/tabuleiro.png')
pygame.display.set_icon(icon)

background = pygame.image.load('resources/images/tabuleiro.png')

WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE =(255, 255, 255)
FPS = 30
print(__name__)
if __name__ == "__main__":
    main.main(FPS, screen, background, WHITE)