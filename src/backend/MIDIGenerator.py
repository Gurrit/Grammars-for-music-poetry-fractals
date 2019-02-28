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
        self.pitch = 60 + self.key
        self.MyMIDI = MIDIFile(80)  # 20 tracks are allowed
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)
        self.direction = 0

    def create_midi_file(self):
        # Create the file
        with open("turtle.mid", "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

    def add_to_track(self, command):

        command_split = command.split(":")

        if command == "f":
            if self.direction == 1:  # Raise the pitch
                # If-satserna nedan definerar skalan
                # if ((self.pitch-4)%12 == self.key or (self.pitch+1))%12 == self.key: # dur
                if (self.pitch - 2) % 12 == self.key or (self.pitch + 1) % 12 == self.key or (
                        self.pitch - 7) % 12 == self.key:  # harmonisk moll
                    self.pitch = self.pitch + 1
                elif (self.pitch - 8) % 12 == self.key:  # harmonisk moll
                    self.pitch = self.pitch + 3
                else:
                    self.pitch = self.pitch + 2
            elif self.direction == 3:
                # if (self.pitch-5)%12 == self.key or self.pitch%12 == self.key: #dur
                if (self.pitch - 3) % 12 == self.key or (self.pitch) % 12 == self.key or (
                        self.pitch - 8) % 12 == self.key:  # harmonisk moll
                    self.pitch = self.pitch - 1
                elif (self.pitch + 1) % 12 == self.key:  # harmonisk moll
                    self.pitch = self.pitch - 3
                else:
                    self.pitch = self.pitch - 2
            else:
                # if self.pitch > 60 + 12 + self.key:
                if self.time > 4 * 32:  # One measure is 4 beats
                    self.pitch = 60 + self.key
                    self.time = 0
                    self.track = self.track + 1
                    self.MyMIDI.addTempo(self.track, self.time, self.tempo)
                    print("new track")
                # if self.pitch < 60 - 12 + self.key:
                #    self.pitch = 60 + self.key
                #    self.time = 0
                #    self.track = self.track +1
                #    self.MyMIDI.addTempo(self.track, self.time, self.tempo)
                #    print("new track")
                self.duration = math.pow(2, random.randint(-2, 2))  # Randomise notelength
                self.MyMIDI.addNote(self.track, self.channel, self.pitch, self.time, self.duration, self.volume)
                self.time = self.time + self.duration
        elif command_split[0] == "r":
            self.direction = (self.direction - 1) % 4
        elif command_split[0] == "l":
            self.direction = (self.direction + 1) % 4
