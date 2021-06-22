# Import and initialize the pygame library
import pygame
pygame.init()


# Background
background = pygame.image.load('resources/images/tabuleiro.png')


# Title and Icon
pygame.display.set_caption("Perfil da Ergonomia")
icon = pygame.image.load('resources/images/tabuleiro.png')
pygame.display.set_icon(icon)

#Obtendo tamanho da imagem
altura_icon= icon.get_height()
largura_icon = icon.get_width()

#Create the screen
screen = pygame.display.set_mode((largura_icon, altura_icon))

# Game Loop
running = True
while running:
    
    # RGB
    screen.fill((255, 255, 255))
    
    # Background Image
    screen.blit(background,(0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Se esc for pressionado finaliza o programa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Inserindo fundo (imagem de fundo)
    # screen.blit(icon, (0,0))

    pygame.display.update()

pygame.quit()

#running = True
#if __name__ == "__main__":
#    print("Tudo certo")
