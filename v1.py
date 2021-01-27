import pygame
import time
import random
from pygame.locals import*
a = pygame.image.load('a.bmp')
b = pygame.image.load('b.bmp')
c = pygame.image.load('c.bmp')
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 80)

pygame.display.set_caption("Escurabutxaques")
w = 1024
h = 720

white = (255,255,255)
red = (255, 64, 64)
black = (0,0,0)
size=(w,h)
count = 1
dis = a
dis2 = b
dis3 = c
screen = pygame.display.set_mode(size) 
textsurface = myfont.render('Roll!', False, (255, 255, 255))

	
while True:
	screen.fill(red)
	
	pygame.draw.rect(screen, black, (312,450,400,150))
	screen.blit(textsurface,(460,500))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	
	if pygame.mouse.get_pressed() ==(1, 0, 0):
			number = random.randint(1,10)
			if number == 10:
				dis = c
			if number == 9:
				dis = c	
			if number == 8:
				dis = b
			if number == 7:
				dis = b
			if number == 6:
				dis = b
			if number == 5:
				dis = a
			if number == 4:
				dis = a
			if number == 3:
				dis = a
			if number == 2:
				dis = a
			if number == 1:
				dis = a
			if number == 10:
				dis2 = c
			if number == 9:
				dis2 = c	
			if number == 8:
				dis2 = b
			if number == 7:
				dis2 = b
			if number == 6:
				dis2 = b
			if number == 5:
				dis2 = a
			if number == 4:
				dis2 = a
			if number == 3:
				dis2 = a
			if number == 2:
				dis2 = a
			if number == 1:
				dis2 = a
			number = random.randint(1,10)
			if number == 10:
				dis3 = c
			if number == 9:
				dis3 = c	
			if number == 8:
				dis3 = b
			if number == 7:
				dis3 = b
			if number == 6:
				dis3 = b
			if number == 5:
				dis3 = a
			if number == 4:
				dis3 = a
			if number == 3:
				dis3 = a
			if number == 2:
				dis3 = a
			if number == 1:
				dis3 = a

	

	screen.blit(dis,(100,100))
	screen.blit(dis2,(408,100))
	screen.blit(dis3,(716,100))
	
	pygame.display.update()
	time.sleep(0.01)