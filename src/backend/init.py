

class init:

    initializer = None

    def __init__(self):
        self._turtle = None
        self._forward = lambda step : self._turtle.forward(step)
        self._right = lambda angle : self._turtle.right(angle)
        self._left = lambda angle : self._turtle.left(angle)

    def get_visualization_map(self):
        if self._turtle is None:
            raise ValueError("No Turtle given")
        return {"f" : self._forward, "r" : self._right, "l" : self._left }

    @staticmethod
    def get_instance():
        if init.initializer is None:
            init.initializer = init()
        return init.initializer

    def set_turtle(self, turtle):
        self._turtle = turtle
        self.turtle_setup()


    def turtle_setup(self):
        pass
