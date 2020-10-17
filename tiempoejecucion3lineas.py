#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:44:31 2020

@author: zerockz
"""

import sys,pygame
from pygame import gfxdraw
from timeit import default_timer 
    
    

pygame.init()
screen = pygame.display.set_mode((200,200))
screen.fill((0,0,0))
pygame.display.flip()
"color de la linea en rgb"
"amarilla bresenham"
yellow = (255,255,0)
"blanca DDA"
white=(255,255,255)
"verde linea basica"
green = (0,255,51)    
    

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
    
    
def ROUND(n):
	return int(n+0.5)

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
        
        

"Tiempo de ejecucion de basica"
inicio = default_timer()    
"coordenadas de basica"
basica(10,10,100,100)
print("ejecucion basica-verde")
fin = default_timer()
int(fin)
int(inicio)
print(fin-inicio)



"Tiempo de ejecucion de DDA"
inicio = default_timer()    
"coordenadas de DDA"
dda(10,40,180,200)
print("ejecucion DDA-Blanco")
fin = default_timer ()
int(fin)
int(inicio)
print(fin-inicio)

"Tiempo de ejecucion de Bresenham"
inicio = default_timer()    
"coordenadas de bresenham"
bresenham(0,20,155,150)
print("ejecucion Bresenham-Amarillo")
int(inicio)
int(fin)
fin = default_timer()
print(fin-inicio)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()