import pygame as pg
import draw_window as dw
import loop_board as lb
from pygame import gfxdraw
from input_text import TextInputBox

def loop_players(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT, sound_on, sound_off):
    pg.init()

    font_menu = pg.font.SysFont('arial', 25, False, False)
    font_title = pg.font.SysFont('arial', 25, False, False)
    font_button = pg.font.SysFont('arial', 45, False, False)

    button_selected = '0'

    background = pg.image.load('resources/images/fundo_jogo_2.png')

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
    pg.draw.rect(screen, DARKBLUE, (320,70,650,80),border_radius=9,width=1)
#circulo renderizado
    #gfxdraw.aacircle(screen, 100, 200, 100, BLUE)
    #gfxdraw.filled_circle(screen, 100, 200, 100, BLUE)
    
    
    font = pg.font.SysFont(None, 35)
    text_input_box = TextInputBox(1050, 200, 200, font)
    group = pg.sprite.Group(text_input_box)

    while run:
        event_list = pg.event.get()

        for event in event_list:
            # botoes do teclado
            if event.type == pg.QUIT:
                run = False
                
            mouse = pg.mouse.get_pos()
            group.update(event_list)
            group.draw(screen)
            pg.display.flip()  
 
           
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

            #title = font_title.render('Quantos jogadores? ', True, BABYBLUE)
           
            
            
            
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
            pg.draw.rect(screen, DARKBLUE, (1000,160,250,500),border_radius=9, width=1)
                
            if button_selected == 1:
                #pg.draw.rect(screen, WHITE, (1000,100,250,50),border_radius=9, width=1)

                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)
            if button_selected == 2:
                #pg.draw.rect(screen, WHITE, (1000,100,250,50),border_radius=9, width=1)

                #pg.draw.rect(screen, WHITE, (1000,100,250,100),border_radius=9, width=1)

                text_button1 = font_button.render('1', True, BLUE)
                pg.draw.circle(screen, WHITE, (360, 110), 35)

                text_button2 = font_button.render('2', True, BLUE)
                pg.draw.circle(screen, WHITE, (x + (diametro) + 10, y), raio)               
                
                
                
                
            if button_selected == 3:
                
                #pg.draw.rect(screen, WHITE, (1000,100,250,50),border_radius=9, width=1)

                #pg.draw.rect(screen, WHITE, (1000,100,250,100),border_radius=9, width=1)
                #pg.draw.rect(screen, WHITE, (1000,100,250,150),border_radius=9, width=1)
                
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
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

            # menu lateral para inserir os x nomes
            #title2 = font_title.render('Insira os nomes aqui', True, BABYBLUE)

            # pg.draw.rect(screen, WHITE, (1000,100,250,500),border_radius=9, width=border_width)

            # converter texto para rect
            #title_rect = title.get_rect()
            #title2_rect = title2.get_rect()
            # botoes

            text_button1_rect = text_button1.get_rect()
            text_button2_rect = text_button2.get_rect()
            text_button3_rect = text_button3.get_rect()
            text_button4_rect = text_button4.get_rect()
            text_button5_rect = text_button5.get_rect()
            text_button6_rect = text_button6.get_rect()
            text_button7_rect = text_button7.get_rect()
            text_button8_rect = text_button8.get_rect()

            # Posicionando texto e inserindo na tela
            #screen.blit(title, (90, 100))
            #screen.blit(title2, (1010, 70))

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
