# sound.py

import pygame

class Sound:
    def __init__(self, path):
        """
        Sound class to handle game sound effects.

        Parameters:
        - path: Path to the sound file.
        """
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        """Play the sound effect."""
        pygame.mixer.Sound.play(self.sound)
