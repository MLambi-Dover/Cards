# pygame template

# 1 - Import packages
import pygame
from pygame.locals import *
import pygwidgets
import sys

from Game import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
background = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)

# 5 - Initialize variables
oGame = Game(window)

running = True
# 6 - Loop forever
while running:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame, end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

    # 8 - Do any "per frame" actions

    # 9 - Clear the window
    background.draw()

    # 10 - Draw all windows
    # Tell the game to draw itself
    oGame.draw()
    # Draw remaining user interface components
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

