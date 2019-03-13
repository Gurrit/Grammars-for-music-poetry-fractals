# from browser import document, html
import turtle
 
gf_string = "B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B"
rightAngle = 60
leftAngle = 60
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
            rightAngleArray.append(rightAngle + 2)
        elif (note == "highc#"):
            colorArray.append("#00FFFF") #baby blue
        elif (note == "highd"):
            leftAngleArray.append(leftAngle + 2)
        elif (note == "highd#"):
            colorArray.append("#0080FF") #bright blue
        elif (note == "highe"):
            rightAngleArray.append(rightAngle - 3)
        elif (note == "highf"):
            colorArray.append("#0000FF") #blue
        elif (note == "highf#"):
            leftAngleArray.append(leftAngle - 3)
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
    #print("doing the turtle")
 
    brad = turtle.Turtle()
    brad.hideturtle()
    brad.speed(0)
    # brad.penup()                #don't draw when turtle moves
    # brad.goto(-400, 190)       #move the turtle to a location
    # brad.pendown() 

    gf_commands = gf_string.split(" ")

    numberOfColors = len(colorArray)
    numberOfRightAngles = len(rightAngleArray)
    numberOfLeftAngles = len(leftAngleArray)
    colorSteps = len(gf_commands)/numberOfColors + len(gf_commands)%numberOfColors
    rightAngleSteps = len(gf_commands)/numberOfRightAngles + len(gf_commands)%numberOfRightAngles
    leftAngleSteps = len(gf_commands)/numberOfLeftAngles + len(gf_commands)%numberOfLeftAngles

    colorIndex = 0
    rightAngleIndex = 0
    leftAngleIndex = 0

    brad.fill(True)
    for i in range(0, len(gf_commands), 1):
        if i%colorSteps==0:
            brad.fill(False)
            brad.color(colorArray[colorIndex])
            colorIndex += 1
            brad.fill(True)
        if i%rightAngleSteps==0:
            rightAngle = rightAngleArray[rightAngleIndex]
            rightAngleIndex += 1
        if i%leftAngleSteps==0:
            leftAngle = leftAngleArray[leftAngleIndex]
            leftAngleIndex += 1
        
        if gf_commands[i] == "A":
            brad.forward(10)
        elif gf_commands[i] == "B":
            brad.forward(10)
        elif gf_commands[i] == "r":
            brad.right(rightAngle)
        elif gf_commands[i] == "l":
            brad.left(leftAngle)

    brad.fill(False)     
 
    turtle.done()
 
main("c,e,f,a#,higha,highc#,highg#,higha#")