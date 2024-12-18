from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root_widget, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)

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

    
    def draw_line(self, Line, fill_colour="black"):
        Line.draw(self.canvas, fill_colour)
    

    def draw_h_line(self, Line, fill_colour="black"):
        Line.draw_h(self.canvas, fill_colour)

    
    def draw_v_line(self, Line, fill_colour="black"):
        Line.draw_v(self.canvas, fill_colour)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

        self.h_points = [self.point_1.x +1, self.point_1.y, self.point_1.x +3, self.point_1.y -2, 
                       self.point_2.x -3, self.point_2.y -2, self.point_2.x -1, self.point_2.y, 
                       self.point_2.x -3, self.point_2.y +2, self.point_1.x +3, self.point_1.y +2]
        
        self.v_points = [self.point_1.x, self.point_1.y +1, self.point_1.x +2, self.point_1.y +3, 
                       self.point_2.x +2, self.point_2.y -3, self.point_2.x, self.point_2.y -1, 
                       self.point_2.x -2, self.point_2.y -3, self.point_1.x -2, self.point_1.y +3]


    def draw(self, Canvas, fill_colour="black"):
        Canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_colour, width=2)
        

    def draw_h(self, Canvas, fill_colour="black"):
        Canvas.create_polygon(self.h_points, outline=fill_colour, fill="white", width=2)

    
    def draw_v(self, Canvas, fill_colour="black"):
        Canvas.create_polygon(self.v_points, outline=fill_colour, fill="white", width=2)

