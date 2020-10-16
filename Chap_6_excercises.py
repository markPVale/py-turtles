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


# def to_secs(hours, minutes, seconds):
#     return (hours * 3600 + minutes * 60 + seconds)


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

    assert day_num("Friday") == 5
    assert day_num("Sunday") == 0
    assert day_num(day_name(3)) == 3
    assert day_name(day_num("Thursday")) == "Thursday"
    assert day_num("Halloween") == None

    assert day_add("Monday", 4) == "Friday"
    assert day_add("Tuesday", 0) == "Tuesday"
    assert day_add("Tuesday", 14) == "Tuesday"
    assert day_add("Sunday", 100) == "Tuesday"

    assert day_add("Sunday", -1) == "Saturday"
    assert day_add("Sunday", -7) == "Sunday"
    assert day_add("Tuesday", -100) == "Sunday"
    assert day_add("Tuesday", -100) == "Sunday"

    assert to_secs(2, 30, 10) == 9010
    assert to_secs(2, 0, 0) == 7200
    assert to_secs(0, 2, 0) == 120
    assert to_secs(0, 0, 42) == 42
    assert to_secs(0, -10, 10) == -590

    assert to_secs(2.5, 0, 10.71) == 9010
    assert to_secs(2.433, 0, 0) == 8758

    assert hours_in(9010) == 2
    assert minutes_in(9010) == 30
    assert seconds_in(9010) == 10

    # assert (3 % 4 == 0)
    # assert (3 % 4 == 3)
    # assert (3 / 4 == 0)
    # assert (3 // 4 == 0)
    # assert (3+4  *  2 == 14)
    # assert (4-2+2 == 0)
    # assert (len("hello, world!") == 13)

    assert compare(5, 4) == 1
    assert compare(7, 7) == 0
    assert compare(2, 3) == -1
    assert compare(42, 1) == 1

    assert hypotenuse(3, 4) == 5
    assert hypotenuse(12, 5) == 13
    assert hypotenuse(24, 7) == 25
    assert hypotenuse(9, 12) == 15

    assert slope(5, 3, 4, 2) == 1.0
    assert slope(1, 2, 3, 2) == 0.0
    assert slope(1, 2, 3, 3) == 0.5
    assert slope(2, 4, 1, 2) == 2.0

    assert intercept(1, 6, 3, 12) == 3.0
    assert intercept(6, 1, 1, 6) == 7.0
    assert intercept(4, 6, 12, 8) == 5.0

    assert is_even(2)
    assert is_even(100)
    assert is_even(2000)

    assert is_odd(3)
    assert is_odd(117)
    assert is_odd(2347888923715)

    assert is_factor(3, 12)
    assert not is_factor(5, 12)
    assert is_factor(7, 14)
    assert not is_factor(7, 15)
    assert is_factor(1, 15)
    assert is_factor(15, 15)
    assert not is_factor(25, 15)

    assert is_multiple(12, 3)
    assert is_multiple(12, 4)
    assert not is_multiple(12, 5)
    assert is_multiple(12, 6)
    assert not is_multiple(12, 7)

    assert f2c(212) == 100
    assert f2c(32) == 0
    assert f2c(-40) == -40
    assert f2c(36) == 2
    assert f2c(37) == 3
    assert f2c(38) == 3
    assert f2c(30) == 4

    assert c2f(0) == 32
    assert c2f(100) == 212
    assert c2f(-40) == -40
    assert c2f(12) == 54
    assert c2f(18) == 64
    assert c2f(-48) == -54








    
    


    

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

# test_suite_ass()



# 5) Can your day_add function already work with negative deltas? 
# For example, -1 would be yesterday, or -7 would be a week ago:

# Yes my func works with negative numbers
# Python returns modulus results that are the same sign as the divisor
#  


# 6) Write a function days_in_month which takes the name of a month, 
# and returns the number of days in the month. Ignore leap years:

def days_in_month(month):
    
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    if month in months:
        return months[month]


print(days_in_month("January"))


# 7) Write a function to_secs that converts hours, minutes and seconds to a total 
# number of seconds. 


# def to_secs(hours, minutes, seconds):
#     return (hours * 3600 + minutes * 60 + seconds)



# print(to_secs(2,30,10))

# test_suite_ass()


# 8) Extend to_secs so that it can cope with real values as inputs. 
# It should always return an integer number of seconds (truncated towards zero):


def to_secs(hours, minutes, seconds):
    return int(hours * 3600 + minutes * 60 + seconds)


print(to_secs(2.5, 0, 10.71))

# test_suite_ass()


# 9) Write three functions that are the “inverses” of to_secs:

# hours_in returns the whole integer number of hours represented by a total number of 
# seconds.

# minutes_in returns the whole integer number of left over minutes in a total number
#  of seconds, once the hours have been taken out.

# seconds_in returns the left over seconds represented by a total number of seconds.

# You may assume that the total number of seconds passed to these functions is an integer

def hours_in(secs):
    return int(secs/3600)

print(hours_in(9010))


def minutes_in(secs):
    return int((secs/60)%60)

print(minutes_in(9010))


def seconds_in(secs):
    return int(secs % 60)

print(seconds_in(9010))


# test_suite_ass()


# 10) Which of these tests fail? Explain why.

# test(3 % 4 == 0) Fail - 4 divides into 3 zero times w/3 remaining (answer = 3)
# test(3 % 4 == 3) True
# test(3 / 4 == 0) Fail - 3/4 = .75
# test(3 // 4 == 0) True - // gives the floor 
# test(3+4  *  2 == 14) True
# test(4-2+2 == 0) True
# test(len("hello, world!") == 13) True


# 11) Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b

def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else: 
        return -1


# 12) Write a function called hypotenuse that returns the length of the hypotenuse 
# of a right triangle given the lengths of the two legs as parameters:


def hypotenuse(a,b):
    return (a ** 2 + b ** 2) ** .5


# 13) Write a function slope(x1, y1, x2, y2) that returns the slope of the line 
# through the points (x1, y1) and (x2, y2). Be sure your implementation of slope 
# can pass the following tests:

# slope = rise/run    rise = y2-y1   run = x2-x1

def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

print(slope(5, 3, 4, 2))

# Then use a call to slope in a new function named intercept(x1, y1, x2, y2) 
# that returns the y-intercept of the line through the points (x1, y1) and (x2, y2)

# slope intercept - y = mx + b 

def intercept(x1, y1, x2, y2):
    # (y2 -y1) = slope(x1, y1, x2, y2)(x2-x1) + b
    m = slope(x1, y1, x2, y2)
    b = (y1) - (m * (x1))
    return b


print(intercept(1, 6, 3, 12))
print(intercept(6, 1, 1, 6))
print(intercept(4, 6, 12, 8))
# test_suite_ass()


# 14) Write a function called is_even(n) that takes an integer as an argument and 
# returns True if the argument is an even number and False if it is odd.

def is_even(num):
    return num % 2 == 0

print(is_even(2))

# 15) Now write the function is_odd(n) that returns True when n is odd 
# and False otherwise. Include unit tests for this function too.

def is_odd(num):
    return num % 2 != 0

print(is_odd(22))


# 16) Write a function is_factor(f, n) that passes these tests:

def is_factor(f, n):
    return n % f == 0 

print(is_factor(3, 12))


# 17) Write is_multiple to satisfy these unit tests:
def is_multiple(a, b):
    return is_factor(b, a)
        

print("this:")

print(is_multiple(55, 5))


# 18) Write the function f2c(t) designed to return the integer value of the nearest 
# degree Celsius for given temperature in Fahrenheit. 
# (hint: you may want to make use of the built-in function, round. 
# Try printing round.__doc__ in a Python shell or looking up help for the round function, 
# and experimenting with it until you are comfortable with how it works.)
    
# C to F = C * (9/5) + 32

# F to C = (F -32) / (9/5)

def f2c(t):
    return round((t -32) / (9/5))

print(f2c(77))


# 19) Now do the opposite: write the function c2f which converts Celsius to Fahrenheit:

def c2f(t):
    return round((t * (9/5)) + 32)

print(c2f(25))