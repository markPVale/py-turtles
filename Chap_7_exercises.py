# # CHAPTER 7 EXERCISES


# # COUNTING DIGITS

def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1 
        n = n // 10
        print(n)
    return count


print(num_digits(710))


# # ENCAPSULATION AND GENERALIZATION

def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

print_multiples(2)

for i in range(1, 7):
    print_multiples(i)


# encapsulation again:

def print_mult_table():
    for i in range(1,7):
        print_multiples(i)

print_mult_table()


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









