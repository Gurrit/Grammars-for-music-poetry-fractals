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
        self.scale_rule = ""
        self.MyMIDI = MIDIFile(80)  # 80 tracks are allowed

    def create_midi_file(self, file_name = "turtle.mid"):
        # Create the file
        print(file_name)
        with open(file_name, "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

    def fill_track(self, tree, data):
        self.new_midi(data)
        if "iteration" in data:
            iteration = data['iteration']
        for index in range(len(tree.get_layer(iteration).nodes[0])):
            old = tree.get_layer(iteration).nodes[0][index].value
        for l in tree.get_layer(iteration).nodes:
            for node in l:
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
        self.time = 0
        self.pitch = self.reference
        self.track = track
        self.MyMIDI.addTempo(track, self.time, self.tempo) 

    def add_to_track(self, old_lineSegment, new_lineSegment):
        delta = round(new_lineSegment.angle - old_lineSegment.angle)
        if abs(delta) > 180:
            delta -= 360 * delta / abs(delta)
        self.pitch += int((delta)/30)
        if abs(self.pitch - self.reference) > 24:
            self.pitch -= 24 * (self.pitch - self.reference)/abs(self.pitch - self.reference)
        if new_lineSegment.new_track:
            self.begin_track(self.track + 1)
        self.to_scale()
        self.MyMIDI.addNote(self.track, self.channel, int(self.pitch), self.time, new_lineSegment.duration, self.volume)
        self.time = self.time + new_lineSegment.duration

# Scale related

    def set_scale(self, data):
        keys = {"c":0, "c#":1, "d":2, "d#":3, "e":4, "f":5, "f#":6, "g":7, "g#":8, "a":9, "a#":10, "b":11}
        if "data" in data:
            scale = data['data'].split()
            self.key = keys[scale[0]]
            self.reference = 60 + self.key
            self.scale_rule = scale[1]
        else:
            self.key = keys['c']
            self.scale_rule = "minor"

    def to_scale(self):
        if self.scale_rule == "major":
            self.fit_pitch([0,2,4,5,7,9,11])
        elif self.scale_rule == "minor":
            self.fit_pitch([0,2,3,5,7,8,10])
        elif self.scale_rule == "minor_harmonic":
            self.fit_pitch([0,2,3,5,7,8,11])
        elif self.scale_rule == "major_pentatonic":
            self.fit_pitch([0,2,4,7,9])
        elif self.scale_rule == "minor_pentatonic":
            self.fit_pitch([0,3,5,7,10])
        elif self.scale_rule == "blues":
            self.fit_pitch([0,3,5,6,7,10])

    def fit_pitch(self, allowed_tones=range(12)):
        i = 0
        while ((self.pitch - self.key) % 12) not in allowed_tones:
            if ((self.pitch - (i+1) - self.key) % 12) in allowed_tones:
                self.pitch -= i+1
            elif ((self.pitch + (i+1) - self.key) % 12) in allowed_tones:
                self.pitch += i+1
            i += 1