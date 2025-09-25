#Madeline Navea
#mn686
#purpose: file for text class
#homework 4 -- create a pygame with predator and prey

#import packages
import pygame
from drawable import Drawable

class Text(Drawable):
    def __init__(self, message="Pygame", x=0, y=0,color=(0,0,0), size=24): #set defaults
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size) #choose font
    
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color) #render
        surface.blit(self.__surface, (int(self.getLoc()[0]), int(self.getLoc()[1]))) #draw it on surface

    def get_rect(self):
        location = self.getLoc()
        return pygame.Rect([location[0] - 15, location[1] - 15, 30, 30])
    
    def setMessage(self, message):
        self.__message = message
