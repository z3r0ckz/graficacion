#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:08:18 2020

@author: zerockz
"""
from pygame import gfxdraw
import sys,pygame
pygame.init()
"tamaño de la pantalla"
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()

"funcion del circulo"
def circulo(radio):
	x,y = 0,radio
	plotCircle(x,y,radio)

def puntosdesimetria(x,y):
	gfxdraw.pixel(screen,x,y,(255,0,0))
	gfxdraw.pixel(screen,-x,y,(255,255,0))
	gfxdraw.pixel(screen,x,-y(128,255,0))
	gfxdraw.pixel(screen,-x,-y(0,255,128))
	gfxdraw.pixel(screen,y,x,(51,253,255))
	gfxdraw.pixel(screen,-y,x,(153,51,255))
	gfxdraw.pixel(screen,y,-x,(255,102,255))
	gfxdraw.pixel(screen,-y,-x,(255,204,255))
	pygame.display.flip()

def plotCircle(x,y,radio):
    x = 0
    y = radio
    d = 3 - (2 * radio)
    
	while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
		puntosdesimetria(x,y,radio)
#valores del circulo 
circulo(100,25) 
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
