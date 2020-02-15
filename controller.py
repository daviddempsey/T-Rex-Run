import os

import pygame
from pygame import *
from gameSetting import *
from ground import *




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
                    game_quit = True;

            display_surface.fill(background_col);
            ground.draw()

            pygame.display.update()

        if game_quit:
            break;

    pygame.quit()
    quit()


game_controller()
