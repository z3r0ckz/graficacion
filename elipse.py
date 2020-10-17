#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:00:19 2020

@author: zerockz
"""

from pygame import gfxdraw
import sys,pygame
pygame.init()
"tamaño de la pantalla del display"
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()
"Color de la linea del elipse "
green = (128,255,0)
aqua = (0,255,128)
blue = (0,128,255)
purple = (153,51,255)
"Funcion de simetria de la elipse"
"se logra al cambiar los signos segun en que parte dle plano cartesiano este"
"++,-+,+-,--"

def simetriaelipse(x,y):
	x,y = int(x),int(y)
	gfxdraw.pixel(screen,x+150,y+150,green)
	gfxdraw.pixel(screen,-x+150,y+150,aqua)
	gfxdraw.pixel(screen,x+150,-y+150,blue)
	gfxdraw.pixel(screen,-x+150,-y+150,purple)

"funcion de la elipse"
"graficacion de linea basica del elipse"
#F(x,y)=b2x2+a2y2-a2b2=0 formula para graficar el elipse 
def elipse(rx,ry):
	rx,ry = float(rx),float(ry)
	x = 0
	y = ry
	d1 = (ry**2)-(rx*rx*ry)+(1/(4*rx*rx))
	dx = float(2*ry*ry*x)
	dy = float(2*rx*rx*y)

	while dx < dy:
		if d1 < 0:
			x += 1
			dx += 2*ry*ry
			d1 += dx + ry*ry
		else:
			x += 1
			y -= 1
			dx += 2*ry*ry
			dy -= 2*rx*rx
			d1 += dx-dy+ry*ry
		simetriaelipse(x,y)

	d2=(ry*ry)*((x+1/2.0)*(x+1/2.0))+(rx*rx*(y-1)*(y-1))-(rx*rx*ry*ry)

	while y > 0:
		if d2 > 0:
			y -= 1
			dy -= 2*rx*rx
			d2 -= dy + rx*rx
		else:
			x += 1
			y -= 1
			dy -= 2*rx*rx
			dx += 2*ry*ry
			d2 += dx-dy+rx*rx
		simetriaelipse(x,y)
	pygame.display.flip()

elipse(120,60)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()