import random
import math
from midiutil import MIDIFile


class MIDIGenerator:

    def __init__(self):
        self.track = 0
        self.channel = 0
        self.time = 0  # In beats
        self.tempo = 120  # In BPM
        self.volume = 100  # 0-127, as per the MIDI standard
        self.key = 0  # c=0, c#=1, d=2 etc.
        self.reference = 60 + self.key
        self.pitch = self.reference
        self.scale_rule = "minor"
        self.MyMIDI = MIDIFile(80)  # 80 tracks are allowed

    def create_midi_file(self, file_name = "turtle.mid"):
        # Create the file
        with open(file_name, "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

    def fill_track(self, tree, data):
        self.new_midi(data)
        if "iteration" in data:
            iteration = data['iteration']
        old = tree.get_layer(iteration).nodes[0].value
        for node in tree.get_layer(iteration).nodes:
            new = node.value
            self.add_to_track(old, new)
            old = node.value


# ======================================== HELP METHODS ======================================== #

# Modifying midis

    def new_midi(self, data):
        self.set_scale(data)
        self.MyMIDI = MIDIFile(80)
        self.begin_track(0)

    def begin_track(self, track):
        self.pitch = self.reference
        self.time = 0
        self.track = track
        self.MyMIDI.addTempo(track, self.time, self.tempo) 

    def add_to_track(self, old_lineSegment, new_lineSegment):
        delta = new_lineSegment.angle - old_lineSegment.angle
        if abs(delta) > 180:
            delta -= 360 * delta / abs(delta)
        self.pitch += int((delta)/30)
        if abs(self.pitch - self.reference) > 24:
            self.pitch -= 24 * delta/abs(delta)
        if new.new_track:
            self.begin_track(self.track + 1)
        self.to_scale()
        self.MyMIDI.addNote(self.track, self.channel, self.pitch, self.time, new.duration, self.volume)
        self.time = self.time + new.duration

# Scale related

    def set_scale(self, data):
        keys = {"c":0, "c#":1, "d":2, "d#":3, "e":4, "f":5, "f#":6, "g":7, "g#":8, "a":9, "a#":10, "b":11}
        if "scale" in data:
            scale = data['scale'].split()
            self.key = keys[scale[0]]
            self.scale_rule = scale[1]
        else:
            self.key = keys['c']
            self.scale_rule = "minor"

    def to_scale(self):
        if self.scale_rule == "major":
            self.to_major()
        elif self.scale_rule == "minor":
            self.to_minor()
        elif self.scale_rule == "minor_harmonic":
            self.to_minor_harmonic()

    def to_minor_harmonic(self):
        if (self.pitch - 1) % 12 == self.key or (self.pitch - 4) % 12 == self.key or (self.pitch - 6) % 12 == self.key or (self.pitch - 9) % 12 == self.key:
            self.pitch = self.pitch - 1
        if (self.pitch + 2) % 12 == self.key:
            self.pitch = self.pitch + 1

    def to_major(self):
        if (self.pitch - 1) % 12 == self.key or (self.pitch - 3) % 12 == self.key or (self.pitch - 6) % 12 == self.key or (self.pitch - 8) % 12 == self.key or (self.pitch - 10) % 12 == self.key:
            self.pitch = self.pitch - 1

    def to_minor(self):
        if (self.pitch - 1) % 12 == self.key or (self.pitch - 4) % 12 == self.key or (self.pitch - 6) % 12 == self.key or (self.pitch - 9) % 12 == self.key or (self.pitch - 11) % 12 == self.key:
            self.pitch = self.pitch - 1
