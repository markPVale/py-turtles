
# 1. What is the python interpreters response to the following?

import turtle
print(list(range(10, 0, -2)))

# The three arguments to the range function are start, stop, and step, respectively.
# In this example, start is greater than stop. What happens if start < stop and step < 0?
# Write a rule for the relationships among start, stop, and step.

# >>> If start > stop then step must be a negative number, if start < stop then step must
# be positive or the result is an empty array.


# 2. Consider this fragment of code:

# turtle.setup(400, 500)
# wn = turtle.Screen()
# tess = turtle.Turtle()
# alex = tess
# alex.color("hotpink")

# # wn.mainloop()

# print(tess is alex)
# print(alex is tess)

# Both Tess and Alex refer to the same object, they are aliases of
# turtle.Turle()
# tess is alex >>> True
# alex is tess >>> True

# The name is bound to the object in the current global namespace
# (according to the python documentation)


# 3. Draw a state snapshot for a and b after the third line of the following
# python code is executed:

# a = [1, 2, 3]
# b = a[:]
# c = b[0] = 5

# a is a list consisting of elements: 1, 2, 3
# b is a close of a
# c is a clone of b that mutated the first element in the list (1) to 5
# c now equals [5, 2, 3] while a and b remain the same.


# 4. What will be the output of the following program?
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
print("Test 1: {0}".format(this == that))
that = this
print("Test 2: {0}".format(this is that))

# Explanation:
# Since lists are mutable, Python doesn't optimize resources by making both variales refer to
# the same object, although they have the same value. So while Test 1 will return False,
# this == that will return True.
# Test 2 however sets the value of that to be this which makes the two variables refer to the
# same object and therefore this is that >>> True.


# REMAINING EXERCISES IN vectors.py file
