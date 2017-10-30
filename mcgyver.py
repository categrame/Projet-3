import pygame
from pygame.locals import*

from classes import*
from constantes import*

pygame.init()

window = pygame.display.set_mode((window_sprite,window_sprite))

loop = 1
game_loop = 1
while loop:

  background = pygame.image.load("img/background.jpg").convert()
  window.blit(background, (0,0))

  level =Level('lvl')
  level.generate()
  level.display(window)

  mcgyver = Char(level)

  
  while game_loop:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
    
      if event.type == KEYDOWN:
        if event.key == K_RIGHT:
          mcgyver.move('right')
        elif event.key == K_LEFT:
          mcgyver.move('left')
        elif event.key == K_UP:
          mcgyver.move('up')
        elif event.key == K_DOWN:
          mcgyver.move('down')      

    window.blit(background, (0,0))
    level.display(window)
    window.blit(mcgyver.direction, (mcgyver.x, mcgyver.y))
    pygame.display.flip()

    if level.building[mcgyver.case_y][mcgyver.case_x] == 'g':
      pygame.display.quit()
      pygame.quit()