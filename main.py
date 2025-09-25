#Madeline Navea
#mn686
#purpose: main file
#homework 4 -- create a pygame with predator and prey
########################################################
#import packages
import pygame
import random
import time
import os

#import classes
from drawable import Drawable
from fly import Fly
from frog import Frog
from text import Text

#helper functions
#####################BOADY"S QUICK SORT#####################
def partition(arr, start, stop):
    randomIndex = random.randint(start, stop)
    arr[stop], arr[randomIndex] = arr[randomIndex], arr[stop]  # Swap pivot with last
    pivot = arr[stop][1]  # Use the time value (index 1 of tuple) as the pivot
    i = start
    for j in range(start, stop):
        if arr[j][1] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[stop] = arr[stop], arr[i]
    return i

def quickSort(arr, start, stop):
    if start < stop:
        pivot_index = partition(arr, start, stop)
        quickSort(arr, start, pivot_index - 1)
        quickSort(arr, pivot_index + 1, stop)
#####################BOADY"S QUICK SORT#####################


#create game loop to ask player if they wanna keep playing
def playGame(allGames, gameNum):
    #initialize game
    pygame.init()
    surface = pygame.display.set_mode((960, 720))  #window
    pygame.display.set_caption('Welcome to the Pond')  #title
    
    path = os.path.dirname(os.path.abspath(__file__))
    background = pygame.image.load(os.path.join(path, 'background.png')) #background
    flies = []  #prey
    fly1 = Fly(random.randint(0, 960), random.randint(0, 720))  #create flies
    fly2 = Fly(random.randint(0, 960), random.randint(0, 720))
    fly3 = Fly(random.randint(0, 960), random.randint(0, 720))
    fly4 = Fly(random.randint(0, 960), random.randint(0, 720))
    fly5 = Fly(random.randint(0, 960), random.randint(0, 720))
    flies.extend([fly1, fly2, fly3, fly4, fly5])  #add to a list
    fliesEaten = 0
    frog = Frog(100, 500) #predator
    
    #starters
    running = True
    animation = True
    startTime = time.time()
    wonGame = False
    fpsClock = pygame.time.Clock()  #start clock
    

    #while game runs
    while running:
        #all intital event stuff
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):  # exit game
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for fly in flies[:]:
                    if frog.intersects(fly):  # Allow eating anytime
                        flies.remove(fly)
                        fliesEaten += 1
                        pygame.display.update()

        #if they didn't win the game and its over 10 seconds
        if not wonGame and (time.time() - startTime > 10):
            totalTime = round(time.time() - startTime, 2)
            allGames[gameNum] = totalTime

            #show end result (they lost)
            surface.fill((0, 0, 0))
            winLose = Text(x=180, y=200, color=(255, 255, 255), size=120, message=f"You Lost.")
            winloseCont = Text(x=300, y=350, color=(255, 255, 255), size=70, message=f"Try again.")
            winloseCont2 = Text(x=150, y=585, color=(255, 0, 0), size=40, message=f"Beat the game under 10 seconds.")
            winLose.draw(surface)
            winloseCont.draw(surface)
            winloseCont2.draw(surface)
            goForward = Text(x=205, y=650, color=(255, 0, 0), message="Press the right arrow button to view scoreboard.")
            goForward.draw(surface)
            pygame.display.update()

            #wait for response
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        waiting = False

            #scoreboard
            surface.fill((0, 0, 0))
            scoreboard = Text(x=400, y=50, color=(255, 255, 0), message="Scoreboard")
            scoreboard.draw(surface)
            sortedTimes = list(allGames.items()) #sort best times
            quickSort(sortedTimes, 0, len(sortedTimes) - 1) #sort best times
            i = 0
            for gameNum, gameTime in sortedTimes:
                msg = f"Game {gameNum}: {gameTime:.2f} seconds"
                if gameTime >= 10:
                    color = (255, 0, 0)  #red (lost)
                else:
                    color = (0, 255, 0)  #green (won)            
                gameText = Text(x=330, y=120 + i * 30, color=color, message=msg)
                gameText.draw(surface)
                i += 1
            prompt = Text(x=200, y=600, color=(255, 255, 255), message='Play again? Press "Y" for yes or "Q" to Quit.')
            prompt.draw(surface)
            pygame.display.update()

            #wait for response
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            return True
                        elif event.key == pygame.K_q:
                            return False
                        

        #if game is not won, animate frog and flies
        if wonGame == False:
            frog.move(pygame.key.get_pressed())  #move frog
            frogX, frogY = frog.getLoc()
            holdSet = 0
            if frog.left() == False:
                holdSet = 83

            for fly in flies[:]:
                if animation == True:
                    fly.move()
                    fly.move_randomly()
        
        #draw the animations
        surface.blit(background, (0, 0))  # draw background
        for fly in flies:
            fly.draw(surface)  # draw flies
        frog.draw(surface)  # draw frog

        fliesEatenText = Text(x=700, y=20, color=(255, 0, 0), message=f"Flies Eaten: {fliesEaten}/5")
        fliesEatenText.draw(surface)

        #if flies empty
        if flies == []:
            endTime = time.time() #stop time
            wonGame = True #they won the game
            totalTime = round(endTime - startTime, 2)  #calculate total time
            allGames[gameNum] = totalTime  #store game
        
            #show end result (they won)
            surface.fill((0, 0, 0))  #clear screen
            winLose = Text(x=185, y=200, color=(0, 255, 0), size=120, message=f"Congrats!")
            winloseCont = Text(x=85, y=350, color=(0, 255, 0), size=70, message=f"You just won the game!")
            finalScore = Text(x=345, y=600, color=(255, 0, 0), message=f"Your time: {totalTime:.2f} seconds")
            goForward = Text(x=205, y=650, color=(255, 0, 0), message="Press the right arrow button to view scoreboard.")
            winLose.draw(surface)
            winloseCont.draw(surface)
            finalScore.draw(surface)
            goForward.draw(surface)
            pygame.display.update()  #update screen

            #wait for decision from user to move forward or quit
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            waiting = False

            #show scoreboard
            surface.fill((0, 0, 0))
            scoreboard = Text(x=400, y=50, color=(255, 255, 0), message="Scoreboard")
            scoreboard.draw(surface)
            sortedTimes = list(allGames.items()) #sort best times
            quickSort(sortedTimes, 0, len(sortedTimes) - 1) #use boady's quick sort algorithm
            i = 0
            for gameNum, gameTime in sortedTimes:
                msg = f"Game {gameNum}: {gameTime:.2f} seconds"
                if gameTime >= 10:
                    color = (255, 0, 0)  #red (lost)
                else:
                    color = (0, 255, 0)  #green (won)            
                gameText = Text(x=330, y=120 + i * 30, color=color, message=msg)
                gameText.draw(surface)
                i += 1
            prompt = Text(x=200, y=600, color=(255, 255, 255), message='Play again? Press "Y" for yes or "Q" to Quit.') #ask user input
            prompt.draw(surface)
            pygame.display.update()

            #wait for response
            waiting = True #waiting for decision from scoreboard
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #quit
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN: #keytype
                        if event.key == pygame.K_y:
                            return True  # play again
                        elif event.key == pygame.K_q: #quir
                            return False

        else:
            timeTaken = round(time.time() - startTime, 2) #timer since the start of the game
            timerText = Text(x=50, y=20, color=(255, 0, 0), message=f"Time: {timeTaken}s") #show timer in top left
            timerText.draw(surface)
            pygame.display.update()
        
        fpsClock.tick(60) #make flies go fast

    return totalTime #to append to full game dict


if __name__ == '__main__':
    allGames = {}
    gameNum = 1
    running = True
    while running:
        running = playGame(allGames, gameNum)
        gameNum += 1
