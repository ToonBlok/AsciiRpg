import tdl
from entities.Player import Player

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
        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def _gameloop(self):
        while not tdl.event.isWindowClosed():
            self.console.draw_char(self.player.x, self.player.y, self.player.symbol, bg=None, fg=(255,255,255))
            self.root.blit(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0)
            tdl.flush() # present changes to the screen
            self.console.draw_char(self.player.x, self.player.y, ' ', bg=None, fg=(255,255,255))

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

        if user_input.key == 'KP8':
            self.player.y = self.player.y - 1
        elif user_input.key == 'KP9':
             self.player.y = self.player.y - 1
             self.player.x = self.player.x + 1
        elif user_input.key == 'KP6':
            self.player.x = self.player.x + 1
        elif user_input.key == 'KP3':
            self.player.y = self.player.y + 1
            self.player.x = self.player.x + 1
        elif user_input.key == 'KP2':
            self.player.y = self.player.y + 1
        elif user_input.key == 'KP1':
             self.player.y = self.player.y + 1
             self.player.x = self.player.x - 1
        elif user_input.key == 'KP4':
            self.player.x = self.player.x - 1
        elif user_input.key == 'KP7':
            self.player.y = self.player.y - 1
            self.player.x = self.player.x - 1
