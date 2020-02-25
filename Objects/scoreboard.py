import os
import sys
sys.path.insert(0, "./Objects")
import pygame
from pygame import *

from display import *
from cactus import *
from cloud import *
from dino import *
from ground import *
from ptera import *
from scoreboard import *

#screen_size = (width, height) = (600, 150)
#screen = pygame.display.set_mode(screen_size)

class Scoreboard():
    def __init__(self, width =- 1, height =- 1):
        self.numbers, self.numbers_rect = load_sprites('numbers.png', 12, 1, 11, int(11 * 6 / 5))
        self.image = pygame.Surface((55, int(11 * 6 / 5)))
        self.rect = self.image.get_rect()
        if width == -1:
            self.rect.left = width * 0.89
        else:
            self.rect.left = width
        if height == -1:
            self.rect.top = height * 0.1

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, score):
        score_digits = [int(i) for i in str(score)]
        for _ in range(len(score_digits), 5):
            score_digits.insert(0, 0)