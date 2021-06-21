# Import and initialize the pygame library
import pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('resources/images/tabuleiro.png')


# Title and Icon
pygame.display.set_caption("Perfil da Ergonomia")
icon = pygame.image.load('resources/images/tabuleiro.png')
pygame.display.set_icon(icon)

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


#running = True

#if __name__ == "__main__":
    
    
#    print("Tudo certo")
