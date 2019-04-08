import math
import random

class lineSegment:

    def __init__(self,coordinate_1,coordinate_2,color="#000000"):
        self.coordinate_1 = coordinate_1
        if abs(coordinate_1.x) < 1e-12:
            coordinate_1.x = 0
        if abs(coordinate_1.y) < 1e-12:
            coordinate_1.y = 0
        self.coordinate_2 = coordinate_2
        if abs(coordinate_2.x) < 1e-12:
            coordinate_2.x = 0
        if abs(coordinate_2.y) < 1e-12:
            coordinate_2.y = 0
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
        if self.x_length < 0:
            self.angle += 180
        if abs(self.angle) > 180:
            self.angle -= 360 * self.angle/abs(self.angle)

    def shortest_distance(self, point):
        x = point.x
        x1 = self.coordinate_1.x
        x2 = self.coordinate_2.x
        y = point.y
        y1 = self.coordinate_1.y
        y2 = self.coordinate_2.y

        if (y1 - y2) == 0 and x < max(x1,x2) and x > min(x1,x2):
            return abs(y-y1)
        elif (y1 - y2) != 0 and (y > min(y2+(x1-x)*(x2-x1)/(y2-y1),y1+(x1-x)*(x2-x1)/(y2-y1))) and (y < max(y2+(x1-x)*(x2-x1)/(y2-y1),y1+(x1-x)*(x2-x1)/(y2-y1))):
            # Ortogonalprojektion
            l = lineSegment(self.coordinate_1, point)
            return abs(l.length * math.sin((l.angle - self.angle)*math.pi/180))

        else:
            return min(lineSegment(self.coordinate_2,point).length, lineSegment(self.coordinate_1,point).length)




class coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def clone(self):
        return coordinate(self.x, self.y)