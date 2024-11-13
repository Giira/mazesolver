from gui import Window, Point, Line, Cell

win = Window(800, 600)

point1 = Point(10, 10)
point2 = Point(110, 110)

point3 = Point(310, 10)
point4 = Point(410, 110)

cell = Cell(point1, point2, True, False, True, True)
cell2 = Cell(point3, point4, False)

win.draw_cell(cell, "black")
win.draw_cell(cell2, "black")

cell.draw_move(cell2, win.canvas)

win.wait_for_close()