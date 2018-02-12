import pygame
from pygame.locals import *
from virtualKeyboard import VirtualKeyboard
import numpy
import random
from copy import copy

# Pygame Constants
FPS = 30
WWIDTH = 320
WHEIGHT = 400

# Board Parameters
BRICKGAP = 4
BRICKLENGTH = 24
BRICKHEIGHT = 24
BOARDWIDTH = 10 #Number of Columns
BOARDHEIGHT = 10 #Number of Rows

XMARGIN = (WWIDTH - ((BOARDWIDTH*BRICKLENGTH)+((BOARDWIDTH-1)*BRICKGAP)))/2
YMARGIN = 100

# Level Generator Parameters
MODEGROUPSIZE = 6
STDEVGROUPSIZE = 3
MINGROUPSIZE = 1
MAXGROUPSIZE = 30

##Colors
#          R    G    B
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (000, 255,   0)
BLUE   = (  0,   0, 255)
GRAY   = (100, 100, 100)
NAVY   = ( 60,  60, 100)
YELLOW = (255, 255,   0)
ORANGE = (255, 128,   0)
PURPLE = (255,   0, 255)
CYAN   = (  0, 255, 255)

BGCOLOR= (197, 193, 184)

# PNG's


# TODO: saveable high scores

############################################################
## Functions
############################################################

def brick_pop_main(main_game_state):

    #TODO: Start with Main Menu (Start Game, High Scores, Quit Game)

    bp_game_state = brick_pop_game()

    bp_game_state.draw_background(main_game_state)

    bp_game_state.generate_board()

    bp_game_state.draw_board(main_game_state)
    bp_game_state.draw_score(main_game_state)

    # Update Display
    pygame.display.update()
    main_game_state.fpsClock.tick(FPS)

    while True:

        # Input FOR TESTING
        # brickXInput = input('Brick X:')
        # brickYInput = input('Brick Y:')

        bp_game_state.draw_board(main_game_state)
        bp_game_state.draw_score(main_game_state)

        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                #quit_game(game_state)
                print('quit')
            elif event.type == MOUSEMOTION:
                main_game_state.mouseX, main_game_state.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                main_game_state.mouseX, main_game_state.mouseY = event.pos
                mouseClicked = True

        if mouseClicked == True:
            if bp_game_state.backIcon_rect.collidepoint(main_game_state.mouseX, main_game_state.mouseY):
                main_game_state.set_state('Main_Screen')
                # TODO: add an 'are you sure' option
                break
            selectedBrick = bp_game_state.get_brick_at_pixel(main_game_state.mouseX, main_game_state.mouseY)
            bp_game_state.select_brick(selectedBrick[0], selectedBrick[1], main_game_state)

        # Check if level is complete
        if bp_game_state.is_level_complete():
            # TODO: Level complete animation
            bp_game_state.level_up(main_game_state)

        # Check if game over
        elif bp_game_state.is_game_over():
            # TODO: Game Over Animation
            # TODO: New Game Button, Back to Hub Button
            bp_game_state.money_plays_handler(main_game_state)
            # TODO: Money Entering Wallet Animation
            main_game_state.newScore(bp_game_state.score)
            bp_game_state.new_game(main_game_state)

        # Update Display
        pygame.display.update()
        main_game_state.fpsClock.tick(FPS)



    return 0

def main_menu():

    return 0

############################################################
## Classes
############################################################

class brick_pop_game():

    def __init__(self):

        self.stuff = 0
        self.score = 0
        self.level = 1
        self.board = [['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'],
                      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX']]

        self.brickList = []
        for x in range(10):
            for y in range(10):
                self.brickList.append([x, y])

        self.pngRed = pygame.image.load('Sprites/Brick_Pop/Brick_Red.png')
        self.pngYel = pygame.image.load('Sprites/Brick_Pop/Brick_Yellow.png')
        self.pngGre = pygame.image.load('Sprites/Brick_Pop/Brick_Green.png')
        self.pngPrp = pygame.image.load('Sprites/Brick_Pop/Brick_Purple.png')
        self.pngBlu = pygame.image.load('Sprites/Brick_Pop/Brick_Blue.png')
        self.pngGry = pygame.image.load('Sprites/Brick_Pop/Brick_Grey.png')
        self.pngBlank = pygame.image.load('Sprites/Brick_Pop/Brick_Blank.png')
        self.pngBG = pygame.image.load('Sprites/Brick_Pop/BP_Background.png')

        self.backIcon = pygame.image.load('Sprites/back_button.png')
        self.backIcon_loc = (10, 8 + 36)
        self.backIcon_rect = pygame.Rect(self.backIcon_loc[0], self.backIcon_loc[1], 30, 30)

        self.update_brick_set()

    def generate_board(self):

        # self.random_board()

        tempColors = self.brickSet
        while True:

            groups = self.get_groups()

            # Find Largest Blank Group
            largestBlankGroup = []
            for group in groups:
                if group[1] == 'XXX':
                    if len(group[0]) >= len(largestBlankGroup):
                        largestBlankGroup = group[0]

            if largestBlankGroup == []:
                self.update_brick_set()
                break

            max = 0
            if len(largestBlankGroup) >= MAXGROUPSIZE:
                max = MAXGROUPSIZE
            else:
                max = len(largestBlankGroup)
            min = MINGROUPSIZE

            # TODO: formula to decide mode based on level

            groupSize = 0
            while True:
                groupSize = int(numpy.random.normal(MODEGROUPSIZE,STDEVGROUPSIZE))
                if groupSize >= min and groupSize <= max:
                    break

            # Color management
            color = random.choice(tempColors)
            del tempColors[tempColors.index(color)]
            if tempColors == []:
                self.update_brick_set()
                tempColors = self.brickSet

            # Fill in group
            doneList = []
            doneCounter = 0
            brick1 = random.choice(largestBlankGroup)
            self.board[brick1[1]][brick1[0]] = color
            doneList.append(brick1)
            doneCounter +=1

            while True:

                if doneCounter == groupSize:
                    break

                brick = random.choice(doneList)

                neighborList = [[brick[0] - 1, brick[1]],
                                [brick[0] + 1, brick[1]],
                                [brick[0], brick[1] + 1],
                                [brick[0], brick[1] - 1]]

                # Delete Neighbors outside bounds or already colored
                delList = []
                for neighborNum in range(len(neighborList)):
                    if neighborList[neighborNum][0] < 0 or neighborList[neighborNum][1] < 0 or neighborList[neighborNum][0] > 9 or neighborList[neighborNum][1] > 9:
                        delList.append(neighborNum)
                    elif self.board[neighborList[neighborNum][1]][neighborList[neighborNum][0]] != 'XXX':
                        delList.append(neighborNum)

                delList.reverse()
                for num in delList:
                    del neighborList[num]

                if neighborList != []:
                    brick1 = random.choice(neighborList)
                    self.board[brick1[1]][brick1[0]] = color
                    doneList.append(brick1)
                    doneCounter += 1



        return 0

    def select_brick(self, brickX, brickY, main_game_state):

        groups = self.get_groups()

        # Find selected group
        selectedGroup = []
        for group in groups:
            if [brickX, brickY] in group[0]:
                selectedGroup = group[0]
                break

        if len(selectedGroup) == 1 or group[1] == 'XXX':
            return False

        self.score_calculation(len(selectedGroup))

        # Delete group members
        for brick in selectedGroup:
            self.board[brick[1]][brick[0]] = 'XXX'

        #TODO: popping animation (going outwards)

        # Draw board with empty spots
        self.draw_board(main_game_state)
        self.draw_score(main_game_state)
        # Update Display
        pygame.display.update()
        main_game_state.fpsClock.tick(FPS)

        # Find number of spots each brick needs to move vertically
        vertMovesDict = {}
        for brick in self.brickList:
            blanksCounter = 0
            tempBrick = copy(brick)
            while True:
                tempBrick[1] = tempBrick[1] + 1
                if tempBrick[1] >= 10:
                    vertMovesDict[str(brick)] = blanksCounter
                    break
                if self.board[tempBrick[1]][tempBrick[0]] == 'XXX':
                    blanksCounter += 1

        # Falling Animation
        self.falling_animation(vertMovesDict, main_game_state)

        # Move bricks vertically
        yList = range(10)
        yList.reverse()
        for y in yList:
            for x in range(10):
                if vertMovesDict[str([x, y])] != 0:
                    self.board[y + vertMovesDict[str([x, y])]][x] = self.board[y][x]
                    self.board[y][x] = 'XXX'

        # Draw board
        self.draw_board(main_game_state)
        self.draw_score(main_game_state)
        # Update Display
        pygame.display.update()
        main_game_state.fpsClock.tick(FPS)

        # Check for any missing columns
        missingColumns = []
        for x in range(10):
            columnGone = True
            for y in range(10):
                if self.board[y][x] != 'XXX':
                    columnGone = False
                    break
            if columnGone == True:
                missingColumns.append(x)

        if missingColumns != []:

            # Find number of spots each brick needs to move horizontally
            horizMovesDict = {}
            for brick in self.brickList:
                columnCounter = 0
                for column in missingColumns:
                    if brick[0] > column:
                        columnCounter += 1
                horizMovesDict[str(brick)] = columnCounter

            # TODO: horizontal moving animation goes here
            self.horizontal_animation(horizMovesDict, main_game_state)

            # Move bricks horizontally
            for x in range(10):
                for y in range(10):
                    if horizMovesDict[str([x, y])] != 0:
                        self.board[y][x - horizMovesDict[str([x, y])]] = self.board[y][x]
                        self.board[y][x] = 'XXX'

            # Draw board
            self.draw_board(main_game_state)
            self.draw_score(main_game_state)
            # Update Display
            pygame.display.update()
            main_game_state.fpsClock.tick(FPS)

        return True

    def update_brick_set(self):

        self.brickSet = []

        if self.level == 1:
            self.brickSet = ['Red', 'Yel', 'Gre']
        elif self.level == 2:
            self.brickSet = ['Red', 'Yel', 'Gre', 'Prp']
        elif self.level == 3:
            self.brickSet = ['Red', 'Yel', 'Gre', 'Prp', 'Blu']
        elif self.level >= 4:
            self.brickSet = ['Red', 'Yel', 'Gre', 'Prp', 'Blu', 'Gry']

    def get_group_size(self, brickX, brickY):

        groupList = [[brickX, brickY]]
        searchedList = []

        color = self.board[brickY][brickX]

        while True:

            # Get Neighbors
            neighborList = [[groupList[0][0] - 1, groupList[0][1]],
                            [groupList[0][0] + 1, groupList[0][1]],
                            [groupList[0][0], groupList[0][1] + 1],
                            [groupList[0][0], groupList[0][1] - 1]]

            # Delete Neighbors outside bounds
            delList = []
            for neighborNum in range(len(neighborList)):
                if neighborList[neighborNum][0] < 0 or neighborList[neighborNum][1] < 0 or neighborList[neighborNum][0] > 9 or neighborList[neighborNum][1] >9:
                    delList.append(neighborNum)
            delList.reverse()
            for num in delList:
                del neighborList[num]

            # Check to see if neighbor has been found / searched already
            for neighbor in neighborList:
                if neighbor not in groupList and neighbor not in searchedList:
                    if self.board[neighbor[1]][neighbor[0]] == color:
                        groupList.append(neighbor)

            searchedList.append(groupList[0])
            del groupList[0]

            if groupList == []:
                break

        return searchedList, color

    def get_groups(self):

        groups = []
        while True:

            group1, color1 = self.get_group_size(self.brickList[0][0], self.brickList[0][1])
            groups.append([group1, color1])

            for brick in group1:
                del self.brickList[self.brickList.index(brick)]

            if self.brickList == []:
                for x in range(10):
                    for y in range(10):
                        self.brickList.append([x, y])
                break

        return groups





        return 0

    def random_board(self):

        # for x in range(10):
        #     for y in range(10):
        #         self.board[y][x] = random.choice(self.brickSet)

        self.board = [['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'Gre', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX'],
                      ['Red', 'Blu', 'Gre', 'XXX', 'XXX', 'Red', 'Blu', 'Gre', 'XXX', 'XXX']]

    def level_up(self, main_game_state):

        self.level += 1
        self.update_brick_set()

        self.generate_board()
        self.draw_board(main_game_state)

    def score_calculation(self, brickNum):

        addedScore = brickNum * (brickNum - 1)
        self.score = self.score + addedScore

        # TODO: score animation (letters pop out, go upwards, and fade)

    def is_level_complete(self):

        completedBool = True
        for x in range(10):
            for y in range(10):
                if self.board[y][x] != 'XXX':
                    completedBool = False
                    break
            if completedBool == False:
                break

        return completedBool

    def is_game_over(self):

        groups = self.get_groups()

        largestGroup = 0
        for group in groups:
            if len(group[0]) >= largestGroup and group[1] != 'XXX':
                largestGroup = len(group[0])

        if largestGroup == 1:
            return True
        else:
            return False

    def new_game(self, main_game_state):

        self.level = 1
        self.update_brick_set()
        self.generate_board()
        self.draw_board(main_game_state)

        self.score = 0

    def draw_background(self, main_game_state):

        main_game_state.displaySurf.blit(self.pngBG, (0,0))
        main_game_state.displaySurf.blit(self.backIcon, self.backIcon_loc)

    def draw_board(self, main_game_state):

        self.draw_background(main_game_state)

        # Board
        for x in range(10):
            for y in range(10):
                colorPNG = 0
                if self.board[y][x] == 'Red':
                    colorPNG = self.pngRed
                elif self.board[y][x] == 'Yel':
                    colorPNG = self.pngYel
                elif self.board[y][x] == 'Gre':
                    colorPNG = self.pngGre
                elif self.board[y][x] == 'Prp':
                    colorPNG = self.pngPrp
                elif self.board[y][x] == 'Blu':
                    colorPNG = self.pngBlu
                elif self.board[y][x] == 'Gry':
                    colorPNG = self.pngGry
                elif self.board[y][x] == 'XXX':
                    colorPNG = self.pngBlank

                topLeftCoords = self.top_left_coords(x,y)

                main_game_state.displaySurf.blit(colorPNG, topLeftCoords)

    def draw_score(self, main_game_state):

        # Score
        scoreStr = 'Score: ' + str(self.score)
        scoreSurf = main_game_state.textBoxFont.render(scoreStr, True, BLACK)
        scoreRect = scoreSurf.get_rect()
        scoreRect.left = XMARGIN
        scoreRect.bottom = YMARGIN - BRICKGAP

        main_game_state.displaySurf.blit(scoreSurf, scoreRect)

    def top_left_coords(self, x, y):

        topLeftCoords = [XMARGIN + (x * BRICKLENGTH) + (x * BRICKGAP), YMARGIN + (y * BRICKHEIGHT) + (y * BRICKGAP)]
        return topLeftCoords

    def get_brick_at_pixel(self, mousex, mousey):

        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                topLeftCoords = self.top_left_coords(boxx, boxy)
                boxRect = pygame.Rect(topLeftCoords[0], topLeftCoords[1], BRICKLENGTH, BRICKHEIGHT)
                if boxRect.collidepoint(mousex, mousey):
                    return [boxx, boxy]
        return [None, None]

    def squared_function(self, c, x):

        # y = c * x ^ 2
        xSq = x**2
        y = xSq * c

        return y

    def falling_animation(self, vertDict, main_game_state):

        counter = 0
        squareCounter = 1

        while True:

            self.draw_background(main_game_state)
            self.draw_score(main_game_state)

            doneCounter = 0
            for brick in self.brickList:

                colorPNG = 0
                if self.board[brick[1]][brick[0]] == 'Red':
                    colorPNG = self.pngRed
                elif self.board[brick[1]][brick[0]] == 'Yel':
                    colorPNG = self.pngYel
                elif self.board[brick[1]][brick[0]] == 'Gre':
                    colorPNG = self.pngGre
                elif self.board[brick[1]][brick[0]] == 'Prp':
                    colorPNG = self.pngPrp
                elif self.board[brick[1]][brick[0]] == 'Blu':
                    colorPNG = self.pngBlu
                elif self.board[brick[1]][brick[0]] == 'Gry':
                    colorPNG = self.pngGry
                elif self.board[brick[1]][brick[0]] == 'XXX':
                    colorPNG = self.pngBlank

                topLeftCoord = self.top_left_coords(brick[0], brick[1])
                brickDistance = vertDict[str(brick)]
                stopTopLeftCoord = [topLeftCoord[0], topLeftCoord[1] + (brickDistance * (BRICKHEIGHT + BRICKGAP))]

                if counter % 6 == 0:
                    mult = int(self.squared_function(1, squareCounter))
                    topLeftCoord[1] = topLeftCoord[1] + mult
                    if topLeftCoord[1] >= stopTopLeftCoord[1]:
                        topLeftCoord[1] = stopTopLeftCoord[1]
                        doneCounter += 1
                    main_game_state.displaySurf.blit(colorPNG, topLeftCoord)

            if counter % 6 == 0:
                squareCounter += 1

            if doneCounter == len(self.brickList):
                break

            # Update Display
            pygame.display.update()
            main_game_state.fpsClock.tick(FPS)

    def horizontal_animation(self, horizDict, main_game_state):

        counter = 0
        squareCounter = 1

        while True:

            self.draw_background(main_game_state)
            self.draw_score(main_game_state)

            doneCounter = 0
            for brick in self.brickList:

                colorPNG = 0
                if self.board[brick[1]][brick[0]] == 'Red':
                    colorPNG = self.pngRed
                elif self.board[brick[1]][brick[0]] == 'Yel':
                    colorPNG = self.pngYel
                elif self.board[brick[1]][brick[0]] == 'Gre':
                    colorPNG = self.pngGre
                elif self.board[brick[1]][brick[0]] == 'Prp':
                    colorPNG = self.pngPrp
                elif self.board[brick[1]][brick[0]] == 'Blu':
                    colorPNG = self.pngBlu
                elif self.board[brick[1]][brick[0]] == 'Gry':
                    colorPNG = self.pngGry
                elif self.board[brick[1]][brick[0]] == 'XXX':
                    colorPNG = self.pngBlank

                topLeftCoord = self.top_left_coords(brick[0], brick[1])
                brickDistance = horizDict[str(brick)]
                stopTopLeftCoord = [topLeftCoord[0] - (brickDistance * (BRICKHEIGHT + BRICKGAP)), topLeftCoord[1]]

                if counter % 6 == 0:
                    mult = int(self.squared_function(1, squareCounter))
                    topLeftCoord[0] = topLeftCoord[0] - mult
                    if topLeftCoord[0] <= stopTopLeftCoord[0]:
                        topLeftCoord[0] = stopTopLeftCoord[0]
                        doneCounter += 1
                    main_game_state.displaySurf.blit(colorPNG, topLeftCoord)

            if counter % 6 == 0:
                squareCounter += 1

            if doneCounter == len(self.brickList):
                break

            # Update Display
            pygame.display.update()
            main_game_state.fpsClock.tick(FPS)

    def money_plays_handler(self, main_game_state):

        numMoneyPlays = main_game_state.myPlayer.moneyPlaysList.count(main_game_state.currentDate)

        if numMoneyPlays < 3:
            main_game_state.myPlayer.moneyPlaysList.append(main_game_state.currentDate)
            main_game_state.myPlayer.money = main_game_state.myPlayer.money + 10 + (5 * (self.level - 1))
