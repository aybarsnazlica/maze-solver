from display import Window, Line, Point


def main():
    win = Window(800, 600)
    line1 = Line(Point(100, 400), Point(300, 200))
    line2 = Line(Point(50, 250), Point(150, 350))
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
