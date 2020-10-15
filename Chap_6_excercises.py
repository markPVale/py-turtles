# 6. Fruitful functions
# 6.1. Return values
# The built-in functions we have used, such as abs, pow, int, max, and range, 
# have produced results. Calling each of these functions generates a value, which we 
# usually assign to a variable or use as part of an expression.


# Multiple return statements e.g.
# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x

# absolute_value(-23)

# # also:

# def absolute_value(x):
#     if x < 0:
#         return -x
#     return x


# WRITING FUNCTIONS USING INCREMENTAL DEV

# def distance(x1, x2, y1, y2):
#     return 0.0

# if no error,  add lines of code

# distance(1, 2, 4, 6)


# add variables
# use print function to check variables
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     print(dx, dy)
#     return 0.0

# distance(1, 2, 4, 6)


# if no errors then add additional variable:
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquare = dx*dx + dy*dy
#     print(dx, dy)
#     print(dsquare)
#     return 0.0

# distance(1, 2, 4, 6)


# Now add final piece of pythagorean theorem
# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquare = dx*dx + dy*dy
#     result = dsquare**.5
#     print(dx, dy)
#     print(dsquare)
#     print(result)
#     return result

# distance(1, 2, 4, 6)

# Key Aspects to the above process of writing code:

# 1) Start with a working skeleton program and make small incremental changes,
# this allows you to pinpoint an error if/when one occurs

# 2) Use temporary variables to refer to intermediate values so that they can 
# be easily inspected 

# 3) Once the program is working, play around with your options. (can it be made shorter,
# easier to understand, etc.)


# DEBUGGING W/print

# Have a clear solution to the problem before you start working on it

# Avoid "chatterbox functions", those that unnecessarily ask the user for input,
# or print output when not needed



# PROGRAMMING WITH STYLE

# limit line length to 78 characters
# when naming identifiers:
#   use CamelCase for classes
#   lowercase_with_underscores for funcs and variables
# place imports at top of file
# keep function definitions together
# use docstrings to seperate functions
# use two blank lines to separate function defiinitions from eachother
# keep top level statements, including function calls, together at the bottom 
#   of the program.


# def absolute_value(x):
#     if x < 0:
#         return -x
#     return x


def absolute_value(n):   # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n


# HELPER FUNCTION

# import sys

# def test(did_pass):
#     """    Print the result of a test.    """
#     # Get the caller's line number.
#     linenum = sys._getframe(1).f_lineno
#     if did_pass:
#         msg = "Test at line {0} ok.".format(linenum)
#     else:
#         msg = ("Test at line {0} FAILED.".format(linenum))
#     print(msg)


# Construct our test suite:

# def test_suite():
#     """  Run the suite of tests for code in this module (this file).  """
#     test(absolute_value(17) == 17)
#     test(absolute_value(-17) == 17)
#     test(absolute_value(0) == 0)
#     test(absolute_value(3.14) == 3.14)
#     test(absolute_value(-3.14) == 3.14)
#     assert absolute_value(3) == 3
#     assert absolute_value(0) == 0
#     assert absolute_value(-55) == 55
    

# Here is the call to run the tests:
# test_suite()  


# 6.9 Excercises

# 1) The four compass points can be abbreviated by single-letter strings as
#  “N”, “E”, “S”, and “W”. Write a function turn_clockwise that takes one of 
# these four compass points as its parameter, and returns the next compass point 
# in the clockwise direction. Here are some tests that should pass:

# test(turn_clockwise("N") == "E")
# test(turn_clockwise("W") == "N")


# def turn_clockwise(dir):
#     if dir == "N":
#         return "E"
#     elif dir == "E":
#         return "S"
#     elif dir == "S":
#         return "W"
#     elif dir == "W":
#         return "N"
#     else:
#         # print("Sorry, that is not a valid direction!")
#         return None 


def turn_clockwise(dir):
    """ Takes direction, dir, in the form of a single letter N, E, S or W.
    Returns the directin 90 degrees clockwise from the input."""

    rotator = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }

    if dir in rotator:
        return rotator[dir]
    else:
        return None


print(turn_clockwise("N"))


def test_suite_ass():
    """  suite of tests using assert statement  """

    # assert turn_clockwise("N")
    # assert turn_clockwise("E")
    # assert turn_clockwise("W")
    # assert turn_clockwise("S")
    # assert turn_clockwise("P")

    # assert day_name(3) == "Wednesday"
    # assert day_name(6) == "Saturday"
    # assert day_name(42) == None

    # assert day_num("Friday") == 5
    # assert day_num("Sunday") == 0
    # assert day_num(day_name(3)) == 3
    # assert day_name(day_num("Thursday")) == "Thursday"
    # assert day_num("Halloween") == None

    assert day_add("Monday", 4) == "Friday"
    assert day_add("Tuesday", 0) == "Tuesday"
    assert day_add("Tuesday", 14) == "Tuesday"
    assert day_add("Sunday", 100) == "Tuesday"

    assert day_add("Sunday", -1) == "Saturday"
    assert day_add("Sunday", -7) == "Sunday"
    assert day_add("Tuesday", -100) == "Sunday"

    
    


    

# test_suite_ass()

# 2) Write a function day_name that converts an integer number 0 to 6 into the 
# name of a day. Assume day 0 is “Sunday”. Once again, return None if the 
# arguments to the function are not valid. Here are some tests that should pass:

def day_name(num):
    
    days = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday"
    }   

    if num in days:
        return days[num]
    else:
        return None

# print(day_name(12))


# test_suite_ass()


# 3) Write the inverse function day_num which is given a day name, and returns its number:

def day_num(day):

    days = {
        "Sunday" : 0,
        "Monday" : 1,
        "Tuesday" : 2,
        "Wednesday" : 3,
        "Thursday" : 4,
        "Friday" : 5,
        "Saturday" : 6,
    }

    if day in days:
        return days[day]
    else:
        return None

print(day_num("Wednesday"))

# test_suite_ass()


# 4) Write a function that helps answer questions like ‘“Today is Wednesday. 
# I leave on holiday in 19 days time. What day will that be?”’ 
# So the function must take a day name and a delta argument — the number of days to add — 
# and should return the resulting day name: 

def day_add(day, duration):

    days = {
        "Sunday" : 0,
        "Monday" : 1,
        "Tuesday" : 2,
        "Wednesday" : 3,
        "Thursday" : 4,
        "Friday" : 5,
        "Saturday" : 6,
    }
    
    if day in days:
        new_day = (days[day] + duration) % 7
        return day_name(new_day)


print(day_add("Wednesday", -1))

test_suite_ass()








