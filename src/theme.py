# theme.py

from color import Color

class Theme:
    def __init__(self, light_bg, dark_bg, light_trace, dark_trace, light_moves, dark_moves):
        """
        Theme class to represent the color theme of the chess game.

        Parameters:
        - light_bg: Light color for the background.
        - dark_bg: Dark color for the background.
        - light_trace: Light color for traced squares.
        - dark_trace: Dark color for traced squares.
        - light_moves: Light color for available moves.
        - dark_moves: Dark color for available moves.
        """
        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)
