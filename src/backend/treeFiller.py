from lineSegment import *
from treeList import *
from config import *
from math import *


class treeFiller:

    def __init__(self, tree, angle, kids, max_duration = 32):
        self.current_position = Coordinate(0,0)
        self.coordinate_stack = []
        self.objectStack = []
        self.tree = tree
        self.angle = angle
        self.kids = kids
        self.max_duration = max_duration
        self.duration_sum = 0

        # For changing the appearance of the drawn fractal
        self.colour_list = []
        self.left_angle_list = []
        self.right_angle_list = []
        self.draw_counter = 0
        self.right_turn_counter = 0
        self.left_turn_counter = 0
        self.color_index = -1
        self.right_angle_index = -1
        self.left_angle_index = -1
        self.current_right_angle = 0
        self.current_left_angle = 0

    def generate_nodes(self, commands, turtle, iteration): #self, commands, turtle, filler, iteration):
        self.coordinate_stack.append(turtle.coordinate.clone())
        # Reset values
        self.duration_sum = 0
        self.color_index = -1
        self.draw_counter = 0
        self.right_turn_counter = 0
        self.left_turn_counter = 0
        self.right_angle_index = -1
        self.left_angle_index = -1

        for command in commands:
            if "F" in command or "A" in command or "B" in command:          #TODO Make more general
                self.create_node(turtle, self.get_forward_commands(commands))
                self.draw_counter += 1
            if "l" in command:
                self.turn_left(turtle, self.get_left_commands(commands))
                self.left_turn_counter += 1
            if "r" in command:
                self.turn_right(turtle, self.get_right_commands(commands))
                self.right_turn_counter += 1

        for i in range(self.tree.depth):
            self.add_tree_layer(i)

        self.tree.treeLists.reverse()

# ======================================== HELP METHODS ======================================== #

    def get_forward_commands(self, commands):
        command_sum = 0
        for command in commands:
            if "F" in command or "A" in command or "B" in command:          #TODO Make more general
                command_sum += 1
        return command_sum

    def get_right_commands(self, commands):
        command_sum = 0
        for command in commands:
            if "r" in command:
                command_sum += 1
        return command_sum

    def get_left_commands(self, commands):
        command_sum = 0
        for command in commands:
            if "l" in command:
                command_sum += 1
        return command_sum

    def create_node(self, turtle, commands_length):
        colour = self.get_node_colour(commands_length)

        turtle.forward(config.step)
        v = lineSegment(self.coordinate_stack.pop().clone(), turtle.coordinate.clone(), colour)
        self.duration_sum += v.duration
        if self.duration_sum > self.max_duration * 4:
            self.duration_sum = 0
            v.new_track = True
        n = Node(v, None)
        self.tree.treeLists[0].append(n)
        self.coordinate_stack.append(turtle.coordinate.clone())

    def get_node_colour(self, forward_commands_length):
        current_colour = "#000000"
        numberOfColors = len(self.colour_list)

        if numberOfColors != 0:
            colorSteps = floor(forward_commands_length / numberOfColors) + forward_commands_length % numberOfColors # Number of steps before changing colour.
            if (self.draw_counter % colorSteps == 0) and (len(self.colour_list) != 0):
                self.color_index += 1
            current_colour = self.colour_list[self.color_index]

        return current_colour

    def turn_left(self, turtle, commands_length):
        self.current_left_angle = int(self.angle)
        numberOfRightAngles = len(self.left_angle_list)

        if numberOfRightAngles != 0:
            leftAngleSteps = floor(commands_length / numberOfRightAngles) + commands_length % numberOfRightAngles
            print("LEFTANGLESTEPS: " + str(leftAngleSteps) + "TURN COUNTER: " + str(self.left_turn_counter))
            if (self.left_turn_counter % leftAngleSteps == 0) and (len(self.left_angle_list) != 0):
                print("Left loop inside")
                self.left_angle_index += 1
            self.current_left_angle = self.left_angle_list[self.left_angle_index]
            print("CURRENT LEFT ANGLE: " + str(self.current_left_angle))
        turtle.left(self.current_left_angle)

    # def turn_left(self, turtle):
    #     turtle.left(self.angle)     #TODO read from leftAngleArray

    # def turn_right(self, turtle):
    #     turtle.right(self.angle)    #TODO read from leftAngleArray

    def turn_right(self, turtle, commands_length):
        self.current_right_angle = int(self.angle)
        numberOfRightAngles = len(self.right_angle_list)

        if numberOfRightAngles != 0:
            rightAngleSteps = floor(commands_length / numberOfRightAngles) + commands_length % numberOfRightAngles
            if (self.right_turn_counter % rightAngleSteps == 0) and (len(self.right_angle_list) != 0):
                self.right_angle_index += 1
            self.current_right_angle = self.right_angle_list[self.right_angle_index]
        turtle.right(self.current_right_angle)

    def add_tree_layer(self, i):
        if i != 0:
            children = []
            for node in self.tree.treeLists[i - 1].nodes:
                children.append(node)
                if len(children) == self.kids:
                    parent = Node(lineSegment(children[0].value.coordinate_1.clone(),
                                              children[self.kids - 1].value.coordinate_2.clone()), children)
                    self.tree.treeLists[i].append(parent)
                    for child in children:
                        if child.value.new_track:
                            parent.value.new_track = True
                    children = []

    def add_modification_lists(self, colours, left_angles, right_angles):
        self.colour_list = colours
        self.left_angle_list = left_angles
        self.right_angle_list = right_angles
