import pygame
from pygame.locals import*

from classes import*
from constantes import*

pygame.init()

window = pygame.display.set_mode((window_sprite,window_sprite))

loop = 1
while loop:

  background = pygame.image.load("img/background.jpg").convert()
  window.blit(background, (0,0))

  level =Level('lvl')
  level.generate()
  level.display(window)

  pygame.display.flip()