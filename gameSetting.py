import os
import pygame
from pygame import *

# load image, set background to transparent,
# scale,and return image and its rectangle

# set screen size
screen_size = (screen_w, screen_h) = (600, 150)

# set background color
background_col = (235, 235, 235)

# initialize pygame
pygame.init()

# set the screen and caption
display_surface = pygame.display.set_mode(screen_size)
pygame.display.set_caption("T-Rex Run")

def load_image(filename, scalex=-1, scaley=-1):
    filepath = os.path.join('sprites',filename)
    # load image from file name and convert it into pixel format
    image = pygame.image.load(filepath).convert()

    # get background color
    colorkey = image.get_at((0, 0))
    # set background to transparent
    # RLEACCEL is a flag that makes the image render faster
    image.set_colorkey(colorkey, RLEACCEL)

    # scale the image if needed
    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    # returns the image and the image rectangle
    return image, image.get_rect()
