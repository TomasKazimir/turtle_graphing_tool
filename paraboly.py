from typing import Tuple
from math import cos, pi, sin, sqrt, tan
import turtle


class TDrawer(turtle.Turtle):

    def __init__(self, pensize: int, screensize: Tuple[int], speed: Tuple[int]) -> None:
        turtle.Turtle.__init__(self)

        self.screen = turtle.Screen()
        self.screen.setup(*[size for size in screensize])
        self.screen.title('Parabolas Bitch')
        self.screen.bgcolor('black')

        self.screensize = screensize

        self.pensize(pensize)

        self.color('gray75', 'gray75')
        self.screen.tracer(*speed)

        self.penup()

        # self.hideturtle()

    def draw_function(self, function, start=-900, end=900, zoom=10, customs: dict = None, precision=1):
        if customs is None:
            customs = {}
        for x in range(int(start*precision), int(end*precision)):
            try:
                functions = {"x": x/zoom/precision,
                             "sqrt": sqrt,
                             "sin": sin,
                             "cos": cos,
                             "tan": tan}
                functions.update(customs)
                y = eval(function,  functions) * zoom
            except Exception as e:
                print(e)
                continue
            self.goto(x/precision, y)
            self.pendown()
            if abs(y) > end:
                self.penup()
        self.penup()

    def draw_axes(self, size, scale, skip=1, zoom=1):
        font = ('Bahnschrift Light Condensed', 10, 'normal')
        # x
        i = 0
        self.goto(0, 0)
        self.pendown()
        while (i-skip) * scale * zoom < size:
            if i % skip < 1:
                self.goto(scale * i * zoom, 0)
                self.write(round(i * scale, 2),
                           font=font)
                self.goto(-scale * i * zoom, 0)
                self.write(round(-i * scale, 2),
                           font=font)
            i += 1
        self.penup()

        # y
        i = 0
        self.goto(0, 0)
        self.pendown()
        while (i-skip) * scale * zoom < size:
            if i % skip < 1:
                self.goto(0, scale * i * zoom)
                self.write(round(i * scale, 2),
                           font=font, align='right')
                self.goto(0, -scale * i * zoom)
                self.write(round(-i * scale, 2),
                           font=font, align='right')
            i += 1
        self.penup()

        self.render_frame()

    def render_frame(self):
        self.screen.update()


if __name__ == '__main__':
    d = TDrawer(1, (1800, 900), (1, 0))
    zoom = 50
    d.draw_axes(800, pi, skip=1, zoom=zoom)
    d.draw_function('sin(x)', zoom=zoom, precision=0.15)
    d.draw_function('sin(x+3.141592653589793)', zoom=zoom, precision=0.15)
    d.draw_function('cos(x+3.141592653589793)', zoom=zoom, precision=0.15)
    d.draw_function('tan(x)', zoom=zoom, precision=10)
    d.draw_function('mod(x,10)', zoom=zoom, customs={
        'mod': (lambda x, y: x % y)})

    c = TDrawer(1, (1800, 900), (1, 0))
    c.draw_function('cos(x)', zoom=zoom, precision=0.15)

    d.screen.exitonclick()
