import pygame
from Classes.Colors import color


# Creating the game window
class GameWin:
    def __init__(self, HEIGHT, WIDTH, TITLE):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.TITLE = TITLE
    
    # returns window dimension
    def set_win_mode(self):
        return pygame.display.set_mode((self.HEIGHT, self.WIDTH))

    # return windows title
    def set_win_title(self):
        return pygame.display.set_caption(self.TITLE)



# Creating our node
class Spot(color):

    # determing the characterstics of default spot
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = color.Color.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # returning the state of the spot
    """
        The possible state could be as follows:
            1. to get the co-ordinate at that point 
            2. to check whether the spot is visited or not
            3. to repesent the areas availabe to visit
            4. to check for the whether it hit the boundary or not
            5. to give the start posiiton
            6. to give the end position 
    """
    def get_pos(self):
        return self.row, self.column
    
    def is_closed(self):
        return self.color == color.Color.RED

    def is_open(self):
        return self.color == color.Color.GREEN

    def is_barrier(self):
        return self.color == color.Color.BLACK
    
    def is_start(self):
        return self.color == color.Color.ORANGE

    def is_end(self):
        return self.color == color.Color.TORQUISE


    # check for reset option
    def reset(self):
        return self.color == color.Color.WHITE 


    # change the state 
    def make_closed(self):
        self.color = color.Color.RED

    def make_open(self):
        self.color = color.Color.GREEN

    def make_barrier(self):
        self.color = color.Color.BLACK

    def make_end(self):
        self.color = color.Color.TORQUISE

    def make_path(self):
        self.color = color.Color.PURPLE
