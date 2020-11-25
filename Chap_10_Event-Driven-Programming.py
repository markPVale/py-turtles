#  Keypress Events

import turtle

# turtle.setup(400, 500)                # Determine the window size
# wn = turtle.Screen()                 # Get a reference to the window
# wn.title("Handling keypresses!")     # Change the window title
# wn.bgcolor("lightgreen")             # Set the background color
# tess = turtle.Turtle()               # Create our favorite turtle

# # The next four functions are our "event handlers".


# def h1():
#     tess.forward(30)


# def h2():
#     tess.left(45)


# def h3():
#     tess.right(45)


# def h4():
# wn.bye()                        # Close down the turtle window


# # These lines "wire up" keypresses to the handlers we've defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")

# # Now we need to tell the window to start listening for events,
# # If any of the keys that we're monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.mainloop()


#  10.2 Mouse Events
#  Mouse events receive the x,y coordinates of the mouse's cursor posittion


# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("How to handle mouse clicks on the window!")
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)
# tess.shape("circle")


# def h1(x, y):
#     wn.title("Got click at coords {0}, {1}".format(x, y))
#     tess.goto(x, y)


# wn.onclick(h1)  # Wire up a click on the window.
# wn.mainloop()


# +++++++++++++++++++++++++++++++++++++++=
# ========================================

# multiple turtles with different parameters

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Handling mouse clicks!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.color("purple")
# alex = turtle.Turtle()
# alex.color("blue")
# alex.forward(100)


# def handler_for_tess(x, y):
#     wn.title("Tess clicked at {0}, {1}".format(x, y))
#     tess.left(42)
#     tess.forward(30)


# def handler_for_alex(x, y):
#     wn.title("Alex clicked at {0}, {1}".format(x, y))
#     alex.right(84)
#     alex.forward(50)


# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)

# wn.mainloop()


# 10.3 Automatic Events From A Timer

# import turtle

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Using a timer")
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)


# def h1():
#     tess.forward(100)
#     tess.left(56)


# wn.ontimer(h1, 2000)
# wn.mainloop()


# Restarting The Timer From The Handler:

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Using a timer to get events!")
# wn.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.color("purple")


# def h1():
#     tess.forward(100)
#     tess.left(56)
#     wn.ontimer(h1, 60)


# h1()
# turtle.Screen().exitonclick()
# wn.mainloop()


#  10.4 An Example: State Machines:

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states 0, 1, 2
#  When the machine changes state, we change tess' position and her fillcolor

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0


wn.onkey(advance_state_machine, "space")

wn.listen()
turtle.Screen().exitonclick()
wn.mainloop()
