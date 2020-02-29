import os,sys
#sys.path.insert(0, "./Objects")
import pygame
from pygame import *
from display import *
from dino import *


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
