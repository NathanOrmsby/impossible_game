import pygame as pg

fpath_desktop = r"C:\Users\norms\PycharmProjects\Textbooks\pygames\impossible_game\pictures"
fpath_laptop = r"C:\Users\natha\PycharmProjects\pygames\impossible_game\pictures"


class Opponent:
    """Class defining moving opponents that player will need to dodge. Bounces off walls in direction opposite
    initial direction

    Attributes:
        -position:
        -direction: direction will switch if they hit a wall
        -img
        -hitbox

    Methods:
        -move
        -detect_player:
        -project to screen
    """

    def __init__(self, position, direction):
        self.x = position[0]
        self.y = position[1]
        self.width = 50
        self.direction = direction
        self.img1 = pg.transform.scale(pg.image.load(fpath_desktop + r"\state1.png"), (self.width, self.width))
        self.img2 = pg.transform.scale(pg.image.load(fpath_desktop + r"\state2.png"), (self.width, self.width))
        self.state = self.img1
        # hitbox
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width

    def move(self):
        """Makes sure the opponent keeps moving in its designated direction."""
        direction = self.direction
        # print("Direction is: {}" .format(self.direction))
        # print("Position is: {}" .format((self.x, self.y)))
        # print("position is: {}" .format((self.x, self.y)))
        if direction == "up":
            self.y -= .3
        elif direction == "down":
            self.y += .3
        elif direction == "right":
            self.x += .3
        elif direction == "left":
            self.x -= .3

    def detect_player(self, player_class):
        """Standard detect player in hitbox method"""

        # Vertical and horizontal case
        # Check if player is within range of destination hitbox, either vertically or horizontally

        # vertical
        if self.t <= player_class.b and player_class.t <= self.b:
            # either right to left or left to right
            if player_class.l < self.l <= player_class.r or player_class.l <= self.r < player_class.r:
                return True
        # Horizontal
        if self.l <= player_class.r and self.r >= player_class.l:
            # top to bottom or bottom to top
            if player_class.t < self.t <= player_class.b or player_class.t <= self.b < player_class.b:
                return True
        return False

    def swap(self):
        """Swaps states for comical movement animation."""
        if self.state == self.img1:
            self.state = self.img2
        elif self.state == self.img2:
            self.state = self.img1

    def project(self, screen):
        """Projects opponent to screen and updates hitbox"""
        screen.blit(self.state, (self.x, self.y))
        # Update hitbox
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width
