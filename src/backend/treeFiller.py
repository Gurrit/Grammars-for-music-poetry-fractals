from lineSegment import *
from treeList import *
from config import *


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
        self.forward_condition = ["F", "A", "B"]
        self.turn_right_condition = ["r"]
        self.turn_left_condition = ["l"]

        # For changing the appearance of the drawn fractal,
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

    # This method is really slow. Takes over 100 seconds on the server to run on sierpinski 7
    def generate_nodes(self, commands, turtle, iteration): #self, commands, turtle, filler, iteration):
        self.coordinate_stack.append(turtle.coordinate.clone())
        duration_sum = 0
        for command in commands:

            if self.is_any_condition_in_command(command, self.forward_condition):
                self.create_node(turtle, self.get_commands(commands, self.forward_condition))
                self.draw_counter += 1
            if self.is_any_condition_in_command(command, self.turn_left_condition):
                self.turn_left(turtle, self.get_commands(commands, self.turn_left_condition))
                self.left_turn_counter += 1
            if self.is_any_condition_in_command(command, self.turn_right_condition):
                self.turn_right(turtle, self.get_commands(commands, self.turn_right_condition))
                self.right_turn_counter += 1

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


    def get_commands(self, commands, conditions):
        command_sum = 0
        for command in commands:
            if self.is_any_condition_in_command(command, conditions):
                command_sum += 1
        return command_sum

    def is_any_condition_in_command(self, command, conditions):
        for condition in conditions:
            if condition not in command:
                continue
            return True
        return False

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
        current_colour = "#FFFFFF"
        numberOfColors = len(self.colour_list)

        if numberOfColors != 0:
            colorSteps = math.floor(forward_commands_length / numberOfColors) + forward_commands_length % numberOfColors # Number of steps before changing colour.
            if (self.draw_counter % colorSteps == 0) and (len(self.colour_list) != 0):
                self.color_index += 1
            current_colour = self.colour_list[self.color_index]

        return current_colour

    def turn_left(self, turtle, commands_length):
        self.current_left_angle = int(self.angle)
        numberOfRightAngles = len(self.left_angle_list)

        if numberOfRightAngles != 0:
            leftAngleSteps = math.floor(commands_length / numberOfRightAngles) + commands_length % numberOfRightAngles
            # print("LEFTANGLESTEPS: " + str(leftAngleSteps) + "TURN COUNTER: " + str(self.left_turn_counter))
            if (self.left_turn_counter % leftAngleSteps == 0) and (len(self.left_angle_list) != 0):
                # print("Left loop inside")
                self.left_angle_index += 1
            self.current_left_angle = self.left_angle_list[self.left_angle_index]
            # print("CURRENT LEFT ANGLE: " + str(self.current_left_angle))
        turtle.left(self.current_left_angle)

    def turn_right(self, turtle, commands_length):
        self.current_right_angle = int(self.angle)
        numberOfRightAngles = len(self.right_angle_list)

        if numberOfRightAngles != 0:
            rightAngleSteps = math.floor(commands_length / numberOfRightAngles) + commands_length % numberOfRightAngles
            # print("RIGHTANGLESTEPS: " + str(rightAngleSteps) + "TURN COUNTER: " + str(self.right_turn_counter))
            if (self.right_turn_counter % rightAngleSteps == 0) and (len(self.right_angle_list) != 0):
                # print("RIGHT loop inside")
                self.right_angle_index += 1
            self.current_right_angle = self.right_angle_list[self.right_angle_index]
            # print("CURRENT RIGHT ANGLE: " + str(self.current_right_angle))
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
