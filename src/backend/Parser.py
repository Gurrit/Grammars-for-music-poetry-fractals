from init import *
from GFFileReader import *
from config import *
from MIDIGenerator import *
from treeList import *
from lineSegment import *
from treeFiller import *
import turtle
from HiddenTurtle import *


class Parser:

    def __init__(self):
        self._turtle_map = {}
        self.tree = TreeList()
        self.angle = 0
        self.kids = 0
        self.trees = {}

    #def parse(self):
    #    self.parser_for_midi()

    #        self.parse_for_turtle()

    def parser_for_midi(self, tree, iteration):
        generator = MIDIGenerator()
        generator.fill_track(tree, iteration)
        generator.create_midi_file("./midi-files/fractal_music.mid")

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
                            + ";" + str(i.value.coordinate_2.x) + ", " + str(i.value.coordinate_2.y))
        return commands
