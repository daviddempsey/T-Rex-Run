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

def game_controller():

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

            screen.fill(background_color)
            ground.draw()

            pygame.display.update()

        if game_quit:
            break

    pygame.quit()
    quit()

game_controller()
