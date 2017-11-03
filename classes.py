#classes.py contain classes for the mcgyver labyrinth project

import pygame
from pygame.locals import*
from constantes import*
import random

#Class who generate level
class Level:

  def __init__(self,file):
    #accepted the "file" argue for the file level
    self.file = file
    self.building = 0

  #read the file and add line in a list
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

  #display the map
  def display(self,window):

    #variable with image per sprite
    wall = pygame.image.load("img/wall.png").convert()
    start = pygame.image.load("img/start.png").convert()
    final = pygame.image.load("img/guard.png").convert()

    #initilization
    line_number = 0
    #for each line in building generate a wall, a departure flag or the guardian in function of sprite_size
    for line in self.building:
      case_number = 0
      for sprite in line:
        x = case_number * SPRITE_SIZE
        y = line_number * SPRITE_SIZE
        if sprite == 'w':
          window.blit(wall,(x,y))
        elif sprite == 'd':
          window.blit(start, (x,y))
        elif sprite =='g':
          window.blit(final,(x,y))
        case_number += 1
      line_number += 1              


#class who generates the character
class Char:

  def __init__(self,level):


    #load the character
    self.image = pygame.image.load('img/mac.png').convert_alpha()

    self.case_x = 0
    self.case_y = 0
    self.x = 0
    self.y = 0
    self.direction = self.image
    self.level = level


  #define the mobility on x and y of the character if the sprite isn't a wall
  def move(self, direction):

    if direction == 'right':
      if self.case_x < (NUMBER_OF_SPRITE - 1):
        if self.level.building[self.case_y][self.case_x+1] != 'w':
          self.case_x += 1
          self.x = self.case_x * SPRITE_SIZE
      self.direction = self.image

    if direction == 'left':
      if self.case_x > 0:
        if self.level.building[self.case_y][self.case_x-1] != 'w':
          self.case_x -= 1
          self.x = self.case_x * SPRITE_SIZE
      self.direction = self.image

    if direction == 'up':
      if self.case_y > 0:
        if self.level.building[self.case_y-1][self.case_x] != 'w':
          self.case_y -= 1
          self.y = self.case_y * SPRITE_SIZE
      self.direction = self.image

    if direction == 'down':
      if self.case_y < (NUMBER_OF_SPRITE - 1):
        if self.level.building[self.case_y+1][self.case_x] != 'w':
          self.case_y += 1
          self.y = self.case_y*SPRITE_SIZE
      self.direction = self.image

#This class generate items and place them randomly on the map. There is also a function to remove it when mcGyver collect them
class Item:

  def __init__(self,img_file, level):

    self.img_file = pygame.image.load(img_file).convert_alpha()
    self.x = 0
    self.y = 0
    self.level = level


  def add(self):
    
    while self.level.building[self.y][self.x] == 'w' or self.level.building[self.y][self.x] == 'd' : 
      self.y = random.randint(1,NUMBER_OF_SPRITE - 1)
      self.x = random.randint(1,NUMBER_OF_SPRITE - 1)
    self.x = self.x*SPRITE_SIZE
    self.y = self.y*SPRITE_SIZE
    return self.x, self.y


  def remove(self):

    self.x = -40
    self.y = -40



