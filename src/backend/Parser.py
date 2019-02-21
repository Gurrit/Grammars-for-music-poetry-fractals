from init import *

class TurtleParser:

    def __init__(self, turtle):
        self._turtle = turtle
        self._turtle_map = {}

    def setup(self):
        init.get_instance().set_turtle(self._turtle)
        self._turtle_map = init.get_instance().get_visualization_map()