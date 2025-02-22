# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
while True:
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

  
    window.fill((255, 255, 255))

    # Using draw.rect module of
# pygame to draw the solid rectangle
    pygame.draw.rect(window, (0, 0, 255),[100, 100, 400, 100], 0)

# Draws the surface object to the screen.
    pygame.display.update()
