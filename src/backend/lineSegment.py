import math
import random

class lineSegment:

    def __init__(self,coordinate_1,coordinate_2,color="#000000"):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2
        self.color = color
        self.x_length = coordinate_2.x - coordinate_1.x
        self.y_length = coordinate_2.y - coordinate_1.y
        self.duration = math.pow(2, random.randint(-2,2))
        self.new_track = False

        self.length = math.sqrt((self.x_length*self.x_length) + (self.y_length*self.y_length))
        if self.x_length != 0:
            self.angle = math.atan(self.y_length / self.x_length) * 180 / math.pi
        elif self.y_length > 0:
            self.angle = 90
        else:
            self.angle = -90




class coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def clone(self):
        return coordinate(self.x, self.y)