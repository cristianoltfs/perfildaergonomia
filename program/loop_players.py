import pygame as pg
import draw_window as dw
import loop_board as lb


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
    while run:
        for event in pg.event.get():
            # botoes do teclado
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                # limitando posicao x e y do campo mouse
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
                    pg.draw.rect(screen, WHITE, (HEIGHT/4, WIDTH/4, HEIGHT/2, WIDTH/2), border_radius=8)

                elif mouse[0] > (x + diametro) + 10 - raio and mouse[1] > y - raio and mouse[0] < (
                            x + diametro) + 10 + raio and mouse[1] < y + raio:
                    print('2 Jogadores')

                elif mouse[0] > x - raio + 160 and mouse[1] > y - raio and mouse[0] < x + raio + 160 and mouse[
                    1] < y + raio:
                    print('3 Jogadores')

                elif mouse[0] > x + (diametro) * 3 + 30 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 3 + 30 + raio and mouse[1] < y + raio:
                    print('4 Jogadores')

                elif mouse[0] > x + (diametro) * 4 + 40 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 4 + 40 + raio and mouse[1] < y + raio:
                    print('5 Jogadores')

                elif mouse[0] > x + (diametro) * 5 + 50 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 5 + 50 + raio and mouse[1] < y + raio:
                    print('6 Jogadores')

                elif mouse[0] > x + (diametro) * 6 + 60 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 6 + 60 + raio and mouse[1] < y + raio:
                    print('7 Jogadores')

                elif mouse[0] > x + (diametro) * 7 + 70 - raio and mouse[1] > y - raio and mouse[0] < x + (
                        diametro) * 7 + 70 + raio and mouse[1] < y + raio:
                    print('8 Jogadores')

            mouse = pg.mouse.get_pos()

            title = font_title.render('Quantos jogadores? ', True, BABYBLUE)

            if button_selected == "0":
                (x, y, raio) = (360, 110, 35)
                diametro = raio * 2
                text_button1 = font_button.render('1', True, WHITE)
                w = pg.draw.circle(screen, WHITE, (x, y), raio, width=BORDERWIDTH)

                text_button2 = font_button.render('2', True, WHITE)
                pg.draw.circle(screen, WHITE, ((x + diametro) + 10, y), raio, width=BORDERWIDTH)

                text_button3 = font_button.render('3', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 2 + 20, y), raio, width=BORDERWIDTH)

                text_button4 = font_button.render('4', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 3 + 30, y), raio, width=BORDERWIDTH)

                text_button5 = font_button.render('5', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 4 + 40, y), raio, width=BORDERWIDTH)

                text_button6 = font_button.render('6', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 5 + 50, y), raio, width=BORDERWIDTH)

                text_button7 = font_button.render('7', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 6 + 60, y), raio, width=BORDERWIDTH)

                text_button8 = font_button.render('8', True, WHITE)
                pg.draw.circle(screen, WHITE, (x + (diametro) * 7 + 70, y), raio, width=BORDERWIDTH)

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
                pg.draw.circle(screen, BLACK, (360, 110), 35)
                pg.draw.circle(screen, BLACK, (x + (diametro) + 10, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro * 2) + 20, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro) * 3 + 30, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro) * 4 + 40, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro) * 5 + 50, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro) * 6 + 60, y), raio)
                pg.draw.circle(screen, BLACK, (x + (diametro) * 7 + 70, y), raio)

            # menu lateral para inserir os x nomes
            title2 = font_title.render('Insira os nomes aqui', True, BABYBLUE)

            # pg.draw.rect(screen, WHITE, (1000,100,250,500),border_radius=9, width=border_width)

            # converter texto para rect
            title_rect = title.get_rect()
            title2_rect = title2.get_rect()
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
            screen.blit(title, (90, 100))
            screen.blit(title2, (1010, 70))

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
