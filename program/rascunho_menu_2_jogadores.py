import pygame as pg
import os
from sys import exit

#inicializar todas as funcoes
pg.init()
#centralizar janela
     
screen_width=1366
screen_height=768
screen = pg.display.set_mode((screen_width, screen_height))

width = screen.get_width() 
height = screen.get_height() 


WHITE = (255, 255, 255)
BABYBLUE = (216, 227, 250)
BLACK = (0, 0, 0)
BLUE = (5, 17, 44)
DARKBLUE = (66, 191, 254)

#fontes e tamanhos
font_menu = pg.font.SysFont('arial', 25, False, False)
font_title = pg.font.SysFont('arial', 25, False, False) #quantos jogadores....
font_button = pg.font.SysFont('arial', 45, False, False)

clock = pg.time.Clock()
FPS=100
#borda do botão
border_width = 1

menu = True
selected="start"
menu = True
button_selected='0'
#fundo
background = pg.image.load('resources/images/fundo_jogo_2.png')
#logomarca
mouse = pg.mouse.get_pos()

#inserindo imagens
screen.blit(background,(0,0))
#screen.blit(logo, (screen_width/2 -124,80))
while menu:
    for event in pg.event.get():
        #botoes do teclado
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            '''
        if event.type == pg.MOUSEBUTTONDOWN:
            #limitando posicao x e y do campo mouse
            if 315 <= mouse[0] <= 385 and 75 <= mouse[1] <= 145:
                    print('mouse')
                    button_selected='1'
                    
                    
                    
                    
                    
                    
            if 385 <= mouse[0] <= 420 and  75 <= mouse[1] <= 145:
                    print('mouse2')
                    button_selected='2'                    
            '''           
                    
        mouse = pg.mouse.get_pos()
        
  
                  
                                          
        title=font_title.render('Quantos jogadores? ',True, BABYBLUE)
        (x, y, raio) = (360, 110, 35)
        diametro = raio * 2
        
        if button_selected =="0":
           
            text_button1 = font_button.render('1',True, WHITE)
            w = pg.draw.circle(screen, WHITE, (x, y),raio, width=border_width)
            w = pg.draw.circle(screen, BLUE, (x, y),raio)

            text_button2 = font_button.render('2',True, WHITE)
            pg.draw.circle(screen, WHITE, ((x + diametro) + 10, y), raio, width=border_width)
            pg.draw.circle(screen, BLUE, ((x + diametro) + 10, y), raio, width=border_width)
            
            text_button3 = font_button.render('3',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 2 + 20, y), raio, width=border_width)
            pg.draw.circle(screen, BLUE, (x + (diametro) * 2 + 20, y), raio, width=border_width)
            
            text_button4 = font_button.render('4',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio, width=border_width)
           
            text_button5 = font_button.render('5',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio, width=border_width)
            
            text_button6 = font_button.render('6',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio, width=border_width)

            text_button7 = font_button.render('7',True, WHITE)
            pg.draw.circle(screen, WHITE, (x+ (diametro) * 6 + 60, y), raio, width=border_width)
           
            text_button8 = font_button.render('8',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 7 + 70, y), raio, width=border_width)

        #cores de selecao
        if 315 <= mouse[0] <= 385 and 75 <=mouse[1] <= 145:
            
            text_button1 = font_button.render('1',True, BLUE)

            pg.draw.circle(screen, WHITE , (360, 110), 35)
            
        elif 385 <= mouse[0] <= 420 and  75 <= mouse[1] <= 145:
            
            text_button2 = font_button.render('2',True, BLUE)
            pg.draw.circle(screen, BLACK , (440, 110),35)    

        else:
                 
            text_button1 = font_button.render('1',True, WHITE)
            w = pg.draw.circle(screen, BLUE, (x, y),raio)
            
            text_button2 = font_button.render('2',True, WHITE)
            pg.draw.circle(screen, BLUE, ((x + diametro) + 10, y), raio)
            
            text_button3 = font_button.render('3',True, WHITE)
            pg.draw.circle(screen, BLUE, (x + (diametro) * 2 + 20, y), raio)
            
            text_button4 = font_button.render('4',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio, width=border_width)
           
            text_button5 = font_button.render('5',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio, width=border_width)
            
            text_button6 = font_button.render('6',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio, width=border_width)

            text_button7 = font_button.render('7',True, WHITE)
            pg.draw.circle(screen, WHITE, (x+ (diametro) * 6 + 60, y), raio, width=border_width)
           
            text_button8 = font_button.render('8',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 7 + 70, y), raio, width=border_width)

            
            
            
      
            
        '''    
        if pg.mouse.get_pressed()[0] and w.rect.collidepoint(pg.mouse.get_pos()):
            print('DEU CERTO'  )
            
        '''
            
            
        '''   
        if button_selected=="2":
            text_button2=font_button.render('2',True, blue)
            pygame.draw.circle(screen,black,((x+diametro)+10),110)
        '''
        
        
        
        
        
        #menu lateral para inserir os x nomes
        title2=font_title.render('Insira os nomes aqui',True, BABYBLUE)

        pg.draw.rect(screen, WHITE, (1000,100,250,500),border_radius=9, width=border_width)









        
        #converter texto para rect
        title_rect = title.get_rect()
        title2_rect = title2.get_rect()
        #botoes
        text_button1_rect = text_button1.get_rect()
        text_button2_rect = text_button2.get_rect()
        text_button3_rect = text_button3.get_rect()
        text_button4_rect = text_button4.get_rect()
        text_button5_rect = text_button5.get_rect()
        text_button6_rect = text_button6.get_rect()
        text_button7_rect = text_button7.get_rect()
        text_button8_rect = text_button8.get_rect()

        
        
        
        # Posicionando texto e inserindo na tela
        screen.blit(title, (90, 100))
        screen.blit(title2, (1010, 70))

        
        screen.blit(text_button1, (360 - (text_button1_rect[2] / 2), 110 - 35 / 2))
        screen.blit(text_button2, (360 + diametro, 110 - 35 / 2))
        screen.blit(text_button3, (360 + diametro * 2 + 10, 110 - 35 / 2))
        screen.blit(text_button4, (360 + diametro * 3 + 20, 110 - 35 / 2))
        screen.blit(text_button5, (360 + diametro * 4 + 30, 110 - 35 / 2))
        screen.blit(text_button6, (360 + diametro * 5 + 40, 110 - 35 / 2))
        screen.blit(text_button7, (360 + diametro * 6 + 50, 110 - 35 / 2))
        screen.blit(text_button8, (360 + diametro * 7+ 60, 110 - 35 / 2))

     
        pg.display.update()
        clock.tick(FPS)






















