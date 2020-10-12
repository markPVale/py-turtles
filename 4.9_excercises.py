# import turtle

# def make_screen(colr, ttle):
#     wn = turtle.Screen()
#     wn.bgcolor(colr)
#     wn.title(ttle)
#     return wn


# def make_turtle(colr, sz):
#     trtl = turtle.Turtle()
#     trtl.color(colr)
#     trtl.pensize(sz)
#     return trtl

# screen = make_screen("lightgreen", "4.9_excercises")
# mikey = make_turtle("blue", 3)


# def square_boy(sqrz):
#     for _ in range(sqrz):
#         for _ in range(4):
#             mikey.forward(20)
#             mikey.left(90)
#         mikey.pu()
#         mikey.forward(50)
#         mikey.pd()

# square_boy(5)

# def mikey_square(sz):    
#     for _ in range(4):
#         mikey.forward(sz)
#         mikey.left(90)
#     mikey.pu()
#     mikey.bk((10))
#     mikey.right(90)
#     mikey.forward(10)
#     mikey.left(90)
#     mikey.pd()


# def multi_square(sz, layers):
#     for layer in range(layers):
#         mikey_square(sz + (20 * layer))

# multi_square(30, 17)
    

# screen.mainloop()

# add this to py-turtles

# 3) Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. 
# When called with draw_poly(tess, 8, 50), it will draw a shape like this:

# import turtle

# wn = turtle.Screen()

# def draw_poly(t, n, sz):
#     for _ in range(n):
#         t.forward(sz)
#         t.left(360/n)

# tess = turtle.Turtle()
# draw_poly(tess, 8, 50)

# wn.mainloop()

# 4) Draw this pretty pattern

# import turtle

# def draw_square(t, sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.left(90)

# wn = turtle.Screen()
# t = turtle.Turtle()

# for _ in range(24):
#     draw_square(t, 50)
#     t.right(15)

# t.hideturtle()

# wn.mainloop()

# 5) The two spirals in this picture differ only by the turn angle. Draw both.

# import turtle

# wn = turtle.Screen()
# t = turtle.Turtle()

# def sq_spiral(t, sz):
#     for _ in range(10):
#         t.right(90)
#         t.forward(sz)
#         t.right(90)
#         t.forward(sz)
#         sz = sz + 10


# sq_spiral(t, 10)



# wn.mainloop()

# import turtle

# wn = turtle.Screen()
# t = turtle.Turtle()

# def sq_spiral(t, sz):
#     for _ in range(20):
#         for _ in range(3):
#             t.right(90)
#             t.forward(sz)
#             sz = sz + 5
#         t.right(89)
#         t.forward(sz)
#         sz = sz + 5

        

# sq_spiral(t, 10)



# wn.exitonclick()


# 6) Write a void function draw_equitriangle(t, sz) which calls draw_poly 
# from the previous question to have its turtle draw a equilateral triangle.


# import turtle

# wn = turtle.Screen()

# def draw_poly(t, n, sz):
#     for _ in range(n):
#         t.forward(sz)
#         t.left(120)

# tess = turtle.Turtle()
# draw_poly(tess, 3, 50)

# wn.exitonclick()

# 7) Write a fruitful function sum_to(n) that returns 
# the sum of all integer numbers up to and including n. 
# So sum_to(10) would be 1+2+3...+10 which would return the value 55.

# def sum_to(n):
#     return sum(range(n + 1))

# print(sum_to(10))


# 8) Write a function area_of_circle(r) which returns the area of a circle of radius r.

# def area_of_circle(r):
#     return 3.14 *(r**2)

# print(area_of_circle(5))

# 9) Write a void function to draw a star, where the length of each side is 100 units. 
# (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle

wn = turtle.Screen()
t = turtle.Turtle()

# def star_boy(sz):
#     for _ in range(5):
#         for _ in range(5):  
#             t.forward(sz)
#             t.right(144)
#         t.pu()
#         t.forward(350)
#         t.right(144)
#         t.pd()

# star_boy(100)

def star_boy2(sz):
    for _ in range(5):
        for _ in range(5):  
            t.forward(sz)
            t.right(144)
        # t.pu()
        t.forward(350)
        t.right(144)
        # t.pd()

star_boy2(100)

wn.exitonclick()

