import pygame
from pygame.locals import *
from virtualKeyboard import VirtualKeyboard
from Animations import gold_burst, watering_animation
from Brick_Pop import brick_pop_main
import sys
import pickle
from time import strftime, time

# Color Inits
colorDict = {
    'Aqua' : ( 0, 255, 255),
    'Black' : ( 0, 0, 0),
    'Blue' : ( 0, 0, 255),
    'Fuchsia' : (255, 0, 255),
    'Gray' : (128, 128, 128),
    'Green' : ( 0, 128, 0),
    'Lime' : ( 0, 255, 0),
    'Maroon' : (128, 0, 0),
    'Navy' : ( 0, 0, 128),
    'Olive' : (128, 128, 0),
    'Purple' : (128, 0, 128),
    'Red' : (255, 0, 0),
    'Silver' : (192, 192, 192),
    'Teal' : ( 0, 128, 128),
    'White' : (255, 255, 255),
    'Yellow' : (255, 255, 0)
}

BGCOLOR= (197, 193, 184)

# Sprites Inits
testSprites = ['Sprites/Cactuar_t1.png',
           'Sprites/Cactuar_t2.png',
           'Sprites/Cactuar_t3.png',
           'Sprites/Cactuar_t4.png',
           'Sprites/Cactuar_t5.png',
           'Sprites/Cactuar_t6.png',]

# Other Inits
FPS = 30
screenWidth = 320
screenHeight = 400

defPlayerName = "Vivibb"

playerX = 0
playerY = 0

############################################################
## Functions
############################################################

def main():

    # Initialize Game
    global game_state
    game_state = game()

    # new_savefile_test(game_state, True)
    game_state.load_game()

    # Title Screen
    game_state = title_screen(game_state)

    if game_state.myPlayer.newGame == True:
        game_state = game_intro(game_state)

    game_state.load_assets()


    #TESTING Brick_Pop
    # brick_pop_main(game_state)

    #TEMPORARY
    # game_state = house_tour(game_state)

    game_state.set_state('Main_Screen')

    # Main Game Loop
    counter = 0
    while True:

        if game_state.state == 'Main_Screen':
            game_state.main_screen()
        elif game_state.state == 'Brick_Pop':
            brick_pop_main(game_state)
        elif game_state.state == 'Water_Animation':
            gold_burst(game_state, game_state.cactus_rect.centerx, game_state.cactus_rect.centery, True)
            game_state.set_state('Main_Screen')
        elif game_state.state == 'Cant_Water':
            TextDisplayFN(game_state, [[game_state.myPlayer.myCactus.name + ' is full!', 'Try again later.']])
            game_state.set_state('Main_Screen')

    return 0

def TextDisplayFN(game_state, textList):

    displayCopy = game_state.displaySurf.copy()

    buffer = 7
    outerBoxHeight = 70
    innerBoxHeight = outerBoxHeight - (2*buffer)

    # Write Text
    game_state.change_font(14)

    redTriList = [0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0]

    pygame.display.update()
    game_state.fpsClock.tick(FPS)

    for text_lines in textList:

        counter = 0
        while True:

            game_state.displaySurf.blit(displayCopy, (0, 0))

            mouseClicked = False

            # Draw Box
            outerBox = pygame.draw.rect(game_state.displaySurf, colorDict['Yellow'], [7, 327, 306, 66])
            innerX = 10
            innerY = 330
            innerWidth = 300
            innerHeight = 60
            innerBox = pygame.draw.rect(game_state.displaySurf, colorDict['White'],
                                        [innerX, innerY, innerWidth, innerHeight])

            # Draw Text
            textSurfTextBox = game_state.textBoxFont.render(text_lines[0], True, colorDict['Black'])
            textRectTextBox = textSurfTextBox.get_rect()
            textRectTextBox.left = innerX + 5
            textRectTextBox.top = innerY + 5
            game_state.displaySurf.blit(textSurfTextBox, textRectTextBox)

            textSurfTextBox = game_state.textBoxFont.render(text_lines[1], True, colorDict['Black'])
            textRectTextBox = textSurfTextBox.get_rect()
            textRectTextBox.left = innerX + 5
            textRectTextBox.top = innerY + 5 + 5 + textRectTextBox.height
            game_state.displaySurf.blit(textSurfTextBox, textRectTextBox)

            for event in pygame.event.get():
                if event.type == QUIT:
                    game_state.quit_game()
                elif event.type == MOUSEMOTION:
                    game_state.mouseX, game_state.mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    game_state.mouseX, game_state.mouseY = event.pos
                    mouseClicked = True

            if mouseClicked == True:
                break
            else:
                redTri = pygame.image.load('Sprites/red_triangle.png')
                game_state.displaySurf.blit(redTri, (textRectTextBox.right + 5, textRectTextBox.top + 5 + redTriList[counter]))

                counter = (counter + 1) % len(redTriList)

            pygame.display.update()
            game_state.fpsClock.tick(FPS)


    game_state.displaySurf.blit(displayCopy, (0, 0))
    pygame.display.update()
    game_state.fpsClock.tick(FPS)

    return game_state

def game_intro(game_state):

    # Load initial game_intro screen
    intro_screen = pygame.image.load('Sprites/Intro_Screen.png')
    game_state.displaySurf.blit(intro_screen, (0, 0))

    # Introduction dialogue
    TextDisplayFN(game_state, [['Hello, and welcome to your', 'own personal cactus simulator'],
                               ['I will be your host, ', 'Master Programmer Jake.'],
                               ['Together we will explore', 'the wonderful world of Cacti!'],
                               ['Please take a moment and', 'enter your name:']])

    # Input Name
    vkeybd = VirtualKeyboard(game_state.displaySurf)
    game_state.init_player(vkeybd.run(defPlayerName))

    game_state.displaySurf.blit(intro_screen, (0, 0)) # Put screen back on

    # Post Name Dialogue
    TextDisplayFN(game_state, [['Thanks ' + game_state.myPlayer.name + '!', ''],
                               ['Now then, I think', 'something\'s missing'],
                               ['...','...'],
                               ['Ahh yes of course, ', 'the cactus!'],
                               ['Lucky for you I just', 'returned from the desert'],
                               ['and have the perfect', 'buddy for you!']
                               ])

    # Load Cactus + Animation
    introScreenCactus = pygame.image.load('Sprites/Intro_Screen_Cactus.png')
    game_state.displaySurf.blit(introScreenCactus, (0, 0))

    game_state = gold_burst(game_state, 112, 149, True)

    # Dialogue
    TextDisplayFN(game_state, [['Meet your new friend!', ''],
                               ['This particular specimen', 'looks like a female.'],
                               ['What would you like', 'to name her?']
                               ])

    # Input Name
    vkeybd = VirtualKeyboard(game_state.displaySurf)
    game_state.myPlayer.init_cactus(vkeybd.run('Cactuar'))

    # Dialogue
    TextDisplayFN(game_state, [['Splendid!', ''],
                               ['You and ' + game_state.myPlayer.myCactus.name, 'will make a great team.'],
                               ['Now that we\'re settled,', 'I\'ll give you a quick'],
                               ['tour of your home.', '']
                               ])

    # game_state.myPlayer.newGame = False
    game_state.save_game()

    return game_state

def new_savefile_test(game_state, newGame):

    game_state.init_player("newP")
    game_state.myPlayer.init_cactus("newC")
    game_state.myPlayer.newGame = newGame

    game_state.myPlayer.waterLevel = 3

    game_state.save_game()

def title_screen(game_state):

    game_state.set_state("Title_Screen")

    backgroundSprites = ["Sprites/title/Title_Screen1.png",
                         "Sprites/title/Title_Screen2.png"]
    startSprite = "Sprites/START.png"

    backgroundCounter = 0
    counter = 0

    while True:

        background = pygame.image.load(backgroundSprites[backgroundCounter])
        start = pygame.image.load(startSprite)

        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                game_state.quit_game()
            elif event.type == MOUSEMOTION:
                game_state.mouseX, game_state.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                game_state.mouseX, game_state.mouseY = event.pos
                mouseClicked = True

        if counter %6 == 0:
            game_state.displaySurf.blit(background, (0,0))
            backgroundCounter = (backgroundCounter + 1) % len(backgroundSprites)

        if counter%30 <=15:
            game_state.displaySurf.blit(start, (85, 200))

        counter+=1

        counter = counter % 2592000

        # Update Display
        pygame.display.update()
        game_state.fpsClock.tick(FPS)

        if mouseClicked == True:
            game_state.set_state("Main_Screen")
            break

    return game_state

def house_tour(game_state):

    game_state.state = "House_Tour"

    alphaVal = 170

    # Load house screen
    house_screen = pygame.image.load('Sprites/main_screen1.png')
    game_state.displaySurf.blit(house_screen, (0, 0))

    # Load Cactus
    #TODO: cactus sprite should come from game_state
    cactus_sprite = pygame.image.load('Sprites/cactus_tutorial.png')
    game_state.displaySurf.blit(cactus_sprite, (112, 246))

    # Load Menu Button
    menu_button_sprite = pygame.image.load('Sprites/menu_button.png')
    menu_button_rect = menu_button_sprite.get_rect()
    game_state.displaySurf.blit(menu_button_sprite, (10, 10))

    # Load Empty Water Meter
    empty_water_meter_sprite = pygame.image.load('Sprites/water_meter/Water_Meter_0_1.png')
    game_state.displaySurf.blit(empty_water_meter_sprite, (303, 157))

    TextDisplayFN(game_state, [['Welcome home ' + game_state.myPlayer.name + '!', ''],
                               ['Let\'s get you acquanted.', '']])

    ########################
    # Cactus + Water
    ########################

    game_state.myPlayer.waterLevel = 0

    fullSprites = ['Sprites/water_meter/Water_Meter_4_1.png',
                   'Sprites/water_meter/Water_Meter_4_2.png',
                   'Sprites/water_meter/Water_Meter_4_3.png',
                   'Sprites/water_meter/Water_Meter_4_4.png',]

    alphaSurface = pygame.Surface((game_state.width, game_state.height))
    alphaSurface.fill((0, 0, 0))
    alphaSurface.set_alpha(alphaVal)
    game_state.displaySurf.blit(alphaSurface, (0, 0))

    cactus_sprite = pygame.image.load('Sprites/cactus_tutorial.png')
    game_state.displaySurf.blit(cactus_sprite, (112, 246))

    TextDisplayFN(game_state, [['I took the liberty of putting', 'your cactus on your desk,'],
                               ['I hope you don\'t mind.', ''],
                               ['I\'m sure you have noticed', 'that ' + game_state.myPlayer.myCactus.name + ' here is quite small.'],
                               ['Don\'t worry, with proper care', 'your cactus will grow in ways'],
                               ['you can\'nt possible imagine!', ''],
                               ['How, you ask?', 'By watering it silly!']])

    # Display thirsty icon
    thirsty_icon = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_thirsty.png')
    game_state.displaySurf.blit(thirsty_icon, (146, 204))


    TextDisplayFN(game_state, [['Looks like ' + game_state.myPlayer.myCactus.name + ' is thirsty, ', 'let\'s water him.']])

    # Load Empty Water Meter
    empty_water_meter_sprite = pygame.image.load('Sprites/water_meter/Water_Meter_0_1.png')
    water_meter_rect = empty_water_meter_sprite.get_rect()
    water_meter_rect = water_meter_rect.move(303,157)
    game_state.displaySurf.blit(empty_water_meter_sprite, (303, 157))

    TextDisplayFN(game_state, [['This is your water meter.', 'You will use it to water your cactus'],
                               ['Uh oh, looks like you\'re', 'all dry at the moment...'],
                               ['Allow me...', '']])

    #TODO: some kind of water fill up animation

    emptyDisplayCopy = game_state.displaySurf.copy()

    game_state.myPlayer.waterLevel = 4

    counter = 0
    waterCounter = 0
    while True:

        game_state.displaySurf.blit(emptyDisplayCopy, (0,0))

        full_water_meter_sprite = pygame.image.load(fullSprites[waterCounter])
        game_state.displaySurf.blit(full_water_meter_sprite, (303, 157))

        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                game_state.quit_game()
            elif event.type == MOUSEMOTION:
                game_state.mouseX, game_state.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                game_state.mouseX, game_state.mouseY = event.pos
                mouseClicked = True

        if mouseClicked == True:
            break

        if counter % 6 == 0:
            waterCounter = (waterCounter + 1) % len(fullSprites)

        counter += 1
        counter = counter % 2592000

        # Update Display
        pygame.display.update()
        game_state.fpsClock.tick(FPS)

    TextDisplayFN(game_state, [['Now that we\'re all filled up,', 'we can get down to business'],
                               ['Tap the water meter to water.', '']])

    # Water the plant

    displayCopy = game_state.displaySurf.copy()

    counter = 0
    initFrame = -1
    wateringAnimationInit = False
    while True:

        if wateringAnimationInit == False:
            game_state.displaySurf.blit(displayCopy, (0, 0))
        else:
            game_state.displaySurf.blit(emptyDisplayCopy, (0, 0))

        mouseClicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                game_state.quit_game()
            elif event.type == MOUSEMOTION:
                game_state.mouseX, game_state.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                game_state.mouseX, game_state.mouseY = event.pos
                mouseClicked = True

        if water_meter_rect.collidepoint(game_state.mouseX, game_state.mouseY) and mouseClicked == True:
            wateringAnimationInit = True

        if wateringAnimationInit == True:

            if initFrame == -1:
                initFrame = counter

            wateringAnimationSprite = watering_animation(initFrame, counter, game_state.myPlayer.waterLevel, 5)

            if wateringAnimationSprite == "DONE":
                game_state.myPlayer.waterLevel =- 1
                break

            else:
                game_state.displaySurf.blit(wateringAnimationSprite, (271, 157))

        counter += 1
        counter = counter % 2592000

        # Update Display
        pygame.display.update()
        game_state.fpsClock.tick(FPS)



    ########################
    # Main Menu
    ########################

    alphaSurface = pygame.Surface((game_state.width, game_state.height))
    alphaSurface.fill((0,0,0))
    alphaSurface.set_alpha(alphaVal)
    game_state.displaySurf.blit(alphaSurface, (0,0))

    menu_button_sprite = pygame.image.load('Sprites/menu_button.png')
    menu_button_rect = menu_button_sprite.get_rect()
    menu_button_rect = menu_button_rect.move(10,10)
    game_state.displaySurf.blit(menu_button_sprite, (10,10))

    TextDisplayFN(game_state, [['This is the main menu button.', ''],
                               ['It will allow you to', 'quit the game, change your'],
                               ['name, change your cactus\'s', 'name, and some other things.'],
                               ['Let\'s try it now!', 'Click on the menu icon.']])

    while True:

        mouseClicked = False

        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT:
                game_state.quit_game()
            elif event.type == MOUSEMOTION:
                game_state.mouseX, game_state.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                game_state.mouseX, game_state.mouseY = event.pos
                mouseClicked = True

        if menu_button_rect.collidepoint(game_state.mouseX, game_state.mouseY) and mouseClicked == True:
            game_state = main_menu(game_state)
            #TODO: tutorial to make go to about page, go to birthday card, remind to quit game in order to save progress
            break

        # Update Display
        pygame.display.update()
        game_state.fpsClock.tick(FPS)


    return game_state

def main_menu(game_state):

    # game_state.state = "Main_Menu"

    #TODO: make main menu
    TextDisplayFN(game_state, [['Main Menu Placeholder.', '']])

    return game_state


############################################################
## Classes
############################################################

class game:

    def __init__(self):

        pygame.init()
        self.displaySurf = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption('Vivibb\'s Cactus')
        self.fpsClock = pygame.time.Clock()
        self.fpsVal = FPS
        self.height = screenHeight
        self.width = screenWidth
        self.mouseX = 0
        self.mouseY = 0
        self.frameCounter = 0

        self.textBoxFont = pygame.font.SysFont('Arial Black', 14)

        self.state = 'Title_Screen'

        self.highScores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.moneyPlaysList = []

        self.update_datetime()

    def set_state(self, command):

        if command == 'Title_Screen':
            self.state = 'Title_screen'
        elif command == 'Main_Screen':
            self.state = 'Main_Screen'
        elif command == 'Brick_Pop':
            self.state = 'Brick_Pop'
        elif command == 'Water_Animation':
            self.state = 'Water_Animation'
        elif command == 'Cant_Water':
            self.state = 'Cant_Water'

    def change_font(self, fontSize):
        self.textBoxFont = pygame.font.SysFont('Arial Black', fontSize)

    def load_assets(self):

        # House Screen
        self.houseScreen = pygame.image.load('Sprites/main_screen1.png')

        # Main Menu BG
        self.BGPng = pygame.image.load('Sprites/Brick_Pop/BP_Background.png')

        # Icons + Locations
        self.menuIcon = pygame.image.load('Sprites/menu_button.png')
        self.menuIcon_loc = (10,8)
        self.menuIcon_rect = pygame.Rect(self.menuIcon_loc[0], self.menuIcon_loc[1], 30, 30)

        self.backIcon = pygame.image.load('Sprites/back_button.png')
        self.backIcon_loc = (10,8)
        self.backIcon_rect = pygame.Rect(self.backIcon_loc[0], self.backIcon_loc[1], 30, 30)

        self.shopIcon = pygame.image.load('Sprites/shop_icon.png')
        self.shopIcon_loc = (278,6)
        self.shopIcon_rect = pygame.Rect(self.shopIcon_loc[0], self.shopIcon_loc[1], 32, 32)

        self.controllaIcon = pygame.image.load('Sprites/controlla.png')
        self.controllaIcon_loc = (218,13)
        self.controllaIcon_rect = pygame.Rect(self.controllaIcon_loc[0], self.controllaIcon_loc[1], 34, 18)

        # Speech Bubbles
        self.speechHappy = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_happy.png')
        self.speechHeart = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_heart.png')
        self.speechSkull = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_skull.png')
        self.speechSleepy = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_sleepy.png')
        self.speechThirsty = pygame.image.load('Sprites/speech_bubbles/PNGs/speech_thirsty.png')

        # Water Container
        self.waterContainer0 = pygame.image.load('Sprites/water_meter/Water_Meter_0_1.png')

        self.waterContainer1 = [pygame.image.load('Sprites/water_meter/Water_Meter_1_1.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_1_2.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_1_3.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_1_4.png')  ]

        self.waterContainer2 = [pygame.image.load('Sprites/water_meter/Water_Meter_2_1.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_2_2.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_2_3.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_2_4.png'), ]

        self.waterContainer3 = [pygame.image.load('Sprites/water_meter/Water_Meter_3_1.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_3_2.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_3_3.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_3_4.png'), ]

        self.waterContainer4 = [pygame.image.load('Sprites/water_meter/Water_Meter_4_1.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_4_2.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_4_3.png'),
                                pygame.image.load('Sprites/water_meter/Water_Meter_4_4.png'), ]

        self.waterContainer_loc = (303, 157)
        self.waterContainer_rect = pygame.Rect(self.waterContainer_loc[0], self.waterContainer_loc[1], 17, 243)

        self.load_cactus_assets()

    def load_cactus_assets(self):

        # Decide which cactus assets to loade
        if self.myPlayer.myCactus.level == 1:
            self.cactusSpriteList_idle = [pygame.image.load('Sprites/Cactus_L1/Cactus_L1_Main1.png'),
                                          pygame.image.load('Sprites/Cactus_L1/Cactus_L1_Main2.png')]
            self.cactusSpriteList_idle_loc = (120, 246)
            self.cactus_rect = pygame.Rect(self.cactusSpriteList_idle_loc[0], self.cactusSpriteList_idle_loc[1], 24, 32)

        if self.myPlayer.myCactus.level == 2:
            self.cactusSpriteList_idle = [pygame.image.load('Sprites/Cactus_L2.png')]
            self.cactusSpriteList_idle_loc = (100, 195)
            self.cactus_rect = pygame.Rect(self.cactusSpriteList_idle_loc[0], self.cactusSpriteList_idle_loc[1], 82,
                                           89)

        #TODO: add rest of cactus sprites

    def get_speechBubble_loc(self):

        # TODO: Make dependent on cactus type
        if self.myPlayer.myCactus.level == 1:
            self.speechBubble_loc = (self.cactusSpriteList_idle_loc[0] + 26, self.cactusSpriteList_idle_loc[1] - 40)
        if self.myPlayer.myCactus.level == 2:
            self.speechBubble_loc = (self.cactusSpriteList_idle_loc[0] + 55, self.cactusSpriteList_idle_loc[1] - 75)

    def newScore(self, score):

        minScore = min(self.myPlayer.highScores)
        if score > minScore:
            del self.myPlayer.highScores[self.myPlayer.highScores.index(minScore)]
            self.myPlayer.highScores.append(score)

        self.myPlayer.highScores.sort()
        self.myPlayer.highScores.reverse()

    def init_player(self, inpName):

        self.myPlayer = player(inpName)

    def save_game(self):
        with open("savegame.dat", "wb") as f:
            pickle.dump(self.myPlayer, f)

    def load_game(self):
        with open("savegame.dat", "rb") as f:
            self.myPlayer = pickle.load(f)

    def quit_game(self):

        self.save_game()

        pygame.quit()
        sys.exit()

    def update_datetime(self):

        self.currentDate = strftime('%m/%d/%y')
        self.currentTime = strftime('%H:%M:%S')

    def TextDisplayFNClass(self, textList):

        displayCopy = self.displaySurf.copy()

        buffer = 7
        outerBoxHeight = 70
        innerBoxHeight = outerBoxHeight - (2 * buffer)

        # Write Text
        self.change_font(14)

        redTriList = [0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0]

        pygame.display.update()
        self.fpsClock.tick(FPS)

        for text_lines in textList:

            counter = 0
            while True:

                self.displaySurf.blit(displayCopy, (0, 0))

                mouseClicked = False

                # Draw Box
                outerBox = pygame.draw.rect(self.displaySurf, colorDict['Yellow'], [7, 327, 306, 66])
                innerX = 10
                innerY = 330
                innerWidth = 300
                innerHeight = 60
                innerBox = pygame.draw.rect(self.displaySurf, colorDict['White'],
                                            [innerX, innerY, innerWidth, innerHeight])

                # Draw Text
                textSurfTextBox = self.textBoxFont.render(text_lines[0], True, colorDict['Black'])
                textRectTextBox = textSurfTextBox.get_rect()
                textRectTextBox.left = innerX + 5
                textRectTextBox.top = innerY + 5
                self.displaySurf.blit(textSurfTextBox, textRectTextBox)

                textSurfTextBox = self.textBoxFont.render(text_lines[1], True, colorDict['Black'])
                textRectTextBox = textSurfTextBox.get_rect()
                textRectTextBox.left = innerX + 5
                textRectTextBox.top = innerY + 5 + 5 + textRectTextBox.height
                self.displaySurf.blit(textSurfTextBox, textRectTextBox)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.quit_game()
                    elif event.type == MOUSEMOTION:
                        self.mouseX, self.mouseY = event.pos
                    elif event.type == MOUSEBUTTONUP:
                        self.mouseX, self.mouseY = event.pos
                        mouseClicked = True

                if mouseClicked == True:
                    break
                else:
                    redTri = pygame.image.load('Sprites/red_triangle.png')
                    self.displaySurf.blit(redTri, (
                    textRectTextBox.right + 5, textRectTextBox.top + 5 + redTriList[counter]))

                    counter = (counter + 1) % len(redTriList)

                pygame.display.update()
                self.fpsClock.tick(FPS)

        self.displaySurf.blit(displayCopy, (0, 0))
        pygame.display.update()
        self.fpsClock.tick(FPS)

        return self

    ###########################
    ## Main Graphics Engine
    ###########################

    # Main Screen

    def main_screen(self):

        self.waterCounter = 0

        while True:
            mouseClicked = False

            self.ms_display_handler()

            if self.myPlayer.newGame == True:
                self.myPlayer.waterLevel = 4
                self.house_tour()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit_game()
                elif event.type == MOUSEMOTION:
                    self.mouseX, self.mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.mouseX, self.mouseY = event.pos
                    mouseClicked = True

            # What does mouse click
            if mouseClicked == True:
                if self.menuIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    self.main_menu()
                elif self.shopIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    self.shop_menu()
                elif self.controllaIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    self.set_state('Brick_Pop')
                    break
                elif self.waterContainer_rect.collidepoint(self.mouseX, self.mouseY):
                    self.water_cactus()
                    break

            # Update Display
            pygame.display.update()
            self.fpsClock.tick(FPS)
            self.frameCounter += 1
            self.frameCounter = self.frameCounter % 2592000

    def ms_display_handler(self):

        # Load house screen
        self.displaySurf.blit(self.houseScreen, (0, 0))

        # Load Buttons
        self.displaySurf.blit(self.menuIcon, self.menuIcon_loc)
        self.displaySurf.blit(self.controllaIcon, self.controllaIcon_loc)
        self.displaySurf.blit(self.shopIcon, self.shopIcon_loc)

        # Load Cactus
        self.cactus_idle_handler()

        # Load Speech Bubble
        self.speech_bubble_handler()

        # Load Water Container
        self.water_handler()

    def cactus_idle_handler(self):
        # This function will handle the cactus idle animation

        if self.myPlayer.myCactus.level == 1:       # Level 1 Cactus
            if self.frameCounter % 180 <= 160:
                self.displaySurf.blit(self.cactusSpriteList_idle[0], self.cactusSpriteList_idle_loc)
            elif self.frameCounter % 180 > 160 and self.frameCounter % 180 <= 165:
                self.displaySurf.blit(self.cactusSpriteList_idle[1], self.cactusSpriteList_idle_loc)
            elif self.frameCounter % 180 > 165 and self.frameCounter % 180 <= 170:
                self.displaySurf.blit(self.cactusSpriteList_idle[0], self.cactusSpriteList_idle_loc)
            elif self.frameCounter % 180 > 170 and self.frameCounter % 180 <= 175:
                self.displaySurf.blit(self.cactusSpriteList_idle[1], self.cactusSpriteList_idle_loc)
            elif self.frameCounter % 180 > 175:
                self.displaySurf.blit(self.cactusSpriteList_idle[0], self.cactusSpriteList_idle_loc)

    def speech_bubble_handler(self):

        self.myPlayer.myCactus.update_mood()
        self.get_speechBubble_loc()
        bubble = self.speechHappy

        if self.myPlayer.myCactus.mood == 'Heart':
            bubble = self.speechHeart
        elif self.myPlayer.myCactus.mood == 'Thirsty':
            bubble = self.speechThirsty
        elif self.myPlayer.myCactus.mood == 'Sleepy':
            bubble = self.speechSleepy
        elif self.myPlayer.myCactus.mood == 'Skull':
            bubble = self.speechSkull

        if self.frameCounter % 60 <= 30:
            self.displaySurf.blit(bubble, self.speechBubble_loc)
        elif self.frameCounter % 60 > 30:
            self.displaySurf.blit(bubble, (self.speechBubble_loc[0], self.speechBubble_loc[1] + 4))

    def water_handler(self):

        waterList = []
        if self.myPlayer.waterLevel == 1:
            waterList = self.waterContainer1
        elif self.myPlayer.waterLevel == 2:
            waterList = self.waterContainer2
        elif self.myPlayer.waterLevel == 3:
            waterList = self.waterContainer3
        elif self.myPlayer.waterLevel == 4:
            waterList = self.waterContainer4

        if self.myPlayer.waterLevel == 0:
            self.displaySurf.blit(self.waterContainer0, self.waterContainer_loc)
        else:
            self.displaySurf.blit(waterList[self.waterCounter], self.waterContainer_loc)
            if self.frameCounter % 6 == 0:
                self.waterCounter = (self.waterCounter + 1) % len(waterList)

    def water_cactus(self):

        waterMult = 1
        if time() - self.myPlayer.myCactus.lastFert <= 259200:
            waterMult = 2

        if self.myPlayer.waterLevel <= 0:
            self.myPlayer.waterLevel = 0
        elif time() - self.myPlayer.myCactus.lastWatered <= 57600:
            self.set_state('Cant_Water')
        else:
            self.myPlayer.waterLevel = self.myPlayer.waterLevel - 1
            self.myPlayer.myCactus.lastWatered = time()
            self.myPlayer.myCactus.EXP += 1*waterMult

            #TODO: get rid of this shit
            if self.myPlayer.myCactus.level == 1 and self.myPlayer.myCactus.EXP == 15:
                self.myPlayer.myCactus.level = 2
                self.myPlayer.myCactus.EXP = 10
                self.load_cactus_assets()

            self.set_state('Water_Animation')

    # House Tour

    def house_tour(self):

        self.TextDisplayFNClass([  ['Welcome to your home!', ''],
                                   ['This will be a rough tutorial of', 'how to use your room.'],
                                   ['(Not gonna lie this was gonna be', 'more fleshed out but I ran'],
                                   ['out of time lol. Ask me if you', 'have questions hehe)'],
                                   ['To the right is the water meter.', ''],
                                   ['It is used to water your cactus.', 'Your cactus can be watered once'],
                                   ['every 16 hours, and will suffer', 'if it isn\'t watered for 32 hours.'],
                                   ['On the top right, we have', 'the shop and Brick Pop.'],
                                   ['Play Brick Pop to earn money, ', 'which you can use to buy water'],
                                   ['and fertilizer for your cactus.', 'Brick Pop can be played'],
                                   ['three times a day for coins, ', 'and unlimited times for fun!'],
                                   ['Finally, we have the main menu', 'on the top left.'],
                                   ['Make sure to go here when you', 'are done playing to save your game.'],
                                   ['Also, be sure to check out the', 'about section for a special surprise!'],])

        self.myPlayer.newGame = False

    # Shop

    def shop_menu(self):

        while True:
            mouseClicked = False

            self.displaySurf.blit(self.BGPng, (0, 0))
            self.displaySurf.blit(self.backIcon, self.backIcon_loc)
            self.draw_shop_menu()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit_game()
                elif event.type == MOUSEMOTION:
                    self.mouseX, self.mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.mouseX, self.mouseY = event.pos
                    mouseClicked = True

            # What does mouse click
            if mouseClicked == True:
                if self.outerBoxWater_R.collidepoint(self.mouseX, self.mouseY):
                    self.myPlayer.buy_water()
                elif self.outerBoxFert_R.collidepoint(self.mouseX, self.mouseY):
                    self.myPlayer.buy_fert()
                elif self.outerBoxCN_R.collidepoint(self.mouseX, self.mouseY):
                    vkeybd = VirtualKeyboard(self.displaySurf)
                    self.myPlayermyCactus.name = vkeybd.run(self.myPlayer.myCactus.name)
                elif self.backIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    self.set_state('Main_Screen')
                    break

            # Update Display
            pygame.display.update()
            self.fpsClock.tick(FPS)
            self.frameCounter += 1
            self.frameCounter = self.frameCounter % 2592000

    def draw_shop_menu(self):

        # Player coin total
        textSurfMoney = self.textBoxFont.render('Coins: ' + str(self.myPlayer.money), True, colorDict['Black'])
        textRectMoney = textSurfMoney.get_rect()
        textRectMoney.right = 310
        textRectMoney.top = 10
        self.displaySurf.blit(textSurfMoney, textRectMoney)

        # Buffers for shop items
        boxBuffer = 3
        otherBuffer = 10

        # Shop Items - Water

        # Left Boxes
        outerBoxWater_L = pygame.draw.rect(self.displaySurf, colorDict['Black'], [20, 100, 200, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['White'], [20 + boxBuffer, 100 + boxBuffer, 200 - (boxBuffer*2), 64 - (boxBuffer*2)])

        textSurfWater = self.textBoxFont.render('One dose of water.', True, colorDict['Black'])
        textRectWater = textSurfWater.get_rect()
        textRectWater.centerx = innerBox.centerx
        textRectWater.centery = innerBox.centery
        self.displaySurf.blit(textSurfWater, textRectWater)

        # Right Boxes
        self.outerBoxWater_R = pygame.draw.rect(self.displaySurf, colorDict['Black'], [242, 100, 60, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['Yellow'],
                                    [242 + boxBuffer, 100 + boxBuffer, 60 - (boxBuffer * 2), 64 - (boxBuffer * 2)])

        textSurfWater = self.textBoxFont.render('30C', True, colorDict['Black'])
        textRectWater = textSurfWater.get_rect()
        textRectWater.centerx = innerBox.centerx
        textRectWater.centery = innerBox.centery
        self.displaySurf.blit(textSurfWater, textRectWater)

        # Shop Items - Fertilizer

        # Left Boxes
        outerBoxFert_L = pygame.draw.rect(self.displaySurf, colorDict['Black'], [20, 100 + 64 + otherBuffer, 200, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['White'],
                                    [20 + boxBuffer, 100 + 64 + otherBuffer + boxBuffer, 200 - (boxBuffer * 2), 64 - (boxBuffer * 2)])

        textSurfFert = self.textBoxFont.render('72 hour Fertilizer', True, colorDict['Black'])
        textRectFert = textSurfFert.get_rect()
        textRectFert.centerx = innerBox.centerx
        textRectFert.centery = innerBox.centery
        self.displaySurf.blit(textSurfFert, textRectFert)

        # Right Boxes
        self.outerBoxFert_R = pygame.draw.rect(self.displaySurf, colorDict['Black'], [242, 100 + 64 + otherBuffer, 60, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['Yellow'],
                                    [242 + boxBuffer, 100 + 64 + otherBuffer + boxBuffer, 60 - (boxBuffer * 2), 64 - (boxBuffer * 2)])

        textSurfFert = self.textBoxFont.render('100C', True, colorDict['Black'])
        textRectFert = textSurfFert.get_rect()
        textRectFert.centerx = innerBox.centerx
        textRectFert.centery = innerBox.centery
        self.displaySurf.blit(textSurfFert, textRectFert)

        # Shop Items - Change Cactus Name
        # Left Boxes
        outerBoxCN_L = pygame.draw.rect(self.displaySurf, colorDict['Black'],
                                          [20, 100 + 64*2 + otherBuffer*2, 200, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['White'],
                                    [20 + boxBuffer, 100 + 64*2 + otherBuffer*2 + boxBuffer, 200 - (boxBuffer * 2),
                                     64 - (boxBuffer * 2)])

        textSurfCN = self.textBoxFont.render('Change Cactus Name', True, colorDict['Black'])
        textRectCN = textSurfCN.get_rect()
        textRectCN.centerx = innerBox.centerx
        textRectCN.centery = innerBox.centery
        self.displaySurf.blit(textSurfCN, textRectCN)

        # Right Boxes
        self.outerBoxCN_R = pygame.draw.rect(self.displaySurf, colorDict['Black'],
                                          [242, 100 + 64*2 + otherBuffer*2, 60, 64])
        innerBox = pygame.draw.rect(self.displaySurf, colorDict['Yellow'],
                                    [242 + boxBuffer, 100 + 64*2 + otherBuffer*2 + boxBuffer, 60 - (boxBuffer * 2),
                                     64 - (boxBuffer * 2)])

        textSurfCN = self.textBoxFont.render('50C', True, colorDict['Black'])
        textRectCN = textSurfCN.get_rect()
        textRectCN.centerx = innerBox.centerx
        textRectCN.centery = innerBox.centery
        self.displaySurf.blit(textSurfCN, textRectCN)

    # Main Menu

    def main_menu(self):

        while True:
            mouseClicked = False

            self.displaySurf.blit(self.BGPng, (0, 0))
            self.displaySurf.blit(self.backIcon, self.backIcon_loc)
            self.draw_main_menu()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit_game()
                elif event.type == MOUSEMOTION:
                    self.mouseX, self.mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.mouseX, self.mouseY = event.pos
                    mouseClicked = True

            # What does mouse click
            if mouseClicked == True:
                if self.backIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    self.set_state('Main_Screen')
                    break
                elif self.textRectTextBox1.collidepoint(self.mouseX, self.mouseY):
                    self.about_menu()
                elif self.textRectTextBox2.collidepoint(self.mouseX, self.mouseY):
                    vkeybd = VirtualKeyboard(self.displaySurf)
                    self.myPlayer.name = vkeybd.run(self.myPlayer.name)
                elif self.textRectTextBox3.collidepoint(self.mouseX, self.mouseY):
                    self.quit_game()

            # Update Display
            pygame.display.update()
            self.fpsClock.tick(FPS)
            self.frameCounter += 1
            self.frameCounter = self.frameCounter % 2592000

    def draw_main_menu(self):

        # Draw Text
        textSurfTextBox = self.textBoxFont.render('About...', True, colorDict['Black'])
        self.textRectTextBox1 = textSurfTextBox.get_rect()
        self.textRectTextBox1.centerx = 160
        self.textRectTextBox1.centery = 100
        self.displaySurf.blit(textSurfTextBox, self.textRectTextBox1)

        textSurfTextBox = self.textBoxFont.render('Change Name', True, colorDict['Black'])
        self.textRectTextBox2 = textSurfTextBox.get_rect()
        self.textRectTextBox2.centerx = 160
        self.textRectTextBox2.centery = 200
        self.displaySurf.blit(textSurfTextBox, self.textRectTextBox2)

        textSurfTextBox = self.textBoxFont.render('Save & Quit', True, colorDict['Black'])
        self.textRectTextBox3 = textSurfTextBox.get_rect()
        self.textRectTextBox3.centerx = 160
        self.textRectTextBox3.centery = 300
        self.displaySurf.blit(textSurfTextBox, self.textRectTextBox3)

    # About

    def about_menu(self):

        while True:
            mouseClicked = False

            self.displaySurf.blit(self.BGPng, (0, 0))
            self.displaySurf.blit(self.backIcon, self.backIcon_loc)
            self.draw_about_menu()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit_game()
                elif event.type == MOUSEMOTION:
                    self.mouseX, self.mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    self.mouseX, self.mouseY = event.pos
                    mouseClicked = True

            # What does mouse click
            if mouseClicked == True:
                if self.backIcon_rect.collidepoint(self.mouseX, self.mouseY):
                    break
                # elif self.envIcon_rect.collidepoint(self.mouseX, self.mouseY):
                #     self.birthday_card()

            # Update Display
            pygame.display.update()
            self.fpsClock.tick(FPS)
            self.frameCounter += 1
            self.frameCounter = self.frameCounter % 2592000

    def draw_about_menu(self):

        # Draw Text
        textSurfJake = self.textBoxFont.render('Jake Myers 2017', True, colorDict['Black'])
        self.textRectJake = textSurfJake.get_rect()
        self.textRectJake.centerx = 160
        self.textRectJake.centery = 100
        self.displaySurf.blit(textSurfJake, self.textRectJake)

        envIcon = pygame.image.load('Sprites/envelope_icon.png')
        envIcon_loc = (160-17, 150)
        self.envIcon_rect = pygame.Rect(envIcon_loc[0], envIcon_loc[1], 34, 24)
        self.displaySurf.blit(envIcon, envIcon_loc)

    # Birthday Card

class player:

    def __init__(self, inpName):

        self.name = inpName
        self.newGame = True

        self.money = 0
        self.waterLevel = 0

        self.highScores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.moneyPlaysList = []

    def init_cactus(self, inpName):

        self.myCactus = cactus(inpName)

    def buy_water(self):

        if self.waterLevel >= 4:
            # TODO: make a message saying you have too much water
            pass
        else:
            self.waterLevel += 1
            self.money -= 30

    def buy_fert(self):

        if time() - self.myCactus.lastFert <= 259200:
            pass # TODO: message
        else:
            self.myCactus.lastFert = time()

class cactus:

    def __init__(self, inpName):

        self.name = inpName
        self.level = 1
        self.EXP = 10
        self.lastWatered = time()
        self.lastFert = 0
        self.mood = 'Happy'

    def update_mood(self):

        if (time() - self.lastWatered) <= 7:
            self.mood = 'Heart'
        elif time() - self.lastWatered <= 57600*2:          # 32 hours
            if int(strftime('%H')) >= 23 or int(strftime('%H')) <= 5:
                self.mood = 'Sleepy'
            else:
                self.mood = 'Happy'
        elif time() - self.lastWatered > 57600:
            self.mood = 'Thirsty'

        if self.EXP <= 5:
            self.mood = 'Skull'

main()