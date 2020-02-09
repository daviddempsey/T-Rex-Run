import pygame

pygame.init()

screen = pygame.display.set_mode((600, 150))
pygame.display.set_caption("TritonHack Dino Game")
pygame.display.update()

#Required for window to display
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False