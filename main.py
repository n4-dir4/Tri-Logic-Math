#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from game import Game

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height] 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create game object
    game = Game()
    # -------- Main Program Loop -----------
    while not done:
        
        done = game.process_events()  # Loop berhenti jika True
        game.run_logic()
        game.display_frame(screen)
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()
