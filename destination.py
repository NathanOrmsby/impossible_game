import pygame as pg

fpath_desktop = r"C:\Users\norms\PycharmProjects\Textbooks\pygames\impossible_game\pictures"
fpath_laptop = r"C:\Users\natha\PycharmProjects\pygames\impossible_game\pictures"


class Destination:
    """The win condition of impossible game. If the player touches an object of this class, advancement to the
    next level takes place. Doesn't move or do anything.
    Attributes:
        -position:
        -picture:
        -hitbox:
    """

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.width = 75
        self.img = pg.transform.scale(pg.image.load(fpath_desktop + r"\win.png"), (self.width, self.width))
        # hitbox
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width

    def detect_player(self, player_class):
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

    def project(self, screen):
        """Projects destination object to screen and updates hitbox"""

        screen.blit(self.img, (self.x, self.y))
        # update hitbox
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width