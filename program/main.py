# Import and initialize the pygame library
import pygame
#Importe para resolução da tela
import ctypes
user32 = ctypes.windll.user32
#tamanho da tela
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Title
pygame.display.set_caption("Perfil da Ergonomia")

# Icon
icon = pygame.image.load('resources/images/tabuleiro.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('resources/images/tabuleiro.png')

#Alterando escala para o monitor
#pygame.transform.scale(background,) ################## EM ANDAMENTO

#Obtendo tamanho da imagem
height_background= icon.get_height()
width_background = icon.get_width()

#Create the screen
screen = pygame.display.set_mode((width_background, height_background))

WHITE =(255, 255, 255)

FPS = 30

circulo = pygame.image.load('resources/images/circulo.png')

def draw_window():
    screen.fill(WHITE)
    screen.blit(background,(0, 0))
    screen.blit(circulo,(500, 250))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        
    pygame.quit()
    
#running = True
if __name__ == "__main__":
    main()