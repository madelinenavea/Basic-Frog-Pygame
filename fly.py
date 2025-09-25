#Madeline Navea
#mn686
#purpose: file for fly class
#homework 4 -- create a pygame with predator and prey

#import packages
from drawable import *
import pygame
import random
import os
import math


path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "flies")
flies = []
for fly in os.listdir(path):
    flies.append(fly)
    print(fly)
print(flies)

class Fly(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__img = pygame.image.load(os.path.join(path, random.choice(flies)))
        self.__img = pygame.transform.scale(self.__img, (30, 30))
        self.__xSpeed = 1.5
        self.__ySpeed = 1.5

    def get_rect(self):
        location = self.getLoc()
        return pygame.Rect([location[0] - 15, location[1] - 15, 30, 30])

    def draw(self, surface):
        location = self.getLoc()
        #pygame.draw.rect(surface, (123, 123, 123), self.get_rect())
        if self.isVisible():
            surface.blit(self.__img, (location[0] - 15, location[1] - 15))

    def move(self):
        #change x and y by some amount
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= 0 or newX >= width:
            self.__xSpeed *= -1
        if newY <= 0 or newY >= height:
            self.__ySpeed *= -1

    def move_randomly(self):
        x, y = self.getLoc()
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)
        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if x <= 0 or x >= width:
            x = max(0, min(x, width))
        if y <= 0 or y >= height:
            y = max(0, min(y, height))

        self.setLoc((x, y))

    