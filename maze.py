from visuals import Cell, Point
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
        x = self.x1
        for i in range(self.num_cols):
            column = []
            y = self.y1
            for j in range(self.num_rows):
                column.append(Cell(Point(x, y), Point(x + self.cell_size_x, y + self.cell_size_y)))
                y += self.cell_size_y
            self.cells.append(column)
            x += self.cell_size_x

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    

    def _draw_cell(self, i, j):
        self.win.draw_cell(self.cells[i][j], "black")
        self._animate()
    

    def _animate(self):
        self.win.redraw()
        sleep(0.05)
