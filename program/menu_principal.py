import pygame

# import os
from pygame.locals import *
# from sys import exit

#inicializar todas as funcoes
pygame.init()
#centralizar janela
# os.environ['SDL_VIDEO_CENTERED'] = '1'
     
screen_width=1366
screen_height=768
screen=pygame.display.set_mode((screen_width, screen_height))

#cores     
white=(255, 255, 255)
white2=( 216, 227, 250) #branco azulado
black=(0, 0, 0)
blue=( 5, 17, 44)
blue2=(   66, 191, 254 ) # azul escuro
#fontes e tamanhos
font_menu = pygame.font.SysFont('arial',25,False, False)
font_title = pygame.font.SysFont('arial',17,False, False)

clock = pygame.time.Clock()
FPS=30
#borda do botão
border_width = 1

menu=True
selected="start"
#menu=True
#som principal
pygame.mixer.music.set_volume(0.4)
fundo=pygame.mixer.music.load('principal.ogg')
pygame.mixer.music.play(-1)

#som do clique
botao=pygame.mixer.Sound('smw_kick.wav')
#som.play()
#fundo
background = pygame.image.load('fundo_jogo_2.jpg')
#logomarca
logo = pygame.image.load('logo_reduzida.png').convert_alpha()

#inserindo imagens
screen.blit(background,(0,0))
screen.blit(logo, (screen_width/2 -124,80))
while menu:
    for event in pygame.event.get():
        #botoes do teclado
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                selected="start"
                botao.play()
            elif event.key==pygame.K_DOWN:
                selected="quit"
                botao.play()
            if event.key==pygame.K_RETURN:
                if selected=="start":
                    print("Start")
                if selected=="quit":
                    pygame.quit()
                    quit()
                    
        title=font_title.render('Seja bem vindo ao Perfil da ergonomia! Um jogo criado dentro da UFOP!',False, white2)
        sub_title=font_title.render('Colaboradores: José da Silva, Aline Santos, Joana Smith, Fabricio',False,white2)

        if selected == "start":
            
            text_start=font_menu.render('Iniciar',True, white)
            
            (x, y, width, height) = (screen_width/2.35,screen_height/2.65,200,50)
            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
            #selecao
            pygame.draw.rect(screen, blue2, (x, y, width-1, height-1),border_radius=9) #azul claro

        else:
            text_start=font_menu.render('Iniciar',True, black)
            (x, y, width, height) = (screen_width/2.35,screen_height/2.65,200,50)
            pygame.draw.rect(screen, blue, (x, y, width-1, height-1),border_radius=9)

        if selected=="quit":
            text_quit=font_menu.render('Sair',True, white)
         

            (x, y, width, height) = (screen_width/2.35,screen_height/2.20,200,50)
            pygame.draw.rect(screen, blue2, (x, y, width-1, height-1),border_radius=9) #azul claro

            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width) 
        else:    
            text_quit=font_menu.render('Sair',True, black)
            
            (x, y, width, height) = (screen_width/2.35,screen_height/2.20,200,50)
            
            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
            pygame.draw.rect(screen, blue, (x, y, width-1, height-1),border_radius=9)
        
        #converter texto para rect
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()    
        # Posicionando texto e inserindo na tela
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 500))
        screen.blit(sub_title, (screen_width/2 - (title_rect[2]/2), 520))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)


   

