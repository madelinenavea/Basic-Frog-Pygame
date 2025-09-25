#Header:
#Madeline Navea
#mn686
#purpose: abstract class Drawable
#homework 4 -- create a pygame with predator and prey

#import packages
from abc import ABC, abstractmethod
import pygame 
class Drawable(ABC):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        self.__visible = True
    
    # getter
    def getLoc(self):
        return (self.__x, self.__y)
    
    # setters
    def setLoc(self, point):
        self.__x = point[0]
        self.__y = point[1]
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y

    #visibility
    def isVisible(self):
        return self.__visible
    def setVisible(self, visible):
        self.__visible = visible

    #for when frog eats fly
    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        return rect1.colliderect(rect2) 

    # abstract methods
    @abstractmethod
    def draw(self, surface): # draw object on screen
        pass
    @abstractmethod
    def get_rect(self): # return bounding box
        pass
