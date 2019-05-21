from fractal_generation.LineSegment import *
from fractal_generation.TreeList import *
from Config import *


def is_any_condition_in_command(command, conditions):
    for condition in conditions:
        if condition not in command:
            continue
        return True
    return False


def map_list_values(lst, command, mapped_values=None):
    if mapped_values is None:
        mapped_values = {}  # Python convention
    for val in lst:
        mapped_values[val] = command
    return mapped_values


def get_commands(commands, conditions):
    command_sum = 0
    for command in commands:
        if is_any_condition_in_command(command, conditions):
            command_sum += 1
    return command_sum


class TreeFiller:

    def __init__(self, tree, angle, max_duration=16):
        self.current_position = Coordinate(0, 0)
        self.coordinate_stack = []
        self.objectStack = []
        self.tree = tree
        self.angle = angle
        self.max_duration = max_duration
        self.duration_sum = 0
        self.forward_condition = ["F", "A", "B"]
        self.turn_right_condition = ["r"]
        self.turn_left_condition = ["l"]
        self.new_layer_condition = ["(N"]
        self.finished_layer_condition = [")"]
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

    def generate_nodes(self, commands, turtle, iterations):
        self.coordinate_stack.append(turtle.coordinate.clone())
        n_condition_map = map_list_values(
            self.forward_condition, get_commands(commands, self.forward_condition))
        n_condition_map = map_list_values(self.turn_left_condition,
                                          get_commands(commands, self.turn_left_condition), n_condition_map)
        n_condition_map = map_list_values(self.turn_right_condition,
                                          get_commands(commands, self.turn_right_condition), n_condition_map)
        fractal_depth = 1
        fractals = [[] for x in range(iterations+1)]     # keeps track of each sublist in each iteration

        for command in commands:
            if is_any_condition_in_command(command, self.new_layer_condition):
                fractal_depth += 1
            if is_any_condition_in_command(command, self.forward_condition):
                self.create_node(turtle, n_condition_map.get(
                    self.forward_condition[0]), fractal_depth, fractals)
                self.draw_counter += 1
            if is_any_condition_in_command(command, self.turn_left_condition):
                self.turn_left(turtle, n_condition_map.get(
                    self.turn_left_condition[0]))
                self.left_turn_counter += 1
            if is_any_condition_in_command(command, self.turn_right_condition):
                self.turn_right(turtle, n_condition_map.get(
                    self.turn_right_condition[0]))
                self.right_turn_counter += 1
            if is_any_condition_in_command(command, self.finished_layer_condition):
                for i in range(command.count(")", 0, len(command))):
                    fractal_depth -= 1
                    self.tree.treeLists[fractal_depth].append(fractals[fractal_depth])
                    fractals[fractal_depth] = []
        self.tree.treeLists.reverse()

    def create_node(self, turtle, commands_length, iters, fractals):
        colour = self.get_node_colour(commands_length)
        turtle.forward(Config.step)
        v = LineSegment(self.coordinate_stack.pop().clone(),
                        turtle.coordinate.clone(), colour)
        self.duration_sum += v.duration
        if self.duration_sum > self.max_duration * 4:
            self.duration_sum = v.duration
            v.new_track = True
        n = Node(v, None)
        for i in range(iters):
            fractals[i].append(n)
        self.coordinate_stack.append(turtle.coordinate.clone())

    def get_node_colour(self, forward_commands_length):
        current_colour = "#000000"
        number_of_colors = len(self.colour_list)

        if number_of_colors != 0:
            color_steps = math.floor(
                forward_commands_length / number_of_colors) + forward_commands_length % number_of_colors  # Number of steps before changing colour.
            if (self.draw_counter % color_steps == 0) and (len(self.colour_list) != 0):
                self.color_index += 1
            current_colour = self.colour_list[self.color_index]

        return current_colour

    def turn_left(self, turtle, commands_length):
        self.current_left_angle = int(self.angle)
        number_of_right_angles = len(self.left_angle_list)

        if number_of_right_angles != 0:
            left_angle_steps = math.floor(
                commands_length / number_of_right_angles) + commands_length % number_of_right_angles
            if (self.left_turn_counter % left_angle_steps == 0) and (len(self.left_angle_list) != 0):
                self.left_angle_index += 1
            self.current_left_angle = self.left_angle_list[self.left_angle_index]
        turtle.left(self.current_left_angle)

    def turn_right(self, turtle, commands_length):
        self.current_right_angle = int(self.angle)
        numberOfRightAngles = len(self.right_angle_list)

        if numberOfRightAngles != 0:
            rightAngleSteps = math.floor(
                commands_length / numberOfRightAngles) + commands_length % numberOfRightAngles
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
                    parent = Node(LineSegment(children[0].value.coordinate_1.clone(),
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
