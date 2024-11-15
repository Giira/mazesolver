from visuals import Point, Line
from cell import Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win
        self.cells = []

        self._create_cells()
        

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
        x2 = self.x1 + self.cell_size_x
        y2 = self.y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        sleep(0.03)
