import pygame as pg
import numpy as np
from opponent import Opponent
from player import Player
from wall import Wall
import time, sys
from destination import Destination


class Level:
    """ This class includes all the different levels of the game.
    Attributes:
        -self.level: Defines which level of the game the player is on.

    Methods:
        -draw map: One for each level, draws the world and everything in it.
    """

    def __init__(self):
        self.level = 1

    def draw_world(self, screen, walls, destination):
        """This method updates the screen given parameters of the world for each level the world for level 1.
        walls: Dictionary containing the wall names and classes"""

        # Draw all walls
        for key in walls.keys():
            wall = walls[key]
            wall.project(screen)

        # Draw destination
        destination.project(screen)

    def create_walls(self):
        """This method creates instantiates the wall classes depending on current level.

        Returns dictionary of wall classes and names."""
        d = {}

        if self.level == 1:
            d["0"] = Wall((0, 0), (1280, 0))
            d["1"] = Wall((0, 0), (0, 720))
            d["2"] = Wall((0, 720), (1280, 720))
            d["3"] = Wall((1280, 720), (1280, 0))
        elif self.level == 2:
            d["0"] = Wall((50, 0), (50, 720))
            d["1"] = Wall((150, 0), (150, 600))
            d["3"] = Wall((50, 720), (250, 720))
            d["4"] = Wall((250, 720), (250, 150))
            d["5"] = Wall((150, 0), (1280, 0))
            d["6"] = Wall((250, 150), (1030, 150))

        return d

    def create_opponents(self):
        """Instantiates the opponent objects present in the current level

        Works similarly to create_walls(). Returns dictionary of opponent classes"""
        d = {}

        if self.level == 2:
            d["0"] = Opponent((1230, 50), "left")
            d["1"] = Opponent((300, 100), "right")

        return d

    def create_player(self):
        """Creates player class with starting position depending on current level"""

        if self.level == 1:
            player = Player((100, 100))
        elif self.level == 2:
            player = Player((100, 360))

        return player

    def create_destination(self):
        """Creates destination class with position depending on current level."""

        if self.level == 1:
            destination = Destination((640, 360))
        elif self.level == 2:
            destination = Destination((900, 300))

        return destination

    def advance(self):
        if self.level < 3:
            self.level += 1
        else:
            print("YOU WIN!!!!!!")
            time.sleep(10)
            pg.quit()
            sys.exit()

