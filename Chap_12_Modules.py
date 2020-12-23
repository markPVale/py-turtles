# Modules


import wordtools
import math
import calendar
import time
import random
# from locale import getlocale, setlocale, LC_ALL, LC_TIME
import locale

rng = random.Random()

dice_throw = rng.randrange(1, 7)
delay_in_seconds = rng.random() * 5.0


# Generate a list containing n random ints between a lower and upper bounds:

# def make_random_ints(num, lower_bound, upper_bound):
#     """
#         Generate a list containing num random ints between lower_bound and
#         upper_bound. upper_bound is an open bound.
#     """

#     # create a random number generator
#     rng = random.Random()
#     result = []
#     for i in range(num):
#         result.append(rng.randrange(lower_bound, upper_bound))
#     return result


# print(make_random_ints(5, 1, 13))

# >>> [11, 11, 4, 1, 2]


# If no duplicates are desired:
# "Shuffle and slice" technique

# Make a list 1-12 (no duplicates)
xs = list(range(1, 13))
# Make a random number generator
rng = random.Random()
# Shuffle the list
rng.shuffle(xs)
# Take the first five elements
result = xs[:5]


# print(result)


# Random results with large data pools:
# "shuffle and slice" would not be ideal for large pools of options to pull from


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
        Generate a list containg num random ints between lower_bound and upper_bound.
        upper_bound is an open bound.
        The resulting list cannot contain duplicates
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


rind = make_random_ints_no_dups(5, 1, 10000000)
print(rind)


def make_random_int_no_dups(num, lower_bound, upper_bound):
    """
      Generate a list containing num random ints between
      lower_bound and upper_bound. upper_bound is an open bound.
      The result list cannot contain duplicates.
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


xs = make_random_int_no_dups(5, 1, 10000000)
print(xs)


#  12.3 The time module

# use the perf_counter() function (.clock() has been deprecated since 3.3) to time how long an operation takes
# The below example compares the speed in which a function, that we created
# can sum elements in a list compared with Python's built in sum function


def do_my_sum(xs):
    sum = 0
    for nums in xs:
        sum += nums
    return sum


# 10 million elements in list to sum
sz = 10000000
testdata = range(sz)

t0 = time.perf_counter()
my_result = do_my_sum(testdata)
t1 = time.perf_counter()
print("my_result   = {0} (time taken = {1:.4f} seconds)".format(
    my_result, t1-t0))

t2 = time.perf_counter()
their_result = sum(testdata)
t3 = time.perf_counter()
print(
    "their_result = {0} (time taken = {1:.4f} seconds".format(their_result, t3-t2))


# 12.3 Math module:
# Notice another difference between this module and our use of random and turtle: in random and turtle
#  we create objects and we call methods on the object.
# This is because objects have state — a turtle has a color, a position, a heading, etc., and every
# random number generator has a seed value that determines its next result.

# Mathematical functions are “pure” and don’t have any state — calculating the square root of
# 2.0 doesn’t depend on any kind of state or history about what happened in the past.
# So the functions are not methods of an object — they are simply functions that are grouped together
# in a module called math.


# 12.4 Creating your own modules

# saved files with .py extension can be imported into other py files


# 12.11 Excercises


# 1.)
# a. calendar module


# create an instance
cal = calendar.TextCalendar()

# print(cal.pryear(2012))

# # b. An adventurous CompSci student believes that it is better mental
# # chunking to have his week start on Thursday,

cal = calendar.TextCalendar(3)

print(cal.pryear(2012))


# c. Find a function to print just the month in which your birthday occurs this year


print(cal.prmonth(2020, 6))


# d. Try this:


# print(locale.getlocale())
# print(LC_ALL)


# d = calendar.LocaleTextCalendar(6, "ENGLISH")
# d.pryear(2012)

# unsupported locale setting. Unable to resolve issue at this time.


# 2. Open help for the math module:

# a.) How many functions are in the math module?
# The math module has 54 functions

# b.) What does math.ceil do? What about math.floor?

# math.ceil = returns the ceiling of x as an Integral:
print(math.ceil(3.5883))
# returns 4

# math.floor = returns the floor of x as an Integral:
print(math.floor(3.5883))
# returns 3

# c.) Describe how we have been computing the same value as math.sqrt without
# using the math module:

# performing the function x ** .5 will perform the same operation as math.sqrt
# e.g.
print(math.sqrt(25))
# returns 5.0
print(25 ** 0.5)
# returns 5.0

# d). What are the two data constants in the math module?

# The default help module lists the math module in python as having
# five data constants:
# e = 2.718281828459045
# inf = inf
# nan = nan
# pi = 3.141592653589793
# tau = 6.283185307179586


# 3). Investigate the copy module. What does deepcopy do?

# Deep copy constructs a new compound object and then, recursively inserts *copies*
# into it of the objects found in the original. This would come in handy
# when working excercise 2 in the last chapter, we could have created two distinct
# instances of turtle instead of an alias for tess


# 4).  Create a module named mymodule1.py. Add attributes myage set to your current age,
# and year set to the current year. Create another module named mymodule2.py.
# Add attributes myage set to 0, and year set to the year you were born.
# Now create a file named namespace_test.py.
# Import both of the modules above and write the following statement:

# print((mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year))


# True is printed since my birthday for this year already occured.

# 5).  Add the following statement to mymodule1.py, mymodule2.py, and
# namespace_test.py from the previous exercise:

# print("My name is", __name__)

# Run namespace_test.py. What happens? Why? Now add the following to the bottom of mymodule1.py:

# The name of the module is printed because the name module belongs the instance in
# which it was created in

# if __name__ == "__main__":
# print("This won't run if I'm  imported.")

# now the above print statement appears when either mymodule1 or mymodule2 is run


# 6).  In a Python shell / interactive interpreter, try the following:

# import this

# returns The Zen of Python, by Tim Peters:
# "Namespaces are one honking great idea -- let's do more of those!"


# 7). Give the Python interpreter’s response to each of the following from a
# continuous interpreter session:

s = "If we took the bones out, it wouldn't be crunchy, would it?"
print(s.split())
# returns : ['If', 'we', 'took', 'the', 'bones', 'out,', 'it', "wouldn't", 'be', 'crunchy,', 'would', 'it?']

print(type(s.split()))
# returns : <class 'list'>

print(s.split("o"))
# returns: ['If we t', '', 'k the b', 'nes ', 'ut, it w', "uldn't be crunchy, w", 'uld it?']

print(s.split("i"))
# returns: ['If we took the bones out, ', "t wouldn't be crunchy, would ", 't?']

print("0".join(s.split("o")))
# returns: If we t00k the b0nes 0ut, it w0uldn't be crunchy, w0uld it?


# Then apply what you have learned to fill in the body of the function below using
# the split and join methods of str objects:

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    return new.join(s.split(old))


print(myreplace(
    " ", "**", "Words will now      be  separated by stars."))

assert myreplace(
    ",", ";", "this, that, and some other thing") == "this; that; and some other thing"
assert myreplace(
    " ", "**", "Words will now be separated by stars.") == "Words**will**now**be**separated**by**stars."


# 8.)  Create a module named wordtools.py with our test scaffolding in place.
# imported wordtools

assert wordtools.cleanword("what?") == "what"
assert wordtools.cleanword("'now!'") == "now"
assert wordtools.cleanword("'now!'") == "now"

assert wordtools.has_dashdash("distance--but")
assert wordtools.has_dashdash("several") != True
assert wordtools.has_dashdash("spoke--")
assert wordtools.has_dashdash("distance--but")
assert wordtools.has_dashdash("-yo-yo-") != True

assert wordtools.extract_words("Now is the time!    'Now', is the time? Yes, now.") == [
    'now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']

assert wordtools.extract_words("she tried to curtsey as she spoke--fancy") == [
    'she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']

assert wordtools.wordcount(
    "now", ["now", "is", "time", "is", "now", "is", "is"]) == 2
assert wordtools.wordcount(
    "is", ["now", "is", "time", "is", "now", "the", "is"]) == 3
assert wordtools.wordcount(
    "time", ["now", "is", "time", "is", "now", "is", "is"]) == 1
assert wordtools.wordcount(
    "frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0
