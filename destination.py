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
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def detect_player(self, player_pos):
        top = self.y - self.width/2
        bottom = self.y + self.width/2
        left = self.rect.left
        right = self.rect.right

        if left <= player_pos[0] <= right and top <= player_pos[1] <= bottom:
            return True
        return False

    def project(self, screen):
        """Projects destination object to screen"""

        screen.blit(self.img, (self.x, self.y))
