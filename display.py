import os
import pygame
from pygame import *

pygame.init() # Initialize pygame

background_color = (235, 235, 235)
screen_size = (width, height) = (600, 150) 
screen = pygame.display.set_mode(screen_size) # Sets screen width/height
pygame.display.set_caption("T-Rex-Run") # Sets window caption/title

FPS = 60
clock = pygame.time.Clock()

def load_image(filename, width = -1, height = -1):

    path = os.path.join('sprites', filename) # Gets path of sprites in its directory
    image = pygame.image.load(path).convert() # Loads image from file name and convert it into pixel format
   
    colorkey = image.get_at((0, 0)) # Gets background color
    
    # Set background to transparent
    # RLEACCEL is a flag that makes the image render faster
    image.set_colorkey(colorkey, RLEACCEL)

    # Scales the image if needed
    if width != -1 or height != -1:
        image = pygame.transform.scale(image, (width, height))

    # Returns the image and the image rectangle
    return (image, image.get_rect())

def load_sprites(sheet_name, sprites_horiz, sprites_vert, width = -1, height = -1):
    path = os.path.join('sprites', sheet_name) # Gets path of sprites in its directory
    spritesheet = pygame.image.load(path).convert() # Loads image from file name and convert it into pixel format

    sheet_rect = spritesheet.get_rect() # Stores width/height of sprite sheet

    sprites = [] # Creates an array of sprites

    width = sheet_rect.width / sprites_horiz # Width of each sprite
    height = sheet_rect.height / sprites_vert # Height of each sprite

    # Loops through each sprite
    for i in range(0, sprites_vert):
        for j in range(0, sprites_horiz):
            vert_pos = i * height # y-position in sheet
            horiz_pos = j * width # x-position in sheet
            # Stores sprite position, width, and height
            sprite_rect = pygame.Rect((horiz_pos, vert_pos, width, height))
            sprite = pygame.Surface(sprite_rect.size).convert() # Gets surface for sprite and convert it into pixel format
            sprite.blit(spritesheet, (0,0), sprite_rect) # Draws sprite out

            colorkey = sprite.get_at((0,0)) # Color at bottom right
            sprite.set_colorkey(colorkey, RLEACCEL)

            if width != -1 or height != -1: # Scales appropriately
                sprite = pygame.transform.scale(sprite, (width, height))

            sprites.append(sprite) # Appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # width/height of a single sprite

    return sprites, sprite_size # Returns all sprites and size of each sprite

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
        screen.fill(background_color) 
        screen.blit(intro_ground[0], intro_ground_rect)
        screen.blit(logo,logo_rect)
        screen.blit(callout, callout_rect)
        intro_dino.draw()

        pygame.display.update() # Presents GUI

        clock.tick(FPS)