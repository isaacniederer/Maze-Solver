from tkinter import (
    Tk, 
    BOTH, 
    Canvas,
)

from line import (
    Line,
    Point,
)

class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
#        self.__root.geometry(f"{self.__width}x{self.__height}")
        self.__root.title("Maze Solver")
        self.canv = Canvas(height=height, width=width)
        self.canv.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close())

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canv, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


