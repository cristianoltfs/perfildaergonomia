# Import and initialize the pygame library
import pygame

#Importe para resolução da tela
# import ctypes
# user32 = ctypes.windll.user32

#tamanho da tela
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# screen = 768, 1366

# Title
pygame.display.set_caption("Perfil da Ergonomia")

# Icon
icon = pygame.image.load('resources/images/tabuleiro.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('resources/images/tabuleiro.png')

circulo = pygame.image.load('resources/images/circulo.png')

#Alterando escala para o monitor
# background = pygame.transform.scale(background, [screensize[0], screensize[1]])

#Obtendo tamanho
height_background= 768
width_background = 1366
#Create the screen
screen = pygame.display.set_mode((width_background, height_background))

WHITE =(255, 255, 255)

FPS = 30

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        draw_window()
        
    pygame.quit()
    
#running = True
if __name__ == "__main__":
    main()