import pygame
import sys

from const import *
from game import Game

class Main:
    def __init__(self) -> None:
        pygame.init() #initializing pygame model
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()


    def mainloop(self):
        game = self.game
        screen = self.screen


        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():

                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                #Moving Mouse
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # Release click
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                #quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
            pygame.display.update()
        

main = Main()
main.mainloop()

