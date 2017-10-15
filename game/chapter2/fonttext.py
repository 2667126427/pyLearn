import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

fontObj = pygame.font.Font('../asserts/Roboto-Regular.ttf', 32)
textSurfaceObj = fontObj.render("Hello world!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAY.fill(WHITE)
    DISPLAY.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
