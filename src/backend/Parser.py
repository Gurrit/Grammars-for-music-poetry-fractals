from TreeSearcher import TreeSearcher
from GFFileReader import *
from MIDIGenerator import *
from treeFiller import *
from HiddenTurtle import *

class Parser:

    def __init__(self):
        self._turtle_map = {}
        self.tree = TreeList()
        self.angle = 0
        self.kids = 0
        self.trees = {}

        self.colours = []
        self.right_angles = []
        self.left_angles = []

    def parse(self):
        self.parser_for_midi()

    #        self.parse_for_turtle()

    def parser_for_midi(self):
        generator = MIDIGenerator()

        for i in range(self.tree.depth):
            generator.fill_track(self.tree, i)
            generator.create_midi_file("fractal_" + str(i) + ".mid")

    def fill_tree(self, filename):
        turtle = HiddenTurtle()
        self.tree = TreeList()
        file_reader = GFFileReader()
        commands = file_reader.read_gf_file(filename)
        if "S" in commands[0]:  # Fix this to not be hardcoded
            self.tree.add_new_iteration(int(commands[0].split(":")[1]))
        if "ang" in commands[1]:
            self.angle = int(commands[1].split(":")[1])
        if "kids" in commands[2]:
            self.kids = int(commands[2].split(":")[1])
        filler = treeFiller(self.tree, self.angle, self.kids)
        filler.add_modification_lists(self.colours, self.left_angles, self.right_angles)
        filler.generate_nodes(commands, turtle, int(commands[0].split(":")[1]))
        self.trees[filename] = self.tree
        return self.tree

    def parse_for_web(self, filename):
        self.tree = self.trees.get(filename)  # change the name?
        if self.tree is None:
            self.fill_tree(filename)
        commands = []
        for i in self.tree.treeLists[len(self.tree.treeLists) - 1].nodes:
            commands.append(str(i.value.coordinate_1.x) + ", " + str(i.value.coordinate_1.y)
                            + ";" + str(i.value.coordinate_2.x) + ", " + str(i.value.coordinate_2.y) + ";" + str(i.value.color))

        return commands

    def find_iteration(self, filename, coord):
        tree = self.trees.get(filename)
        searcher = TreeSearcher(tree)
        c = coord.split(",")
        x = int(''.join([i for i in c[0] if i.isdigit()]))
        y = int(''.join([i for i in c[1] if i.isdigit()]))
        layer = searcher.closest_iteration(Coordinate(x, y))
        commands = []
        for i in layer.nodes:
            commands.append(str(i.value.coordinate_1.x) + ", " + str(i.value.coordinate_1.y)
                            + ";" + str(i.value.coordinate_2.x) + ", " + str(i.value.coordinate_2.y))
        return commands

    def add_modification_lists(self, colours, left_angles, right_angles):
        self.colours = colours
        self.left_angles = left_angles
        self.right_angles = right_angles
