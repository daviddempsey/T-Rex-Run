import pygame as pygame

screen_size = (600, 150)
background_col = (235, 235, 235)

pygame.init()
pygame.display.set_caption("T-Rex Run")

display_surface = pygame.display.set_mode(screen_size)


def game_controller():
    # load sprites
    game_quit = False;  # when user clicks on the close button
    while not game_quit:
        # while not game over
        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            game_quit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True;

            display_surface.fill(background_col);
            pygame.display.update()

        if game_quit:
            break;

        # update sprites
    pygame.quit()
    quit()


game_controller()

