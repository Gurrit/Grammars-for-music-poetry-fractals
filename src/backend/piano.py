class Piano:

    def __init__(self):
        # gf_string = "F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F"
        self.rightAngle = 0
        self.leftAngle = 0
        self.colorArray = []
        self.rightAngleArray = []
        self.leftAngleArray = []
 
# --------------------------------------- Turtle -----------------------------------------------------------
    def interpret_notes(self, notes, angle):
        note_array = notes.split(",")
        self.rightAngle = int(angle)
        self.leftAngle = int(angle)

        for note in note_array:
            if (note == "c"):
                self.rightAngleArray.append(self.rightAngle - 1)
            elif (note == "c#"):
                self.colorArray.append("#FF0000") #red
            elif (note == "d"):
                self.leftAngleArray.append(self.leftAngle - 1)
            elif (note == "d#"):
                self.colorArray.append("#FF8000") #orange
            elif (note == "e"):
                self.rightAngleArray.append(self.rightAngle + 1)
            elif (note == "f"):
                self.colorArray.append("#FFFF00") #yellow
            elif (note == "f#"):
                self.leftAngleArray.append(self.leftAngle + 1)
            elif (note == "g"):
                self.colorArray.append("#80FF00") #bright green
            elif (note == "g#"):
                self.rightAngleArray.append(self.rightAngle - 2)
            elif (note == "a"):
                self.colorArray.append("#00FF00") #green
            elif (note == "a#"):
                self.leftAngleArray.append(self.leftAngle - 2)
            elif (note == "b"):
                self.colorArray.append("#00FF80") #turqouise
            if (note == "highc"):
                self.rightAngleArray.append(self.rightAngle + 2)
            elif (note == "highc#"):
                self.colorArray.append("#00FFFF") #baby blue
            elif (note == "highd"):
                self.leftAngleArray.append(self.leftAngle + 2)
            elif (note == "highd#"):
                self.colorArray.append("#0080FF") #bright blue
            elif (note == "highe"):
                self.rightAngleArray.append(self.rightAngle - 3)
            elif (note == "highf"):
                self.colorArray.append("#0000FF") #blue
            elif (note == "highf#"):
                self.leftAngleArray.append(self.leftAngle - 3)
            elif (note == "highg"):
                self.colorArray.append("#7F00FF") #purple
            elif (note == "highg#"):
                self.rightAngleArray.append(self.rightAngle + 3)
            elif (note == "higha"):
                self.colorArray.append("#FF00FF") #pink
            elif (note == "higha#"):
                self.leftAngleArray.append(self.leftAngle + 3)
            elif (note == "highb"):
                self.colorArray.append("#FF007F") #magenta

    def reset_drawing_arrays(self):
        del self.colorArray[:]
        del self.rightAngleArray[:]
        del self.leftAngleArray[:]