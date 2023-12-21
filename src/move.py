# move.py

class Move:
    def __init__(self, initial, final):
        """
        Move class to represent a chess move.

        Parameters:
        - initial: Initial square.
        - final: Final square.
        """
        self.initial = initial
        self.final = final

    def __str__(self):
        """
        Convert the move to a string representation.

        Returns:
        - String representation of the move.
        """
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        """
        Check if two moves are equal.

        Parameters:
        - other: Another move.

        Returns:
        - True if moves are equal, False otherwise.
        """
        return self.initial == other.initial and self.final == other.final
