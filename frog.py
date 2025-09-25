#Header:
#Madeline Navea
#mn686
#purpose: file for frog class
#homework 4 -- create a pygame with predator and prey

#import packages
from drawable import *
import pygame
import random
import os

#import pngs of frogs in a list
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "frog")
frogs = []
frog1 = pygame.image.load(os.path.join(path, "frog1.png"))
frog1 = pygame.transform.scale(frog1, (200, 200))
frogs.append(frog1)
frog2 = pygame.image.load(os.path.join(path, "frog2.png"))
frog2 = pygame.transform.scale(frog2, (200, 200))
frogs.append(frog2)
frog3 = pygame.image.load(os.path.join(path, "frog3.png"))
frog3 = pygame.transform.scale(frog3, (200, 200))
frogs.append(frog3)
frog4 = pygame.image.load(os.path.join(path, "frog4.png"))
frog4 = pygame.transform.scale(frog4, (200, 200))
frogs.append(frog4)


class Frog(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__frogs = frogs #all frogs
        self.__frame = 0 #which frop png to show
        self.__moving = False #if theyre moving
        self.__counter = 0 #when to show png
        self.__lookLeft = False #flip png
        self.__jump = False #go up
        self.__up = 0  #how much to go up

    def get_rect(self):
        location = self.getLoc()
        return pygame.Rect([location[0] - 20, location[1] - 20, 30, 30])
    
    def left(self):
        return self.__lookLeft
    
    def draw(self, surface):
        x, y = self.getLoc()
        image = self.__frogs[self.__frame]
        if self.__lookLeft == True and self.isVisible() == True:
            image = pygame.transform.flip(image, True, False)
        surface.blit(image, (x - 100, y - 100))

    #not using this
    #def follow_mouse(self):
    #    mouse_x, mouse_y = pygame.mouse.get_pos()
    #    self.setLoc((mouse_x, mouse_y))

    #move frog when left/right keys are used
    def move(self, keys):
        x, y = self.getLoc()
        self.__moving = False #dont let it move until key pressed
        if keys[pygame.K_LEFT]: #move left
            x -= 5
            self.__moving = True
            self.__lookLeft = True
        elif keys[pygame.K_RIGHT]: #move right
            x += 5
            self.__moving = True
            self.__lookLeft = False
        if keys[pygame.K_UP] and self.__jump == False: #jump
            self.__jump = True
            self.__up = -30
        if self.__jump == True: #if frog jump
            self.__up += 1 #make frog move up
            y += self.__up
            if y >= 500: #if frog more than og position
                y = 500 #set back to og position
                self.__up = 0 
                self.__jump = False #stop jump
        self.setLoc((x, y))

        #animation png frame types
        if self.__jump == True: #if frog jumping
            if self.__up < 0: #if frog go up..
                self.__frame = 1 #show jump up png
            else: #if frog go down..
                self.__frame = 2 #show frog fall png
        elif self.__moving == True:  #if frog moves
            self.__counter += 1 
            if self.__counter % 5 == 0: #every 5 frames
                self.__frame = 1 + (self.__frame % 2) #show png 1 and 2
        else: #if frog not moving or jumping
            if (self.__jump == False) and (y == 500): #if frog not jumping and on ground...
                self.__frame = 3 #show png 3
            else:
                self.__frame = 0 #show png1 (stand still)

