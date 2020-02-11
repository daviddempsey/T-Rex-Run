import pygame
from loadSprites import *

class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, size_x = -1, size_y = -1):
        pygame.sprite.Sprite.__init__(self, self.containers) # creates sprite
        self.cacti, self.cactusrect = load_sprites('cacti-small.png', 3,
                                                       1, sizex, sizey)
        self.cactusrect.bottom = int(0.98*height) # positions cacti on ground
        self.cactusrect.left = width + self.cactusrect.width # pos off screen
        self.cactus = self.cacti[random.randrange(0,3)] # random sprite
        self.movement = [-1*speed, 0] # moves left

    def draw(self):
        screen.blit(self.cactus, self.cactusrect) # draws cactus on screen

    def update(self):
        self.cactusrect = self.cactusrect.move(self.movement) # moves cactus

        if self.cactusrect.right < 0: # deletes if moved off screen
            self.kill()
