from Entities.Entity import Entity

class Player(Entity):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, '@')
