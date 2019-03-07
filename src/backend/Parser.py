from init import *
from GFFileReader import *
from config import *
from MIDIGenerator import *
from treeList import *
from lineSegment import *
import turtle

class Parser:

    def __init__(self, turtle):
        #self._turtle = turtle
        self._turtle_map = {}
        self.tree = TreeList()
        self.angle = 0

    def parse(self):
        self.parser_for_midi()
        self.parse_for_turtle()

    def parser_for_midi(self):
        generator = MIDIGenerator()

        file_reader = GFFileReader()
        commands = file_reader.read_gf_file()

        for command in commands:
            generator.add_to_track(command)

        generator.create_midi_file()

    def parse_for_turtle(self):
        init.get_instance().set_turtle(self._turtle)
        self._turtle_map = init.get_instance().get_visualization_map()

        file_reader = GFFileReader()
        commands = file_reader.read_gf_file()

        for command in commands:
            # Command form: Forward 'f', right 'r:angle', left 'l:angle'
            if command is "f":
                self._turtle_map.get(command)(config.step)
            else:
                command_split = command.split(":")
                angle = command_split[1]
                self._turtle_map.get(command_split[0])(int(angle))

        turtle.done()

    def fill_tree(self):

        file_reader = GFFileReader()
        filler = treeFiller()
        commands = file_reader.read_gf_file()

        for command in commands:
            if command is "f":
            

            if "ang" is in command:
                self.angle = command.split(":")[1]

            




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