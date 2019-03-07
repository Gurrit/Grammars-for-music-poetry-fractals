import math

class lineSegment:

    def __init__(self,coordinate_1,coordinate_2,color="#000000"):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2
        self.color = color
        self.x_length = coordinate_2.x - coordinate_1.x
        self.y_length = coordinate_2.y - coordinate_1.y

        self.length = math.sqrt((self.x_length*self.x_length) + (self.y_length*self.y_length))
        self.angle = math.atan(self.y_length / self.x_length)




class coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    
