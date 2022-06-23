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

# Timer for swapping animations for opponent
count = 0

# Game loop
while running:

    # Mouse position
    mouse_pos = pygame.mouse.get_pos()

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)

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
        if wall.detect_player_collision(player):
            wall.block_player(player)

        # Opponent interactions. if they exist on the current level
        if opponents is not None:
            for i in opponents.keys():
                opp = opponents[i]

                # Bounce off walls
                if wall.detect_opponent_collision(opp):
                    wall.bounce_opponent(opp)


    # Conditional for advancing to next level, or resetting level.
    advance = False

    # Check for win
    if destination.detect_player(player):
        level.advance()
        opponents = level.create_opponents()
        advance = True

    # Loop through opponents and call functions
    if opponents is not None:
        for key in opponents.keys():
            opp = opponents[key]
            # Move
            opp.move()
            # Update
            # if count % 120 == 0:
            #     opp.swap()
            # Check for player
            if opp.detect_player(player):
                advance = True
            opp.project(SCREEN)
            count += 1

    if advance:
        print("ADVANCE")
        player = level.create_player()

    # Update player class
    player.update(SCREEN)
    # Update display
    pygame.display.update()
