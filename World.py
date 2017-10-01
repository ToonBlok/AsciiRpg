import tdl
from Entities.Player import Player
from Entities.Cat import Cat
from Tile import Tile

class World:
    def __init__(self):
        self.MAP_HEIGHT = 45
        self.MAP_WIDTH = 80
        self.COLOR_DARK_WALL = (0, 0, 100)
        self.COLOR_DARK_GROUND = (50, 50, 150)

    def create(self, SCREEN_HEIGHT, SCREEN_WIDTH):

        # fill map with "unblocked" tiles
        self.map = [[Tile(False)
            for y in range(SCREEN_HEIGHT)]
                for x in range(SCREEN_WIDTH)]

        # Temporary
        self.map[30][22].blocked = True
        self.map[30][22].block_sight = True
        self.map[50][22].blocked = True
        self.map[50][22].block_sight = True

    def render(self, console, ):
        for y in range(self.MAP_HEIGHT):
            for x in range(self.MAP_WIDTH):
                wall = self.map[x][y].block_sight
                if wall:
                    console.draw_char(x, y, None, fg=None, bg=self.COLOR_DARK_WALL)
                else:
                    console.draw_char(x, y, None, fg=None, bg=self.COLOR_DARK_GROUND)

