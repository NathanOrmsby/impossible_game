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
        self.width = 100
        self.direction = direction
        self.img1 = pg.transform.scale(pg.image.load(fpath_desktop + r"\state1.png"), (self.width, self.width))
        self.img2 = pg.transform.scale(pg.image.load(fpath_desktop + r"\state2.png"), (self.width, self.width))
        self.rect = self.img1.get_rect(center=(self.x, self.y))
        self.state = self.img1

    def move(self):
        """Makes sure the opponent keeps moving in its designated direction."""
        direction = self.direction
        print("position is: {}" .format((self.x, self.y)))
        if direction == "up":
            self.y -= .3
        elif direction == "down":
            self.y += .3
        elif direction == "right":
            self.x += .3
        elif direction == "left":
            self.x -= .3

    def detect_player(self, player_pos):
        """Standard detect player in hitbox method"""

        top = self.y - self.width / 2
        bottom = self.y + self.width / 2
        left = self.rect.left
        right = self.rect.right

        if left <= player_pos[0] <= right and top <= player_pos[1] <= bottom:
            return True
        return False

    def swap(self):
        """Swaps states for comical movement animation."""
        if self.state == self.img1:
            self.state = self.img2
        elif self.state == self.img2:
            self.state = self.img1

    def project(self, screen):
        """Projects opponent to screen"""
        screen.blit(self.state, (self.x, self.y))
