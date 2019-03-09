from lineSegment import *
from math import *

class HiddenTurtle:

    def __init__(self):
        self.coordinate = coordinate(0, 0)
        self.angle = 0

    def forward(self, distance):
        x = math.cos(self.angle) * distance
        y = math.sin(self.angle) * distance
        self.coordinate.x += x
        self.coordinate.y += y

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle
