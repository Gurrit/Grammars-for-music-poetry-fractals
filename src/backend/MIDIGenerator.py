import random
import math
from midiutil import MIDIFile


class MIDIGenerator:

    def __init__(self):
        self.track = 0
        self.channel = 0
        self.time = 0  # In beats
        self.duration = 1  # In beats
        self.tempo = 120  # In BPM
        self.volume = 100  # 0-127, as per the MIDI standard
        self.key = 0  # c=0, c#=1, d=2 etc.
        self.reference = 60 + self.key
        self.pitch = self.reference
        self.intervalAngle = 0 # Used to determine how much the note will change
        self.MyMIDI = MIDIFile(80)  # 80 tracks are allowed
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)

    def create_midi_file(self, file_name = "turtle.mid"):
        # Create the file
        with open(file_name, "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

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
            

    def fill_track(self, tree, iteration):
        self.MyMIDI = MIDIFile(80)
        self.time = 0
        self.track = 0
        self.pitch = self.reference
        old = tree.get_layer(iteration).nodes[0].value
        for node in tree.get_layer(iteration).nodes:
            new = node.value
            delta = new.angle - old.angle
            if abs(delta) > 180:
                delta -= 360 * delta / abs(delta)
            #print("Iteration " + str(iteration) + ": " + str(new.angle) + " - " + str(old.angle) + " = " + str(delta))
            self.pitch += (delta)/30
            if abs(self.pitch - self.reference) > 24:
                self.pitch -= 24 * delta/abs(delta)
            self.to_major()
            #self.to_minor()
            #self.to_minor_harmonic()
            if new.new_track:
                self.pitch = self.reference
                self.time = 0
                self.track = self.track + 1
                self.MyMIDI.addTempo(self.track, self.time, self.tempo)
            self.MyMIDI.addNote(self.track, self.channel, self.pitch, self.time, new.duration, self.volume)
            self.time = self.time + new.duration
            old = node.value
        #print("--------------------------------------------------")

    
    def add_to_track(self, command):

        command_split = command.split(":")

        if command == "f":
            if self.time > 4 * 32 or self.pitch < self.reference - 3*12 or self.pitch > self.reference + 3*12:  # One measure is 4 beats, one octave is 12 semitones
                self.pitch = self.reference
                self.time = 0
                self.track = self.track + 1
                self.MyMIDI.addTempo(self.track, self.time, self.tempo)
            self.duration = math.pow(2, random.randint(-2, 2))  # Randomise notelength
            self.pitch = self.pitch + self.intervalAngle/30 # 30 degrees = 1 semitone
            # Make the note fit into the selected scale, uncomment to choose
            #self.to_minor_harmonic()
            #self.to_major()
            self.to_minor()
            # Add the note
            self.MyMIDI.addNote(self.track, self.channel, self.pitch, self.time, self.duration, self.volume)
            self.time = self.time + self.duration # Move position in the track to the end of the note just added
            self.intervalAngle = 0
        elif command_split[0] == "r":
            self.intervalAngle = (self.intervalAngle - int(command_split[1]))
        elif command_split[0] == "l":
            self.intervalAngle = (self.intervalAngle + int(command_split[1]))
