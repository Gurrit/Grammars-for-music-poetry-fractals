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
        self.reference = 72 + self.key
        self.pitch = self.reference
        self.intervalAngle = 0 # Used to determine how much the note will change
        self.MyMIDI = MIDIFile(80)  # 20 tracks are allowed
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)

    def create_midi_file(self):
        # Create the file
        with open("turtle.mid", "wb") as output_file:
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
        elif command_split[0] == "r":
            self.intervalAngle = (self.intervalAngle - int(command_split[1]))
        elif command_split[0] == "l":
            self.intervalAngle = (self.intervalAngle + int(command_split[1]))
