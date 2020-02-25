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

class Ground():
    def __init__(self,speed=-5):
	
        #loadimageandtherectanglearoundtheimage
        self.ground1,self.groundrect1 = load_image('ground.png')
        self.ground2,self.groundrect2 = load_image('ground.png')

        #placethegrondatthebottomofthescreen
        self.groundrect1.bottom = self.groundrect2.bottom = height
        self.groundrect1.right = self.groundrect2.left#connect the two grounds

        #setthespeed
        self.speed = speed

    def draw(self):
        #renderthegroundontothescreen
        screen.blit(self.ground1,self.groundrect1)
        screen.blit(self.ground2,self.groundrect2)

    def update(self):
        #movethegroundacrossthescreen
        self.groundrect1.left += self.speed
        self.groundrect2.left += self.speed

        #onceground1isoutofthescreenplaceitbehindground2
        if self.groundrect1.right<0:
            self.groundrect1.left = self.groundrect2.right

        #onceground2isoutofthescreen,placeitbehindground1
        if self.groundrect2.right<0:
            self.groundrect2.left = self.groundrect1.right
