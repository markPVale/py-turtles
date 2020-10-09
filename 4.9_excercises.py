import turtle

def make_screen(colr, ttle):
    wn = turtle.Screen()
    wn.bgcolor(colr)
    wn.title(ttle)
    return wn


def make_turtle(colr, sz):
    trtl = turtle.Turtle()
    trtl.color(colr)
    trtl.pensize(sz)
    return trtl

screen = make_screen("lightgreen", "4.9_excercises")
mikey = make_turtle("blue", 3)


# def square_boy(sqrz):
#     for _ in range(sqrz):
#         for _ in range(4):
#             mikey.forward(20)
#             mikey.left(90)
#         mikey.pu()
#         mikey.forward(50)
#         mikey.pd()

# square_boy(5)

def mikey_square(sz):    
    for _ in range(4):
        mikey.forward(sz)
        mikey.left(90)
    mikey.pu()
    mikey.bk((10))
    mikey.right(90)
    mikey.forward(10)
    mikey.left(90)
    mikey.pd()


def multi_square(sz, layers):
    for layer in range(layers):
        mikey_square(sz + (20 * layer))

multi_square(30, 17)
    

screen.mainloop()