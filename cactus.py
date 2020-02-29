import os
import sys,inspect
sys.path.insert(0, "./Objects")
import random
import pygame
from pygame import *

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from display import *

from cactus import *
from cloud import *
from dino import *
from ground import *
from ptera import *
from scoreboard import *

class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, size_x = -1, size_y = -1):
        pygame.sprite.Sprite.__init__(self, self.containers) # creates sprite
        self.cacti, self.rect = load_sprites('cacti-small.png', 3,
                                                       1, size_x, size_y)
        self.rect.bottom = int(0.98*height) # positions cacti on ground
        self.rect.left = width + self.rect.width # pos off screen
        self.cactus = self.cacti[random.randrange(0,3)] # random sprite
        self.movement = [-1*speed, 0] # moves left

    def draw(self):
        screen.blit(self.cactus, self.rect) # draws cactus on screen

    def update(self):
        self.rect = self.rect.move(self.movement) # moves cactus

        if self.rect.right < 0: # deletes if moved off screen
            self.kill()
