# -*- coding: utf-8 -*-
import pygame
import random
pygame.init()

#colors
white = (255,255,255)
red  = (255,0,0)
green = (66, 245, 206)
blue = (0,0,255)
black = (0,0,0)
yellow = (245, 233, 66)
screen_width = 1000
screen_height = 600

# creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("SnakeWithRajiv")
pygame.display.update()

#game specific variable



clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

with open("highscore.txt", 'r') as f:
	highscore = f.read()
def text_score(text,color,x,y):
	screen_text = font.render(text,True,color)  
	gameWindow.blit(screen_text,[x,y])

def snk_plot(gameWindow,color,snk_list,snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])



#game Loop
def gameloop():
	exit_game = False
	game_over = False
	snake_x = 45 ; snake_y = 55 ; score = 0
	vel_x = 0 ;vel_y = 0
	food_x, food_y  = random.randint(50,screen_width/2), random.randint(50,screen_height/2) 
	food_size = 10
	init_velocity = 5
	snake_size = 10
	fps = 40
	snk_list = []
	snk_length  = 1
	while not exit_game:
		if game_over:
			gameWindow.fill((245, 144, 66))
			text_score(" Game Over !! ",black, 400, 250)
			text_score(" Press Enter to continue....",black, 250, 350)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						gameloop()
		else:
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						vel_x = init_velocity ; vel_y = 0

					if event.key == pygame.K_LEFT:
						vel_x = -init_velocity ; vel_y = 0

					if event.key  == pygame.K_UP:
						vel_y = -init_velocity ; vel_x = 0

					if event.key == pygame.K_DOWN:
						vel_y = init_velocity ; vel_x = 0

			snake_x += vel_x
			snake_y += vel_y
			if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
				score+=10
				food_x, food_y  = random.randint(0,screen_width/2), random.randint(0,screen_height/2)        
				snk_length +=5
				print(highscore)
			
			gameWindow.fill(green)
			text_score("Score: "+ str(score*10),red,5,5)
			pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])

			head = []
			head.append(snake_x) ; head.append(snake_y)
			snk_list.append(head)

			if len(snk_list)>snk_length:
				del snk_list[0]

			if head in snk_list[:-1]:
				game_over = True	
			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
				game_over  =  True
				
			snk_plot(gameWindow,blue,snk_list,snake_size)	    
		
		pygame.display.update()
		clock.tick(fps)
	
	pygame.quit()
	quit()
gameloop()