#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:59:21 2020

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
def circulo(radio,offset):
	x,y = 0,radio
	plotCircle(x,y,radio,offset)
    
"dibujamos 1/8 del circulo"
#plot circle  dibuja el circulo
# en esta parte dividimos el circulo en 8  octantes y vamos moviendo los
#signos para irnos recorriendo dentro del plano cartesiano
#la parte de X o Y nos da el cuadrante del plano
#y la parte de offset nos dice que parte del octante (borde) estamos dibujando
#si la de arriba o la de abajo del cuarto del circulo
    
def puntosdesimetria(x,y,offset):

	gfxdraw.pixel(screen,y+offset,-x+offset,(255,31,226))
	pygame.display.flip()

def plotCircle(x,y,radio,offset):
	d = 5/4.0 - radio
	puntosdesimetria(x,y,radio+offset)
	while x < y:
		if d < 0:
			x += 1
			d += 2*x + 1
		else:
			x += 1
			y -= 1
			d += 2*(x-y) + 1
		puntosdesimetria(x,y,radio+offset)
#valores del circulo 
circulo(100,25) 
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()