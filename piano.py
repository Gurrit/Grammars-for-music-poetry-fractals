# from browser import document, html
import turtle
 
gf_string = "F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F r F r F l F l F r F r F r F l F l F r F l F r F l F l F r F l F r F l F l F r F r F r F l F l F r F"
rightAngle = 90
leftAngle = 90
colorArray = []
rightAngleArray = []
leftAngleArray = []
 
def main(notes):
    # print("is in main!: " + str(notes) + str(ations))
    translateNotes(notes)
 
 
def translateNotes(notess):
    # print("is in translatenotes!: " + str(notess) + str())
    noteArray = notess.split(",")
    interprete_notes(noteArray)    
 
    go_turtle(noteArray)
 
# --------------------------------------- Turtle -----------------------------------------------------------
def interprete_notes(noteArray):
 
    for note in noteArray:
 
        if (note == "c"):
            rightAngleArray.append(rightAngle - 1)
        elif (note == "c#"):
            colorArray.append("#FF0000") #red
        elif (note == "d"):
            leftAngleArray.append(leftAngle - 1)
        elif (note == "d#"):
            colorArray.append("#FF8000") #orange
        elif (note == "e"):
            rightAngleArray.append(rightAngle + 1)
        elif (note == "f"):
            colorArray.append("#FFFF00") #yellow
        elif (note == "f#"):
            leftAngleArray.append(leftAngle + 1)
        elif (note == "g"):
            colorArray.append("#80FF00") #bright green
        elif (note == "g#"):
            rightAngleArray.append(rightAngle - 2)
        elif (note == "a"):
            colorArray.append("#00FF00") #green
        elif (note == "a#"):
            leftAngleArray.append(leftAngle - 2)
        elif (note == "b"):
            colorArray.append("#00FF80") #turqouise
        if (note == "highc"):
            rightAngleArray.append(rightAngle + 29)
        elif (note == "highc#"):
            colorArray.append("#00FFFF") #baby blue
        elif (note == "highd"):
            leftAngleArray.append(leftAngle + 2)
        elif (note == "highd#"):
            colorArray.append("#0080FF") #bright blue
        elif (note == "highe"):
            rightAngleArray.append(rightAngle - 20)
        elif (note == "highf"):
            colorArray.append("#0000FF") #blue
        elif (note == "highf#"):
            leftAngleArray.append(leftAngle - 20)
        elif (note == "highg"):
            colorArray.append("#7F00FF") #purple
        elif (note == "highg#"):
            rightAngleArray.append(rightAngle + 3)
        elif (note == "higha"):
            colorArray.append("#FF00FF") #pink
        elif (note == "higha#"):
            leftAngleArray.append(leftAngle + 3)
        elif (note == "highb"):
            colorArray.append("#FF007F") #magenta

def go_turtle(grammarArrayen):

    brad = turtle.Turtle()
    brad.hideturtle()
    brad.speed(0)

    gf_commands = gf_string.split(" ")
    gf_commands_length = len(gf_commands)

    numberOfColors = len(colorArray)
    numberOfRightAngles = len(rightAngleArray)
    numberOfLeftAngles = len(leftAngleArray)

    colorSteps = gf_commands_length
    rightAngleSteps = gf_commands_length
    leftAngleSteps = gf_commands_length

    if numberOfColors != 0:
        colorSteps = gf_commands_length/numberOfColors + gf_commands_length % numberOfColors

    if numberOfRightAngles != 0:
        rightAngleSteps = gf_commands_length/numberOfRightAngles + gf_commands_length % numberOfRightAngles
    if numberOfLeftAngles != 0:
        leftAngleSteps = gf_commands_length/numberOfLeftAngles + gf_commands_length % numberOfLeftAngles

    colorIndex = 0
    rightAngleIndex = 0
    leftAngleIndex = 0

    right = 90
    left = 90

    brad.fill(True)
    for i in range(0, gf_commands_length, 1):
        if (i % colorSteps == 0) and (colorSteps != gf_commands_length):
            brad.fill(False)
            brad.color(colorArray[colorIndex])
            colorIndex += 1
            brad.fill(True)
        if (i % rightAngleSteps == 0) and (rightAngleSteps != gf_commands_length):
            print("HHELLO")
            right = rightAngleArray[rightAngleIndex]
            rightAngleIndex += 1
        if (i % leftAngleSteps == 0) and (leftAngleSteps != gf_commands_length):
            left = leftAngleArray[leftAngleIndex]
            leftAngleIndex += 1

        if (gf_commands[i] == "A") or (gf_commands[i] == "B") or (gf_commands[i] == "F"):
            brad.forward(3)
        elif gf_commands[i] == "r":
            brad.right(right)
        elif gf_commands[i] == "l":
            brad.left(left)

    brad.fill(False)

    turtle.done()
 
main("c#,d#,g,highe,highf#, highc")