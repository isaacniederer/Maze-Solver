import random as rand

import sys

from window import Window

from line import (
    Line,
    Point,
)

from cell import(
    Cell,
)

from maze import(
    Maze,
)


#sys.setrecursionlimit(10**5)
win = Window(600, 450)
maze = Maze(3, 3, 20, 20, 20, 20, win)
maze._break_entrance_and_exit()
maze._break_walls_r(0, 0)
maze._reset_cells_visited()
maze.solve()
win.wait_for_close()
