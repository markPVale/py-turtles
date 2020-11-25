# 1) We’ve said nothing in this chapter about whether you can pass tuples as
# arguments to a function. Construct a small Python example to test whether
# this is possible, and write up your findings.

def f(a, b):
    """
    Test to see if a tuple can be passed as an argument to a function
    """
    person = ("a", "b", "c", "d", "e")
    for persons in person:
        print((persons, a), (persons, b))


f("he cool", "word")

# The output of the above function:
# ('a', 'he cool') ('a', 'word')
# ('b', 'he cool') ('b', 'word')
# ('c', 'he cool') ('c', 'word')
# ('d', 'he cool') ('d', 'word')
# ('e', 'he cool') ('e', 'word')


# 2) Is a pair a generalization of a tuple, or is a tuple a generalization of a pair?

# By definition:
# generalize = make a general or broad statement by inferring from specific cases.

# A tuple is a generalization of a pair.

# 3) Is a pair a kind of tuple, or is a tuple a kind of pair?

# A pair is a type of tuple. Tuples can have multiple values (more than two).
