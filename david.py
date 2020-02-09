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
            sprite = image.convert() # converts image type
            sprite.blit(spritesheet, (0,0), sprite_rect) # draws sprite out

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = sprite.get_at((0,0)) # color at bottom right
                image.set_colorkey(colorey, RLEACCEL)

            if scale_x != -1 or scale_y != -1: # scales appropriately
                sprite = pygame.transform.scale(sprite, (scale_x, scale_y))

            sprites.append(sprite) # appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # size of a single sprite

    return sprites, sprite_size # returns all sprites and size of each sprite

class TRex():
    def init(self, size_x = -1, size_y = -1):
        # loads standing dinosaur sprites
        self.dinos, self.dinosize = load_sprites('dino.png', 5, 1, size_x, \
                                                 size_y, -1)
        # loads ducking dinosaur sprites
        self.duckingdinos, self.ducksize = load_sprites('dino_ducking.png',\
                                                        2, 1, 59, size_y,\
                                                        -1)


    def draw(self):
    def checkbounds(self):
    def update(self):
