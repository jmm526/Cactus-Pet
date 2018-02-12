import pygame, time
from pygame.locals import *

class TextDisplay():

    def __init__(self, screen):

        self.screen = screen
        self.rect = self.screen.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height

        # make a copy of the screen
        self.screenCopy = screen.copy()

        # Make Text Box
        self.outerBox = pygame.Rect(2,322, 316, 76)
        self.outerBox.fill(255,255,0)



def TextDisplayFN(screen):

    outerBox = pygame.Rect(2,322, 316, 76)
    outerBox.fill(255,255,0)

    innerBox = pygame.Rect(5, 325, 310, 70)
    innerBox.fill(255, 255, 0)
