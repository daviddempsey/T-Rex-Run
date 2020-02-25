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

class Ptera(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self.self.containers)
        self.pteras, self.pterarect = load_sprites('ptera.png', 2, 1, size_x,
                                                   size_y)
        # various possible heights for pteradactyl
        self.ptera_height = [height*0.82, height*0.75, height*0.60]
        self.pterarect.centery = self.ptera_height[random.randrange(0,3)]

        self.pterarect.left = width + self.pterarect.width # pos off screen
        self.ptera = self.pteras[0] # sets initial ptera sprite
        self.movement = [-1*speed, 0] # sets movement speed
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.ptera, self.pterarect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index+1)%2
        # makes wings flap by changing sprite
        self.ptera = self.pteras[self.index]
        self.pterarect = self.pterarect.move(self.movement)
        self.counter += 1
        if self.pterarect.right < 0:
            self.kill() # removes ptera if out of bounds
