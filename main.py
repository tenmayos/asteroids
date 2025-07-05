import pygame
from constants import *

def main():
    # Init and config
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
