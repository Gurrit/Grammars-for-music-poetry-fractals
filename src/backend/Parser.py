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

    def parse(self):
        self.parser_for_midi()
#        self.parse_for_turtle()

    def parser_for_midi(self):
        generator = MIDIGenerator()

        file_reader = GFFileReader()
        commands = file_reader.read_gf_file()

        for command in commands:
            generator.add_to_track(command)

        generator.create_midi_file()

#    def parse_for_turtle(self):
#        init.get_instance().set_turtle(self._turtle)
#        self._turtle_map = init.get_instance().get_visualization_map()

#        file_reader = GFFileReader()
#        commands = file_reader.read_gf_file()

#        for command in commands:
            # Command form: Forward 'f', right 'r:angle', left 'l:angle'
#            if command is "f":
#                self._turtle_map.get(command)(config.step)
#            else:
#                command_split = command.split(":")
#                angle = command_split[1]
#                self._turtle_map.get(command_split[0])(int(angle))

#        turtle.done()

    def fill_tree(self):
        turtle = HiddenTurtle()
        file_reader = GFFileReader()
        commands = file_reader.read_gf_file()
        #while "(N" not in commands:
        if "S" in commands[0]:
            self.tree.add_new_iteration(int(commands[0].split(":")[1]))
        if "ang" in commands[1]:
            self.angle = int(commands[1].split(":")[1])
        if "kids" in commands [2]:
            self.kids = int(commands[2].split(":")[1])
        filler = treeFiller(self.tree, self.angle, self.kids)
        filler.generate_nodes(commands, turtle, int(commands[0].split(":")[1]))
        return self.tree

    
    #def generate_nodes(self, commands, turtle, filler, iteration):
    #    nodes = []
    #    map = init.get_instance().get_filler_map()
    #    distance = config.step
    #    while ")" not in commands[0]:       # This should be reversed, and taken from the end of the list, for likely
            # performance reasons
    #        if "F" in commands[0]:
    #            turtle.forward(distance)
    #            nodes.append(Node(lineSegment(turtle.coordinate, filler.coordinate_stack.pop()), None))
    #        elif "r" in commands[0]:
    #            turtle.right(self.angle)
    #        elif "l" in commands[0]:
    #            turtle.left(self.angle)
    #        elif "(N" in commands[0]:
    #            iteration = commands.split(":", 1)[1]
    #            (remaining, layer_below) = self.generate_nodes(commands, turtle, filler, iteration)
    #            commands = remaining
    #        commands = commands.pop(0)
    #    return commands, nodes


#parser = Parser(turtle.Turtle())
#parser.parse()


def parse_for_web():
    init.get_instance()
    turtle_map = init.get_instance().get_web_map()

    file_reader = GFFileReader()
    commands = file_reader.read_gf_file()
    web_commands = []
    for command in commands:
        # Command form: Forward 'f', right 'r:angle', left 'l:angle'
        if command is "f":
            web_commands.append(turtle_map.get(command)(config.step))
        else:
            command_split = command.split(":")
            angle = command_split[1]
            web_commands.append(turtle_map.get(command_split[0])(int(angle)))
    return web_commands