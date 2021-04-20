import pygame
from pygame.locals import *
# Handles sound
from pygame import mixer

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Frames per second
FPS = 3
# Assigning the width and height of snake game window
Width_window = 720
height_window = 600
size_cell = 30

assert height_window % size_cell == 0, "Window Height must be a multiple of Cell Size"
assert Width_window % size_cell == 0, "Window Width must be a multiple of Cell Size"
cell_width= int(Width_window / size_cell)
cell_height = int(height_window / size_cell)

# Setting colour for using them in snake game window
BLACK    = (0,     0,   0)
GREEN    = (0,   255,   0)
RED      = (255,   0,   0)
DARKGREEN= (0,   155,   0)
DARKGRAY = (40,   40,  40)
YELLOW   = (255, 255,   0)
WHITE    = (255, 255, 255)
BLUE     = (0, 204, 204)
BGCOLOR = BLUE

# Control Keys
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Setting the initial start up point for the head
HEAD = 0

# Going to connect snake game to my gesture control feature at end
# Background sound
mixer.music.load('./GameSound/snake_sound.mp3')
# Play music in a loop
mixer.music.play(-1) # -1 -> Play on loop