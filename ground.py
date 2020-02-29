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

class Ground():
    def __init__(self,speed=-5):

        #loadimageandtherectanglearoundtheimage
        self.ground1,self.rect1 = load_image('ground.png')
        self.ground2,self.rect2 = load_image('ground.png')

        #placethegrondatthebottomofthescreen
        self.rect1.bottom = self.rect2.bottom = height
        self.rect1.right = self.rect2.left#connect the two grounds

        #setthespeed
        self.speed = speed

    def draw(self):
        #renderthegroundontothescreen
        screen.blit(self.ground1,self.rect1)
        screen.blit(self.ground2,self.rect2)

    def update(self):
        #movethegroundacrossthescreen
        self.rect1.left += self.speed
        self.rect2.left += self.speed

        #onceground1isoutofthescreenplaceitbehindground2
        if self.rect1.right<0:
            self.rect1.left = self.rect2.right

        #onceground2isoutofthescreen,placeitbehindground1
        if self.rect2.right<0:
            self.rect2.left = self.rect1.right
