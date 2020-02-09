import os
import sys
import pygame
import random
from pygame import *

# forked repo has code here to fix audio delay

screen_size = (width, height) = (600, 150)
FPS = 60 # frames per second
gravity = 0.6

# forked repo has colors here

# forked repo has high score her

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("T-Rex Rush")

# forked repo has sound constants here


def load_sprites(sheet_name, sprites_horiz, sprites_vert, scale_x = -1,
                 scale_y = -1, colorkey = None):
    sheet_path = os.path.join('sprites', sheet_name) # stores path
    spritesheet = pygame.image.load(sheet_path) # loads spritesheet
    spritesheet = spritesheet.convert() # converts image type

    sheet_rect = spritesheet.get_rect() # stores width/height of sprite sheet

    sprites = [] # array of sprites

    width = sheet_rect.width/sprites_horiz # width of each sprite
    height = sheet_rect.height/sprite_vert # height of each sprite

    # loops through each sprite
    for i in range(0, sprites_vert):
        for j in range(0, sprites_horiz):
            vert_pos = i*height # y-pos in sheet
            horiz_pos = j*width # x-pos in sheet
            # stores sprite position, width, and height
            sprite_rect = pygame.Rect((horiz_pos, vert_pos, width, height))
            sprite = pygame.Surface(sprite_rect.size) # surface for sprite
            sprite = sprite.convert() # converts image type
            sprite.blit(spritesheet, (0,0), sprite_rect) # draws sprite out

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = sprite.get_at((0,0)) # color at bottom right
                sprite.set_colorkey(colorey, RLEACCEL)

            if scale_x != -1 or scale_y != -1: # scales appropriately
                sprite = pygame.transform.scale(sprite, (scale_x, scale_y))

            sprites.append(sprite) # appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # width/height of a single sprite

    return sprites, sprite_size # returns all sprites and size of each sprite

class Dino():
    def __init__(self, size_x = -1, size_y = -1):
        # loads standing dinosaur sprites
        self.dinos, self.dinosize = load_sprites('dino.png', 5, 1, size_x, \
                                                 size_y, -1)
        # loads ducking dinosaur sprites
        self.duckingdinos, self.ducksize = load_sprites('dino_ducking.png',\
                                                        2, 1, 59, size_y,\
                                                        -1)
        self.dinosize.bottom = int(0.98*height) # sets bottom y-pos ?
        self.dinosize.left = width/15 # sets left pos of dinosaur

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
        self.standing_width = self.dinosize.width
        self.duck_width = self.ducksize.width

    # draws out dino on screen
    def draw(self):
        screen.blit(self.dino, self.dinosize)

    # prevents dino from jumping out of bounds
    def checkbounds(self):
        if self.dinosize.bottom > int(0.98*height):
            self.dinosize.bottom = int(0.98*height)
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
            self.dinosize.width = self.standing_width
        else:
            # adjusts sprite to ducking sprite
            self.sprite = self.duckingdinos[(self.index) % 2]
            self.dinosize.width = self.duck_width

        self.dino = self.dino.move(self.movement) # moves dino accordingly
        self.checkbounds() # ensures dino stays on screen

        if not self.isDead and self.counter % 7 == 6 \
                and self.isBlinking == False:
            self.score += 1 # score increases every update
            if self.score % 100 == 0 and self.score != 0: # checkpoint reached
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1) # increases time counter by 1
