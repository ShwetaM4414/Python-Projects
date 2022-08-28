# Import library
from tkinter import HIDDEN, NORMAL, Tk, Canvas


# Function for toggling of the eyes
def ToggleEyes():
    # returns the value of option that is fill for lefteye
    currentColor = canvas.itemcget(lefteye, 'fill')

    # check if currentColor white or not
    if currentColor == 'white':
        newColor = canvas.body_color
    else:
        newColor = 'white'

    # returns the value of option for leftPupil
    currentState = canvas.itemcget(leftPupil, 'state')

    # check if the currentState is HIDDEN or not
    if currentState == HIDDEN:
        newState = NORMAL
    else:
        newState = HIDDEN

    # change the attributes
    canvas.itemconfigure(leftPupil, state=newState)
    canvas.itemconfigure(rightPupil, state=newState)
    canvas.itemconfigure(lefteye, fill=newColor)
    canvas.itemconfigure(rightEye, fill=newColor)


# function for blinking the eyes
def blink():
    ToggleEyes()

    # after 300 milliseconds passed it will toggle the eyes
    window.after(300, ToggleEyes)

    # after 3000 milliseconds i.e 3 seconds passed blink function will be called
    window.after(3000, blink)


# function for toggling the pupils
def TogglePupils():

    # Checks if eyes are crossed or not
    if not canvas.eyes_crossed:

        # move left pupil from one position to other
        canvas.move(leftPupil, 10, -5)

        # move right pupil from one position to other
        canvas.move(rightPupil, -10, -5)
        canvas.eyes_crossed = True
    else:
        canvas.move(leftPupil, -10, 5)
        canvas.move(rightPupil, 10, 5)
        canvas.eyes_crossed = False


# Function for toggling the Tongue
def ToggleTongue():

    # Checks if tongue out or not
    if not canvas.tongue_out:
        canvas.itemconfigure(tipTongue, state=NORMAL)
        canvas.itemconfigure(mainTongue, state=NORMAL)
        canvas.tongue_out = True
    else:
        canvas.itemconfigure(tipTongue, state=HIDDEN)
        canvas.itemconfigure(mainTongue, state=HIDDEN)
        canvas.tongue_out = False


def Cheeky(event):
    ToggleTongue()
    TogglePupils()
    HideHappy(event)
    window.after(1000, ToggleTongue)
    window.after(1000, TogglePupils)
    return


def ShowHappy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        canvas.itemconfigure(leftCheek, state=NORMAL)
        canvas.itemconfigure(rightCheek, state=NORMAL)
        canvas.itemconfigure(happyMouth, state=NORMAL)
        canvas.itemconfigure(normalMouth, state=HIDDEN)
        canvas.itemconfigure(sadMouth, state=HIDDEN)
        canvas.happy_level = 3
    return


def HideHappy(event):
    canvas.itemconfigure(leftCheek, state=HIDDEN)
    canvas.itemconfigure(rightCheek, state=HIDDEN)
    canvas.itemconfigure(happyMouth, state=HIDDEN)
    canvas.itemconfigure(normalMouth, state=NORMAL)
    canvas.itemconfigure(sadMouth, state=HIDDEN)
    return


def sad():

    # Checks if happy level is 0 or not
    if canvas.happy_level == 0:
        canvas.itemconfigure(happyMouth, state=HIDDEN)
        canvas.itemconfigure(normalMouth, state=HIDDEN)
        canvas.itemconfigure(sadMouth, state=NORMAL)
    else:
        canvas.happy_level -= 1
    window.after(5000, sad)


# Create a window
window = Tk()

# Create the widget
canvas = Canvas(window, width=400, height=400)

canvas.configure(bg='black', highlightthickness=5)

canvas.body_color = 'SteelBlue3'

# Creates a circle or an ellipse at the given coordinate
body = canvas.create_oval(35, 20, 365, 350, outline=canvas.body_color, fill=canvas.body_color)
leftEar = canvas.create_polygon(75, 80, 75, 10, 165, 70, outline=canvas.body_color, fill=canvas.body_color)
rightEar = canvas.create_polygon(255, 45, 325, 10, 320, 70, outline=canvas.body_color, fill=canvas.body_color)
leftFoot = canvas.create_oval(65, 320, 145, 360, outline=canvas.body_color, fill=canvas.body_color)
rightFoot = canvas.create_oval(250, 320, 330, 360, outline=canvas.body_color, fill=canvas.body_color)

lefteye = canvas.create_oval(130, 110, 160, 170, outline='black', fill='white')
leftPupil = canvas.create_oval(140, 145, 150, 155, outline='black', fill='black')
rightEye = canvas.create_oval(230, 110, 260, 170, outline='black', fill='white')
rightPupil = canvas.create_oval(240, 145, 250, 155, outline='black', fill='black')

normalMouth = canvas.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
happyMouth = canvas.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
sadMouth = canvas.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
mainTongue = canvas.create_rectangle(170, 250, 230, 290, outline='tomato4', fill='tomato4', state=HIDDEN)
tipTongue = canvas.create_oval(170, 285, 230, 300, outline='tomato4', fill='tomato4', state=HIDDEN)
leftCheek = canvas.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
rightCheek = canvas.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

canvas.pack()

# Bind an event handler to canvas item
canvas.bind('<Motion>', ShowHappy)
canvas.bind('<Leave>', HideHappy)
canvas.bind('<Double-1>', Cheeky)

canvas.happy_level = 10
canvas.eyes_crossed = False
canvas.tongue_out = False

window.after(1000, blink)
window.after(5000, sad)

window.mainloop()
