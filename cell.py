from display import Line, Point


class Cell:
    def __init__(
        self,
        window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._window = window

    def draw(self, point1, point2):
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y

        lines_to_draw = []
        line_left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        line_right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        line_top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        line_bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

        if self.has_left_wall:
            lines_to_draw.append(line_left)

        if self.has_right_wall:
            lines_to_draw.append(line_right)

        if self.has_top_wall:
            lines_to_draw.append(line_top)

        if self.has_bottom_wall:
            lines_to_draw.append(line_bottom)

        for line in lines_to_draw:
            self._window.draw_line(line)
