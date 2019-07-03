import pygame
import sys
import random
pygame.init()
screen=pygame.display.set_mode((400,400))

game_over=False
clock=pygame.time.Clock()
x=60
y=60
a=0
score=0
rand_x=50
rand_y=50
myFont=pygame.font.SysFont("comicsansms",35)
pygame.display.set_caption("Snako Gecko 1")
def collision(x,y,rand_x,rand_y):
	f=random.randint(0,400)
	g=random.randint(0,370)
	new_x=x+15
	new_y=y+15
	l=False
	if abs(rand_x-new_x)<=20 and abs(rand_y-new_y)<=20:
		rand_x=f
		rand_y=g
		l=True
	if l== True:
		return [rand_x,rand_y,8]
	else:
		return [rand_x,rand_y,0]

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over=True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				#pygame.quit()
				sys.exit()
			if event.key == pygame.K_UP:
				a=1
			if event.key == pygame.K_DOWN:
				a=2
			if event.key == pygame.K_LEFT:
				a=3
			if event.key == pygame.K_RIGHT:
				a=4
	
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(0,255,0),pygame.Rect(x,y,30,30))
	pygame.draw.circle(screen,(245, 66, 87),(rand_x,rand_y),5)
	if a==1:
		y-=5
	if a==2:
		y+=5
	if a==3:
		x-=5
	if a==4:
		x+=5
	if y<=-30:
		y=400
		y-=5
	if y>=400:
		y=-30
		y+=5
	if x<=-30:
		x=400
		x-=5
	if x>=400:
		x=-30
		x+=5
	coll=collision(x,y,rand_x,rand_y)
	rand_x=coll[0]
	rand_y=coll[1]
	score+=coll[2]
	text= "SCORE: "+ str(score)
	print(text)
	l=myFont.render(text,1,(255,255,255))
	screen.blit(l,(200,350))
	clock.tick(30)
	pygame.display.update()