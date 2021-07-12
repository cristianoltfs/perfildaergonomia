import pygame as pg
import loop_players as lp
import loop_name as ln
#som principal
pg.mixer.init()

pg.mixer.music.set_volume(0.3)
pg.mixer.music.load('resources/sounds/principal.ogg')
pg.mixer.music.play(-1)

#som do clique
botton_click_sound = pg.mixer.Sound('resources/sounds/smw_kick.wav')

logo_begin = pg.image.load('resources/images/logo_reduzida.png')

def loop_begin(FPS,
               screen,
               background,
               WHITE,
               BLACK,
               BABYBLUE,
               BLUE,
               DARKBLUE,
               BORDERWIDTH,
               WIDTH,
               HEIGHT):
    
    font_menu = pg.font.SysFont('arial',25,False, False)
    font_title = pg.font.SysFont('arial',17,False, False)

    sound_on = pg.image.load('resources/images/sound_on.png')
    sound_off = pg.image.load('resources/images/sound_off.png')

    clock = pg.time.Clock()

    screen.blit(background, (0,0))
    screen.blit(logo_begin, (WIDTH/2 -124,80))
    screen.blit(sound_on, (WIDTH/1.03, 10))

    musica = 1
    run = True
    selected = "start"

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            #botoes do teclado
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    selected = "start"
                    botton_click_sound.play()
                elif event.key == pg.K_DOWN:
                    selected="quit"
                    botton_click_sound.play()
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_RETURN:
                    if selected == "start":
                        ln.loop_name(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT, sound_on, sound_off)
                    if selected == "quit":
                        run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x = pg.mouse.get_pos()[0]
                y = pg.mouse.get_pos()[1]

                if x > WIDTH / 2.35 and y > HEIGHT / 2.65 and x < WIDTH / 2.35 + 200 and y < HEIGHT / 2.65 + 50:
                    ln.loop_name(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT,sound_on, sound_off)

                if x > WIDTH / 2.35 and y > HEIGHT / 2.20 and x < WIDTH/2.35 + 200 and y < HEIGHT / 2.20 + 50:
                    run = False

                if x > WIDTH / 1.03 and y > 10 and x < WIDTH / 1.03 + 34 and y < 10 + 34 and musica == 1:
                    screen.blit(sound_off, (WIDTH / 1.03, 10))
                    pg.mixer.music.set_volume(0)
                    musica = 0

                elif x > WIDTH / 1.03 and y > 10 and x < WIDTH / 1.03 + 34 and y < 10 + 34 and musica == 0:
                    pg.mixer.music.set_volume(0.4)
                    screen.blit(sound_on, (WIDTH / 1.03, 10))
                    musica = 1
                        
            title = font_title.render('Seja bem vindo ao Perfil da ergonomia! Um jogo criado dentro da UFOP!', False, BABYBLUE)
            sub_title = font_title.render('Colaboradores: José da Silva, Aline Santos, Joana Smith, Fabricio', False,BABYBLUE)
    
            if selected == "start":
                
                text_start = font_menu.render('Iniciar',True, WHITE)
                
                (x, y, width, height) = (WIDTH / 2.35, HEIGHT / 2.65, 200, 50)
                pg.draw.rect(screen, WHITE, (x, y, width, height), border_radius=9, width=BORDERWIDTH)
                #selecao
                pg.draw.rect(screen, DARKBLUE, (x, y, width - 1, height - 1), border_radius=9)
    
            else:
                text_start = font_menu.render('Iniciar', True, BLACK)
                (x, y, width, height) = (WIDTH / 2.35, HEIGHT / 2.65, 200, 50)
                pg.draw.rect(screen, BLUE, (x, y, width - 1, height - 1),border_radius=9)
    
            if selected == "quit":
                text_quit = font_menu.render('Sair',True, WHITE)
             
    
                (x, y, width, height) = (WIDTH / 2.35,HEIGHT / 2.20, 200, 50)
                pg.draw.rect(screen, DARKBLUE, (x, y, width-1, height-1), border_radius=9) #azul claro
    
                pg.draw.rect(screen, WHITE, (x, y, width, height), border_radius=9, width=BORDERWIDTH)
            else:    
                text_quit = font_menu.render('Sair',True, BLACK)
                
                (x, y, width, height) = (WIDTH / 2.35, HEIGHT / 2.20, 200, 50)
                
                pg.draw.rect(screen, WHITE, (x, y, width, height), border_radius=9, width=BORDERWIDTH)
                pg.draw.rect(screen, BLUE, (x, y, width-1, height - 1), border_radius=9)
            
            #converter texto para rect
            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
           
            # Posicionando texto e inserindo na tela
            screen.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 500))
            screen.blit(sub_title, (WIDTH / 2 - (title_rect[2] / 2), 520))
            screen.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
            screen.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 360))
            pg.display.update()

    
    pg.quit()