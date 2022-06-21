import pygame, sys
from player import Player
from wall import Wall
from level import Level

SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("GAME")

background_colour = (234, 212, 252)

running = True

# Create player class
player = Player((250, 360))

# Create level class
level = Level()

# Game loop
while running:

    # Throw on background
    SCREEN.fill(background_colour)

    # Draw the world
    wall_dict = level.create_walls()
    level.draw_world(SCREEN, wall_dict)

    # Loop through events
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    # If arrow keys are pressed, move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
    elif keys[pygame.K_DOWN]:
        player.move_down()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    elif keys[pygame.K_LEFT]:
        player.move_left()

    # Loop through walls and call functions
    for key in wall_dict.keys():
        wall = wall_dict[key]

        # Wall alignment
        wall.determine_state()
        wall.determine_points()

        # Player interactions
        wall.locate_player((player.x, player.y))
        if wall.detect_collision((player.x, player.y)):
            wall.block_player(player)

        # Debugging
        # print("Player location: {}" .format(wall.player_loc))
    # Update player class
    player.update(SCREEN)
    # Update display
    pygame.display.update()