import os
import sys
import pygame
import random
from pygame import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60
gravity = 0.6

# Colors
background = (235, 235, 235)

# Initializes screen/window
screen_size = (width, height) = (600, 150)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("T-Rex Rush")

def load_image(name, width, height):
    path = os.path.join('sprites', name) # Gets the name of an image from sprites folder
    image = pygame.image.load(path) # Loads an image for display
    image = image.convert() # Converts image into displayable one?
    
    # Sets the transparency of each image
    colorkey = image.get_at((0, 0))    
    image.set_colorkey(colorkey, RLEACCEL)

    image = pygame.transform.scale(image, (width, height)) # Scales image dimensions

    return (image, image.get_rect()) # Returns image / image rect

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

def intro_screen():
    intro_dino = Dino(44, 47) # Initializes intro screen with a dino
    gameStart = False # Game won't start until key press

    # Loads the callout image and its dimensions
    callout, callout_rect = load_image('call_out.png', 196, 45) 
    callout_rect.left = width * 0.05
    callout_rect.top = height * 0.4

    # Loads the ground sprite
    intro_ground,intro_ground_rect = load_sprites('ground.png', 15, 1, -1, -1)
    intro_ground_rect.left = width / 20
    intro_ground_rect.bottom = height

    # Loads the logo image and its dimensions
    logo,logo_rect = load_image('logo.png', 240, 40)
    logo_rect.centerx = width * 0.6
    logo_rect.centery = height * 0.6
    while not gameStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN: # On a key press ...
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # If spacebar or up arrow is pressed then dino jumps
                    intro_dino.isJumping = True 
                    gameStart = False # CHANGE TO TRUE WHEN FINISHED WITH gameplay()
                    intro_dino.movement[1] = -1 * intro_dino.jumpSpeed # Modifies y movement for dinosaur jumping

        intro_dino.update() # Dino will update when action is triggered

        # Intro screen initialized
        screen.fill(background) 
        screen.blit(intro_ground[0], intro_ground_rect)
        screen.blit(logo,logo_rect)
        screen.blit(callout, callout_rect)
        intro_dino.draw()

        pygame.display.update() # Presents GUI

        clock.tick(FPS)

class Dino():
    def __init__(self, size_x = -1, size_y = -1):
        # loads standing dinosaur sprites
        self.dinos, self.dinosize = load_sprites('dino.png', 5, 1, size_x, size_y)
        # loads ducking dinosaur sprites
        self.duckingdinos, self.ducksize = load_sprites('dino_ducking.png', 2, 1, 59, size_y)
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

        self.dinosize = self.dinosize.move(self.movement) # moves dino accordingly
        self.checkbounds() # ensures dino stays on screen

        if not self.isDead and self.counter % 7 == 6 \
                and self.isBlinking == False:
            self.score += 1 # score increases every update
            if self.score % 100 == 0 and self.score != 0: # checkpoint reached
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1) # increases time counter by 1
        
class Scoreboard():
    def __init__(self, width =- 1, height =- 1):
        self.numbers, self.numbers_rect = load_sprites('numbers.png', 12, 1, 11, int(11 * 6 / 5))
        self.image = pygame.Surface((55, int(11 * 6 / 5)))
        self.rect = self.image.get_rect()
        if width == -1:
            self.rect.left = width * 0.89
        else:
            self.rect.left = width
        if height == -1:
            self.rect.top = height * 0.1

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, score):
        score_digits = [int(i) for i in str(score)]
        for _ in range(len(score_digits), 5):
            score_digits.insert(0, 0)

def main():
    isGameQuit = intro_screen()
    #if not isGameQuit:
        #gameplay()

main()