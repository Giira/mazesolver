from visuals import Point, Line
from cell import Cell
from time import sleep
from random import seed, choice

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win
        self.cells = []
        self.seed = None

        if self.seed is not None:
            seed(self.seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self.window))
            self.cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        

    def _draw_cell(self, i, j):
        if self.window is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        sleep(0.03)


    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            ij_list = []
                        
            if i != self.num_cols -1:
                if not self.cells[i+1][j].visited:
                    ij_list.append((i+1, j, "right"))
            if i != 0:
                if not self.cells[i-1][j].visited:
                    ij_list.append((i-1, j, "left"))
            if j != self.num_rows -1:
                if not self.cells[i][j+1].visited:
                    ij_list.append((i, j+1, "bottom"))
            if j != 0:
                if not self.cells[i][j-1].visited:
                    ij_list.append((i, j-1, "top"))
            
            if ij_list == []:
                self._draw_cell(i, j)
                return
            direction = choice(ij_list)
            
            match direction[2]:
                case "right":
                    self.cells[i][j].has_right_wall = False
                    self.cells[i+1][j].has_left_wall = False
                    self._break_walls_r(i+1, j)
                case "left":
                    self.cells[i][j].has_left_wall = False
                    self.cells[i-1][j].has_right_wall = False
                    self._break_walls_r(i-1, j)
                case "top":
                    self.cells[i][j].has_top_wall = False
                    self.cells[i][j-1].has_bottom_wall = False
                    self._break_walls_r(i, j-1)
                case "bottom":
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[i][j+1].has_top_wall = False
                    self._break_walls_r(i, j+1)
                        

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    
    def solve(self, i=0, j=0):
        return self._solve_r(i, j)


    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_cols -1 and j == self.num_rows -1:
            return True
        
        if i > 0 and not self.cells[i][j].has_left_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], undo=True)

        if j > 0 and not self.cells[i][j].has_top_wall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1], undo=True)
        
        if i < self.num_cols - 1 and not self.cells[i][j].has_right_wall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j], undo=True)

        if j < self.num_rows -1 and not self.cells[i][j].has_bottom_wall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1], undo=True)
        return False
