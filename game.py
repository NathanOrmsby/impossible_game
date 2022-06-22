import pygame, sys
from player import Player
from wall import Wall
from level import Level
from destination import Destination

SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("GAME")

background_colour = (234, 212, 252)

running = True

# Create level class
level = Level()

# Create player class
player = level.create_player()

# Create destination class:
destination = level.create_destination()

# Create opponent classes. none on level 1
opponents = None
# Game loop
while running:

    # Throw on background
    SCREEN.fill(background_colour)

    # Draw the world
    wall_dict = level.create_walls()
    level.draw_world(SCREEN, wall_dict, destination)

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
        if wall.detect_player_collision((player.x, player.y)):
            wall.block_player(player)

        # Opponent interactions. if they exist on the current level
        if opponents is not None:
            for i in opponents.keys():
                opp = opponents[i]
                if wall.detect_opponent_collision((opp.x, opp.y)):
                    wall.bounce_opponent(opp)

    # Conditional for advancing to next level, or resetting level.
    advance = False

    # Check for win
    if destination.detect_player((player.x, player.y)):
        level.advance()
        opponents = level.create_opponents()
        advance = True
    if advance:
        player = level.create_player()

    # Loop through opponents and call functions
    if opponents is not None:
        for key in opponents.keys():
            print(key)
            opp = opponents[key]
            # Move
            opp.move()
            # Update
            opp.swap()
            opp.project(SCREEN)


    # Update player class
    player.update(SCREEN)
    # Update display
    pygame.display.update()