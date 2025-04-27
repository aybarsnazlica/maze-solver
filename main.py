from display import Window, Point
from cell import Cell


def main():
    window = Window(800, 600)

    c1 = Cell(window, has_left_wall=False)
    c1.draw(Point(50, 50), Point(100, 100))

    c2 = Cell(window, has_right_wall=False)
    c2.draw(Point(150, 150), Point(200, 200))

    c3 = Cell(window, has_top_wall=False)
    c3.draw(Point(250, 250), Point(300, 300))

    c4 = Cell(window, has_bottom_wall=False)
    c4.draw(Point(450, 450), Point(500, 500))

    c1.draw_move(c2)
    c3.draw_move(c4, undo=True)

    window.wait_for_close()


if __name__ == "__main__":
    main()
