import pygame
import math

BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 255)
WHITE = (255, 255, 255) # 0
GREEN = (0, 255, 0) # 1
ROCK = (187, 187, 187) # 2
GREY = (160, 160, 160)
LIGHTBLUE = (173, 216, 230)
 
WIDTH = 25
HEIGHT = 25

# all grids are 32 by 32

grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
] 

unit_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 6, 8, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 6, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 3, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 5, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 7, 5, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
] 

movement_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
] 

for row in range(32):
    grid.append([])
    for column in range(32):
        grid[row].append(0)  
 
for row in range(32):
    movement_grid.append([])
    for column in range(32):
        movement_grid[row].append(0)  

current_units = []           

pygame.init()
WINDOW_SIZE = [1000, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Two Player Grid Game")

done = False

clock = pygame.time.Clock()

def sidemenu():
    font = pygame.font.Font(None, 26)
    text_list = []
    wanted_text_list = [
        ["How to play:", 805, 20, BLACK],
        ["Beats", 850, 80, BLACK],
        ["Beats", 850, 140, BLACK],
        ["Beats", 850, 200, BLACK],
        ["Anything unit against", 805, 240, BLACK],
        ["itself will both die", 805, 257, BLACK],
        ["Click on units to move", 805, 300, BLACK],
        ["them, the goal is to ", 805, 317, BLACK],
        ["destroy your opponents", 805, 334, BLACK],
        ["base", 805, 351, BLACK],
        ["Reinforments comes in", 805, 400, BLACK],
        ["every 10 turns", 805, 417, BLACK],
    ]

    

    for i in wanted_text_list:
        text = font.render(i[0], True, i[3])
        textpos = text.get_rect(x = i[1], y = i[2])
        out = (text, textpos)
        text_list.append(out)

        
    for i in text_list:
        screen.blit(i[0], i[1])

    color = BLACK
    pygame.draw.ellipse(screen, color, [(810) + 9, (80), 8, 8], 0)
    pygame.draw.line(screen, color, [(810) + 12, (80) + 7], [(810) + 12, (80) + 14], 2)
    pygame.draw.line(screen, color, [(810) + 12, (80) + 14], [(810) + 7, (80) + 22], 2)
    pygame.draw.line(screen, color, [(810) + 12, (80) + 14], [(810) + 17, (80) + 22], 2)
    pygame.draw.line(screen, color, [(810) + 6, (80) + 10], [(810) + 19, (80) + 10], 2)

    pygame.draw.rect(screen, color, [(910) + 5, (80) + 15, 14, 6])
    pygame.draw.ellipse(screen, color, [(910) + 5, (80) + 18, 7, 7], 0)
    pygame.draw.ellipse(screen, color, [(910) + 9, (80) + 18, 7, 7], 0)
    pygame.draw.ellipse(screen, color, [(910) + 13, (80) + 18, 7, 7], 0)
    pygame.draw.rect(screen, color, [(910) + 6, (80) + 10, 6, 6])
    pygame.draw.line(screen, color, [(910) + 9, (80) + 11], [(910) + 15, (80) + 11], 2)

    

    pygame.draw.rect(screen, color, [(810) + 5, (140) + 15, 14, 6])
    pygame.draw.ellipse(screen, color, [(810) + 5, (140) + 18, 7, 7], 0)
    pygame.draw.ellipse(screen, color, [(810) + 9, (140) + 18, 7, 7], 0)
    pygame.draw.ellipse(screen, color, [(810) + 13, (140) + 18, 7, 7], 0)
    pygame.draw.rect(screen, color, [(810) + 6, (140) + 10, 6, 6])
    pygame.draw.line(screen, color, [(810) + 9, (140) + 11], [(810) + 15, (140) + 11], 2)

    pygame.draw.rect(screen, color, [(910) + 7, (140) + 20, 12, 2])
    pygame.draw.rect(screen, color, [(910) + 11, (140) + 17, 2, 3])
    pygame.draw.rect(screen, color, [(910) + 15, (140) + 17, 2, 3])
    pygame.draw.rect(screen, color, [(910) + 9, (140) + 14, 8, 5])
    pygame.draw.ellipse(screen, color, [(910) + 7, (140) + 14, 4, 4], 0)
    pygame.draw.ellipse(screen, color, [(910) + 14, (140) + 14, 4, 4], 0)
    pygame.draw.rect(screen, color, [(910) + 13, (140) + 10, 2, 4])
    pygame.draw.rect(screen, color, [(910) + 7, (140) + 9, 12, 2])

    

    pygame.draw.rect(screen, color, [(810) + 7, (200) + 20, 12, 2])
    pygame.draw.rect(screen, color, [(810) + 11, (200) + 17, 2, 3])
    pygame.draw.rect(screen, color, [(810) + 15, (200) + 17, 2, 3])
    pygame.draw.rect(screen, color, [(810) + 9, (200) + 14, 8, 5])
    pygame.draw.ellipse(screen, color, [(810) + 7, (200) + 14, 4, 4], 0)
    pygame.draw.ellipse(screen, color, [(810) + 14, (200) + 14, 4, 4], 0)
    pygame.draw.rect(screen, color, [(810) + 13, (200) + 10, 2, 4])
    pygame.draw.rect(screen, color, [(810) + 7, (200) + 9, 12, 2])
    
    pygame.draw.ellipse(screen, color, [(910) + 9, (200), 8, 8], 0)
    pygame.draw.line(screen, color, [(910) + 12, (200) + 7], [(910) + 12, (200) + 14], 2)
    pygame.draw.line(screen, color, [(910) + 12, (200) + 14], [(910) + 7, (200) + 22], 2)
    pygame.draw.line(screen, color, [(910) + 12, (200) + 14], [(910) + 17, (200) + 22], 2)
    pygame.draw.line(screen, color, [(910) + 6, (200) + 10], [(910) + 19, (200) + 10], 2)



    
    font = pygame.font.Font(None, 22)
    text_list2 = []
    
    if playerturn == 0:
        wanted_text_list2 = [
            ["Current turn: Purple", 805, 550, PURPLE],
        ]
    elif playerturn == 1:
        wanted_text_list2 = [
            ["Current turn: RED", 805, 550, RED],
        ]

    for i in wanted_text_list2:
        text = font.render(i[0], True, i[3])
        textpos = text.get_rect(x = i[1], y = i[2])
        out = (text, textpos)
        text_list2.append(out)

        
    for i in text_list2:
        screen.blit(i[0], i[1])

def updategame():
    # map
    for row in range(32):
        for column in range(32):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = ROCK
            pygame.draw.rect(screen,color, [(WIDTH) * column, (HEIGHT) * row, WIDTH, HEIGHT])
    
    # Highlights what units can move
    temp = 2
    for i in current_units:
        if i[0] == "Red":
            temp = 1
        elif i[0] == "Purple":
            temp = 0
        if (temp == playerturn) and (i[4] == 1):
            grid[i[2]][i[3]] = 2


    
    # add units from 'current_units' list
    for unit in current_units:
        temp_row = unit[2]
        temp_column = unit[3]
        if unit[0] == "Red":
            unit_grid[temp_row][temp_column] = unit[1]
        elif unit[0] == "Purple":
            unit_grid[temp_row][temp_column] = unit[1]
        else:
            unit_grid[temp_row][temp_column] = 0


    # movement map
    for row in range(32):
        for column in range(32):
            if movement_grid[row][column] == 1:
                color = WHITE
                pygame.draw.rect(screen,color, [(WIDTH) * column, (HEIGHT) * row, WIDTH, HEIGHT])
            elif movement_grid[row][column] == 2:
                color = LIGHTBLUE
                pygame.draw.rect(screen,color, [(WIDTH) * column, (HEIGHT) * row, WIDTH, HEIGHT])
            

    # unit drawing
    for row in range(32):
        for column in range(32):
            if unit_grid[row][column] == 0:
                pass
            elif unit_grid[row][column] == 1:
                color = RED
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row, 8, 8], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 7], [(WIDTH) * column + 12, (HEIGHT) * row + 14], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 7, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 17, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10], [(WIDTH) * column + 19, (HEIGHT) * row + 10], 2)
            elif unit_grid[row][column] == 2:
                color = PURPLE
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row, 8, 8], 0)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 7], [(WIDTH) * column + 12, (HEIGHT) * row + 14], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 7, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 12, (HEIGHT) * row + 14], [(WIDTH) * column + 17, (HEIGHT) * row + 22], 2)
                pygame.draw.line(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10], [(WIDTH) * column + 19, (HEIGHT) * row + 10], 2)
            elif unit_grid[row][column] == 3:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 15, 14, 6])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10, 6, 6])
                pygame.draw.line(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 11], [(WIDTH) * column + 15, (HEIGHT) * row + 11], 2)
            elif unit_grid[row][column] == 4:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 15, 14, 6])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 5, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 18, 7, 7], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 6, (HEIGHT) * row + 10, 6, 6])
                pygame.draw.line(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 11], [(WIDTH) * column + 15, (HEIGHT) * row + 11], 2)
            elif unit_grid[row][column] == 5:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 20, 12, 2])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 11, (HEIGHT) * row + 17, 2, 3])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 17, 2, 3])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 14, 8, 5])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 14, 4, 4], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 14, (HEIGHT) * row + 14, 4, 4], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 10, 2, 4])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 9, 12, 2])
            elif unit_grid[row][column] == 6:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 20, 12, 2])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 11, (HEIGHT) * row + 17, 2, 3])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 17, 2, 3])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 9, (HEIGHT) * row + 14, 8, 5])
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 14, 4, 4], 0)
                pygame.draw.ellipse(screen, color, [(WIDTH) * column + 14, (HEIGHT) * row + 14, 4, 4], 0)
                pygame.draw.rect(screen, color, [(WIDTH) * column + 13, (HEIGHT) * row + 10, 2, 4])
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 9, 12, 2])
            elif unit_grid[row][column] == 7:
                color = RED
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 13, 12, 8])
                pygame.draw.line(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 13], [(WIDTH) * column + 15, (HEIGHT) * row + 3], 3)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 15, (HEIGHT) * row + 3], [(WIDTH) * column + 15, (HEIGHT) * row + 10], [(WIDTH) * column + 4, (HEIGHT) * row + 7]], 1)
            elif unit_grid[row][column] == 8:
                color = PURPLE
                pygame.draw.rect(screen, color, [(WIDTH) * column + 7, (HEIGHT) * row + 13, 12, 8])
                pygame.draw.line(screen, color, [(WIDTH) * column + 15, (HEIGHT) * row + 13], [(WIDTH) * column + 15, (HEIGHT) * row + 3], 3)
                pygame.draw.polygon(screen, color, [[(WIDTH) * column + 15, (HEIGHT) * row + 3], [(WIDTH) * column + 15, (HEIGHT) * row + 10], [(WIDTH) * column + 4, (HEIGHT) * row + 7]], 1)

def AddUnit(Typ, row, col, mov):
    if Typ == 1 or Typ == 3 or Typ == 5 or Typ == 7:
        if mov == 0:
            current_units.append(["Red", Typ, row, col, 0])
        elif mov == 1:
            current_units.append(["Red", Typ, row, col, 1])
    elif Typ == 2 or Typ == 4 or Typ == 6 or Typ == 8:
        if mov == 0:
            current_units.append(["Purple", Typ, row, col, 0])
        elif mov == 1:
            current_units.append(["Purple", Typ, row, col, 1])

def ForceRemoveUnit(row0, col0):
    temp = 0
    for del_unit in current_units:
        if del_unit[2] == row0 and del_unit[3] == col0:
            current_units.pop(temp)
            unit_grid[row0][col0] = 0
            updategame()
        else:
            temp += 1

def resetmovegrid():
    for row in range(32):
        for column in range(32):
            movement_grid[row][column] = 0

def unitbattle(row1, col1, row2, col2):
    commit = 0
    Attackervalue = unit_grid[row1][col1]
    Defendervalue = unit_grid[row2][col2]
    
    # make sure the two units are not on the same team
    if Attackervalue == 1 or Attackervalue == 3 or Attackervalue == 5 or Attackervalue == 7:
        if Defendervalue == 2 or Defendervalue == 4 or Defendervalue == 6 or Defendervalue == 8:
            commit = 1
    elif Attackervalue == 2 or Attackervalue == 4 or Attackervalue == 6 or Attackervalue == 8:
        if Defendervalue == 1 or Defendervalue == 3 or Defendervalue == 5 or Defendervalue == 7:
            commit = 1

    if commit == 1: #for the types: 1 = infantry, 2 = tank, 3 = helicopter, 4 = base
        A_type = int(math.ceil(Attackervalue / 2))
        D_type = int(math.ceil(Defendervalue / 2))

        A_death = 0
        D_death = 0

        # 1 beats 2, 2 beats 3, 3 beats 1, if they are the same number then they both die

        if A_type == 1 and D_type == 1:
            A_death = 1
            D_death = 1
        elif A_type == 1 and D_type == 2:
            D_death = 1
        elif A_type == 1 and D_type == 3:
            A_death = 1

        elif A_type == 2 and D_type == 1:
            A_death = 1
        elif A_type == 2 and D_type == 2:
            A_death = 1
            D_death = 1
        elif A_type == 2 and D_type == 3:
            D_death = 1

        elif A_type == 3 and D_type == 1:
            D_death = 1
        elif A_type == 3 and D_type == 2:
            A_death = 1
        elif A_type == 3 and D_type == 3:
            A_death = 1
            D_death = 1

        elif A_type == 4:
            A_death = 1
        elif D_type == 4:
            D_death = 1

        if A_death == 1 and D_death == 1:
            ForceRemoveUnit(row1, col1)
            ForceRemoveUnit(row2, col2)
        elif A_death == 1:
            ForceRemoveUnit(row1, col1)
        elif D_death == 1:
            ForceRemoveUnit(row2, col2)
            winner = findunit(row1, col1)
            winner[4] = 0
        
def turns(turncount):
    if turncount == 20:
        AddUnit(2, 0, 30)
        AddUnit(4, 0, 31)
        AddUnit(6, 1, 31)
        AddUnit(1, 30, 0)
        AddUnit(3, 31, 0)
        AddUnit(5, 31, 1)

def calcunits(team):
    number = 0
    for i in current_units:
        if (i[0] == team) and (i[1] != 7) and (i[1] !=8):
            i[4] = 1
            number += 1
    return number

def findunit(row, col):
    for i in current_units:
        if (i[2] == row) and (i[3] == col):
            return i

def checkforwinner():
    rbase = 1
    pbase = 1
    for row in range(32):
        for column in range(32):
            if grid[row][column] == 7:
                rbase = 0
            elif grid[row][column] == 8:
                pbase = 0
    if pbase == 0: # red win condition
        return 1
    elif rbase == 0: # purple win condition
        return 2
    else:
        return 0


for row in range(32):
    for column in range(32):
        if unit_grid[row][column] != 0:
            AddUnit(unit_grid[row][column], row, column, 0)

TC = 0
storedrow = -1
storedcol = -1
storedvalue = -1
storedrow2 = -1
storedcol2 = -1
storedvalue2 = -1
playerturn = 0 # 0 = purple, 1 = red

movement = calcunits("Purple")

while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True
        if (event.type == pygame.MOUSEBUTTONDOWN) and (pygame.mouse.get_pos()[0] <= 800):
            pos = pygame.mouse.get_pos()
            proceed = 0
            column = pos[0] // (WIDTH)
            row = pos[1] // (HEIGHT)
            if movement_grid[row][column] == 2:
                for temp_row in range(32):
                    for temp_column in range(32):
                        if movement_grid[temp_row][temp_column] == 1:
                            storedrow2 = temp_row
                            storedcol2 = temp_column
                            if unit_grid[row][column] == 0:
                                storedvalue2 = unit_grid[temp_row][temp_column]
                                ForceRemoveUnit(storedrow2, storedcol2)
                                grid[storedrow2][storedcol2] = 1
                                AddUnit(storedvalue2, row, column, 0)
                                movement -= 1
                                resetmovegrid()
                            elif unit_grid[row][column] != 0:
                                unitbattle(storedrow2, storedcol2, row, column)
                                grid[storedrow2][storedcol2] = 1
                                movement -= 1
                                resetmovegrid()
                            if movement == 0:
                                TC += 1
                                turns(TC)
                                if TC >= 10:
                                    TC = 0
                                if playerturn == 0:
                                    playerturn = 1
                                    movement = calcunits("Red")
                                else:
                                    playerturn = 0
                                    movement = calcunits("Purple")
            elif (movement_grid[row][column] == 0) and unit_grid[row][column] != 0 and unit_grid[row][column] != 7 and unit_grid[row][column] != 8:
                if (unit_grid[row][column] == 2) or (unit_grid[row][column] == 4) or (unit_grid[row][column] == 6):
                    selected = findunit(row, column)
                    if (playerturn == 0) and (movement > 0) and (selected[4] == 1):
                        proceed = 1
                elif (unit_grid[row][column] == 1) or (unit_grid[row][column] == 3) or (unit_grid[row][column] == 5):
                    selected = findunit(row, column)
                    if (playerturn == 1) and (movement > 0) and (selected[4] == 1):
                        proceed = 1
                if proceed == 1:
                    resetmovegrid()
                    storedrow = row
                    storedcol = column
                    storedvalue = 0
                    movement_grid[row][column] = 1

                    for i in range(0, 5):
                        highlight = (i + row)
                        VAL = (highlight - 2)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != row) and ((column + 1) <= 31):
                            movement_grid[VAL][column + 1] = 2
                    for i in range(0, 7):
                        highlight = (i + row)
                        VAL = (highlight - 3)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != row):
                            movement_grid[VAL][column] = 2
                    for i in range(0, 5):
                        highlight = (i + row)
                        VAL = (highlight - 2)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != row) and ((column - 1) >= 0):
                            movement_grid[VAL][column - 1] = 2



                            
                    for i in range(0, 5):
                        highlight = (i + column)
                        VAL = (highlight - 2)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != column) and ((row + 1) <= 31):
                            movement_grid[row + 1][VAL] = 2
                    for i in range(0, 7):
                        highlight = (i + column)
                        VAL = (highlight - 3)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != column):
                            movement_grid[row][VAL] = 2
                    for i in range(0, 5):
                        highlight = (i + column)
                        VAL = (highlight - 2)
                        if (VAL >= 0) and (VAL <= 31) and (VAL != column) and ((row - 1) >= 0):
                            movement_grid[row - 1][VAL] = 2




                    if (row + 1 <= 31) and (column + 1 <= 31):
                        movement_grid[row + 1][column + 1] = 2
                    if (row + 1 <= 31) and (column - 1 >= 0):
                        movement_grid[row + 1][column - 1] = 2
                    if (row - 1 >= 0) and (column + 1 <= 31):
                        movement_grid[row - 1][column + 1] = 2
                    if (row - 1 >= 0) and (column - 1 >= 0):
                        movement_grid[row - 1][column - 1] = 2
            else:
                resetmovegrid()



    screen.fill(GREY)
    
    updategame()
    sidemenu()

    winner = checkforwinner()
    if winner == 1:
        done = True
    elif winner == 2:
        done = True

    clock.tick(60)
    pygame.display.flip()
 


pygame.quit()