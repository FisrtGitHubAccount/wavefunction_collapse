from typing import List


"""This file contains all the Classes needed for the wavefunction collapse algorithm.
The docstrings should be self explanatory.
"""


class Pattern:
    """
    Class of subpatterns derived from the input
    """

    def __init__(self, pixels):
        self.pixels = pixels

    def __len__(self):
        return 1


UP = (0, -1)   # index of the pixel above relative to the pixel of interest
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
dirs = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]


class Index(Pattern):
    """
    Tells which combinations of patterns are allowed for all patterns

    data (dict):
        pattern -> posible_connections (dict):
                    relative_position -> patterns (list)
    """

    def __init__(self, patterns: List[Pattern]):
        # used function annotation here (specified the expected type of the input fo the function)
        # reminder that Pattern is a Class of subpattern
        self.data = {}
        for pattern in patterns:
            self.data[pattern] = {}
            for d in dirs:
                self.data[pattern][d] = []

    def add_rule(self, pattern: Pattern, relative_position: tuple, next_pattern: Pattern):
        """
        Add all the possible 'next_pattern' to the self.data dictionary with the base 'pattern' as the key  
        """
        self.data[pattern][relative_position].append(next_pattern)

    def check_possibility(self, pattern: Pattern, check_pattern: Pattern, relative_pos: tuple):
        if isinstance(pattern, list):
            pattern = pattern[0]
        return check_pattern in self.data[pattern][relative_pos]
