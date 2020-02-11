import pygame
from pygame import *
import os

def load_sprites(sheet_name, sprites_horiz, sprites_vert, scale_x = -1,
                 scale_y = -1):
    sheet_path = os.path.join('sprites', sheet_name) # stores path
    spritesheet = pygame.image.load(sheet_path) # loads spritesheet
    spritesheet = spritesheet.convert() # converts image type

    sheet_rect = spritesheet.get_rect() # stores width/height of sprite sheet

    sprites = [] # array of sprites

    width = sheet_rect.width/sprites_horiz # width of each sprite
    height = sheet_rect.height/sprites_vert # height of each sprite

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

            colorkey = sprite.get_at((0,0)) # color at bottom right
            sprite.set_colorkey(colorkey, RLEACCEL)

            if scale_x != -1 or scale_y != -1: # scales appropriately
                sprite = pygame.transform.scale(sprite, (scale_x, scale_y))

            sprites.append(sprite) # appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # width/height of a single sprite

    return sprites, sprite_size # returns all sprites and size of each sprite
