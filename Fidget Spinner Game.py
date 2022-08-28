# importing libraries
import turtle

# Creating turtle screen
window = turtle.Screen()

# set a background color of the turtle screen
window.bgcolor('dark grey')

# Set the size and position of the main window.
window.setup(600, 600)

# Set title of turtle window
window.title('Fidget Spinner')

# Creates and returns a new turtle object
border = turtle.Turtle()

# Set the turtle’s speed
border.speed(8)

# Set the color
border.color('black')

# Set the line thickness to width
border.width(5)

# Make the turtle invisible.
border.hideturtle()

# Creates and returns a new turtle object
text = turtle.Turtle()
text.color('black')
text.hideturtle()

sp = turtle.Turtle()
sp.color('black')
sp.width(3)
sp.hideturtle()

# initial state of spinner is null (stable)
state = {'turn': 0}
length = 120
radius = 130


# Draw fidget spinner
def spinner():
    # Delete the turtle’s drawings from the screen.
    sp.clear()

    # Angle of fidget spinner
    angle = state['turn'] / 10

    # Turns the turtle clockwise
    sp.right(angle)

    #  Moves the turtle forward by the specified amount
    sp.forward(length)
    sp.width(20)

    # Draw a circular dot with diameter size
    sp.dot(radius, 'blue')
    sp.dot(60, 'black')
    sp.back(length)
    sp.right(120)

    sp.forward(length)
    sp.width(20)
    sp.dot(radius, 'green')
    sp.dot(60, 'black')
    sp.back(length)
    sp.right(120)

    sp.forward(length)
    sp.width(20)
    sp.dot(radius, 'red')
    sp.dot(60, 'black')
    sp.back(length)
    sp.right(120)


# Flick fidget spinner
def Flick():
    # acceleration of spinner
    state['turn'] += 40


# Animate fidget spinner
def Animate():
    if state['turn']:
        state['turn'] -= 1

    spinner()

    # Ontimer calls a Animate after 20 milliseconds.
    window.ontimer(Animate, 20)


def main():
    # Pull the pen up – no drawing when moving.
    border.penup()

    # Move turtle to an absolute position.
    border.goto(-290, 290)

    # Pull the pen down – drawing when moving.
    border.pendown()

    for i in range(4):
        border.forward(575)
        border.right(90)

    sp.penup()
    sp.goto(0, 70)
    sp.pendown()

    text.penup()
    text.goto(-130, -230)
    text.pendown()
    style = ('aerial', 30, 'italic')

    # Write text at the current turtle position
    text.write('Fidget Spinner', font=style)

    # Turn turtle animation off
    window.tracer(False)

    # keyboard key for the rotation of spinner.
    window.onkey(Flick, 'space')

    # Set focus on TurtleScreen
    window.listen()
    Animate()

    turtle.done()


main()
