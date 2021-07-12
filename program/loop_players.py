import pygame as pg
import draw_window as dw
import loop_board as lb
from pygame import gfxdraw

def loop_players(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT, sound_on, sound_off):
    pg.init()

    font_button = pg.font.SysFont('arial', 45, False, False)

    button_selected = '0'

    background = pg.image.load('resources/images/fundo_jogo_2.png')
    
    arrow = pg.image.load('resources/images/seta.png')
    
    clock = pg.time.Clock()
    run = True
    musica = 1
    dw.draw_window(screen, background, WHITE)
    screen.blit(sound_on, (WIDTH / 1.03, 10))
    (x, y, raio) = (360, 110, 35)
    diametro = raio * 2
    botao_jogadores = pg.image.load('resources/images/botao-1.png')
    botao_nomes = pg.image.load('resources/images/botao-2.png')
    screen.blit(botao_jogadores, (80, 13))
    screen.blit(sound_on, (WIDTH/1.03, 10))
    screen.blit(botao_nomes, (1000, 13))
    arrow_rect = arrow.get_rect()

    screen.blit(arrow,(1170,530))

    pg.draw.rect(screen, DARKBLUE, (320,70,650,80),border_radius=9,width=2)
    pg.draw.rect(screen, BLUE, (320,70,648,78),border_radius=9)

    #Nome dos jogadores
    pg.draw.rect(screen, DARKBLUE, (320,170,650,400),border_radius=9,width=2)
    pg.draw.rect(screen, BLUE, (320,170,648,398),border_radius=9)

    pg.draw.rect(screen, DARKBLUE, (1000,170,250,100),border_radius=9, width=2)
    pg.draw.rect(screen, BLUE, (1000,170,248,98),border_radius=9)



    user_text = ''
    base_font = pg.font.SysFont(None, 35)
    input_rect=pg.Rect(1018,200,222,44)
    active = False
    color=BABYBLUE
    font_title = pg.font.SysFont('arial',30,False, False)
    name_player=''
    cont=1
    ok=False
    cont2=0
    arquivo = open("nome.txt", "r")
    arquivo_2=open('sala.txt','r')
    nome=arquivo.readlines()
    sala=arquivo_2.readlines()
    print(nome)

    while run:
        #clock.tick(60)

        event_list = pg.event.get()
        text=('Bem-vindo %s !...Você está na sala: %s ' %(nome[0],sala[0]))
        
        title = font_title.render(text, False, BABYBLUE)
        screen.blit(title,(350,30))

        for event in event_list:
            # botoes do teclado
            if event.type == pg.QUIT:
                run = False
            mouse = pg.mouse.get_pos()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                # limitando posicao x e y do campo mouse
                #apertando os botoes
                if 315 <= mouse[0] <= 385 and 75 <= mouse[1] <= 145:
                    print('mouse')
                    button_selected = '1'
                if 385 <= mouse[0] <= 420 and 75 <= mouse[1] <= 145:
                    print('mouse2')
                    button_selected = '2'

                if mouse[0] > WIDTH/1.03 and mouse[1] > 10 and mouse[0] < WIDTH/1.03 + 34 and mouse[1] < 10 + 34 and musica == 1:
                    screen.blit(sound_off, (WIDTH / 1.03, 10))
                    pg.mixer.music.set_volume(0)
                    musica = 0

                elif mouse[0] > WIDTH/1.03 and mouse[1] > 10 and mouse[0] < WIDTH/1.03 + 34 and mouse[1] < 10 + 34 and musica == 0:
                    pg.mixer.music.set_volume(0.4)
                    screen.blit(sound_on, (WIDTH / 1.03, 10))
                    musica = 1

                if mouse[0] > x - raio and mouse[1] > y - raio and mouse[0] < x + raio and mouse[1] < y + raio:
                    print('1 Jogador')
                    button_selected = 1

                elif mouse[0] > (x + diametro) + 10 - raio and mouse[1] > y - raio and mouse[0] < (
                            x + diametro) + 10 + raio and mouse[1] < y + raio:
                    print('2 Jogadores')
                    button_selected = 2

                elif mouse[0] > x - raio + 160 and mouse[1] > y - raio and mouse[0] < x + raio + 160 and mouse[
                    1] < y + raio:
                    print('3 Jogadores')
                    button_selected = 3

                elif mouse[0] > x + (diametro) * 3 + 30 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 3 + 30 + raio and mouse[1] < y + raio:
                    print('4 Jogadores')
                    button_selected = 4


                elif mouse[0] > x + (diametro) * 4 + 40 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 4 + 40 + raio and mouse[1] < y + raio:
                    print('5 Jogadores')
                    button_selected = 5

                elif mouse[0] > x + (diametro) * 5 + 50 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 5 + 50 + raio and mouse[1] < y + raio:
                    print('6 Jogadores')
                    button_selected = 6

                elif mouse[0] > x + (diametro) * 6 + 60 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 6 + 60 + raio and mouse[1] < y + raio:
                    print('7 Jogadores')
                    button_selected = 7

                elif mouse[0] > x + (diametro) * 7 + 70 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 7 + 70 + raio and mouse[1] < y + raio:
                    print('8 Jogadores')
                    button_selected = 8

            mouse = pg.mouse.get_pos()
            
            
            if event.type == pg.MOUSEBUTTONDOWN:
                
                if input_rect.collidepoint(event.pos):
                    active = not active
                    
                else:
                    active = False
                    
                color = DARKBLUE if active else BABYBLUE

            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        name_player=user_text
                        ok=True
                        print(name_player)
                        user_text = ''
                    elif event.key == pg.K_BACKSPACE:
                        user_text = user_text[:-1]
                    if len(user_text)>=12:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode                
                    
                    
            pg.draw.rect(screen,color,input_rect,border_radius=8)
            text_surface = base_font.render(user_text,True,WHITE)
            
            screen.blit(text_surface,(input_rect.x + 5,input_rect.y))
            if ok:
                name_player=('JOGADOR: %d --- %s' %(cont,name_player))
                name=font_title.render(name_player,True,WHITE)
                screen.blit(name,(340,190+cont2))

                cont=cont+1
                cont2=cont2+35
                ok=False

                
                
            # cores de selecao
            if mouse[0] > x - raio and mouse[1] > y - raio and mouse[0] < x + raio and mouse[1] < y + raio:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)


            elif mouse[0] > (x + diametro) + 10 - raio and mouse[1] > y - raio and mouse[0] < (
                    x + diametro) + 10 + raio and mouse[1] < y + raio:
                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

            elif mouse[0] > x - raio + 160 and mouse[1] > y - raio and mouse[0] < x + raio + 160 and mouse[
                1] < y + raio:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

                text_button3 = font_button.render('3', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

            elif mouse[0] > x + (diametro) * 3 + 30 - raio and mouse[1] > y - raio and mouse[0] < x + (
            diametro) * 3 + 30 + raio and mouse[1] < y + raio:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

                text_button3 = font_button.render('3', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

                text_button4 = font_button.render('4', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)

            elif mouse[0] > x + (diametro) * 4 + 40 - raio and mouse[1] > y - raio and mouse[0] < x + (
            diametro) * 4 + 40 + raio and mouse[1] < y + raio:
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

            elif mouse[0] > x + (diametro) * 5 + 50 - raio and mouse[1] > y - raio and mouse[0] < x + (
            diametro) * 5 + 50 + raio and mouse[1] < y + raio:
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

            elif mouse[0] > x + (diametro) * 6 + 60 - raio and mouse[1] > y - raio and mouse[0] < x + (
            diametro) * 6 + 60 + raio and mouse[1] < y + raio:
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

            elif mouse[0] > x + (diametro) * 7 + 70 - raio and mouse[1] > y - raio and mouse[0] < x + (
            diametro) * 7 + 70 + raio and mouse[1] < y + raio:
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
                pg.draw.circle(screen, DARKBLUE, (360, 110), 35)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) + 10, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro * 2) + 20, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) * 3 + 30, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) * 4 + 40, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) * 5 + 50, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) * 6 + 60, y), raio)
                pg.draw.circle(screen, DARKBLUE, (x + (diametro) * 7 + 70, y), raio)
                
                text_button1 = font_button.render('1', True, WHITE)
                text_button2 = font_button.render('2', True, WHITE)
                text_button3 = font_button.render('3', True, WHITE)
                text_button4 = font_button.render('4', True, WHITE)
                text_button5 = font_button.render('5', True, WHITE)
                text_button6 = font_button.render('6', True, WHITE)
                text_button7 = font_button.render('7', True, WHITE)
                text_button8 = font_button.render('8', True, WHITE)
                
            if button_selected == 1:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)
            if button_selected == 2:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)               
                
            
            if button_selected == 3:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

                text_button3 = font_button.render('3', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)                
                
            if button_selected == 4:
                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)

                text_button3 = font_button.render('3', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro * 2) + 20, y), raio)

                text_button4 = font_button.render('4', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio)                
                
                
                
                
            if button_selected == 5:
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
                
                
                
                
                
                
            if button_selected == 6:
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

                
            if button_selected == 7:
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
                
               
            if button_selected == 8:
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
   
            text_button1_rect = text_button1.get_rect()
            text_button2_rect = text_button2.get_rect()
            text_button3_rect = text_button3.get_rect()
            text_button4_rect = text_button4.get_rect()
            text_button5_rect = text_button5.get_rect()
            text_button6_rect = text_button6.get_rect()
            text_button7_rect = text_button7.get_rect()
            text_button8_rect = text_button8.get_rect()

        

            screen.blit(text_button1, (360 - (text_button1_rect[2] / 2), 110 - 35 / 1.25))
            screen.blit(text_button2, (360 + diametro, 110 - 35 / 1.25))
            screen.blit(text_button3, (360 + diametro * 2 + 10, 110 - 35 / 1.25))
            screen.blit(text_button4, (360 + diametro * 3 + 20, 110 - 35 / 1.25))
            screen.blit(text_button5, (360 + diametro * 4 + 30, 110 - 35 / 1.25))
            screen.blit(text_button6, (360 + diametro * 5 + 40, 110 - 35 / 1.25))
            screen.blit(text_button7, (360 + diametro * 6 + 50, 110 - 35 / 1.25))
            screen.blit(text_button8, (360 + diametro * 7 + 60, 110 - 35 / 1.25))

            pg.display.update()
            clock.tick(FPS)

    pg.quit()
