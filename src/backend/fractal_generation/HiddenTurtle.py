from fractal_generation.LineSegment import *


class HiddenTurtle:

    def __init__(self):
        self.coordinate = Coordinate(0, 0)
        self.angle = 0

    def forward(self, distance):
        x = math.cos(self.angle * math.pi/180) * distance
        y = math.sin(self.angle * math.pi/180) * distance
        self.coordinate.x += x
        self.coordinate.y += y

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle
