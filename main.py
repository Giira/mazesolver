from visuals import Window
from maze import Maze

def main():
    margin = 50
    num_cols = 14
    num_rows = 10
    cell_width = 50
    cell_height = 50
    screen_x = margin * 2 + num_cols * cell_width
    screen_y = margin * 2 + num_rows * cell_height

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height, win)

    maze.solve()

    win.wait_for_close()

main()