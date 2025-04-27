from display import Window, Point
from cell import Cell


def main():
    window = Window(800, 600)

    c1 = Cell(window, has_left_wall=False)
    c1.draw(Point(50, 50), Point(100, 100))

    c2 = Cell(window, has_right_wall=False)
    c2.draw(Point(150, 150), Point(200, 200))

    window.wait_for_close()


if __name__ == "__main__":
    main()
