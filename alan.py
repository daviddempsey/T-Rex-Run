import os
import sys
import pygame
import random
from pygame import *
 
pygame.init()

screen_size = (width, height) = (600, 150)
FPS = 60
gravity = 0.6

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("T-Rex Rush")
pygame.display.update()

def load_sprites(sheet_name, sprites_horiz, sprites_vert, scale_x = -1,
                 scale_y = -1, colorkey = None):
    sheet_path = os.path.join('sprites', sheet_name) # stores path
    spritesheet = pygame.image.load(sheet_path) # loads spritesheet
    spritesheet = spritesheet.convert() # converts image type

    sheet_rect = spritesheet.get_rect() # stores width/height of sprite sheet

    sprites = [] # array of sprites

    width = sheet_rect.width / sprites_horiz # width of each sprite
    height = sheet_rect.height / sprites_vert # height of each sprite

    # loops through each sprite
    for i in range(0, sprites_vert):
        for j in range(0, sprites_horiz):
            vert_pos = i * height # y-pos in sheet
            horiz_pos = j * width # x-pos in sheet
            # stores sprite position, width, and height
            sprite_rect = pygame.Rect((horiz_pos, vert_pos, width, height))
            sprite = pygame.Surface(sprite_rect.size) # surface for sprite
            sprite = sprite.convert() # converts image type
            sprite.blit(spritesheet, (0, 0), sprite_rect) # draws sprite out

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = sprite.get_at((0,0)) # color at bottom right
                sprite.set_colorkey(colorkey, RLEACCEL)

            if scale_x != -1 or scale_y != -1: # scales appropriately
                sprite = pygame.transform.scale(sprite, (scale_x, scale_y))

            sprites.append(sprite) # appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # size of a single sprite

    return sprites, sprite_size # returns all sprites and size of each sprite

def extractDigits(number):
    digits = [] #Initializes array of digits
    if number > -1: 
        while(number / 10 != 0):
            digits.append(number % 10)
            number = int(number / 10)

        digits.append(number % 10)
        
        for _ in range(len(digits), 5):
            digits.append(0)
        
        digits.reverse()
        return digits

class Scoreboard():
    def __init__(self, offset_x = 1, offset_y = 1):
        self.score = 0
        self.tempimages, self.temprect = load_sprites('numbers.png', 12, 1, 11, int(11 * 6 / 5), -1)
        self.image = pygame.Surface((55, int(11 * 6 / 5)))
        self.rect = self.image.get_rect()
        if offset_x == -1:
            self.rect.left = width * 0.89 # Sets the width of the score object
        else:
            self.rect.left = offset_x # Will position current scoreboard to the right
        if offset_y == -1:
            self.rect.top = height * 0.1 # Sets the height of the score object

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, score):
        score_digits = extractDigits(score)
        self.image.fill((255, 255, 255))
        for s in score_digits:
            self.image.blit(self.tempimages[s], self.temprect)
            self.temprect.left += self.temprect.width
        
        self.temprect.left = 0

def game_controller():
    # load sprites
    game_quit = False  # when user clicks on the close button
    while not game_quit:
        # while not game over
        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            game_quit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
            
            screen.fill((255, 255, 255))
            pygame.display.update()

        if game_quit:
            break

        # update sprites
    pygame.quit()
    quit()

game_controller()