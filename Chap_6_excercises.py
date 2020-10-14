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

import sys

def test(did_pass):
    """    Print the result of a test.    """
    # Get the caller's line number.
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# Construct our test suite:

def test_suite():
    """  Run the suite of tests for code in this module (this file).  """
    # test(absolute_value(17) == 17)
    # test(absolute_value(-17) == 17)
    # test(absolute_value(0) == 0)
    # test(absolute_value(3.14) == 3.14)
    # test(absolute_value(-3.14) == 3.14)
    assert absolute_value(3) == 3
    assert absolute_value(0) == 0
    assert absolute_value(-55) == 55
    

# Here is the call to run the tests:
test_suite()  





