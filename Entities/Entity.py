class Entity:
    def __init__(self, x, y, color, symbol = '?'):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def render(self, console):
        console.draw_char(self.x, self.y, self.symbol, self.color)

    def clear(self, console):
        console.draw_char(self.x, self.y, ' ', self.color)


