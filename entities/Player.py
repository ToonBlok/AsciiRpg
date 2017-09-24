from entities.Entity import Entity

class Player(Entity):
    def __init__(self, x, y, color):
        super().__init__(int(x / 2), int(y / 2), color, '@')
