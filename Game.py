import libtcodpy as tcod
from entities.Player import Player

class Game:
    def __init__(self):
        self._setup()
        self._gameloop()

    def _setup(self):
        self.SCREEN_WIDTH = 80
        self.SCREEN_HEIGHT = 50
        self.LIMIT_FPS = 20
        tcod.sys_set_fps(self.LIMIT_FPS)

        font_path = 'arial10x10.png'  # this will look in the same folder as this script
        font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD  # the layout may need to change with a different font file
        tcod.console_set_custom_font(font_path, font_flags)

        window_title = 'AsciiRPG'
        fullscreen = False
        tcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, window_title, fullscreen)

        # Spawn player
        self.player = Player(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def _gameloop(self):
        while not tcod.console_is_window_closed():
            tcod.console_set_default_foreground(0, tcod.white) # 0 = screen
            tcod.console_put_char(0, self.player.x, self.player.y, self.player.symbol, tcod.BKGND_NONE) # 0 = screen
            tcod.console_flush() # present changes to the screen

            tcod.console_put_char(0, self.player.x, self.player.y, ' ', tcod.BKGND_NONE)
             #handle keys and exit game if needed
            exit = self._handle_keys()
            if exit:
                break

    def _handle_keys(self):
        key = tcod.console_wait_for_keypress(True) # Entire game will stop until input is received

        if key.vk == tcod.KEY_ENTER and key.lalt:
            #Alt+Enter: toggle fullscreen
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        elif key.vk == tcod.KEY_ESCAPE:
            return True  #exit game

        # movement keys
        if tcod.console_is_key_pressed(tcod.KEY_KP8):
            self.player.y = self.player.y - 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP9):
            self.player.y = self.player.y - 1
            self.player.x = self.player.x + 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP2):
            self.player.y = self.player.y + 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP3):
            self.player.y = self.player.y + 1
            self.player.x = self.player.x + 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP4):
            self.player.x = self.player.x - 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP1):
            self.player.y = self.player.y + 1
            self.player.x = self.player.x - 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP6):
            self.player.x = self.player.x + 1
        elif tcod.console_is_key_pressed(tcod.KEY_KP7):
            self.player.y = self.player.y - 1
            self.player.x = self.player.x - 1
