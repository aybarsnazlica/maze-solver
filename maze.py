import time

from cell import Cell
from display import Point


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        point1, point2, = Point(x1, y1), Point(x2, y2)
        self._cells[i][j].draw(point1, point2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return

        self._window.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        top_x, top_y = 0, 0
        self._cells[top_x][top_y].has_top_wall = False
        self._draw_cell(top_x, top_y)
        bottom_x, bottom_y = self._num_cols - 1, self._num_rows - 1
        self._cells[bottom_x][bottom_y].has_bottom_wall = False
        self._draw_cell(bottom_x, bottom_y)
