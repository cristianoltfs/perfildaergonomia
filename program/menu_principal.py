#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:38:16 2021

@author: joao
"""

import pygame
import os
from pygame.locals import *
from sys import exit
#inicializar todas as funcoes
pygame.init()
altura=768
largura=1366
    # Game Initialization
pygame.init()
     
    # Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
     
    # Game Resolution
screen_width=1366
screen_height=768
screen=pygame.display.set_mode((largura, altura))
     
    # Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
     
    return newText
     
     
white=(255, 255, 255)

black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=( 73, 151, 216)
blue2=(   66, 191, 254 )
yellow=(255, 255, 0)
     
font2 = pygame.font.SysFont('arial',25,False, False)
font_title = pygame.font.SysFont('arial',15,False, False)

clock = pygame.time.Clock()
FPS=40

menu=True
selected="start"
menu=True
som=pygame.mixer.Sound('inicio.wav')
botao=pygame.mixer.Sound('smw_kick.wav')
som.play()
background = pygame.image.load('fundo_jogo.png')
logo = pygame.image.load('ergonomia_logo.png').convert_alpha()

logo = pygame.transform.scale(logo, (200, 200))
logo_rect= logo.get_rect()

logo_rect.x = screen_width/2 - 100
logo_rect.y = 100
screen.blit(background,(0,0))
#screen.blit(logo_rect,(0,0))
screen.blit(logo, logo_rect)
#screen.blit((logo), (0,0,altura/2,largura/2)) 
while menu:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                selected="start"
            elif event.key==pygame.K_DOWN:
                selected="quit"
            if event.key==pygame.K_RETURN:
                if selected=="start":
                    print("Start")
                if selected=="quit":
                    pygame.quit()
                    quit()
                    
        #screen.fill(blue)
        title=font_title.render('Seja bem vindo ao Perfil da ergonomia! Um jogo criado dentro da UFOP!',True, white)
        sub_title=font_title.render('Colaboradores: José da Silva, Aline Santos, Joana Smith, Fabricio',True,white)

        if selected=="start":
            
            text_start=font2.render('Iniciar',True, white)
            
            (x, y, width, height) = (largura/2.35,altura/2.65,200,50)
            border_width = 1
            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
            #pygame.draw.rect(screen, blue2, (x, y, width-1, height-1),border_radius=9)

        else:
            text_start=font2.render('Iniciar',True, black)

            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
            (x, y, width, height) = (largura/2.35,altura/2.65,200,50)
            border_width = 1
            
            #pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)

        if selected=="quit":
            text_quit=font2.render('Sair',True, white)
            botao.play()

            (x, y, width, height) = (largura/2.35,altura/2.20,200,50)
            border_width = 1
            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
            #pygame.draw.rect(screen, blue2, (x, y, width-1, height-1),border_radius=9)
            
            
            

        else:
            
            text_quit=font2.render('Sair',True, black)
            
            (x, y, width, height) = (largura/2.35,altura/2.20,200,50)
            border_width = 1
            
            pygame.draw.rect(screen, white, (x, y, width, height),border_radius=9, width=border_width)
     
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
     
            # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 500))
        screen.blit(sub_title, (screen_width/2 - (title_rect[2]/2), 520))

        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)


   

