# Chess Game

Welcome to the Chess Game project! This is a Python implementation of the classic chess game, designed with clarity, simplicity, and user-friendliness in mind. Below is a brief overview of each module in this project.

## Modules

### **board.py**

The `board.py` module contains the `Board` class, which represents the chessboard. It handles the initialization of the chessboard, piece movements, and various game-related calculations.

### **color.py**

In `color.py`, the `Color` class defines a pair of light and dark colors. It is utilized to manage color schemes throughout the game.

### **config.py**

The `config.py` module houses the `Config` class, responsible for managing game configuration settings. It includes features such as changing themes and handling sound effects.

### **const.py**

`const.py` contains constant values used throughout the project, providing a centralized location for easy modification and maintenance.

### **dragger.py**

The `dragger.py` module implements the `Dragger` class, which handles the dragging and dropping of chess pieces during gameplay.

### **game.py**

In `game.py`, the `Game` class orchestrates the entire chess game. It manages player turns, theme changes, and sound effects, creating a cohesive gaming experience.

### **main.py**

The `main.py` module serves as the entry point to the game. It initializes the Pygame environment, sets up the game window, and starts the main game loop.

### **move.py**

`move.py` introduces the `Move` class, representing a move in the game. It provides methods for string representation, equality comparison, and initialization.

### **piece.py**

The `piece.py` module defines the base `Piece` class and specific piece classes such as `Pawn`, `Knight`, `Bishop`, `Rook`, `Queen`, and `King`. These classes represent individual chess pieces with unique characteristics.

### **sound.py**

In `sound.py`, the `Sound` class is responsible for handling game sound effects. It initializes sound objects and provides a method to play the sound effect.

### **square.py**

The `square.py` module introduces the `Square` class, representing individual squares on the chessboard. It includes methods for checking the presence of a piece and determining if the square is within a valid range.

### **theme.py**

The `theme.py` module defines the `Theme` class, representing a set of colors for different elements in the game, such as the board background, piece traces, and valid move indicators.

## How to Play

To play the game, run the `main.py` file, and a Pygame window will appear. Use the mouse to interact with the pieces and make moves. Press 't' to change themes and 'r' to reset the game. Enjoy the timeless game of chess with an elegant and intuitive interface!

Feel free to explore the codebase, make modifications, and enhance the project. Good luck, and may your chess skills shine on the virtual board!
