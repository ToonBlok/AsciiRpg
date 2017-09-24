import libtcodpy as tcod

class Game:
    def __init__(self):
        self.setup()
        self.gameloop()

    def setup(self):
        self.SCREEN_WIDTH = 80
        self.SCREEN_HEIGHT = 50
        self.LIMIT_FPS = 20

        font_path = 'arial10x10.png'  # this will look in the same folder as this script
        font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD  # the layout may need to change with a different font file
        tcod.console_set_custom_font(font_path, font_flags)

        window_title = 'AsciiRPG'
        fullscreen = False
        tcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, window_title, fullscreen)

    def gameloop(self):
        while not tcod.console_is_window_closed():
            tcod.console_set_default_foreground(0, tcod.white) # 0 = screen
            tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE) # 0 = screen
            tcod.console_flush() # present changes to the screen
