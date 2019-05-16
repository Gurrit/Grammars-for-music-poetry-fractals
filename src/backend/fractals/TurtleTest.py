import turtle


class KOCHTest:

    def __init__(self):
        self._koch_fractal_string = "l r l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l F l r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r F r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r l F l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l r F r l r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r F r l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l F l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l r F r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r l F l r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r F r l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l F l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l r F r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r l r F r l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l F l r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r F r l F r F r F l F l r F l F l F r F r F l F l F r l F l F r F r F l r l F l r F l F l F r F r l F r F r F l F l F r F r F l r F r F l F l F r l r l"
        self._turtle = turtle.Turtle()
        self._dragon_fractal_string = ""
        self._turtle.speed(0)

    def parse(self):

        # parts = self._koch_fractal_string.split(" ")
        # print(parts)
        # for part in parts:
        #    self.read_part(part)

        current_string = self._koch_fractal_string
        self._turtle.penup()
        self._turtle.goto(0, 0)
        self._turtle.pendown()
        self._turtle.hideturtle()

        parts_d = current_string.split(" ")
        self._turtle.color("red")
        for part_d in parts_d:
            self.read_part(part_d)

        turtle.done()

    def read_part(self, part):
        print("PART: " + part)
        if (part == "F") or (part == "B"):
            self._turtle.forward(4)
        elif part == "r":
            self._turtle.right(90)
        elif part == "l":
            self._turtle.left(90)


test = KOCHTest()
test.parse()