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
white=(255,255,255)
"funcion de redondeo"
def ROUND(n):
	return int(n+0.5)
"funcion de DDA"
"Se efectúa un muestreo de la línea e intervalos unitarios en una coordenada y "
"se determinan los valores enteros correspondientes más próximos a la "
"trayectoria de la línea para la otra coordenada"
"va dibujando en pantalla y redondeando los valores del calculo ln 32"
def dda(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
    
	for i in range(length):
		x+= dx
		y+= dy
		gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
	pygame.display.flip()
"valores dda"
dda(10,40,180,200)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()