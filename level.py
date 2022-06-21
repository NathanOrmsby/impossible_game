import pygame as pg
import numpy as np
from opponent import Opponent
from player import Player
from wall import Wall


class Level:
    """ This class includes all the different levels of the game.
    Attributes:
        -self.level: Defines which level of the game the player is on.

    Methods:
        -draw map: One for each level, draws the world and everything in it.
    """

    def __init__(self):
        self.level = 1

    def draw_world(self, screen, walls):
        """This method updates the screen given parameters of the world for each level the world for level 1.
        walls: Dictionary containing the wall names and classes"""

        # Draw all walls
        for key in walls.keys():
            wall = walls[key]
            wall.project(screen)

    def create_walls(self):
        """This method creates instantiates the wall classes depending on current level.

        Returns dictionary of wall classes and names."""
        wall_dict = {}

        # walls for level 1
        if self.level == 1:
            wall_dict["wall0"] = Wall((300, 600), (900, 600))

        return wall_dict

