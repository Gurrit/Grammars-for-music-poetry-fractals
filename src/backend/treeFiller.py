from lineSegment import *
from treeList import *
from config import *


class treeFiller:

    def __init__(self, tree, angle, kids, max_duration = 32):
        self.current_position = coordinate(0,0)
        self.coordinate_stack = []
        self.objectStack = []
        self.tree = tree
        self.angle = angle
        self.kids = kids
        self.max_duration = max_duration

    def generate_nodes(self, commands, turtle, iteration): #self, commands, turtle, filler, iteration):
        self.coordinate_stack.append(turtle.coordinate.clone())
        duration_sum = 0
        for command in commands:
            if "F" in command or "A" in command or "B" in command:
                turtle.forward(config.step)
                v = lineSegment(self.coordinate_stack.pop().clone(), turtle.coordinate.clone())
                duration_sum += v.duration
                if duration_sum > self.max_duration * 4:
                    duration_sum = 0
                    v.new_track = True
                n = Node(v, None)
                self.tree.treeLists[0].append(n)
                self.coordinate_stack.append(turtle.coordinate.clone())
            if "l" in command:
                turtle.left(self.angle)
            if "r" in command:
                turtle.right(self.angle)
        for i in range(self.tree.depth):
            if i != 0:
                children = []
                for node in self.tree.treeLists[i-1].nodes:
                    children.append(node)
                    if len(children) == self.kids:
                        parent = Node(lineSegment(children[0].value.coordinate_1.clone(),children[self.kids - 1].value.coordinate_2.clone()),children)
                        self.tree.treeLists[i].append(parent)
                        for child in children:
                            if child.value.new_track:
                                parent.value.new_track = True
                        children = []
        self.tree.treeLists.reverse()


