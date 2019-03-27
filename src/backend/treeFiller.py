from lineSegment import *
from treeList import *
from config import *


class treeFiller:

    def __init__(self, tree, angle, kids):
        self.current_position = coordinate(0,0)
        self.coordinate_stack = []
        self.objectStack = []
        self.tree = tree
        self.angle = angle
        self.kids = kids

    def generate_nodes(self, commands, turtle, iteration): #self, commands, turtle, filler, iteration):
        self.coordinate_stack.append(turtle.coordinate.clone())
        for command in commands:
            if "F" in command:
                turtle.forward(config.step)
                v = lineSegment(self.coordinate_stack.pop().clone(), turtle.coordinate.clone())
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
                        self.tree.treeLists[i].append(Node(lineSegment(children[0].value.coordinate_1.clone(),children[self.kids - 1].value.coordinate_2.clone()),children))
                        children = []
        
        self.tree.treeLists.reverse()

