import pygame
from pygame.locals import*

from classes import*
from constantes import*
import random

pygame.init()

window = pygame.display.set_mode((window_sprite,window_sprite))

loop = 1
game_loop = 1
lethal_item = 0
while loop:

  background = pygame.image.load("img/background.jpg").convert()
  window.blit(background, (0,0))

  level =Level('lvl')
  level.generate()
  level.display(window)

  mcgyver = Char(level)

  obj1 = Item('img/aiguille.png',level)
  obj1.add()
  obj2 = Item('img/ether.png',level)
  obj2.add()
  obj3 = Item('img/tube.png',level)
  obj3.add()
  
 

  
  

  
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
    window.blit(obj1.img_file, (obj1.x, obj1.y))
    window.blit(obj2.img_file, (obj2.x, obj2.y))
    window.blit(obj3.img_file, (obj3.x, obj3.y))
    window.blit(mcgyver.direction, (mcgyver.x, mcgyver.y))
    

    if level.building[mcgyver.case_y][mcgyver.case_x] == 'g' and lethal_item == 3:
      pygame.display.quit()
      pygame.quit()
    elif level.building[mcgyver.case_y][mcgyver.case_x] == 'g' and lethal_item != 3:
      print("you lose")

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