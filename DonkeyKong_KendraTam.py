# Kendra Tam
# DonkeyKong_KendraTam.py
# May 27, 2016
# This program is simulating the arcade game Donkey Kong

#importing
import pygame, sys
from pygame.locals import *
import random

#Define Colour Values (R,G,B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
PURPLE = (170, 0, 225)
colours = [GREEN, RED, LIGHTBLUE, YELLOW, PURPLE]

#declaring global variables
leaderboard = {}

score = 0
highestScore = 0
levelNum = 0
difficulty = 0

replay = True
pressed = False
climbDone = False
introDone = False
startDone = False
startOutput = False
gameStart = False
throwBarrel = False
jumpLeft = False
jumpRight = False
jumpStill = False
hit = False
deathScene = False
gameDone = False
winGame = False
winLevel = False
scoreWin = False
winGameSceneOutput = False
winGameSceneDone = False

option = "top"
direction = "right"

platformsX = [55, 55, 51, 60, 56, 56, 56]
platformsY = [9, 10, 8, 9, 11, 9, 9, 11]
platNum = 0

dkClimb = 0
climbCount = 15
platNum = 0
dkJumpX = 378
dkJumpY = 172
dkJumpYNum = 0

marioX = 150
marioY = 720
addJump = -7
jumpCount = 0
jumpPoint = 0
deathCount = 0
lives = 2

barrelX = []
barrelY = []
throwCountdown = 0
barrelDirection = []
fall = []
fallCount = []
barrelLeft = []
barrelRight = []

platInclineX = [100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720]
inclineCount = 0

ladderX1 = [295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315, 555, 555, 600, 440, 320]
ladderX2 = [305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325, 565, 565, 610, 450, 335]
ladderY1 = [710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309, 314, 417, 241, 154, 232]
ladderY2 = [720, 705, 657, 620, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329, 369, 432, 311, 232, 272]
fullLadderUp = [False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True]
fullLadderDown = [True, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False]

leftBoundariesY = [541, 341]
rightBoundariesY = [638, 438, 244]

barrelLadderX = [320, 610, 560, 280, 160, 250, 400, 610, 350, 160, 300, 610]
barrelLadderY1 = [243, 252, 326, 270, 350, 428, 437, 449, 535, 547, 627, 645]
barrelLadderY2 = [343, 322, 446, 344, 420, 538, 527, 519, 625, 617, 727, 715]
barrelAdjust = [-2, 1, -1, 4, 2, 3, 5, 1, 5, 1, 4, 1]

confettiX = []
confettiY = []
confettiRadius = []
confettiSpeed = []
confettiColour = []

#Define Images
title = pygame.image.load("title-screen.png")
start = pygame.image.load("start.png")
winScreen = pygame.image.load("win-screen.png")
gameOverScreen = pygame.image.load("game-over-screen.png")

selectIcon = pygame.image.load("select-icon.png")
life = pygame.image.load("mario-life.png")

withLadder = pygame.image.load("withLadder.png")
platform0 = pygame.image.load("platform0.png")
platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")
platform4 = pygame.image.load("platform4.png")
platform5 = pygame.image.load("platform5.png")
platform6 = pygame.image.load("platform6.png")
platforms = [platform0, platform1, platform2, platform3, platform4, platform5, platform6]
level = pygame.image.load("level.png")

blue0 = pygame.image.load("blue0.png")
blue1 = pygame.image.load("blue1.png")
blue2 = pygame.image.load("blue2.png")
blue3 = pygame.image.load("blue3.png")
blue4 = pygame.image.load("blue4.png")
blue5 = pygame.image.load("blue5.png")
blueNumbers = [blue0, blue1, blue2, blue3, blue4, blue5]
white0 = pygame.image.load("white0.png")
white1 = pygame.image.load("white1.png")
white2 = pygame.image.load("white2.png")
white3 = pygame.image.load("white3.png")
white4 = pygame.image.load("white4.png")
white5 = pygame.image.load("white5.png")
white6 = pygame.image.load("white6.png")
white7 = pygame.image.load("white7.png")
white8 = pygame.image.load("white8.png")
white9 = pygame.image.load("white9.png")
whiteNumbers = [white0, white1, white2, white3, white4, white5, white6, white7, white8, white9]

marioLeft = pygame.image.load("mario-left.png")
marioRight = pygame.image.load("mario-right.png")
runLeft = pygame.image.load("run-left.png")
runRight = pygame.image.load("run-right.png")
marioJumpLeft = pygame.image.load("jump-left.png")
marioJumpRight = pygame.image.load("jump-right.png")
marioClimb1 = pygame.image.load("marioClimb1.png")
marioClimb2 = pygame.image.load("marioClimb2.png")
dead = pygame.image.load("dead.png")
marioImage = marioRight

paulineHelp = pygame.image.load("pauline-help.png")
paulineStill = pygame.image.load("pauline-still.png")

dkUp1 = pygame.image.load("DK_up1.png")
dkUp2 = pygame.image.load("DK_up2.png")
dkEmptyClimb1 = pygame.image.load("dkClimbEmpty1.png")
dkEmptyClimb2 = pygame.image.load("dkClimbEmpty2.png")
dkForward = pygame.image.load("dkForward.png")
dkLeft = pygame.image.load("dkLeft.png")
dkRight = pygame.image.load("dkRight.png")
dkDefeat = pygame.image.load("DK-defeat.png")
dkImage = dkForward

barrelStack = pygame.image.load("barrel-stack.png")
barrelDown = pygame.image.load("barrel-down.png")
barrel1 = pygame.image.load("barrel1.png")
barrel2 = pygame.image.load("barrel2.png")
barrel3 = pygame.image.load("barrel3.png")
barrel4 = pygame.image.load("barrel4.png")
barrelSequence = [barrel1, barrel2, barrel3, barrel4]
barrelPic = []

brokenHeart = pygame.image.load("broken-heart.png")
fullHeart = pygame.image.load("full-heart.png")
clock = pygame.time.Clock()
#declares values for 400 confetti pieces
for i in range(0, 400):
    #chooses random x value and appends it to list
    x = random.randint(0, 800)
    confettiX.append(x)
    
    #chooses random y value and appends it to list
    y = random.randint(-500, -100)
    confettiY.append(y)
    
    #chooses random radius and appends it to list
    r = random.randint(1, 4)
    confettiRadius.append(r)
    
    #chooses random speed and appends it to list
    s = random.randint(5, 20)
    confettiSpeed.append(s)
    
    #chooses random colour and appends it to list
    colour = random.randint(0,4)
    confettiColour.append(colours[colour])


# instructions - outputs the instructions on the console
# @param: none
# @return: none
def instructions():
    print ("Donkey Kong has kidnapped Pauline!")
    print ("You must now help Mario save her by climbing all the way")
    print ("up the structure to the platform where she is being held.")
    print ("You will have three lives, and you get points by rescuing")
    print ("Pauline and jumping over barrels.")
    print ("To win, save her 5 times or get a score of 999999 or over.")
    print ("Use the arrow keys to move, and press the space to jump.")
    print ("In the menus, use the up and down keys to choose your option")
    print ("and the return key to select it.")
    print ("GOOD LUCK!")



# getName - user inputs name
# @param: none
# @return: name(str)
def getName():
    
    

    return name


# highScore - finds the high score and adds the current user's score to the leaderboard
# @param: none
# @return: highestScore (int)
def highScore():
    
    #adds user's score
    leaderboard["Player"] = score
    
    #sorting the scores from least to greatest
    scores = leaderboard.values()
    


# outputLeaderboard - sorts the scores from greatest to least and ouputs it
# @param: none
# @return: none
def outputLeaderboard():
    
    #declaring variables
    rank = 1
    scores = leaderboard.values()
    names = leaderboard.keys()
    sortedNames = []

    
    # #goes through all the scores
    # for i in range(0, len(scores)):
    #     #goes through all the names
    #     for j in range(0, len(names)):
            
    #         #checks if the name has already been sorted
    #         if (names[j] in sortedNames) == False:
    #             #if the score is the same as the score associated name in leaderboard, append it to the sorted names
    #             if scores[i] == leaderboard[names[j]]:
    #                 sortedNames.append(names[j])
    
    # print ("LEADERBOARD")
    # print ("***********")
    
    # #goes through all the scores
    # for i in range(len(leaderboard)-1, -1, -1):
        
    #     #if it is not the first time the loop is going and the score is different from the previous score, and 1 to the ranks
    #     if i < len(leaderboard)-1:
    #         if scores[i] != scores[i+1]:
    #             rank = rank + 1
        
    #     #output
    #     print (rank, "|", sortedNames[i], ":", scores[i])

    # print ("THANKS FOR PLAYING! :)")



# collide - checks whether or not mario has collided into a barrel
# @param: none
# @return: hit(boolean)
def collide():
    global hit
    
    #goes through all the barrels
    for i in range(0, len(barrelX)):
        #if mario's image touches the barrels image anywhere, hit is True
        if marioX+20 >= barrelX[i] and marioX <= barrelX[i]+26 and marioY+30 >= barrelY[i] and marioY <= barrelY[i]+20:
            hit = True
            
    return hit


# ladderCheck - checks whether or not there is a ladder at mario's location
# @param: none
# @return: upLadder(boolean), downLadder(boolean), moveSides(boolean)
def ladderCheck():
    global marioY
    
    #declares variables
    upLadder = False
    downLadder = False
    moveSides = True
    
    #goes through all the ladders
    for i in range(0, len(ladderX1)):
        # if mario is in range of a ladder, he can move up, down, and to the sides
        if marioX >= ladderX1[i] and marioX <= ladderX2[i] and marioY >= ladderY1[i] and marioY <= ladderY2[i]:
            downLadder = True
            upLadder = True
            moveSides = False
            
            #if mario is at the top of a ladder, he can't move up further
            if marioY == ladderY1[i]:
                upLadder = False
                
                #if the ladder isn't broken going up, he can move to the sides when at the top
                if fullLadderUp[i]:
                    moveSides = True      
            
            #if mario is at the bottom of the ladder, he can't move down further 
            if marioY == ladderY2[i]:
                downLadder = False
                
                #if the ladder isn't broken going down, he can move to the sides when at the bottom 
                if fullLadderDown[i]:
                    moveSides = True
        
        #break out of the loop to stop checking for which ladder mario because the computer has already found it
        if upLadder or downLadder:
            break
            
    return upLadder, downLadder, moveSides


# incline - moves Mario up so that he can go on an incline when walking/jumping on the platform
# @param: y(int), x(int), direction(str), objectt(str)
# @return: y(int) or move(int)
def incline(y, x, direction, objectt):
    global inclineCount
    
    #lines 344 to 371 checks which platform the object is on and then declares the range where the object inclines and how much it moves vertically when going right on a inclined part
    
    #if the object is on the bottom platform
    if y <= 720 and y >= 657:
        startNum = 6
        endNum = len(platInclineX) - 1
        move = 3
        
    #if object is on the second or fourth platform 
    elif (y <= 638 and y >= 553) or (y >= 353 and y <= 438):
        startNum = 0
        endNum = len(platInclineX) - 2
        move = -3
        
    #if object is on the thrid or fifth platform
    elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):
        startNum = 1
        endNum = len(platInclineX) - 1
        move = 3
        
    #if object is on the top platform
    elif y <= 245 and y >= 149:
        startNum = 8
        endNum = len(platInclineX) - 2
        move = -3
    
    #if not on a platform (on a ladder)
    else:
        startNum = 0
        endNum = 0
        move = 0
    
    #goes through the platIncline list, with a range of different numbers depending on which platform the object is on
    for i in range(startNum, endNum):
        
        #if the object has the same x as one of the x incline spot, the object will incline up or down
        if x == platInclineX[i]:
            
            #if the object is mario and he is jumping left or right, keep track of how many inclines he has passed while jumping
            if (jumpLeft or jumpRight) and objectt == "mario":
                inclineCount = inclineCount + 1    
            
            #else find out which direction he is moving
            else:
                #if it's right, minus move from y
                if direction == "right":
                    y = y - move
                #if its left, add move to y                  
                elif direction == "left":
                    y = y + move
    
    #returns move if the function is for mario when jumping
    if (jumpLeft or jumpRight) and objectt == "mario":
        return move
    #else return the new y value
    else:
        return y


# boundaries - checks all of Mario's, the barrels boundaries
# @param: none
# @return: left(boolean), right(boolean)
def boundaries(x, y):
    #declare variables
    left = True
    right = True
    
    #if x is in that range, mario has reached a possible boundary to the left of him
    if x <= 105 and x >= 96:
        #goes through the y coordinate of the left boundaries
        for i in range(0, len(leftBoundariesY)):
            
            #if mario is in that range of the y boundary too, left is False and mario can't move left
            if y <= leftBoundariesY[i] and y >= leftBoundariesY[i] - 49:
                left = False
                
    #if x is in that range, mario has reached a possible boundary to the right of him            
    elif x >= 660 and x <= 669:
        #goes through the y coordinate of the right boundaries
        for i in range(0, len(rightBoundariesY)):
            
            #if mario is in that range of the y boundary too, right is False and mario can't move right
            if y <= rightBoundariesY[i] and y >= rightBoundariesY[i] - 49:
                right = False
                     
    return left, right


# introScene - the start scene of the game
# @param: none
# @return: none
def introScene():
        #if DK has climbed less than 390 pixels, blit the background with the ladder
        if dkClimb <= 390:
            screen.blit(withLadder, (48, 0))
            
            #images will switch to make it look like DK is moving
            #if dkClimb is divisble by 30, blit the first climb image
            if dkClimb % 30 == 0:
                screen.blit(dkUp2, (350, 660-dkClimb))
                
            #else blit the other climb image
            else:  
                screen.blit(dkUp1, (370, 660-dkClimb))
        
        #if DK has climbed for between 390 and 580 pixels, blit platform0 and keep dk's image as dkUp2    
        elif dkClimb > 390 and dkClimb <= 580:
            screen.blit(platform0, (55, 9))
            screen.blit(dkUp2, (350, 660-dkClimb))
        
        #if DK is done climbing, blit the falling platforms beams, Pauline and DK jumping
        if climbDone:
            screen.blit(platforms[platNum], (platformsX[platNum], platformsY[platNum]))
            pauline(paulineStill)
            screen.blit(dkForward, (dkJumpX, dkJumpY))


# startScreen - outputs the start screen
# @param: none
# @return: none
def startScreen():
    #blit image
    screen.blit(start, (48, 0))


# backgroud - outputs the level and barrel stack
# @param: none
# @return: none
def background():
    #blit images
    screen.blit(level, (31, -14))
    screen.blit(barrelStack, (60, 188))


# dk - outputs DK onto screen
# @param: none
# @return: none
def dk():
    #blit image
    screen.blit(dkImage, (130, 176))


# mario - outputs Mario onto screen
# @param: none
# @return: none
def mario():
    #blit image
    screen.blit(marioImage, (marioX, marioY))
 
 
# pauline - outputs pauline on to screen
# @param: paulinePic(image)
# @return: none
def pauline(paulinePic):
    #blit image
    screen.blit(paulinePic, (335, 133))


#barrels - blit all the barrels onto the screen
# @param: none
# @return: none
def barrel():
    #goes through all the barrels to find each barrel information so it can blit it
    for i in range(0, len(barrelPic)):
        screen.blit(barrelPic[i], (barrelX[i],barrelY[i]))


# lives - blit visual representation of how many lives Mario has left
# @param: none
# @return: none
def marioLives():
    #goes through all the lives you have left
    for i in range(0, lives):
        #blit images, adding 20 to the y each time you run the loop
        screen.blit(life, (60+i*20, 100))


# levelNumber - blit the level number
# @param: none
# @return: none
def levelNumber():
    #goes through all the blue numbers
    for i in range(0, len(blueNumbers)):
        #if the ten's digit is equal to i, blit the image for the number
        if levelNum / 10 == i:
            screen.blit(blueNumbers[i], (611, 86))
        #if the ones's digit is equal to i, blit the image for the number
        if levelNum % 10 == i:
            screen.blit(blueNumbers[i], (635, 86))


# playersScores - blit the scores
# @param: scoreType(int), scoreX(int), scoreY(int)
# @return: none
def playersScores(scoreType, scoreX, scoreY):
    
    #declares variables
    tempScore = str(scoreType)
    numOfZero = 6-len(tempScore)
    
    #goes through to blit all the zeros needed in front of the score
    for i in range(0, numOfZero):
        screen.blit(whiteNumbers[0], (scoreX, scoreY))
        
        #add 24 to space the number out each time
        scoreX = scoreX + 24
    
    #goes through each digit/number in the string
    # for i in range(0, len(tempScore)):
    #     #goes through the numbers 0 to 10
    #     for j in range(0, 10):
            
    #         #change tempScore[i] to integer to compare it with j
    #         #if they are equal, output the coressponding number image
    #         if int(tempScore[i]) == j:
    #             screen.blit(whiteNumbers[j], (scoreX, scoreY))
                
    #             #add 24 to space the number out each time
    #             scoreX = scoreX + 24


# win - images outputed when you complete a level
# @param: none
# @return: none
def win():
    
    #blit images
    background()
    screen.blit(marioLeft, (440, 150))
    
    #if DK has climbed less than 30 pixels, blit Pauline with a full heart
    if dkClimb <= 30:
        pauline(paulineStill)
        screen.blit(fullHeart, (386, 130))
    #else just blit a broken heart
    else:
        screen.blit(brokenHeart, (387, 130))
    
    #if the game is not won, switch between two images to blit
    if winGame == False:
        if dkClimb % 30 == 0:
            screen.blit(dkImage1, (240 - moveOver1, 160-dkClimb))
        else:  
            screen.blit(dkImage2, (240 - moveOver2, 160-dkClimb))
            
    #else just blit DK        
    else:
        dk()


# end - shows end of the game
# @param: endScreen(image)
# @return: none
def end(endScreen):
    
    #blit image
    screen.blit(endScreen, (0, 30))
    
    #if the bottom option is selected, blit the icon next to the bottom option
    if option == "bottom":    
        screen.blit(selectIcon, (270, 640))
    
    #else blit it next to the top option
    else:
        screen.blit(selectIcon, (270, 575))
 

# confetti - outputs confetti on the screen
# @param: none
# @return: none
def confetti():
    
    #goes through all 400 confetti pieces
    for i in range(0, 400):
        #blit image with the correct confetti info for each piece
        pygame.draw.circle(screen, confettiColour[i], (confettiX[i], confettiY[i]), confettiRadius[i], 0) 


        
# @redraw_screen - function that redraws the screen
def redraw_screen():
    
    #find global variables
    global climbDone
    global gameStart
    global gameDone
    global winGameSceneDone
    global startDone
    global startOutput
    
    #filling colour of screen
    screen.fill(BLACK)
    
    #drawing commands
    
    #if game is done, output end screen and user and high score
    if gameDone:
        #calls drawing fucntions
        end(gameOverScreen)
        playersScores(score, 388, 387)
        playersScores(highestScore, 485, 445)
    
    #if winGame is True, go to the win game sequences
    elif winGame:
        #if this is true, blit the images to show the moment DK is defeated
        if winGameSceneOutput:
            #calls drawing fucntions
            win()
            marioLives()
                
            levelNumber()
            playersScores(score, 88, 40)
            playersScores(highestScore, 327, 40)
        
        #if this is true, output the win game menu with confetti
        elif winGameSceneDone:
            #calls drawing fucntions
            end(winScreen)
            confetti()
            playersScores(score, 388, 387)
            playersScores(highestScore, 485, 445)
    
    #else the user has not won or lost the game yet
    else:
        #if pressed is false, the title screen is being blited
        if pressed == False:
            screen.blit(title, (54, 18))
        
        #if pressed is true and introDone, blit the intro sequence
        elif pressed and introDone == False:
            #calls drawing fucntions
            introScene()
            marioLives()
        
        #if intro is done and the game hasn't started yet, blit the start screen
        elif introDone == True and gameStart == False:
            #calls drawing fucntions
            startScreen()
            marioLives()
            
            #establishing the start is done by resetting the variables
            startOutput = True
            startDone = True
        
        #if the game has started and the level is not won or mario has died, blit the normal game play images
        elif (gameStart and winLevel == False) or deathScene:
            #calls drawing fucntions
            background()
            dk()
            mario()
            pauline(paulineHelp)
            marioLives()
            
            #blit barrels if scoreWin and deathScene is false
            if scoreWin == False and deathScene == False:
                barrel()
        
        #if user wins the level output winning sequence
        elif winLevel:
            #calls drawing fucntions
            win()
            marioLives()
        
        #calls drawing fucntions
        levelNumber()
        playersScores(score, 88, 40)
        playersScores(highestScore, 327, 40)
     
    #updating
    pygame.display.update()



#prints instructions on console
instructions()

#loop whole game if user wants to keep restarting
pygame.init()
walk = pygame.mixer.Sound("walking\\walking.wav")
jump = pygame.mixer.Sound("jump\\jump.wav")
while replay:

    
    #start creating a graphical program
    #Set Screen Dimensions
    WIDTH = 800
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    
    #Name of Window Opened
    pygame.display.set_caption('Donkey Kong')
    
    #starting game play
    inPlay = True
    print ("Hit ESC to end the program.")
    print
    
    #keep looping and keeping graphical interface is run while inPlay is true
    while inPlay:
        
        #if the climbing is happening, check how much DK has climbed
        if pressed == True and climbDone == False:
            #if he has just started, add to the level number
            if dkClimb == 0:
                levelNum = levelNum + 1
            
            #if DK has climbed 390 pixels, delay the program
            if dkClimb == 390:
                pygame.time.delay(500)
            
            #if DK has reached 560 pixels and over, reset the climbCount faster to make it look like he's jumping
            if dkClimb >= 560:
                climbCount = -20
            
            #DK hasn't reached 510 again on the way down from his jumping, keep adding to dkClimb
            if dkClimb != 510 or climbCount != -20:
                dkClimb = dkClimb + climbCount
            
            #else DK has finished climbing and the variable is re-set
            else:
                climbDone = True
        
        #if DK has finished climbing but the intro is not done yet, move on to DK jumping
        elif climbDone and introDone == False:
            #if the platNum is less than or equal to 6, DK is still jumping
            if platNum <= 6:
                #if dkJumpY is 152, reset which way he's jumping to start going down
                if dkJumpY == 152:
                    dkJumpYNum = 10
                
                #if dkJumpY is 172, reset which way he's jumping to start going up
                if dkJumpY == 172:
                    dkJumpYNum = -10
                    
                    #change the platNum to change the background image so that a platform "falls"
                    platNum = platNum + 1
                
                #move DK to the left 12 pixels
                dkJumpX = dkJumpX - 12
                
                #if platNum is not 6, keep jumping/changing the y coordinates
                if platNum != 6:
                    dkJumpY = dkJumpY + dkJumpYNum
                
                else:
                    introDone = True
                    pygame.time.delay(1000)
            #else the intro is done and delay for a second before continuing
            #else:
                # introDone = True
                # pygame.time.delay(1000)
        
        #if the gameStart is true, the game play has started
        if gameStart:
            
            #if scoreWin and winLevel are false, check for collisions
            if scoreWin == False and winLevel == False:
                hit = collide()
            
            #checks if mario has hit a boundary to the left or right of him    
            moveLeft, moveRight = boundaries(marioX, marioY)
            
            #if hit is fallse, mario has not hit a barrel and normal game play continues
            if hit == False:
                
                #checks if mario is on a ladder and whether he can go up, down or left and right
                upLadder, downLadder, moveSides = ladderCheck()
                
                #if mario reaches a y value of less than or equal to 154, he has won the game
                if marioY <= 154:
                    #reset variables 
                    winLevel = True
                    dkClimb = -15
                    climbCount = 15
                    marioX = 150
                    marioY = 720
                    marioImage = marioRight
                
                #if mario is jumping, change x and/or y values accordingly
                if jumpLeft or jumpRight or jumpStill:
                    
                    #keeps track of how many jumps
                    jumpCount = jumpCount + 1
                    
                    #changes y coordinates
                    marioY = marioY + addJump
                    
                    #when jumpCount is 7, make mario come back down by change the number he goes up/down by
                    if jumpCount == 7:
                        addJump = 7
                    
                    #if jumpCount is 14, mario has come back down 
                    if jumpCount == 14:
                        
                        #if mario jumped over a barrel, add 100 to the score 
                        if jumpPoint == 1:
                            score = score + 100
                        
                        #if mario was facing right, change the image back to him facing right, and change mario's Y value if he had jumpped over some inclines
                        if direction == "right":
                            marioImage = marioRight
                            marioY = marioY - move*inclineCount
                        #else mario was facing left, change the image back to him facing left, and change mario's Y value if he had jumpped over some inclines
                        else:
                            marioImage = marioLeft
                            marioY = marioY + move*inclineCount
                            
                        #reseting variables
                        addJump = -7
                        jumpCount = 0
                        jumpPoint = 0
                        inclineCount = 0
                        
                        jumpLeft = False
                        jumpRight = False
                        jumpStill = False
                        
                    #if mario has reached a boundary on the sides, don't add to x values
                    if marioX != 60 and marioX != 710 and (marioX != 320 or marioY >= 232):
                        #checks how many inclines mario jumped over and whether to move up or down when mario lands
                        move = incline(marioY, marioX, direction, "mario")
                        
                        #if mario is jumping left and he can move left, minus 5 to his x coordinates
                        if jumpLeft and moveLeft:
                            marioX = marioX - 5
                        #if mario is jumping right and he can move right, add 5 to his x coorinates
                        elif jumpRight and moveRight:
                            marioX = marioX + 5
                    
                    #goes through all the barrels
                    for i in range(0, len(barrelX)):
                        #checks if mario has jumped over a barrel, if so, there is one point will be added if he completes the jump
                        if marioX >= barrelX[i] and marioX <= barrelX[i]+28 and marioY <= barrelY[i]-23 and marioY >= barrelY[i]-65:
                            jumpPoint = 1
                
                #scoreWin is false, keep the barrels rolling
                if scoreWin == False:
                    
                    #goes through all the barrels
                    for i in range(0, len(barrelPic)):
                        #if the barrel reaches the end of the structure, make the barrel disappear off the screen
                        if barrelX[i] <= 31:
                            barrelX[i] = -30
                            barrelY[i] = -30
                        
                        #if the barrel is not falling, check to see if it is
                        if fall[i] == False:
                            barrelLeft[i], barrelRight[i] = boundaries(barrelX[i], barrelY[i]-15)
                            
                            #reset variable if the barrel has hit a platform and can't move either left or right
                            if barrelLeft[i] == False or barrelRight[i] == False:
                                fall[i] = True
                        
                        #checks which platform the barrel is on to determine which direction it's going
                        if (barrelY[i] <= 255 and barrelY[i] >= 243) or (barrelY[i] <= 452 and barrelY[i] >= 415) or (barrelY[i] <= 648 and barrelY[i] >= 611):
                            barrelDirection[i] = "right"
                            
                        elif (barrelY[i] <= 353 and barrelY[i] >= 317) or (barrelY[i] <= 550 and barrelY[i] >= 513) or (barrelY[i] <= 731 and barrelY[i] >= 709):
                            barrelDirection[i] = "left"
                        
                        #if the barrel is not on a ladder it is either rolling or falling
                        if barrelPic[i] != barrelDown:
                            
                            #if the barrel is not falling, it is rolling left or right
                            if fall[i] == False:
                                
                                if barrelDirection[i] == "right":
                                    barrelX[i] = barrelX[i] + 10
                                else:
                                    barrelX[i] = barrelX[i] - 10
                                
                                #checks if the barrel needs to incline up/down and changes the value in the function
                                barrelY[i] = incline(barrelY[i]-11, barrelX[i], barrelDirection[i], "barrel")
                                barrelY[i] = barrelY[i] + 11
                                #subtracted 11 then added it back so that in the function, the values that the functions checks with the y value can be used for both the barrel and mario

                            #else the barrel is in the process of falling    
                            else:
                                #add one to keep track of how long it has fallen
                                fallCount[i] = fallCount[i] + 1
                                
                                #if the barrel is falling on the left side, x is being subtracted by 5
                                if barrelLeft[i] == False:
                                    barrelX[i] = barrelX[i] - 5
                                
                                #if it's falling from the right x is being added by 5
                                elif barrelRight[i] == False:
                                    barrelX[i] = barrelX[i] + 5
                                
                                #changing y by 7 each time    
                                barrelY[i] = barrelY[i] + 7
                                
                                #if the count has reached 8, stop falling and reset the values for the next time
                                if fallCount[i] == 8:
                                    #adjust to make sure it lands on platform right
                                    barrelY[i] = barrelY[i] + 6
                                    
                                    #resetting variables
                                    fallCount[i] = 0
                                    fall[i] = False
                                    barrelLeft[i] = True
                                    barrelRight[i] = True
                            
                            #changes the picture of the barrel each time
                            #if the barrelPic is at index 3, change it to at index 0
                            if barrelPic[i] == barrelSequence[3]:
                                barrelPic[i] = barrelSequence[0]
                                
                            #else change it to the next number in the list
                            else:
                                for j in range(0, len(barrelSequence)-1):
                                    if barrelPic[i] == barrelSequence[j]:
                                        barrelPic[i] = barrelSequence[j+1]
                        
                        #if the barrelPic[i] is barrel down, the barrel is going down a ladder and add 10 to the y value each time                
                        else:
                            barrelY[i] = barrelY[i] + 10
                        
                        #goes through all the ladder coordinates for the barrels
                        for j in range(0, len(barrelLadderX)):
                            #if the barrel's x and y coordinates are same as both barrelLadderX[j] and barrelLadderY[j], respectively, use a random number to choose whether the barrel should go down it or not
                            if barrelX[i] == barrelLadderX[j] and barrelY[i] == barrelLadderY1[j]:
                                barrelChoice = random.randint(0, 1)
                                
                                #if the random number that was picked is 0, the barrel image and coordinates will be reset
                                if barrelChoice == 0:
                                    barrelPic[i] = barrelDown
                                    
                                    #adjust a bit because the barrel going down is wider than the other barrel images
                                    barrelX[i] = barrelX[i] - 2
                            
                            #if the barrel has reached the end of a ladder, reset the variables back
                            if barrelX[i]+2 == barrelLadderX[j] and barrelY[i] == barrelLadderY2[j]:
                                barrelPic[i] = barrelSequence[0]
                                barrelX[i] = barrelX[i] + 2
                                
                                #this makes sure that when it comes down it lands properly on the platform instead of 5 pixels too high, as the barrels move 10 pixels at a time
                                barrelY[i] = barrelY[i] + barrelAdjust[j]
                    
                    #if throwBarrel is false, get a random number to decide whether or not DK will throw another barrel        
                    if throwBarrel == False:
                        #after each level the range will be smaller, meaning a higher chance of throwing barrels
                        dkChoice = random.randint(0, 50-difficulty)
                        
                        #if the number is 0, reset variables to throw the barrel
                        if dkChoice == 0:
                            dkImage = dkLeft
                            throwBarrel = True
                        #else, don't throw any barrels    
                        else:
                            dkImage = dkForward
                            throwBarrel = False
                    
                    #if throwBarrel is true, go through these changes
                    if throwBarrel:
                        
                        #add to give DK some time to get barrel
                        throwCountdown = throwCountdown + 1
                        
                        #if throwCountdown is 20, create a new barrel
                        if throwCountdown == 20:
                            #reset variable
                            dkImage = dkRight
                            
                            #declaring new barrel information
                            barrelX.append(250)
                            barrelY.append(243)
                            barrelDirection.append("right")
                            barrelPic.append(barrel1)
                            fall.append(False)
                            fallCount.append(0)
                            barrelLeft.append(True)
                            barrelRight.append(True)
                            
                        #if throwCountdown reaches 40, reset variables to when DK wasn't throwing    
                        if throwCountdown == 40:
                            throwCountdown = 0
                            dkImage = dkForward
                            throwBarrel = False
            
            #else, mario gets hit, start the death sequences
            else:
                #if the deathScene is not done
                if deathScene == False:
                    #moves the dead mario's y coordinates down to make sure he rests where his feet were, not where his head was
                    if deathCount == 0:
                        marioY = marioY + 10
                    
                    deathCount = deathCount + 1
                    
                    #when the count reaches 60, the short delay is over, reset variables, and lose a life
                    if deathCount == 60:
                        deathScene = True
                        deathCount = 0 
                        lives = lives - 1
                    
                    #resets variables
                    marioImage = dead
                    
                #if deathScene is true, reset variables to start at the beginning of level again
                else:
                    startDone = False
                    gameStart = False
                    throwBarrel = False
                    deathScene = False
                    hit = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    inclineCount = 0
                    jumpPoint = 0
                    marioX = 150
                    marioY = 720
                    addJump = -7
                    jumpCount = 0
                    direction = "right"
                    marioImage = marioRight
                
                #if lives is less than 0, gameDone is True, and put score in leaderboards and find the high score using highScore()
                if lives < 0:
                    gameDone = True
                    highestScore = highScore()
        
        #if the score reaches over 999999, you win the game
        if score >= 999999:
            #resetting values
            score = 999999  #this is the max number the game can output
            scoreWin = True
            dkImage = dkDefeat
        
        #if you win the level, start winLevel processes
        if winLevel:
            #if the levelNum is 5 or scoreWin is true, reset values to output correct images in redraw_screen
            if levelNum == 5 or scoreWin:
                #if this is false, reset values to start the end of the game
                if winGameSceneDone == False:
                    dkImage = dkDefeat
                    winGameSceneOutput = True
                #else, add to the confetti's y coordinates find the highscore and put user's score into leadboard
                else:
                    # goes through all the confetti circles
                    for i in range(0, 400):
                        #add to make if fall down
                        confettiY[i] = confettiY[i] + confettiSpeed[i]
                    highestScore = highScore()
                
                #reset values
                gameStart = False
                winGame = True
            
            #else, continue on to the next level
            else:
                
                #DK climbs up
                dkClimb = dkClimb + climbCount
                
                #if DK climbs 15 pixels, add 250 to the score and delay for time
                if dkClimb == 15:
                    score = score + 250
                    pygame.time.delay(1000)
                
                #if DK climbs less than or equal to 30 pixels, the two images are dk not holding pauline
                if dkClimb <= 30:
                    dkImage1 = dkEmptyClimb1
                    dkImage2 = dkEmptyClimb2
                    moveOver1 = 0
                    moveOver2 = 0
                #else, dk is holding pauline in these two images
                else:
                    dkImage1 = dkUp1
                    dkImage2 = dkUp2
                    
                    #adjusts image so that he climbs up smoothly
                    moveOver1 = 13
                    moveOver2 = 35
                
                #if DK has climbed 150 pixels, reset variables for the next level
                if dkClimb == 150: 
                    winLevel = False
                    climbDone = False
                    introDone = False
                    startDone = False
                    gameStart = False
                    throwBarrel = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    hit = False
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    inclineCount = 0
                    dkClimb = 0
                    platNum = 0
                    climbCount = 15
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    addJump = -7
                    jumpCount = 0
                    direction = "right"
                    
                    #to make the next level more difficult
                    difficulty = difficulty + 8
            
        #deals with any keyboard options once program is run
        #looks for the event (action of using keyboard)
        pygame.event.get()
        
        # get_pressed() method generates a True/False list for the status of all keys
        keys = pygame.key.get_pressed()
        
        #looks for escape to be pressed
        if keys[pygame.K_ESCAPE]:
            #finds highscore and adds score to the dictionary
            highestScore = highScore()
            
            #reset variables to quit program
            inPlay = False
            replay = False
        
        #looks for space to be pressed to make pressed True and start the game
        if keys[pygame.K_SPACE]:
            pressed = True
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(jump)
        
        #must satisfy all these conditions in order for pressing  the left, right, up, down, space(for jumping), and return key to do anything
        if (gameStart and jumpLeft == False and jumpRight == False and jumpStill == False and winLevel == False and hit == False) or gameDone or winGame:      
            
            #looks for left arrow to be pressed
            if keys[pygame.K_LEFT] and moveSides and (marioX != 320 or marioY > 232) and moveLeft and marioX != 60:
                #changes mario's y to incline up/go down with the slope
                marioY = incline(marioY, marioX, direction, "mario")
                # if mario is already facing left, subtract 5 from marioX
                if direction == "left":
                    marioX = marioX - 5
                
                #if the images for mario is marioLeft change it to runLeft
                if marioImage == marioLeft:
                    marioImage = runLeft
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)


                #else, change it to marioLeft
                else:
                    marioImage = marioLeft
                    
                #if space is pressed while left is also being pressed, jumpLeft is True and change the image 
                if keys[pygame.K_SPACE]:
                    jumpLeft = True
                    marioImage = marioJumpLeft
                    # if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(jump)
                
                direction = "left"
            #looks for right arrow to be pressed   
            elif keys[pygame.K_RIGHT] and moveSides and moveRight and marioX != 710:
                #changes mario's y to incline up/go down with the slope
                marioY = incline(marioY, marioX, direction, "mario")
                
                #if mario was already facing right, add 5 to the x value
                if direction == "right":
                    marioX = marioX + 5
                #if the images for mario is marioRight change it to runRight
                if marioImage == marioRight:
                    marioImage = runRight
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)
                #else change it to marioRight
                else:
                    marioImage = marioRight
                
                #if space is pressed while right is also being pressed, jumpRight is True and change the image
                if keys[pygame.K_SPACE]:
                    jumpRight = True
                    marioImage = marioJumpRight
                
                direction = "right"
            
            #looks for up arrow to be pressed   
            elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
                pygame.mixer.Sound.stop(walk)
            if keys[pygame.K_UP] and (upLadder or gameDone or winGame):
                # if upLadder is true, move mario up 5 pixels
                if upLadder:
                    marioY = marioY - 5
                    
                    #if marioImage is marioClimb1, change it to marioClimb2
                    if marioImage == marioClimb1:
                        marioImage = marioClimb2
                    #otherwise, change it to marioClimb1
                    else:
                        marioImage = marioClimb1
                
                #if the user is on one of the menus, change the option to select the top one
                if gameDone or winGame:
                    option = "top"
            
            #looks for down arrow to be pressed and only excutes when you can go down a ladder, and to sele
            if keys[pygame.K_DOWN] and (downLadder or gameDone or winGame):
                #if downLadder is true, change mario's y coordinates to go down
                if downLadder:
                    marioY = marioY + 5
                    
                    #if marioImage is marioClimb1, change it to marioClimb2
                    if marioImage == marioClimb1:
                        marioImage = marioClimb2
                    #otherwise, change it to marioClimb1
                    else:
                        marioImage = marioClimb1
                
                #if user is on one of the menus, change the option to select the bottom one
                if gameDone or winGame:
                    option = "bottom"
            
            #looks for space bar to be pressed and can only do something when mario already jumping left or right and you're not in the middle of a ladder
            if keys[pygame.K_SPACE] and jumpLeft == False and jumpRight == False and moveSides:
                #it makes jumpStil true
                jumpStill = True
                
                #if you are facing left, blit the image of mario jumping, facing right
                if direction == "right":
                    marioImage = marioJumpRight
                    
                #else blit mario jumping and facing left
                else:
                    marioImage = marioJumpLeft
            
            #looks for return to be pressed and it can only do something when the game is lost or won
            if keys[pygame.K_RETURN] and (gameDone or winGame):
                #if the top option is selected, reset the game
                if option == "top":
                    
                    #reset variables to restart
                    inPlay = False
                    winLevel = False
                    pressed = False
                    climbDone = False
                    introDone = False
                    gameStart = False
                    startDone = False
                    gameDone = False
                    throwBarrel = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    winGame = False
                    winLevel = False
                    deathScene = False
                    scoreWin = False
                    winGameSceneDone = False
                    score = 0
                    levelNum = 0
                    dkClimb = 0
                    climbCount = 15
                    platNum = 0
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    marioX = 150
                    marioY = 720
                    addJump = -7
                    marioJumpCount = 0
                    lives = 2
                    difficulty = 0
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                
                #if the bottom option is selected, you will quit the game    
                elif option == "bottom":
                    #reset variables
                    inPlay = False
                    replay = False
        clock.tick(30)
        pygame.display.update()      
        if inPlay:
            redraw_screen()                 # the screen window must be constantly redrawn - animation
            # pygame.time.delay(30)           # pause for 20 miliseconds
        
        if startOutput:
            # pygame.time.delay(2000)
            
            startOutput = False
            gameStart = True
        
        if winGameSceneOutput:
            # pygame.time.delay(2500)
            
            winGameSceneOutput = False
            winGameSceneDone = True
    
    pygame.quit()                       # always quit pygame when done!        
#---------------------------------------#

#outputs the leaderboard on the console
outputLeaderboard()