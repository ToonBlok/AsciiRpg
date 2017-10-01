import tdl
from Entities.Player import Player
from Entities.Cat import Cat
from World import World

class Game:
    def __init__(self):
        self._setup()
        self._gameloop()

    def _setup(self):
        self.SCREEN_WIDTH = 80
        self.SCREEN_HEIGHT = 50
        self.LIMIT_FPS = 20

        tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
        self.root = tdl.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, title='AsciiRPG', fullscreen=False)
        tdl.setFPS(self.LIMIT_FPS)

        # Create an offscreen console
        self.console = tdl.Console(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        # Spawn player
        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, (255,255,255))
        self.cat = Cat(self.SCREEN_WIDTH + 4, self.SCREEN_HEIGHT, (255,255,255))
        self.entities = [self.player, self.cat]

        # Map
        self.world = World()
        self.world.create(self.SCREEN_HEIGHT, self.SCREEN_WIDTH)


    def _render(self):
        self.world.render(self.console)

        for entity in self.entities:
            entity.render(self.console)

    def _gameloop(self):
        while not tdl.event.isWindowClosed():

            self._render()

            self.root.blit(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0)
            tdl.flush() # present changes to the screen

            for entity in self.entities:
                entity.clear(self.console)

            #handle keys and exit game if needed
            exit = self._handle_keys()
            if exit:
                break

    def _handle_keys(self):
        user_input = tdl.event.key_wait()

        if user_input.key == 'ENTER' and user_input.alt:
            # Alt+Enter: toggle fullscreen
            tdl.set_fullscreen(not tdl.get_fullscreen())
        elif user_input.key == 'ESCAPE':
            return True  # exit game

        #if not self.world[self.x + dx][self.y + dy].blocked:

        if user_input.key == 'KP8':
            self.player.move(0, -1)
        elif user_input.key == 'KP9':
            self.player.move(1, -1)
        elif user_input.key == 'KP6':
            self.player.move(1, 0)
        elif user_input.key == 'KP3':
            self.player.move(1, 1)
        elif user_input.key == 'KP2':
            self.player.move(0, 1)
        elif user_input.key == 'KP1':
            self.player.move(-1, 1)
        elif user_input.key == 'KP4':
            self.player.move(-1, 0)
        elif user_input.key == 'KP7':
            self.player.move(-1, -1)
