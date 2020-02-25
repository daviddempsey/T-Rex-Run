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

#gravity = 0.6
#screen_size = (width, height) = (600, 150)
#screen = pygame.display.set_mode(screen_size)

class Dino():
    def __init__(self, size_x = -1, size_y = -1):
        # loads standing dinosaur sprites
        self.dinos, self.dinorect = load_sprites('dino.png', 5, 1, size_x, \
                                                 size_y)
        # loads ducking dinosaur sprites
        self.duckingdinos, self.ducksize = load_sprites('dino_ducking.png',\
                                                        2, 1, 59, size_y)
        self.dinorect.bottom = int(0.98*height) # sets bottom y-pos ?
        self.dinorect.left = width/15 # sets left pos of dinosaur

        self.dino = self.dinos[0] # initial dinosaur sprite

        self.index = 0 # sprite index in sprite sheet
        self.counter = 0 # keeps track of time passed
        self.score = 0 # keeps track of score

        # initial state conditions
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False

        self.movement = [0, 0] # x/y movement of dinosaur
        self.jumpSpeed = 11.5

        # stores width of ducking and standing dino
        self.standing_width = self.dinorect.width
        self.duck_width = self.ducksize.width

    # draws out dino on screen
    def draw(self):
        screen.blit(self.dino, self.dinorect)

    # prevents dino from jumping out of bounds
    def checkbounds(self):
        if self.dinorect.bottom > int(0.98*height):
            self.dinorect.bottom = int(0.98*height)
            self.isJumping = False

    def update(self):
        if self.isJumping: # accounts for gravity
            self.movement[1] = self.movement[1] + gravity
            self.index = 0

        elif self.isBlinking:
            if self.index == 0: # changes sprite to blinking dino
                if self.counter % 400 == 399:
                    self.index = (self.index + 1) % 2 # should be 1
            else: # changes back to eyes open dino
                if self.counter % 20 == 19:
                    self.index = (self.index + 1) % 2 # should be 0

        elif self.isDucking:
            if self.counter % 5 == 0: # changes sprite index to move feet
                self.index = (self.index + 1) % 2
        else: # if dino isn't ducking and just running
            if self.counter % 5 == 0: # changes sprite index to move feet
                self.index = (self.index +1) % 2 + 2

        if self.isDead: # changes sprite to dead dino
            self.index = 4

        if not self.isDucking:
            self.sprite = self.dinos[self.index] # adjusts sprite accordingly
            self.dinorect.width = self.standing_width
        else:
            # adjusts sprite to ducking sprite
            self.sprite = self.duckingdinos[(self.index) % 2]
            self.dinorect.width = self.duck_width

        self.dinorect = self.dinorect.move(self.movement) # moves dino accordingly # Changed dino to dinorect -Alan :)
        self.checkbounds() # ensures dino stays on screen

        if not self.isDead and self.counter % 7 == 6 \
                and self.isBlinking == False:
            self.score += 1 # score increases every update
            if self.score % 100 == 0 and self.score != 0: # checkpoint reached
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter += 1 # increases time counter by 1
