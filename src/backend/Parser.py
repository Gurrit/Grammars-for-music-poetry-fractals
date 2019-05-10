from fractal_generation.TreeSearcher import TreeSearcher
from utils.MIDIGenerator import *
from fractal_generation.TreeFiller import *
from fractal_generation.HiddenTurtle import *
from utils.GFFileReader import *
from utils.GenerationUtils import *
import time


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

    def parser_for_midi(self, tree, data):
        generator = MIDIGenerator()
        generator.fill_track(tree, data)
        generator.create_midi_file(generate_midi_name(data))

    def fill_tree(self, filename, name=None):
        turtle = HiddenTurtle()
        self.tree = TreeList()
        commands = read_gf_file(filename)
        if "S" in commands[0]:  # Fix this to not be hardcoded
            self.tree.add_new_iteration(int(commands[0].split(":")[1]))
        if "ang" in commands[1]:
            self.angle = int(commands[1].split(":")[1])
        if "kids" in commands[2]:
            self.kids = int(commands[2].split(":")[1])
        filler = TreeFiller(self.tree, self.angle, self.kids)
        filler.add_modification_lists(
            self.colours, self.left_angles, self.right_angles)
        filler.generate_nodes(commands, turtle, int(commands[0].split(":")[1]))
        if name is not None:
            self.trees[name] = self.tree
        return self.tree

    def parse_for_web(self, name, file, modified):
        t1 = (time.time())
        self.tree = self.trees.get(name)
        if self.tree is None or modified:
            self.fill_tree(file, name)
        commands = [i.value for i in self.tree.treeLists[len(self.tree.treeLists) - 1].nodes]
        print(time.time() - t1)
        # if these are removed, some very cool results can be had.
        self.colours = []
        self.right_angles = []
        self.left_angles = []
        return commands

    def find_iteration(self, filename, coord, filename2):
        tree = self.trees.get(filename)
        tree2 = self.trees.get(filename2)
        searcher = TreeSearcher(tree)
        c = coord.split(",")
        x = int(''.join([i for i in c[0] if i.isdigit()]))
        y = int(''.join([i for i in c[1] if i.isdigit()]))
        from_layer = searcher.closest_iteration(Coordinate(x, y))
        print("from_layer: " + from_layer.to_string())
        print("from_layer: " + str(from_layer.layerIndex))

        layer = tree2.get_layer(tree2.depth - from_layer.layerIndex - 1)
        commands = [i.value for i in layer.nodes]
        origin_commands = [i.value for i in from_layer.nodes]
        print("layer: " + str(layer.layerIndex))
        print("layer: " + layer.to_string())
        return [commands, origin_commands]

    def add_modification_lists(self, colours, left_angles, right_angles):
        self.colours = colours
        self.left_angles = left_angles
        self.right_angles = right_angles
