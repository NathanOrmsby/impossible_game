import pygame as pg
import sys
from player import Player
from opponent import Opponent


class Wall:
    """This class defines the walls that restrict player and opponent movement in the game. (line segment)
    Attributes:
        -point1: First point of line segment
        -point2: Second point of line segment
        -state: Defines the state of the wall, vertical or horizontal.
        -player_loc: Notes where the player is relative to the wall

        Horizontal walls prevent player movement from right to left and vice versa across wall.
        Vertical walls prevent top to bottom movement and vice versa

    Methods:
        -Determine state: Determines the state of the wall based on the given points
        -locate player: Locates player depending on orientation and position of wall. Changes attribute player_loc
        -Block player: Depending on player_loc and wall orientation, inhibits movement of player across wall.
        -project: Projects the wall onto the screen
        -Characteristics: Color, size and stuff
    """

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.state = None
        self.player_loc = None
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.color = (0, 0, 0)
        self.width = 10

    def determine_state(self):
        """Determines the orientation of the wall

        """
        point1 = self.point1
        point2 = self.point2

        # Matching x coordinates mean vertical wall
        if point1[0] == point2[0]:
            self.state = "vertical"
        # Matching y coordinates mean horizontal wall
        elif point1[1] == point2[1]:
            self.state = "horizontal"

        else:
            print("Walls must either be vertical or horizontal!")
            pg.quit()
            sys.exit()

    def determine_points(self):
        "Determines top and bottom points for vertical wall. Right and left points for horizontal wall"

        point1 = self.point1
        point2 = self.point2

        if self.state == "vertical":

            if point1[1] < point2[1]:
                self.top = point1
                self.bottom = point2
            elif point2[1] < point1[1]:
                self.top = point2
                self.bottom = point1

        elif self.state == "horizontal":

            if point1[0] < point2[0]:
                self.left = point1
                self.right = point2
            elif point2[0] < point1[0]:
                self.left = point2
                self.right = point1

    def locate_player(self, player_pos):  # works for vertical
        """Locates player based on orientation and position of wall object.

        """

        # print("Player position: {}" .format(player_pos))
        if self.state == "vertical":
            # print("Vertical wall")
            # print("Top: {}. Bottom: {}." .format(self.top, self.bottom))
            # Player must be within vertical range of wall
            if self.top[1] <= player_pos[1] <= self.bottom[1]:
                # Assign player position
                if player_pos[0] < self.top[0]:
                    self.player_loc = "left"
                elif player_pos[0] > self.top[0]:
                    self.player_loc = "right"

        elif self.state == "horizontal":
            # Player must be within horizontal range of wall
            if self.left[0] < player_pos[0] < self.right[0]:
                # Assign player position
                if player_pos[1] < self.left[1]:
                    self.player_loc = "above"
                elif player_pos[1] > self.left[1]:
                    self.player_loc = "below"

    def detect_player_collision(self, player_loc):
        """Returns true if the player is colliding with a wall. Will be used to call block_player method.

        Also contains case for detecting opponent"""

        if self.state == "vertical":
            right_buffer = self.top[0] + 2.5
            left_buffer = self.top[0] - 32

            if left_buffer <= player_loc[0] <= right_buffer:
                return True

        elif self.state == "horizontal":
            top_buffer = self.left[1] - 32
            bottom_buffer = self.left[1] + 2.5
            if top_buffer <= player_loc[1] <= bottom_buffer:
                return True

        return False

    def detect_opponent_collision(self, opponent_loc):
        """Does same thing as detect_player_collision: Just for opponents."""

        if self.state == "vertical":
            right_buffer = self.top[0] + 2.5
            left_buffer = self.top[0] - 32

            if left_buffer <= opponent_loc[0] <= right_buffer:
                return True

        elif self.state == "horizontal":
            top_buffer = self.left[1] - 32
            bottom_buffer = self.left[1] + 2.5

            if top_buffer <= opponent_loc[1] <= bottom_buffer:
                return True

        return False

    def block_player(self, player_class):
        """Blocks player depending on player_loc attribute and wall orientation. Only call after player_loc has
        been assigned value by class method "locate_player()". """

        # Vertical wall
        if self.state == "vertical":
            # If player on right, counter leftward movement
            if self.player_loc == "right":
                player_class.x += 1
            # If player on left, counter rightward movement
            elif self.player_loc == "left":
                player_class.x -= 1

        # Horizontal wall. blocks up and down movement
        if self.state == "horizontal":

            if self.player_loc == "above":
                player_class.y -= 1
            elif self.player_loc == "below":
                player_class.y += 1

    def bounce_opponent(self, opponent_class):
        # Vertical wall
        if self.state == "vertical":
            # Bounce in opposite direction opponent is moving
            if opponent_class.direction == "left":
                opponent_class.direction = "right"
            elif opponent_class.direction == "right":
                opponent_class.direction = "left"

        # Horizontal wall
        if self.state == "horizontal":
            if opponent_class.direction == "down":
                opponent_class.direction = "up"
            elif opponent_class.direction == "up":
                opponent_class.direction = "down"

    def project(self, screen):
        """Projects a drawn line segment that acts as the visual wall to the screen."""
        wall = pg.draw.line(screen, self.color, self.point1, self.point2, width=self.width)
