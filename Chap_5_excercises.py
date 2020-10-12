# A Turtle Bar Chart

# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")

# def draw_bar(t, height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(" " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.pu()
#     t.forward(10)
#     t.pd()

    



# tess = turtle.Turtle()
# tess.color("blue", "red")
# tess.pensize(3)

# tess.pu()
# tess.bk(100)
# tess.pd()

# xs = [48, 117, 200, 240, 160, 260, 220]

# for v in xs:
#     draw_bar(tess, v)

# wn.exitonclick()

# 1) Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. 
# Write a function which is given the day number, and it returns the day name (a string).

def day_of_wk(num):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return(days[num])

print(day_of_wk(2))
print(type(day_of_wk(2)))