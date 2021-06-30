import pygame as pg

pg.init()

WIDTH, HEIGHT = 1366, 768
screen = pg.display.set_mode((WIDTH, HEIGHT))

#width = screen.get_width()
#height = screen.get_height()


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
<<<<<<< HEAD
FPS=100
=======
FPS = 40
>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
#borda do botão
BORDERWIDTH = 1

run = True
#selected="start"

button_selected = '0'
#fundo
background = pg.image.load('resources/images/fundo_jogo_2.png')
#logomarca
mouse = pg.mouse.get_pos()

#inserindo imagens
screen.blit(background,(0,0))
#screen.blit(logo, (screen_width/2 -124,80))
while run:
    for event in pg.event.get():
        #botoes do teclado
        if event.type == pg.QUIT:
<<<<<<< HEAD
            pg.quit()
            exit()
            '''
=======
            run = False
       
>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
        if event.type == pg.MOUSEBUTTONDOWN:
            #limitando posicao x e y do campo mouse
            if 315 <= mouse[0] <= 385 and 75 <= mouse[1] <= 145:
                    print('mouse')
                    button_selected='1'
                    
                    
                    
                    
                    
                    
            if 385 <= mouse[0] <= 420 and  75 <= mouse[1] <= 145:
                    print('mouse2')
                    button_selected='2'                    
<<<<<<< HEAD
            '''           
                    
=======


>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
        mouse = pg.mouse.get_pos()

        title=font_title.render('Quantos jogadores? ',True, BABYBLUE)
        (x, y, raio) = (360, 110, 35)
        diametro = raio * 2
        
        if button_selected =="0":
<<<<<<< HEAD
           
            text_button1 = font_button.render('1',True, WHITE)
            w = pg.draw.circle(screen, WHITE, (x, y),raio, width=border_width)
            w = pg.draw.circle(screen, BLUE, (x, y),raio)

            text_button2 = font_button.render('2',True, WHITE)
            pg.draw.circle(screen, WHITE, ((x + diametro) + 10, y), raio, width=border_width)
            pg.draw.circle(screen, BLUE, ((x + diametro) + 10, y), raio, width=border_width)
            
            text_button3 = font_button.render('3',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 2 + 20, y), raio, width=border_width)
            pg.draw.circle(screen, BLUE, (x + (diametro) * 2 + 20, y), raio, width=border_width)
=======
            (x, y, raio) = (360, 110, 35)
            diametro = raio * 2
            text_button1 = font_button.render('1', True, WHITE)
            w = pg.draw.circle(screen, WHITE, (x, y), raio, width=BORDERWIDTH)
            
            text_button2 = font_button.render('2',True, WHITE)
            pg.draw.circle(screen, WHITE, ((x + diametro) + 10, y), raio, width=BORDERWIDTH)
            
            text_button3 = font_button.render('3',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 2 + 20, y), raio, width=BORDERWIDTH)
>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
            
            text_button4 = font_button.render('4',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio, width=BORDERWIDTH)
           
            text_button5 = font_button.render('5',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio, width=BORDERWIDTH)
            
            text_button6 = font_button.render('6',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio, width=BORDERWIDTH)

            text_button7 = font_button.render('7',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 6 + 60, y), raio, width=BORDERWIDTH)
           
            text_button8 = font_button.render('8',True, WHITE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 7 + 70, y), raio, width=BORDERWIDTH)

        #cores de selecao
        if mouse[0] > x - raio and mouse[1] > y - raio and mouse[0] < x + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

<<<<<<< HEAD
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

=======
        elif mouse[0] > (x + diametro) + 10 - raio and mouse[1] > y - raio and mouse[0] < (x + diametro) + 10 + raio and mouse[1] < y + raio:
            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

        elif mouse[0] > x - raio + 160 and mouse[1] > y - raio and mouse[0] < x + raio + 160 and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

        elif mouse[0] > x + (diametro) * 3 + 30 - raio and mouse[1] > y - raio and mouse[0] < x + (diametro) * 3 + 30 + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            text_button4 = font_button.render('4', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

        elif mouse[0] > x + (diametro) * 4 + 40 - raio and mouse[1] > y - raio and mouse[0] < x + (diametro) * 4 + 40 + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            text_button4 = font_button.render('4', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

            text_button5 = font_button.render('5', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio)

        elif mouse[0] > x + (diametro) * 5 + 50 - raio and mouse[1] > y - raio and mouse[0] < x + (diametro) * 5 + 50 + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            text_button4 = font_button.render('4', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

            text_button5 = font_button.render('5', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio)

            text_button6 = font_button.render('6', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio)

        elif mouse[0] > x + (diametro) * 6 + 60 - raio and mouse[1] > y - raio and mouse[0] < x + (diametro) * 6 + 60 + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            text_button4 = font_button.render('4', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

            text_button5 = font_button.render('5', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio)

            text_button6 = font_button.render('6', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio)

            text_button7 = font_button.render('7', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 6 + 60, y), raio)

        elif mouse[0] > x + (diametro) * 7 + 70 - raio and mouse[1] > y - raio and mouse[0] < x + (diametro) * 7 + 70 + raio and mouse[1] < y + raio:
            text_button1 = font_button.render('1', True, BLUE)
            pg.draw.circle(screen, WHITE, (360, 110), 35)

            text_button2 = font_button.render('2', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

            text_button3 = font_button.render('3', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            text_button4 = font_button.render('4', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

            text_button5 = font_button.render('5', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio)

            text_button6 = font_button.render('6', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio)

            text_button7 = font_button.render('7', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 6 + 60, y), raio)

            text_button8 = font_button.render('8', True, BLUE)
            pg.draw.circle(screen, WHITE, (x + (diametro) * 7 + 70, y), raio)

        else:
            pg.draw.circle(screen, BLACK, (360, 110), 35)
            pg.draw.circle(screen, BLACK, (x + (diametro) + 10, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro * 2) + 20, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro) * 3 + 30, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro) * 4 + 40, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro) * 5 + 50, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro) * 6 + 60, y), raio)
            pg.draw.circle(screen, BLACK, (x + (diametro) * 7 + 70, y), raio)
>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
            
            
            
      
            
        '''    
        if pg.mouse.get_pressed()[0] and w.rect.collidepoint(pg.mouse.get_pos()):
            print('DEU CERTO'  )
<<<<<<< HEAD
            
        '''
            
            
        '''   
=======

        '''    
>>>>>>> ff63a638bf33dced31c1f3b223acca6291a0deaf
        if button_selected=="2":
            text_button2=font_button.render('2',True, blue)
            pygame.draw.circle(screen,black,((x+diametro)+10),110)
        '''

        #menu lateral para inserir os x nomes
        title2 = font_title.render('Insira os nomes aqui',True, BABYBLUE)

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
        screen.blit(text_button8, (360 + diametro * 7 + 60, 110 - 35 / 2))

        pg.display.update()
        clock.tick(FPS)


pg.quit()




















