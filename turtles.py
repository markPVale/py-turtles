import turtle

# wn = turtle.Screen()
# alex = turtle.Turtle()

# alex.forward(50)
# alex.left(90)
# alex.forward(30)

# wn.mainloop()

# ========================================

# color_choice = input("what color would you like? ")

# wn_color = input("Please enter a screen-color choice from this list: aquamarine, bisque, cadet blue  ")

# pen_size = int(input("how thick?"))

# wn = turtle.Screen()
# wn.bgcolor(wn_color)
# wn.title("Hello, Tess!")

# tess = turtle.Turtle()


# tess.color(color_choice)
# tess.pensize(pen_size)

# tess.forward(150)
# tess.left(120)
# tess.forward(250)

# wn.mainloop()


# ================================================






#  import turtle
# wn = turtle.Screen()         # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# wn.title("Tess & Alex")

# tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)

# alex = turtle.Turtle()       # Create alex

# tess.forward(80)             # Make tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)               # Complete the triangle

# tess.right(180)              # Turn tess around
# tess.forward(80)             # Move her away from the origin

# alex.forward(50)             # Make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# wn.mainloop()


# for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     invite = "Hi " + f + "! Please come to my party on Saturday!"
#     print(invite)


# Excercises 3.8

# 1) Write a program that prints 'We like Python's turtles!' 1000x

# for i in range(1000):
#     statement = "We like Python's turtles!"
#     print(statement)


# 2) Give three attributes of your cellphone object. Give three methods of your cellphone.

# Attributes = Flat, Glass Screen, Black
# Methods = Calls, Texts, Web Browse


#3) Write a program that uses a for loop to print:
# One of the months of the year is January, etc.

# for i in ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]:
#     statement = "one of the months of the year is " + i 
#     print(statement)


#4) Suppose our turtle tess is at heading 0 — facing east. 
# We execute the statement tess.left(3645). 
# What does tess do, and what is her final heading?


# wn = turtle.Screen()
# alex = turtle.Turtle()

# alex.left(3645)

# Answer: turns around to the left 10.125 times



# 5) Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Write a loop that prints each of the numbers on a new line.
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs:
#     print(i)

# Write a loop that prints each number and its square on a new line.
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs:
#     print(i, i**2)

# Write a loop that adds all the numbers from the list into a variable called total. 
# You should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# total = 0
# for i in xs:
#     total += i
# print(total)

# Print the product of all the numbers in the list. 
# (product means all multiplied together)

# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# total = 1
# for i in xs:
#     total *= i
# print(total)


# 6) Use for loops to make a turtle draw these regular polygons 
# (regular means all sides the same lengths, all angles the same):

# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

# EQUILATERAL TRIANGLE:
# wn = turtle.Screen()
# alex = turtle.Turtle()

# inner_angles = [60, 60, 60]
# for angle in inner_angles:
#     alex.forward(250)
#     alex.left(120)

# wn.mainloop()

# =====================================

# SQUARE:
# wn = turtle.Screen()
# alex = turtle.Turtle()

# inner_angles = [45, 45, 45, 45]

# for angle in inner_angles:
#     alex.forward(250)
#     alex.left(angle * 2)

# wn.mainloop()

# =====================================

# HEXAGON
# wn = turtle.Screen()
# alex = turtle.Turtle()

# inner_angles = [60, 60, 60, 60, 60, 60]

# for angle in inner_angles:
#     alex.forward(150)
#     alex.left(angle)

# wn.mainloop()

# =====================================

# OCTAGON
# wn = turtle.Screen()
# alex = turtle.Turtle()

# inner_angles = [45, 45, 45, 45, 45, 45, 45, 45]

# for angle in inner_angles:
#     alex.forward(100)
#     alex.left(angle)

# wn.mainloop()

# 7) A drunk pirate makes a random turn and then takes 100 steps forward, 
# makes another random turn, takes another 100 steps, turns another random amount, etc. 
# A social science student records the angle of each turn before the next 100 
# steps are taken. 
# Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. 
# (Positive angles are counter-clockwise.) 
# Use a turtle to draw the path taken by our drunk friend.

# wn = turtle.Screen()
# alex = turtle.Turtle()

# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# for angle in angles:
#     if angle > 0:
#         alex.left(angle)
#         alex.forward(100)
#     else:
#         alex.right(angle)
#         alex.forward(100)

# print("The pirate's heading is: ", alex.heading())

# wn.mainloop()

# =====================================

# 9) If you were going to draw a regular polygon with 18 sides, 
# what angle would you need to turn the turtle at each corner?

wn = turtle.Screen()
alex = turtle.Turtle()

inner_angles = range(20)
for angle in inner_angles:
    alex.forward(50)
    alex.left(20)

wn.mainloop()