from display import Window
from maze import Maze


def main():
    num_rows = 18
    num_cols = 20
    screen_x = 800
    screen_y = 600
    margin = 50
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    window = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()
