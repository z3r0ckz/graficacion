#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:47:49 2020

@author: zerockz
"""

import sys,pygame
from pygame import gfxdraw

pygame.init()
"tamaño de la ventana desplegada"
screen = pygame.display.set_mode((200,200))
"color de la ventana"
screen.fill((0,0,0))
"para que muestre la linea"
pygame.display.flip()
"color de la linea RGB"
green=(0,255,51)

"Declaramos la pendiente"
"Calculo basico de la pendiente para poder graficar"
m=0

def basica(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    
    gfxdraw.pixel(screen,x1,y1,green)
    
    x=x1
    y=y1
    X=x2

    if(m<1):
        b=y-m*X
        for x in range(x1+1,x2):
            y=m*x+b
            ++x
            gfxdraw.pixel(screen,x,y,green)
    else:
        b=y-m*X
        for y in range(y1+1,y2):
          x=(y-b)/m
          ++y
          gfxdraw.pixel(screen,int(x),int(y),green)
        pygame.display.flip()
        
"coordenadas basicas"
basica(10,10,100,100)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()