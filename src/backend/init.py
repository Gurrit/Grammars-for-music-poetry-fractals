from config import *

class init:

    initializer = None

    def __init__(self):
        self._turtle = None
        self._forward = lambda step : self._turtle.forward(config.step)
        self._right = lambda angle : self._turtle.right(angle)
        self._left = lambda angle : self._turtle.left(angle)

        self._filler_append = lambda coordinate, treeFiller : treeFiller.stack.append(coordinate)
        self._filler_pop = lambda treeFiller : treeFiller.stack.pop()
        self._filler_layer = lambda amount, tree : tree.add_new_iteration(amount)

        self._web_forward = lambda step : "turtle.forward(" + str(config.step) + ")"
        self._web_right = lambda angle : "turtle.right(" + str(angle) + ")"
        self._web_left = lambda angle : "turtle.left(" + str(angle) + ")"
        
    def get_visualization_map(self):
        if self._turtle is None:
            raise ValueError("No Turtle given")
        return {"f" : self._forward,
                "r" : self._right,
                "l" : self._left
                }

    def get_filler_map(self):
        return {"(S" : self._filler_layer,
                "(N" : self._filler_append,
                "F)" : self._filler_pop
                }

    def get_web_map(self):
        return {
            "A": self._web_forward,
            "B": self._web_forward,
            "F": self._web_forward,
            "r": self._web_right,
            "l": self._web_left
        }

    @staticmethod
    def get_instance():
        if init.initializer is None:
            init.initializer = init()
        return init.initializer

    def set_turtle(self, turtle):
        self._turtle = turtle
        self.turtle_setup()

    def turtle_setup(self):
        self._turtle.speed(0)
        self._turtle.penup()
        self._turtle.goto(0, 0)
        self._turtle.pendown()
        self._turtle.hideturtle()
        #self._turtle.color("red") Doesnt work
        # self._turtle.tracer(0, 0) #TODO doesn't generate the full fractal for some reason??

