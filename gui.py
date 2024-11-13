from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Root Widget"
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()

        self.running = False


    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    

    def close(self):
        self.running = False

    
    def draw_line(self, Line, fill_colour):
        Line.draw(self.canvas, fill_colour)


    def draw_cell(self, Cell, fill_colour):
        Cell.draw(self.canvas, fill_colour)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## x=0 is the left limit
    ## y=0 is the top limit


class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2


    def draw(self, Canvas, fill_colour):
        Canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_colour, width=2)


class Cell:
    def __init__(self, point1, point2, lw=True, rw=True, tw=True, bw=True):
        self.has_left_wall = lw
        self.has_right_wall = rw
        self.has_top_wall = tw
        self.has_bottom_wall = bw
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
    

    def draw(self, Canvas, fill_colour):
        if self.has_left_wall:
            lw_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            lw_line.draw(Canvas, fill_colour)
        if self.has_right_wall:
            rw_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            rw_line.draw(Canvas, fill_colour)
        if self.has_top_wall:
            tw_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            tw_line.draw(Canvas, fill_colour)
        if self.has_bottom_wall:
            bw_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bw_line.draw(Canvas, fill_colour)
    

    def draw_move(self, to_cell, Canvas, undo=False):
        if not undo:
            fill_colour = "red"
        else:
            fill_colour = "gray"

        x1, y1 = self.find_centre()
        x2, y2 = to_cell.find_centre()

        line = Line(Point(x1, y1), Point(x2, y2))
        line.draw(Canvas, fill_colour)

    
    def find_centre(self):
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self._y2) / 2
        return mid_x, mid_y