import os
import sys
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
    global high_score
    gamespeed = 4
    startMenu = False
    gameOver = False
    gameQuit = False
    playerDino = Dino(44,47)
    new_ground = Ground(-1*gamespeed)
    scb = Scoreboard()
    highsc = Scoreboard(width*0.78)
    counter = 0

    # groups sprites together
    cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    # groups sprites into objects
    Cactus.containers = cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    # loads replay/game over images
    retbutton_image,retbutton_rect = load_image('replay_button.png',35,31)
    gameover_image,gameover_rect = load_image('game_over.png',190,11)

    # loads in numbers for keeping score
    temp_images,temp_rect = load_sprites('numbers.png',12,1,11,int(11*6/5))
    HI_image = pygame.Surface((22,int(11*6/5)))
    HI_rect = HI_image.get_rect()
    HI_image.fill(background_color)
    HI_image.blit(temp_images[10],temp_rect)
    temp_rect.left += temp_rect.width
    HI_image.blit(temp_images[11],temp_rect)
    HI_rect.top = height*0.1
    HI_rect.left = width*0.73

    # runs while game is not quit
    while not gameQuit:
        while startMenu: # does nothing at start menu
            pass
        while not gameOver:
            if pygame.display.get_surface() == None: # can be removed?
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = True
                break
            else:
                for event in pygame.event.get(): # quits game if necessary
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = True

                    # handles ducking
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if playerDino.rect.bottom == int(0.98*height):
                                playerDino.isJumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                playerDino.movement[1] = -1*playerDino.jumpSpeed

                        if event.key == pygame.K_DOWN:
                            if not (playerDino.isJumping and playerDino.isDead):
                                playerDino.isDucking = True

                    # handles jump
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            playerDino.isDucking = False
            for c in cacti: # moves cacti on screen
                c.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(playerDino,c):
                    playerDino.isDead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            for p in pteras: # moves pteradactyl on screen
                p.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(playerDino,p):
                    playerDino.isDead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            # keeps adding obstacles
            if len(cacti) < 2:
                if len(cacti) == 0:
                    last_obstacle.empty()
                    last_obstacle.add(Cactus(gamespeed,40,40))
                else:
                    for l in last_obstacle:
                        if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                            last_obstacle.empty()
                            last_obstacle.add(Cactus(gamespeed, 40, 40))

            # keeps adding pteradactyls
            if len(pteras) == 0 and random.randrange(0,200) == 10 and counter > 500:
                for l in last_obstacle:
                    if l.rect.right < width*0.8:
                        last_obstacle.empty()
                        last_obstacle.add(Ptera(gamespeed, 46, 40))

        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            game_quit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True

            screen.fill(background_color)
            new_ground.draw()

            pygame.display.update()

        if game_quit:
            break
            # creates clouds
            if len(clouds) < 5 and random.randrange(0,300) == 10:
                Cloud(width,random.randrange(height/5,height/2))

            playerDino.update()
            cacti.update()
            pteras.update()
            clouds.update()
            new_ground.update()
            scb.update(playerDino.score)
            highsc.update(high_score)

            screen.fill(background_col)
            new_ground.draw()
            clouds.draw(screen)
            scb.draw()
            if high_score != 0:
                highsc.draw()
                screen.blit(HI_image,HI_rect)
            cacti.draw(screen)
            pteras.draw(screen)
            playerDino.draw()

            pygame.display.update()

            clock.tick(FPS)

            if playerDino.isDead:
                gameOver = True
                if playerDino.score > high_score:
                    high_score = playerDino.score

            if counter%700 == 699:
                new_ground.speed -= 1
                gamespeed += 1

            counter = (counter + 1)

        if gameQuit:
            break

        while gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameQuit = True
                            gameOver = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            gameOver = False
                            gameplay()
            highsc.update(high_score)
            if pygame.display.get_surface() != None:
                disp_gameOver_msg(retbutton_image,gameover_image)
                if high_score != 0:
                    highsc.draw()
                    screen.blit(HI_image,HI_rect)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()

game_controller()
def main():
    isGameQuit = introscreen()
    if not isGameQuit:
        gameplay()

main()
