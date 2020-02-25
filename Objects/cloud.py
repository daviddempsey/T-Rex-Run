import os
import sys,inspect
sys.path.insert(0, "./Objects")
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

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.cloud, self.cloudrect = load_image('cloud.png', int(90*30/42), 30)
        self.speed = 1 # sets cloud speed attribute
        self.cloudrect.left = x # x-pos of cloud
        self.cloudrect.top = y # y-pos of cloud
        self.movement = [-1*self.speed, 0]

    def draw(self):
        screen.blit(self.cloud, self.cloudrect) # draws cloud on screen

    def update(self):
        self.cloud = self.cloud.move(self.movement)
        if self.cloudrect.right < 0:
            self.kill() # removes cloud if out of bounds
