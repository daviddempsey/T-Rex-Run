import pygame as pygame
import main

def load_image(name, scalex=-1, scaley=-1):
    image = pygame.image.load(name).convert()
    if scalex != -1 or scaley != -1:
        image = pygame.transform.scale(image,(scalex,scaley))
    return image, image.get_rect()

class Ground:
    def _init_(self, speed):
        speed = -5
        self.image1,self.rect1 = load_image('ground.png')
        self.image2,self.rect2 = load_image('ground.png')


