import pygame as pg

fpath_desktop = r"C:\Users\norms\PycharmProjects\Textbooks\pygames\impossible_game\pictures"
fpath_laptop = r"C:\Users\natha\PycharmProjects\pygames\impossible_game\pictures"


class Player:
    """Player class that player moves around map.
    Attributes:
        -starting_pos: Where player spawns
        -state: design of player. 1 for up, down, left, and right.
        -hitbox: rectangle around image of the player
        -Blocked: Boolean statement that turns true if player is running into a wall


    Methods:
        -Move commands: up, down, left, right. manipulated by arrow keys
    """

    def __init__(self, pos):
        self.position = pos
        self.x = pos[0]
        self.y = pos[1]
        self.width = 30
        self.up = pg.transform.scale(pg.image.load(fpath_desktop + r"\up.png"), (self.width, self.width))
        self.down = pg.transform.scale(pg.image.load(fpath_desktop + r"\down.png"), (self.width, self.width))
        self.right = pg.transform.scale(pg.image.load(fpath_desktop + r"\right.png"), (self.width, self.width))
        self.left = pg.transform.scale(pg.image.load(fpath_desktop + r"\left.png"), (self.width, self.width))
        self.rect = self.up.get_rect(topleft=(self.x, self.y))
        self.state = "up"
        self.blocked = False
        # hitbox
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width

    def move_up(self):
        self.y -= 0.3
        self.state = "up"

    def move_down(self):
        self.y += 0.3
        self.state = "down"

    def move_right(self):
        self.x += 0.3
        self.state = "right"

    def move_left(self):
        self.x -= 0.3
        self.state = "left"

    def update(self, screen):
        state = self.state
        if state == "up":
            screen.blit(self.up, (self.x, self.y))
        elif state == "down":
            screen.blit(self.down, (self.x, self.y))
        elif state == "right":
            screen.blit(self.right, (self.x, self.y))
        elif state == "left":
            screen.blit(self.left, (self.x, self.y))

        # Update hitbox:
        self.t = self.y
        self.b = self.y + self.width
        self.l = self.x
        self.r = self.x + self.width
