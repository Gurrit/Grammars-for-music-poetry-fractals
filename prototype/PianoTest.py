# from browser import document, html
import turtle

gf_string = "B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B r A r B r A l B l A l B l A r B r A r B l A l B r A r B r A r B l A l B l A r B r A l B l A l B l A r B r A l B l A l B r A r B r A r B l A l B"


def main(notes):
    # print("is in main!: " + str(notes) + str(ations))
    translateNotes(notes)


def translateNotes(notess):
    # print("is in translatenotes!: " + str(notess) + str())
    array = notess.split(",")
    print(str(array))
    newArray = []
    grammarArray = []

    go_turtle(array)

# --------------------------------------- Turtle -----------------------------------------------------------
def go_turtle(grammarArrayen):
    print("doing the turtle")

    brad = turtle.Turtle()
    brad.hideturtle()
    brad.ht()
    brad.speed(0)
    # brad.penup()                #don't draw when turtle moves
    # brad.goto(-400, 190)       #move the turtle to a location
    # brad.pendown()

    rightAngle = 60
    leftAngle = 60
    for note in grammarArrayen:

        if (note == "a"):
            rightAngle = rightAngle - 5
        elif (note == "b"):
            leftAngle = leftAngle - 5
        elif (note == "c"):
            rightAngle = rightAngle + 5
        elif (note == "d"):
            leftAngle = leftAngle + 5
        elif (note == "e"):
            brad.color("blue")
        elif (note == "f"):
            brad.color("red")
        elif (note == "g"):
            brad.color("green")

            # TODO add colour list

    for command in gf_string.split(" "):
        if command == "A":
            brad.forward(10)
        elif command == "B":
            brad.forward(10)
        elif command == "r":
            brad.right(rightAngle)
        elif command == "l":
            brad.left(leftAngle)

    turtle.done()

main("a,d,f,g")