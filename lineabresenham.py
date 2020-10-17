# -*- coding: utf-8 -*-
"""
Editor de Spyder
z3r0ckz
Este es un archivo temporal.
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
"color de la linea"
yellow=(255,255,0)


def bresenham(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1

	D = 2*dy - dx
	gfxdraw.pixel(screen,x1,y1,yellow)
	y = y1
    
	for x in range(x1+1,x2+1):
		if D > 0:
			y += 1
			gfxdraw.pixel(screen,x,y,yellow)
			D += (2*dy-2*dx)
		else:
			gfxdraw.pixel(screen,x,y,yellow)
			D += 2*dy
	pygame.display.flip()
    
bresenham(0,20,155,150)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()