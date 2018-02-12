import pygame, sys
from pygame.locals import *


########################################################################
## Image Loading
########################################################################

goldBurstList = ['Sprites/goldburst/gold_burst1.png',
                 'Sprites/goldburst/gold_burst2.png',
                 'Sprites/goldburst/gold_burst3.png',
                 'Sprites/goldburst/gold_burst4.png',
                 'Sprites/goldburst/gold_burst5.png',
                 'Sprites/goldburst/gold_burst6.png',
                 'Sprites/goldburst/gold_burst7.png',
                 'Sprites/goldburst/gold_burst8.png',
                 'Sprites/goldburst/gold_burst9.png',
                 'Sprites/goldburst/gold_burst10.png',
                 'Sprites/goldburst/gold_burst11.png',
                 'Sprites/goldburst/gold_burst12.png',
                 'Sprites/goldburst/gold_burst13.png',
                 'Sprites/goldburst/gold_burst14.png',
                 'Sprites/goldburst/gold_burst15.png',
                 'Sprites/goldburst/gold_burst16.png',
                 ]

wateringAnimationList1 = ['Sprites/watering_animation/PNGs/watering_mode_animation_1_1.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_2.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_3.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_4.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_5.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_6.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_7.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_8.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_9.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_10.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_11.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_12.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_13.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_14.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_15.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_16.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_17.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_18.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_19.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_20.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_21.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_22.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_23.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_24.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_25.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_26.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_27.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_28.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_29.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_30.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_31.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_32.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_33.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_34.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_35.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_36.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_1_37.png'
                          ]

wateringAnimationList2 = ['Sprites/watering_animation/PNGs/watering_mode_animation_2_1.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_2.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_3.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_4.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_5.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_6.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_7.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_8.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_9.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_10.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_11.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_12.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_13.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_14.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_15.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_16.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_17.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_18.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_19.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_20.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_21.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_22.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_23.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_24.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_25.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_26.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_27.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_28.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_29.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_30.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_31.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_32.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_33.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_34.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_35.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_36.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_2_37.png'
                          ]

wateringAnimationList3 = ['Sprites/watering_animation/PNGs/watering_mode_animation_3_1.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_2.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_3.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_4.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_5.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_6.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_7.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_8.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_9.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_10.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_11.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_12.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_13.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_14.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_15.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_16.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_17.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_18.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_19.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_20.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_21.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_22.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_23.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_24.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_25.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_26.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_27.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_28.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_29.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_30.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_31.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_32.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_33.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_34.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_35.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_36.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_3_37.png'
                          ]

wateringAnimationList4 = ['Sprites/watering_animation/PNGs/watering_mode_animation_4_1.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_2.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_3.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_4.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_5.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_6.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_7.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_8.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_9.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_10.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_11.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_12.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_13.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_14.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_15.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_16.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_17.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_18.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_19.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_20.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_21.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_22.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_23.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_24.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_25.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_26.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_27.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_28.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_29.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_30.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_31.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_32.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_33.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_34.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_35.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_36.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_37.png',
                          'Sprites/watering_animation/PNGs/watering_mode_animation_4_38.png'
                          ]



########################################################################
## Functions
########################################################################

def gold_burst(game_state, posX, posY, fadeBool):

    displayCopy = game_state.displaySurf.copy()

    alphaSurface = pygame.Surface((game_state.width, game_state.height))
    alphaSurface.fill((255,255,255))
    alphaSurface.set_alpha(0)

    spinCounter = 0
    locCounter = 0

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game_state.displaySurf.blit(displayCopy, (0, 0))

        if fadeBool == True:
            alphaSurface.set_alpha(255-(locCounter*(255/110)))
            game_state.displaySurf.blit(alphaSurface, (0,0))

        # 1
        bit1 = pygame.image.load(goldBurstList[spinCounter])
        game_state.displaySurf.blit(bit1, (posX-4, posY+4-(4*locCounter)))

        # 2
        game_state.displaySurf.blit(bit1, (posX-4+(3*locCounter), posY +4 - (3*locCounter)))

        # 3
        game_state.displaySurf.blit(bit1, (posX - 4+(4*locCounter), posY + 4))

        # 4
        game_state.displaySurf.blit(bit1, (posX - 4+(3*locCounter), posY + (3 * locCounter)))

        # 5
        game_state.displaySurf.blit(bit1, (posX - 4, posY+4+(4*locCounter)))

        # 6
        game_state.displaySurf.blit(bit1, (posX - 4-(3*locCounter), posY + (3 * locCounter)))

        # 7
        game_state.displaySurf.blit(bit1, (posX - 4-(4*locCounter), posY + 4))

        # 8
        game_state.displaySurf.blit(bit1, (posX - 4-(3*locCounter), posY - (3 * locCounter)))

        spinCounter = (spinCounter + 1) % len(goldBurstList)
        locCounter+=1

        pygame.display.update()
        game_state.fpsClock.tick(game_state.fpsVal)

        if locCounter >= 110:
            break

    return game_state

def watering_animation(counterStart, counterCurrent, initWaterLevel, framesPerImage):

    imageList = []

    if initWaterLevel == 1:
        imageList = wateringAnimationList1
    elif initWaterLevel == 2:
        imageList = wateringAnimationList2
    elif initWaterLevel == 3:
        imageList = wateringAnimationList3
    elif initWaterLevel == 4:
        imageList = wateringAnimationList4

    counter = counterCurrent - counterStart
    imageNum = (counter - (counter%framesPerImage)) / framesPerImage

    if imageNum >= len(imageList):
        return "DONE"
    else:
        wateringAnimationSurf = pygame.image.load(imageList[imageNum])
        return wateringAnimationSurf








