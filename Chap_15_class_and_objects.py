
# class Point:
#     """ Point class represents and manipulates x, y coords."""

#     def __init__(self):
#         """ Create a new point at the origin """
#         self.x = 0
#         self.y = 0


# p = Point()
# q = Point()

# print(p.x, p.y, p.x, p.y)


# The function Point is a constructor, it creates a new object instance.
#   The combined process of 'make me a new object' and 'get its settings initialized to the factory
# default settings' is called instantiation.


#   We can give default values:
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

# # # The x and y paramaters are both optional in the code above. If the caller
# # # doesn't supply the arguments, the default value of 0 is used for both;


# p = Point(4, 2)
# q = Point(6, 3)
# r = Point()
# print(p.x, q.y, r.x)


# def print_point(pt):
#     print('({0}, {1})'.format(pt.x, pt.y))


# print_point(p)


# Instances as return values

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my)


def halfway(self, target):
    mx = (self.x + target.x) / 2
    my = (self.y + target.y) / 2

    return Point(mx, my)


p = Point(3, 4)
q = Point(5, 12)
r = halfway(p, q)

print(r.to_string())


# Exercises

# 1. Rewrite the distance function from the chapter titled Fruitful functions so that it takes two Points as
# parameters instead of four numbers
