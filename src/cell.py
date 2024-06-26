from window import (
    Window,
)

from line import (
    Line,
    Point
)

class Cell():
    def __init__(self, x1, y1, x2, y2, win):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win

    def draw(self):
        if self.left_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x1, self.__y2)
                ),
                "black"
            )
        else:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1+1),
                    Point(self.__x1, self.__y2)
                ),
                "#d9d9d9"
            )
        if self.right_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y1),
                    Point(self.__x2, self.__y2)
                ),
                "black"
            )
        else:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y1+1),
                    Point(self.__x2, self.__y2)
                ),
                "#d9d9d9"
            )
        if self.top_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x2, self.__y1)
                ),
                "black"
            )
        else:
            self.__win.draw_line(
                Line(
                    Point(self.__x1+1, self.__y1),
                    Point(self.__x2, self.__y1)
                ),
                "#d9d9d9"
            )
        if self.bottom_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y2),
                    Point(self.__x2, self.__y2)
                ),
                "black"
            )
        else:
            self.__win.draw_line(
                Line(
                    Point(self.__x1+1, self.__y2),
                    Point(self.__x2, self.__y2)
                ),
                "#d9d9d9"
            )

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        to_line = Line(
                    Point(
                        (self.__x1 + self.__x2) // 2,
                        (self.__y1 + self.__y2) // 2
                    ), 
                    Point(
                        (to_cell.__x1 + to_cell.__x2) // 2,
                        (to_cell.__y1 + to_cell.__y2) // 2
                    )
                  )
        to_line.draw(self.__win.canv, color)

    def change_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def change_left_wall(self):
        self.left_wall = False

    def change_right_wall(self):
        self.right_wall = False

    def change_top_wall(self):
        self.top_wall = False

    def change_bottom_wall(self):
        self.bottom_wall = False


    def __repr__(self):
        return f"x1:{self.__x1} y1:{self.__y1} x2:{self.__x2} y2:{self.__y2}"
