import pygame
from pygame.locals import*
from constantes import*

class Level:

  def __init__(self,file):
    self.file = file
    self.building = 0

  def generate(self):

    with open(self.file, "r") as file:

      level_building = []

      for line in file:
        line_level = []

        for sprite in line:
          if sprite != '\n':
            line_level.append(sprite)

        level_building.append(line_level)
      
      self.building = level_building

  def display(self,window):

    wall = pygame.image.load("img/wall.png").convert()
    start = pygame.image.load("img/start.png").convert()
    final = pygame.image.load("img/final.png").convert()

    line_number = 0
    for line in self.building:
      case_number = 0
      for sprite in line:
        x = case_number * sprite_size
        y = line_number * sprite_size
        if sprite == 'w':
          window.blit(wall,(x,y))
        elif sprite == 'd':
          window.blit(start, (x,y))
        elif sprite =='g':
          window.blit(final,(x,y))
        case_number += 1
      line_number += 1              
