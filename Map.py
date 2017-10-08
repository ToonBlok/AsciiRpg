import tdl
from Entities.Player import Player
from Entities.Cat import Cat
from Tile import Tile
from Rect import Rect

class Map:
    def __init__(self):
        self.HEIGHT = 45
        self.WIDTH = 80
        self.COLOR_DARK_WALL = (0, 0, 100)
        self.COLOR_DARK_GROUND = (50, 50, 150)

    def create(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        #fill tiles with "unblocked" tiles
        self.tiles = [[Tile(True)
            for y in range(SCREEN_HEIGHT)]
                for x in range(SCREEN_WIDTH)]

        room = Rect(5, 1, 10, 10)
        self.create_room(room)

        # Temporary
        #         [y][x], want y is één array die een heleboel x arrays onthoudt
        #self.tiles[30][22].blocked = True
        #self.tiles[30][22].block_sight = True
        #self.tiles[50][22].blocked = True
        #self.tiles[50][22].block_sight = True

    def render(self, console, ):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                wall = self.tiles[x][y].block_sight
                if wall:
                    console.draw_char(x, y, None, fg=None, bg=self.COLOR_DARK_WALL)
                else:
                    console.draw_char(x, y, None, fg=None, bg=self.COLOR_DARK_GROUND)

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False


