"""\\\\mcgyver.py, by Martin Gaucher, 11/02/2017 ////
This game is a labyrinth where Mc Gyver must collect items to create a syringe
and sting the guard to escape the jail. """

#importation of all library needed to run the game

import pygame
from pygame.locals import*

from classes import*
from constantes import*
#random library for items
import random 

#pygame initialization
pygame.init()

#define the game area
window = pygame.display.set_mode((WINDOW_SPRITE,WINDOW_SPRITE))
#window name
pygame.display.set_caption(WINDOW_TITLE)

#sound use in game
home_sound = pygame.mixer.music.load("music/generique2.wav")
applause = pygame.mixer.Sound("music/applause.wav")
final_sound = pygame.mixer.Sound("music/final_scream.wav")

#initialize variable
loop = 1
lethal_item = 0
choix = 0

#main loop
while loop:

	#main screen image 
	home = pygame.image.load("img/mcgyveropening.png")
	window.blit(home, (0,0))

	#refresh
	pygame.display.flip()

	game_loop = 1
	home_loop = 1
	pygame.mixer.music.load("music/generique2.wav")
	pygame.mixer.music.play()

	#home loop wich display the menu to play or leave the game
	while home_loop:

		#timer for the loop : 30 ms
		pygame.time.Clock().tick(30)


		#listener for event
		for event in pygame.event.get():

			#condition to leave the game if Esc is pressed
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				loop = 0
				game_loop = 0
				home_loop = 0
				pygame.mixer.music.stop()
				pygame.quit()

			#condition to play the game if F1 is pressed
			elif event.type == KEYDOWN:
				if event.key == K_F1:
					home_loop = 0
					choix = 1
					pygame.mixer.music.stop()


	#if the user pressed F1 => generate map and character
	if choix == 1:
		background = pygame.image.load("img/background.jpg").convert()
		window.blit(background, (0,0))

		#Generate the level and display it
		level =Level('lvl')
		level.generate()
		level.display(window)

		#Generate McGyver
		mcgyver = Char(level)

		#Generate and place randomly three items
		obj1 = Item('img/aiguille.png',level)
		obj1.add()
		obj2 = Item('img/ether.png',level)
		obj2.add()
		obj3 = Item('img/tube.png',level)
		obj3.add()

		pygame.mixer.music.load("music/main_music.wav")
		pygame.mixer.music.play()

	#main game loop
	while game_loop:

		noplay = 0 #variable to avoid the death song when the variable lethal_item is reinitialize
		pygame.time.Clock().tick(30)
		pygame.display.flip()

		for event in pygame.event.get():

			#keys to move McGyver
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					mcgyver.move('right')
				elif event.key == K_LEFT:
					mcgyver.move('left')
				elif event.key == K_UP:
					mcgyver.move('up')
				elif event.key == K_DOWN:
					mcgyver.move('down')      

		#refresh and replace mcGyver and items on the map
		window.blit(background, (0,0))
		level.display(window)
		window.blit(obj1.img_file, (obj1.x, obj1.y))
		window.blit(obj2.img_file, (obj2.x, obj2.y))
		window.blit(obj3.img_file, (obj3.x, obj3.y))
		window.blit(mcgyver.direction, (mcgyver.x, mcgyver.y))

		#condition to back to menu if ESC is pressed
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				game_loop = 0
				home_loop = 1
				pygame.mixer.music.stop()


		#condition to win the game : collect items and go to the guardian
		if level.building[mcgyver.case_y][mcgyver.case_x] == 'g' and lethal_item == 3:
			applause.play()
			pygame.mixer.music.stop()
			win_menu = 1
			noplay = 1
			game_loop = 0
			lethal_item = 0


			while win_menu:

				win = pygame.image.load("img/win.png")
				window.blit(win, (0,0))
				pygame.display.flip()

				for event in pygame.event.get():

					if event.type == KEYDOWN and event.key == K_F1:
						home_loop = 1
						win_menu  = 0
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						pygame.quit()

		#the game is lose when mcGyver face the guard whithout the 3 items 	
		elif level.building[mcgyver.case_y][mcgyver.case_x] == 'g' and lethal_item != 3 and noplay != 1:
			game_loop = 0
			home_loop = 1
			lose_menu = 1
			final_sound.play()
			pygame.mixer.music.stop()

			while lose_menu:

				win = pygame.image.load("img/lose.png")
				window.blit(win, (0,0))
				pygame.display.flip()

				for event in pygame.event.get():

					if event.type == KEYDOWN and event.key == K_F1:
						home_loop = 1
						lose_menu  = 0
						lethal_item = 0
					elif event.type == KEYDOWN and event.key == K_ESCAPE:
						pygame.quit()
			

		#three conditions to get items when mcGyver is on the same position than them
		if mcgyver.x == obj1.x and mcgyver.y == obj1.y:

			obj1.remove()
			lethal_item +=1

		elif mcgyver.x == obj2.x and mcgyver.y == obj2.y:
			obj2.remove()
			lethal_item +=1

		elif mcgyver.x == obj3.x and mcgyver.y == obj3.y:
			obj3.remove()
			lethal_item +=1   

		pygame.display.flip()
