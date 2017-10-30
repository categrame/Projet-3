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
    final = pygame.image.load("img/guard.png").convert()

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


class Char:

  def __init__(self,level):


    self.image = pygame.image.load('img/mac.png').convert_alpha()

    self.case_x = 0
    self.case_y = 0
    self.x = 0
    self.y = 0
    self.direction = self.image
    self.level = level


  def move(self, direction):

    if direction == 'right':
      if self.case_x < (number_of_sprite - 1):
        if self.level.building[self.case_y][self.case_x+1] != 'w':
          self.case_x += 1
          self.x = self.case_x * sprite_size
      self.direction = self.image

    if direction == 'left':
      if self.case_x > 0:
        if self.level.building[self.case_y][self.case_x-1] != 'w':
          self.case_x -= 1
          self.x = self.case_x * sprite_size
      self.direction = self.image

    if direction == 'up':
      if self.case_y > 0:
        if self.level.building[self.case_y-1][self.case_x] != 'w':
          self.case_y -= 1
          self.y = self.case_y * sprite_size
      self.direction = self.image

    if direction == 'down':
      if self.case_y < (number_of_sprite - 1):
        if self.level.building[self.case_y+1][self.case_x] != 'w':
          self.case_y += 1
          self.y = self.case_y*sprite_size
      self.direction = self.image