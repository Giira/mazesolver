from visuals import Window
from maze import Maze

def main():
    margin = 50
    screen_x = 800
    screen_y = 600
    num_cols = 15
    num_rows = 11
    cell_width = 50
    cell_height = 50

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height, win)

    win.wait_for_close()

main()