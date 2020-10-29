from Classes.Game import game
import math
from queue import PriorityQueue

def main():
    win = game.GameWin(500, 500, 'A* Path finding Algorithm')
    win.set_win_mode()
    win.set_win_title()

if __name__ == '__main__':
    main()
