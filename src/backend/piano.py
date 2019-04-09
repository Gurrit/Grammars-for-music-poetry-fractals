# from browser import document, html
#import turtle

class Piano:

    def __init__(self):
        # gf_string = "F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F"
        self.rightAngle = 90
        self.leftAngle = 90
        self.colorArray = []
        self.rightAngleArray = []
        self.leftAngleArray = []
 
# def main(notes):
#     # print("is in main!: " + str(notes) + str(ations))
#     translateNotes(notes)
#
#
# def translateNotes(notess):
#     # print("is in translatenotes!: " + str(notess) + str())
#     noteArray = notess.split(",")
#     interprete_notes(noteArray)
 
    #go_turtle(noteArray)
 
# --------------------------------------- Turtle -----------------------------------------------------------
    def interprete_notes(self, notes):
        note_array = notes.split(",")

        print("PIANO NOTES: " + str(note_array))
        index = 0

        for note in note_array:

            index += 1

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

        print("PIANOINDEX: " + str(index))

    def reset_drawing_arrays(self):
        del self.colorArray[:]
        del self.rightAngleArray[:]
        del self.leftAngleArray[:]


#def go_turtle(grammarArrayen):

#    brad = turtle.Turtle()
 #   brad.hideturtle()
  #  brad.speed(0)

   # gf_commands = gf_string.split(" ")
    #gf_commands_length = len(gf_commands)

    #numberOfColors = len(colorArray)
    #print("Number of colors:" + str(numberOfColors))
    #numberOfRightAngles = len(rightAngleArray)
    #print("Number of right angles:" + str(numberOfRightAngles))
    #numberOfLeftAngles = len(leftAngleArray)
    #print("Number of left angles:" + str(numberOfLeftAngles))

    #colorSteps = gf_commands_length
    #rightAngleSteps = gf_commands_length
    #leftAngleSteps = gf_commands_length

    #if numberOfColors != 0:
     #   colorSteps = gf_commands_length/numberOfColors + gf_commands_length % numberOfColors
      #  print("Color steps:" + str(colorSteps))

    #if numberOfRightAngles != 0:
     #   rightAngleSteps = gf_commands_length/numberOfRightAngles + gf_commands_length % numberOfRightAngles
      #  print("Right angle steps:" + str(rightAngleSteps))
    #if numberOfLeftAngles != 0:
     #   leftAngleSteps = gf_commands_length/numberOfLeftAngles + gf_commands_length % numberOfLeftAngles
      #  print("Left angle steps:" + str(leftAngleSteps))

    #colorIndex = 0
    #rightAngleIndex = 0
    #leftAngleIndex = 0

    #brad.fill(True)
    #for i in range(0, gf_commands_length, 1):
     #   if (i % colorSteps == 0) and (len(colorArray) != 0):
      #      brad.fill(False)
       #     brad.color(colorArray[colorIndex])
        #    colorIndex += 1
         #   brad.fill(True)
          #  print("Color index:" + str(colorIndex))
        #if (i % rightAngleSteps == 0) and (len(rightAngleArray) != 0):
         #   rightAngle = rightAngleArray[rightAngleIndex]
          #  rightAngleIndex += 1
           # print("Right angle index:" + str(rightAngleIndex))
        #elif len(rightAngleArray) == 0:
         #   rightAngle = 90
        #if (i % leftAngleSteps == 0) and (len(leftAngleArray) != 0): 
         #   leftAngle = leftAngleArray[leftAngleIndex]
          #  leftAngleIndex += 1
           # print("Left angle index:" + str(leftAngleIndex))
        #elif len(leftAngleArray) == 0:
         #   leftAngle = 90

        #if (gf_commands[i] == "A") or (gf_commands[i] == "B") or (gf_commands[i] == "F"):
         #   brad.forward(3)
        #elif gf_commands[i] == "r":
         #   brad.right(rightAngle)
        #elif gf_commands[i] == "l":
         #   brad.left(leftAngle)

    #brad.fill(False)

    #turtle.done()
 
#main("c#,d#,g,highc,highf#")