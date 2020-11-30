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

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()


# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights """
#     tess.pensize(3)
#     tess.color("black", "darkgrey")
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(200)
#     tess.circle(40, 180)
#     tess.forward(200)
#     tess.left(90)
#     tess.end_fill()


# draw_housing()

# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")

# # A traffic light is a kind of state machine with three states,
# # Green, Orange, Red.  We number these states 0, 1, 2
# #  When the machine changes state, we change tess' position and her fillcolor

# # This variable holds the current state of the machine
# state_num = 0


# def advance_state_machine():
#     global state_num
#     if state_num == 0:
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1:
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else:
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0


# wn.onkey(advance_state_machine, "space")

# wn.listen()
# turtle.Screen().exitonclick()
# wn.mainloop()


#  10.6 Exercises

# 1) Add some new key bindings to the first sample program:

# Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
# Pressing keys + or - should increase or decrease the width of tess’ pen.
# Ensure that the pen size stays between 1 and 20 (inclusive).


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


# def t_red():
#     tess.color("red")


# def t_green():
#     tess.color("green")


# def t_blue():
#     tess.color("blue")


# def twu():
#     size = tess.width()
#     increase = size + 1
#     while size <= 20:
#         tess.width(increase)


# def twd():
#     size = tess.width()
#     decrease = size - 1
#     while size > 1:
#         tess.width(decrease)


# def shapey():
#     screen = turtle.Screen()
#     sides = screen.textinput(
#         "would you like to make a line?", "enter num of sides 1-9: ")
#     for i in range(int(sides)):
#         tess.forward(20)
#         tess.left(20)
#     turtle.listen()


# def h4():
#     wn.bye()                        # Close down the turtle window


# # These lines "wire up" keypresses to the handlers we've defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
# wn.onkey(t_red, "r")
# wn.onkey(t_green, "g")
# wn.onkey(t_blue, "b")
# wn.onkey(twu, '+')
# wn.onkey(twd, "-")
# wn.onkey(shapey, "1")


# # Now we need to tell the window to start listening for events,
# # If any of the keys that we're monitoring is pressed, its
# # handler will be called.
# wn.listen()
# wn.exitonclick()
# wn.mainloop()


# 2 Change the traffic light program so that changes occur automatically,
#   driven by a timer.

# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Tess becomes a traffic light!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()


# def draw_housing():
#     """ Draw a nice housing to hold the traffic lights """
#     tess.pensize(3)
#     tess.color("black", "darkgrey")
#     tess.begin_fill()
#     tess.forward(80)
#     tess.left(90)
#     tess.forward(200)
#     tess.circle(40, 180)
#     tess.forward(200)
#     tess.left(90)
#     tess.end_fill()


# draw_housing()

# tess.penup()
# # Position tess onto the place where the green light should be
# tess.forward(40)
# tess.left(90)
# tess.forward(50)
# # Turn tess into a big green circle
# tess.shape("circle")
# tess.shapesize(3)
# tess.fillcolor("green")

# # A traffic light is a kind of state machine with three states,
# # Green, Orange, Red. We number these states 0, 1, 2
# # When the machine changes state, we change tess' position and
# # her fillcolor.

# # This variable holds the current state of the machine
# state_num = 0


# def advance_state_machine():
#     global state_num
#     if state_num == 0:
#         # Transition from state 0 to state 1
#         tess.forward(70)
#         tess.fillcolor("orange")
#         state_num = 1
#     elif state_num == 1:
#         tess.forward(70)
#         tess.fillcolor("red")
#         state_num = 2
#     else:
#         tess.back(140)
#         tess.fillcolor("green")
#         state_num = 0

# #  Bind the event handler to the timer key.
#     wn.ontimer(advance_state_machine, 2000)


# advance_state_machine()
# # wn.listen()
# wn.mainloop()


# In an earlier chapter we saw two turtle methods, hideturtle and showturtle
# that can hide or show a turtle. This suggests that we could take a different
# approach to the traffic lights program. Add to your program above as follows:
# draw a second housing for another set of traffic lights. Create three separate turtles
# to represent each of the green, orange and red lights, and position them appropriately
#  within your new housing. As your state changes occur, just make one of the three turtles
# visible at any time. Once you’ve made the changes, sit back and ponder some deep thoughts:
# you’ve now got two different ways to use turtles to simulate the traffic lights, and both
# seem to work. Is one approach somehow preferable to the other? Which one more closely
# resembles reality — i.e. the traffic lights in your town?


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tg = turtle.Turtle()
ty = turtle.Turtle()
tr = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tg.pensize(3)
    tg.color("black", "darkgrey")
    tg.begin_fill()
    tg.forward(80)
    tg.left(90)
    tg.forward(200)
    tg.circle(40, 180)
    tg.forward(200)
    tg.left(90)
    tg.end_fill()


draw_housing()

tg.penup()
# Position tess onto the place where the green light should be
tg.forward(40)
tg.left(90)
tg.forward(70)
# Turn tess into a big green circle
# tess.shape("circle")
tg.shapesize(3)
tg.fillcolor("green")

ty.penup()
ty.forward(40)
ty.left(90)
ty.forward(130)
ty.shapesize(3)
ty.color("yellow")

tr.penup()
tr.forward(40)
tr.left(90)
tr.forward(200)
tr.shapesize(3)
tr.color("red")


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine_t():
    global state_num
    if state_num == 0:
        tg.hideturtle()
        tr.hideturtle()
        ty.showturtle()
        # Transition from state 0 to state 1
        # tess.forward(70)
        # tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tg.hideturtle()
        tr.showturtle()
        ty.hideturtle()
        # tess.forward(70)
        # tess.fillcolor("red")
        state_num = 2
    else:
        tg.showturtle()
        tr.hideturtle()
        ty.hideturtle()
        state_num = 0

#  Bind the event handler to the timer key.
    wn.ontimer(advance_state_machine_t, 2000)


advance_state_machine_t()

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.penup()
    tess.forward(-100)
    tess.pendown()
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
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
c_state_num = 0


def advance_state_machine():
    global c_state_num
    if c_state_num == 0:
        # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        c_state_num = 1
    elif c_state_num == 1:
        tess.forward(70)
        tess.fillcolor("red")
        c_state_num = 2
    else:
        tess.back(140)
        tess.fillcolor("green")
        c_state_num = 0

#  Bind the event handler to the timer key.
    wn.ontimer(advance_state_machine, 2000)


# advance_state_machine()
# # wn.listen()
# wn.mainloop()


advance_state_machine()
# wn.listen()
wn.mainloop()
