from cell import (
    Cell,
)

import random as rand

import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed=None,
        ):
        self.x1 = x1
        self.y1 = y1 
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.win = win
        self._create_cells()
        if seed is not None:
            rand.seed(seed)

    def _create_cells(self):
        for i in range(0, self.num_cols):
            self._cells.append([])
            for j in range(0, self.num_rows):
                self._cells[i].append(Cell(0,0,0,0, self.win))

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].change_coords(
                self.x1 + (j*self.cell_size_x), 
                self.y1 + (i*self.cell_size_y),
                self.x1 + ((j+1)*self.cell_size_x),
                self.y1 + ((i+1)*self.cell_size_y)
            )
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].change_top_wall()
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].change_bottom_wall()
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append([i-1,j])
            if i < self.num_cols-1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append([i+1,j])
            if j > 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append([i,j-1])
            if j < self.num_rows-1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append([i,j+1])
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            idx = rand.randint(0, len(to_visit)-1)
            tup = to_visit[idx]
            if i < tup[0]:
                self._cells[i][j].change_bottom_wall()
                self._cells[tup[0]][tup[1]].change_top_wall()
            if i > tup[0]:
                self._cells[i][j].change_top_wall()
                self._cells[tup[0]][tup[1]].change_bottom_wall()
            if j < tup[1]:
                self._cells[i][j].change_right_wall()
                self._cells[tup[0]][tup[1]].change_left_wall()
            if j > tup[1]:
                self._cells[i][j].change_left_wall()
                self._cells[tup[0]][tup[1]].change_right_wall()
            self._break_walls_r(tup[0],tup[1]) 

    def _reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        if self._cells[i][j].left_wall == False and j > 0:
            if self._cells[i][j-1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1) == True:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        if self._cells[i][j].right_wall == False and j < self.num_rows-1:
            if self._cells[i][j+1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1) == True:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if self._cells[i][j].top_wall == False and i > 0:
            if self._cells[i-1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j) == True:
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if self._cells[i][j].bottom_wall == False and i < self.num_cols-1:
            if self._cells[i+1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j) == True:
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        return False



