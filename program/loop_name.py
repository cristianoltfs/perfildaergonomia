import pygame as pg
import draw_window as dw
import loop_board as lb
from pygame import gfxdraw
import loop_players as lp

def loop_name(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT, sound_on, sound_off):
    pg.init()
    room=list(range(1,101))
    
    logo_begin = pg.image.load('resources/images/logo_reduzida.png')

    text_sound = pg.mixer.Sound('resources/sounds/text.ogg')
    botton_click_sound = pg.mixer.Sound('resources/sounds/smw_kick.wav')


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
    screen.blit(sound_on, (WIDTH/1.03, 10))

    screen.blit(logo_begin, (WIDTH/2 -124,80))
    
    (x, y, width, height) = (WIDTH / 2.35, HEIGHT / 2.65, 200, 50)


    #Nome dos jogadores
    pg.draw.rect(screen, DARKBLUE, (x,y,width+2,height+52),border_radius=9, width=2)
    pg.draw.rect(screen, BLUE, (x,y,width,height+50),border_radius=9)
    user_text = ''
    user_text_2 = ''

    base_font = pg.font.SysFont(None, 35)
    input_rect=pg.Rect(x+5,y+30,190,65)
    
    input_rect_room=pg.Rect(x+5,y+145,190,55)

    active = False
    active_2=False
    color=BABYBLUE
    color_2=BABYBLUE

    font_title = pg.font.SysFont(None, 30)
    name_player=''
    ok=False

    font_title = pg.font.SysFont('arial',20,False, False)
    #sala
    pg.draw.rect(screen, DARKBLUE, (x,y+120,width+2,height+42),border_radius=9, width=2)
    pg.draw.rect(screen, BLUE, (x,y+120,width,height+40),border_radius=9)

    while run:
        clock.tick(60)
        event_list = pg.event.get()
        sub_title = font_title.render('Insira seu nome: ', False,BABYBLUE)
        screen.blit(sub_title, (x+5,y+5,190,35))
        title_room = font_title.render('Número da sala: ', False,BABYBLUE)
        screen.blit(title_room, (x+5,y+120,190,35))

        
        
        
        for event in event_list:
            # botoes do teclado
            if event.type == pg.QUIT:
                run = False
                
            mouse = pg.mouse.get_pos()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                # limitando posicao x e y do campo mouse
                #apertando os botoes
                

                if mouse[0] > WIDTH/1.03 and mouse[1] > 10 and mouse[0] < WIDTH/1.03 + 34 and mouse[1] < 10 + 34 and musica == 1:
                    screen.blit(sound_off, (WIDTH / 1.03, 10))
                    pg.mixer.music.set_volume(0)
                    musica = 0

                elif mouse[0] > WIDTH/1.03 and mouse[1] > 10 and mouse[0] < WIDTH/1.03 + 34 and mouse[1] < 10 + 34 and musica == 0:
                    pg.mixer.music.set_volume(0.4)
                    screen.blit(sound_on, (WIDTH / 1.03, 10))
                    musica = 1


            mouse = pg.mouse.get_pos()
            
            
            if event.type == pg.MOUSEBUTTONDOWN:
                
                if input_rect.collidepoint(event.pos):
                    active = not active
                    
                else:
                    active = False
                if input_rect_room.collidepoint(event.pos):
                    active_2=not active_2
                else: 
                    active_2=False
                    
                color = DARKBLUE if active else BABYBLUE
                color_2 = DARKBLUE if active_2 else BABYBLUE

                


            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        name_player=user_text
                        print(name_player)
                        arquivo = open('nome.txt', 'a')
                        arquivo.truncate(0)                        
                     
                        arquivo.writelines(user_text)
                        arquivo.close()                          
                        user_text = ''
                        botton_click_sound.play()
              

                    elif event.key == pg.K_BACKSPACE:
                        user_text = user_text[:-1]
                        text_sound.play()
                 
                    else:
                        user_text += event.unicode       
                        text_sound.play()
                       
                        
                    if len(user_text)>=15:
                        user_text = user_text[:-1]                        
                    
                    
            pg.draw.rect(screen,color,input_rect,border_radius=8)
            text_surface = base_font.render(user_text,True,WHITE)
            
            screen.blit(text_surface,(input_rect.x + 5,input_rect.y))
            if ok:
               
                lp.loop_players(FPS, screen, WHITE, BLACK, BABYBLUE, BLUE, DARKBLUE, BORDERWIDTH, WIDTH, HEIGHT, sound_on, sound_off)
                #numero da sala
            if event.type == pg.KEYDOWN:
                if active_2:
                    if event.key == pg.K_RETURN:
                        room=user_text_2
                        ok=True
                        print(name_player)
                        arquivo_2 = open('sala.txt', 'a')
                        arquivo_2.truncate(0)                        
                        arquivo_2.writelines(user_text_2)
                        arquivo_2.close()                          
                        user_text_2 = ''
                        
                        botton_click_sound.play()
                       
                        
                        
                        user_text_2 = ''
                    elif event.key == pg.K_BACKSPACE:
                        user_text_2 = user_text_2[:-1]
                        text_sound.play()

                    else:
                        user_text_2 += event.unicode  
                        text_sound.play()
                        
                    if len(user_text_2)>=4:
                        user_text_2 = user_text_2[:-1]                    
                    
            pg.draw.rect(screen,color_2,input_rect_room,border_radius=8)
            text_surface = base_font.render(user_text_2,True,WHITE)
            screen.blit(text_surface,(input_rect_room.x + 5,input_rect_room.y))
            pg.display.update()
            clock.tick(FPS)
          

    pg.quit()
