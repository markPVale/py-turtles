# # CHAPTER 7 EXERCISES


# # COUNTING DIGITS

# def num_digits(n):
#     count = 0
#     while n != 0:
#         count = count + 1 
#         n = n // 10
#         print(n)
#     return count


# print(num_digits(710))


# # ENCAPSULATION AND GENERALIZATION

# def print_multiples(n):
#     for i in range(1, 7):
#         print(n * i, end="   ")
#     print()

# print_multiples(2)

# for i in range(1, 7):
#     print_multiples(i)


# encapsulation again:

# def print_mult_table():
#     for i in range(1,7):
#         print_multiples(i)

# print_mult_table()


# NESTED LOOPS FOR NESTED DATA

movies = [
    ("Harry Potter", ["Harry", "Ron", "Hermione"]),
    ("The Greyhound", ["Tom Hanks", "Elisabeth Shue"]),
    ("The Gentlemen", ["Mathew McConaughey", "Charlie Hunnam", "Michelle Dockery"]),
    ("The Vast of Night", ["Sierra McCormick", "Jake Horowitz","Gail Cronauer"])
]

for (title, actors) in movies:
    print(title, "has", actors, "in it")


for (title, actors) in movies:
    for actor in actors:
        if actor == "Tom Hanks":
            print(title, "stars T.H.")


# EXERCISES

# 1) Write a function to count how many odd numbers are in a list

def count_odds(lst):
    """ write a function that returns the number of odd numbers in a list (param) """
    counter = 0

    for nums in lst:
        if nums % 2 != 0:
            counter += 1
    print(counter)
    return counter

assert count_odds([]) == 0
assert count_odds([1,2,3,4,5]) == 3
assert count_odds([2,4,6,8]) == 0
assert count_odds([1,1,11,1,1]) == 5
assert count_odds([2,2112135]) == 1


# 2) Sum up all the even numbers in a list:


def sum_even(lst):
    """ write a function that returns the sum of all the even numbers 
    within a list (param) """
    sum_total = 0
    for nums in lst:
        if nums % 2 == 0:
            sum_total += nums
    print(sum_total)
    return sum_total

assert sum_even([1,2,3,4,5,6]) == 12
assert sum_even([1,2,3]) == 2
assert sum_even([1,2,4,6,8,9]) == 20
assert sum_even([1,2,2,2,2,2,2,2]) == 14
assert sum_even([1,3,5,7]) == 0



# 3) Sum up all the negative numbers in a list:


def sum_odd(lst):
    """ Write a function that returns the sum of all odd 
    integers within a list (param) """
    sum_total = 0
    for nums in lst:
        if nums % 2 != 0:
            sum_total += nums
    print(sum_total)
    return sum_total

assert sum_odd([]) == 0
assert sum_odd([1,2,3,4,5]) == 9
assert sum_odd([1,1,1,1,1,1]) == 6
assert sum_odd([2,4,6,8,9]) == 9
assert sum_odd([1,2,3]) == 4


#  4) Count how many words in a list have length 5:


def len_five(lst):
    """ Write a function that returns the number of words in a list with a 
    length of five letters """
    count = 0
    for words in lst:
        if len(words) == 5:
            count += 1
    print(count)
    return count

assert len_five(["cat", "bat", "match"]) == 1
assert len_five(["cat", "bat", "mat"]) == 0
assert len_five(["cat", "bat", "match", "smash", "little"]) == 2
assert len_five(["cat", "bat", "match", "snake", "abcde"]) == 3
assert len_five(["cat", "bat", "match", "latch", "scratch"]) == 2


# 5) Sum all the elements in a list up to but not including the first even number. 
# (Write your unit tests. What if there is no even number?)

def sum_before_even(lst):
    """ write a function that returns the sum of all integers before reaching 
    the first even integer in the list """
    sum_list = 0
    for nums in lst:
        if nums % 2 != 0:
            sum_list += nums
        elif nums % 2 == 0:
            break
    print(sum_list)
    return sum_list

assert sum_before_even([1,3,5,6]) == 9
assert sum_before_even([2,1,3,5,6]) == 0
assert sum_before_even([1,3,5,7]) == 16
assert sum_before_even([1,3,5,11,17,2]) == 37
assert sum_before_even([1]) == 1


# 6) Count how many words occur in a list up to and including the first 
# occurrence of the word “sam”. (Write your unit tests for this case too. 
# What if “sam” does not occur?)

def num_before_sam(lst):
    """ write a function that counts the number of words in a list before the 
    word 'sam' appears """
    count = 0
    for words in lst:
        if words == "sam":
            break
        else:
            count += 1
    print(count)
    return count

assert num_before_sam(["pam", "jimmy", "ryan", "sam", "jeff"]) == 3
assert num_before_sam(["pam", "jimmy", "ryan", "saam", "jeff", "sam"]) == 5
assert num_before_sam(["sam"]) == 0
assert num_before_sam([5, 3, "stan", "sam"]) == 3
assert num_before_sam([5, 3, "stan", "sam"]) == 3
assert num_before_sam([5, 3, "stan", "monkey", "josh", "marcus", "uncle_roger"]) == 7



# 7) Add a print function to Newton’s sqrt function that prints out better each time 
# it is calculated. Call your modified function with 25 as an argument and record 
# the results.

def newt_sqrt(num):
    """ Write a function that prints better each time it calculates 
    Newton's sqrt function """
    # better = (approx + n/approx)/2
    approx = num/2
    while True:
        better = (approx + num/approx)/2
        if abs(approx - better) < .001:
            return better
        else:
            approx = better
    
print(newt_sqrt(25))
print(newt_sqrt(49))
print(newt_sqrt(36))
print(newt_sqrt(81))
print(newt_sqrt(85))


# 8) Trace the execution of the last version of print_mult_table and 
# figure out how it works

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="   ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, i + 1)
    print()

print_mult_table(5)

# for every number in the variable range, the function 
#   print_multiples is run 
# print_multiples takes the first number of the variable in print_mult_table --> for 1 
# --> print_multiples(1, (1+1))
#for the ints i range(1, (1+1) +1) --> range(1,3) --> affected range = 1 and 2
#  print_multiples prints i * ints in affected range (1 * 1), (1 *2)


# 9) Write a function print_triangular_numbers(n) that prints out the first n 
# triangular numbers. A call to print_triangular_numbers(5) would produce the 
# following output:

# 1       1
# 2       3
# 3       6
# 4       10
# 5       15

# def print_triangular_numbers(n):
    

def print_rng(n):
    for i in range(1, n + 1):
        print(i,  int(i * (i + 1)/2))


print_rng(5)


# 10) Write a function, is_prime, which takes a single integer argument and 
# returns True when the argument is a prime number and False otherwise. 
# Add tests for cases like this:

def prime_numero(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                print(False)
                return False
                break    
        else:
            print(True)
            return True

prime_numero(42)

assert prime_numero(43)
assert prime_numero(11)
# assert prime_numero(35)
assert prime_numero(19911121)



# 11) Revisit the drunk pirate problem from the exercises in 
# chapter 3. This time, the drunk pirate makes a turn, and then takes some steps 
# forward, and repeats this. Our social science student now records 
# pairs of data: the angle of each turn, and the number of steps taken after the turn. 
# Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)]. 
# Use a turtle to draw the path taken by our drunk friend.

# import turtle

# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("green")
# t.color("blue")

coordinates =  [(160, 20), (-43, 10), (270, 8), (-43, 12)]

# print(len(coordinates))

def drunky(coordinates):
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.bgcolor("green")
    t.color("blue")
    for (angles, steps) in coordinates:
        if angles < 0:
            t.right(angles)
            t.forward(steps * 10)
        else:
            t.left(angles)
            t.forward(steps * 10)
    
    wn.exitonclick()

# drunky([(160, 20), (-43, 10), (270, 8), (-43, 12)])


# 12) Many interesting shapes can be drawn by the turtle by giving a list of pairs 
# like we did above, where the first item of the pair is the angle to turn, 
# and the second item is the distance to move forward. Set up a list of pairs so 
# that the turtle draws a house with a cross through the centre, as show here. 
# This should be done without going over any of the lines / edges more than once, 
# and without lifting your pen.


def housey(coordinates):
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.bgcolor("green")
    t.color("blue")
    for (angles, steps) in coordinates:
        if angles <= 0:
            t.right(angles)
            t.forward(steps * 10)
        else:
            t.left(angles)
            t.forward(steps * 10)
    
    wn.exitonclick()

# housey([(0, 20), (90, 20), (90, 20), (90, 20), (135, 20*2**.5), (90, 20*.5**.5), 
# (90, 20*.5**.5), (90, 20*2**.5)])



# 13) Not all shapes like the one above can be drawn without lifting your pen, 
# or going over an edge more than once. Which of these can be drawn?

# Eulerian Paths - A finite graph that visits every edge exactly once

# Eulerian Circuit - A Eulerian trail that starts and ends on the same vertex. For a 
#     Eulerian circuit to exist, all vertices must have an even degree


# 14) What will num_digits(0) return? Modify it to return 1 for this case. 
# Why does a call to num_digits(-24) result in an infinite loop? 
# (hint: -1//10 evaluates to -1) Modify num_digits so that it works correctly 
# with any integer value. Add these tests:


# def num_digits(n):
#     count = 0
#     while n != 0:
#         count = count + 1
#         n = n // 10
#         print(count)
#     return count


# Since -24 // 10 eventually gets to -1, and -1 // 10 = -1, there will be an infinite
# loop since n will never reach 0.

# The function is meant to count the number of individual digits in a number range 
# (1 - range + 1).

#redux:

def num_digits(n):
    return len(str(abs(n)))

print(num_digits(10))

assert num_digits(0) == 1
assert num_digits(-12345) == 5


# 16) Write a function sum_of_squares(xs) that computes the sum of the squares 
# of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) 
# should return 4+9+16 which is 29:

def sum_of_squares(xs):
    for nums in xs:
        return nums ** 2


print(sum_of_squares([2,3,4]))




