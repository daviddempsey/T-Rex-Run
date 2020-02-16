import os
import sys
sys.path.insert(0, "./Objects")

import pygame
from pygame import *

from dino import *
from ptera import *
from cactus import *
from loadSprites import *
from cloud import *
from ground import *
from gameSetting import *

screen_size = (width, height)=(600, 150)
background = (235, 235, 235)
clock = pygame.time.Clock()
FPS = 60

def game_controller():
    intro_screen()

    ground = Ground()

    # load sprites
    game_quit = False;  # when user clicks on the close button
    while not game_quit:
        # while not game over

        ground.update()

        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            game_quit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True

            display_surface.fill(background)
            ground.draw()

            pygame.display.update()

        if game_quit:
            break

    pygame.quit()
    quit()

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
                    gameStart = True # CHANGE TO TRUE WHEN FINISHED WITH gameplay()
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

def disp_gameOver_msg(retry_image, gameover_image):
    retry_image_rect = retry_image.get_rect()
    retry_image_rect.centerx = width / 2
    retry_image_rect.top = height * 0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height * 0.35

    screen.blit(retry_image, retry_image_rect)
    screen.blit(gameover_image, gameover_rect)

game_controller()