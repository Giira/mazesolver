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