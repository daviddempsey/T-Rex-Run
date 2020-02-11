import pygame
from loadSprites import *

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.cloud, self.cloudrect = load_image('cloud.png', int(90*30/42), 30)
        self.speed = 1 # sets cloud speed attribute
        self.cloudrect.left = x # x-pos of cloud
        self.cloudrect.top = y # y-pos of cloud
        self.movement = [-1*self.speed, 0]

    def draw(self):
        screen.blit(self.cloud, self.cloudrect) # draws cloud on screen

    def update(self):
        self.cloud = self.cloud.move(self.movement)
        if self.cloudrect.right < 0:
            self.kill() # removes cloud if out of bounds
