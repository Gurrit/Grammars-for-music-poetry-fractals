from lineSegment import *
from treeList import *


class treeFiller:

    def __init__(self):
        self.current_position = coordinate(0,0)
        self.coordinate_stack = []
        self.objectStack = []

