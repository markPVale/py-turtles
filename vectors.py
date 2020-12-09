# 5. Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write functions to perform standard operations on vectors. Create a script named vectors.py and write Python code to pass the tests in each case.

# Write a function add_vectors(u, v) that takes two lists of numbers of the
# same length, and returns a new list containing the sums of the corresponding elements of each:

import numpy as np


def add_vectors(list1, list2):
    # new_list = [x + y for x, y in zip(list1, list2)]
    print(range(len(list1)))
    new_list = [list1[i] + list2[i] for i in range(len(list1))]
    return new_list


print(add_vectors([1, 1, 3], [1, 3, 4]))

assert add_vectors([1, 1], [1, 1]) == [2, 2]
assert add_vectors([1, 2], [1, 4]) == [2, 6]
assert add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4]


# test(add_vectors([1, 1], [1, 1]) == [2, 2])
# test(add_vectors([1, 2], [1, 4]) == [2, 6])
# test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


# 6. Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns
# the scalar multiple of v by s. :

def scalar_mult(s, v):
    scalar_list = [s*nums for nums in v]
    return scalar_list


print(scalar_mult(5, [1, 2]))

assert scalar_mult(3, [1, 0, -1]) == [3, 0, -3]
assert scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]


# 7. Write a function dot_product(u, v) that takes two lists of numbers of the same length,
# and returns the sum of the products of the corresponding elements of each (the dot_product).

def dot_product(u, v):
    product_list = [u[i] * v[i] for i in range(len(u))]
    return sum(product_list)


print(dot_product([1, 1], [1, 1]))

assert dot_product([1, 2], [1, 4]) == 9
assert dot_product([1, 2, 1], [1, 4, 3]) == 12


# Extra challenge for the mathematically inclined: Write a function cross_product(u, v) that
# takes two lists of numbers of length 3 and returns their cross product.
# You should write your own tests.


def cross_product(u, v):
    # cx = u[1]*v[2] - u[2]*v[1]
    # cy = u[2]*v[0] - u[0]*v[2]
    # cz = u[0]*v[1] - u[1]*v[0]
    # return [cx, cy, cz]

    # np.array(u)
    # np.array(v)
    return np.cross(u, v)


print(cross_product([1, 3, 2], [2, 1, 4]))
print(cross_product([2, 3, 4], [5, 6, 7]))
