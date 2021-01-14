# 14). In the spirit of Test-driven development

# We’d like to know the index where a specific item occurs within in a list of items.
# Specifically, we’ll return the index of the item if it is found,
# or we’ll return -1 if the item doesn’t occur in the list.
# Let us start with some tests:


# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# assert search_linear(friends, "Zoe") == 1
# assert search_linear(friends, "Joe") == 0
# assert search_linear(friends, "Paris") == 6
# assert search_linear(friends, "Bill") == -1


# Motivated by the fact that our tests don’t even run,
# let alone pass, we now write the function:

from math import log, ceil
import time
import urllib.request


def search_linear(xs, target):
    """
        Find and return the index of target in sequence xs
    """
    for i, v in enumerate(xs):
        if v == target:
            return i
    return -1


friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
assert search_linear(friends, "Zoe") == 1
assert search_linear(friends, "Joe") == 0
assert search_linear(friends, "Paris") == 6
assert search_linear(friends, "Bill") == -1


# 14.3)

# vocab = ["apple", "boy", "dog", "down",
#                           "fell", "girl", "grass", "the", "tree"]
# book_words = "the apple fell from the tree to the grass".split()
# test(find_unknown_words(vocab, book_words) == ["from", "to"])
# test(find_unknown_words([], book_words) == book_words)
# test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

# The basic strategy is to run through each of the words in the book,
# look it up in the vocabulary, and if it is not in the vocabulary,
# save it into a new resulting list which we return from the function:


# My 'unassisted' attempt:
# def find_unknown_words(vocab, wds):
#     result = []
#     for wrd in wds:
#         if wrd not in vocab:
#             result.append(wrd)
#     return result


# Using the previous algorithm in new algorith:

# def find_unknown_words(vocab, wds):
#     result = []
#     for w in wds:
#         if (search_linear(vocab, w) < 0):
#             result.append(w)
#     return result


vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
# book_words = "the apple fell from the tree to the grass".split()

# find_unknown_words(vocab, book_words)

# assert find_unknown_words(vocab, book_words) == ["from", "to"]
# assert find_unknown_words([], book_words) == book_words
# assert find_unknown_words(vocab, ["the", "boy", "fell"]) == []


# Now let us look at the scalability. We have more realistic vocabulary
# in the text file that could be downloaded at the beginning of this chapter,
# so let us read in the file (as a single string) and split it into a list
# of words

alice_url = "http://openbookproject.net/thinkcs/python/english3e/_downloads/alice_in_wonderland.txt"

vocab_url = "http://openbookproject.net/thinkcs/python/english3e/_downloads/vocab.txt"


# use function from last exercise to download the file from the server:

# import urllib.request

# urllib.request.urlretrieve(url, destination_filename)

# Fetch Alice in Wonderland from the web and add it to new file:
# urllib.request.urlretrieve(alice_url, "alice.txt")

# Fetch 'vocab' from the web and add it to new file:
# urllib.request.urlretrieve(vocab_url, "vocab.txt")


# def retrieve_page(url):
#     """
#         Retreive the contents of a web page.
#         The contents is converted to a string before returning it.
#     """
#     my_socket = urllib.request.urlopen(url)
#     dta = str(my_socket.read())
#     my_socket.close()
#     return dta

def load_words_from_file(filename):
    """ Read words from filename, return list of words."""
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} ".format(
#     len(bigger_vocab), bigger_vocab[:6]))


# Now let us load up a book
# We need to clean up the contents of the book.
# This will involve removing punctuation, and converting everything to the same case

# text_to_words("my name is Earl!") == ["my", "name", "is", "earl"]
# text_to_words("'Well, I never!', said Alice.") == [
#     "well", "i", "never", "said", "alice"]


# Translate method for strings:

def text_to_words(the_text):
    my_substitutions = the_text.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
                                          "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


assert text_to_words("my name is Earl!") == ["my", "name", "is", "earl"]
assert text_to_words("'Well, I never!', said Alice.") == [
    "well", "i", "never", "said", "alice"]


# Now we're ready to read in our book:

def get_words_from_book(filename):
    read_file = open(filename, "r")
    content = read_file.read()
    read_file.close()
    wds = text_to_words(content)
    return wds


book_words = get_words_from_book("alice.txt")
# print("There are {0} words in the book, the first 100 are\n {1}".format(
#     len(book_words), book_words[:100]))


# Now we have all the pieces ready, let us see what words in this book are not
# in the vocabulary:

# missing_words = find_unknown_words(bigger_vocab, book_words)

# print(missing_words)


# We wait a considerable time now, something like a minute,
# before Python finally works its way through this


# Let us try to improve the efficiency of this:

# import time

# Note, that time.clock() has since been deprecated, using:
# t0 = time.process_time()
# missing_words = find_unknown_words(book_words, book_words)
# t1 = time.process_time()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))
# >>> There are 0 unkown words.
# >>> That took 2.7484 seconds.

# t0 = time.perf_counter()
# missing_words = find_unknown_words(book_words, book_words)
# t1 = time.perf_counter()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))
# >>> There are 0 unkown words.
# >>> That took 2.7542 seconds.


# 14.4) Binary Search

# Lets start with some tests. Remember, the list needs to be sorted:

# xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# assert search_binary(xs, 20) == -1
# assert search_binary(xs, 99) == -1
# assert search_binary(xs, 1) == -1
# assert for(i, v) in enumerate(xs):
# test(search_binary(xs, v) == i)

# It is useful to think about region-of-interest(ROI) with the list being searched.
# In the tests above, we start our seach within an ROI in the center of the data,
# this results in three possible outcomes:
#   we found the target
#   we can discard the front half of the data
#   we can discard the second half of the data

# Example Code:

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    b = 0
    ub = len(xs)
    while True:
        # If search comes up empty:
        if b == ub:
            return -1
        # Probe the middle of the ROI
        mid_index = (b + ub) // 2

        # Fetch the item at the position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'".format(
        #     b, ub, ub-b, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            b = mid_index + 1
        else:
            ub = mid_index


# def find_unknown_words(vocab, wds):
#     result = []
#     for w in wds:
#         if (search_binary(vocab, w) < 0):
#             result.append(w)
#     return result


# xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
# assert search_binary(xs, 20) == -1
# assert search_binary(xs, 99) == -1
# assert search_binary(xs, 1) == -1

# for(i, v) in enumerate(xs):
#     assert search_binary(xs, v) == i


# Substitute a call to this search algorithm instead of calling the
# search_linear in find_unknown_words

# first linear:
# t0 = time.perf_counter()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.perf_counter()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))
# returns
# >>> There are 3396 unknown words.
# >>> That took 13.4931 seconds.

# with binary search:
# returns:
# >>> There are 3396 unknown words.
# >>> That took 0.0641 seconds.


# Formula for how many probes are needed for a list of (N) size:
# k = [sqrtlog(N+1)]

# or how big of a list we can deal with given (k) amount of probes:
# N = 2**K - 1


# Example: A list has 1000 elements, what is max number of probes needed to do a
# binary search?

# form math import log, ceil
print(ceil(log(1000 + 1, 2)))
# >>> 10
# Summation: to find a target in a list of 1000 elements,
# the max number of probes needed is 10


# 14.5 Removing adjacent duplicates from the list
#  One approach: sort the list and remove adjacent duplicates

# remove_adjacent_dups([1,2,3,3,3,5,6,9,9]) == [1,2,3,5,6,9]
# test(remove_adjacent_dups([]) == [])
# test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
#    ["a", "big", "bite", "dog"])


def remove_adjacent_dups(xs):
    """Return a new list in which all adjacent
    ducplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


# Run this on alice.txt

# all_words = get_words_from_book('alice.txt')
# all_words.sort()
# book_words = remove_adjacent_dups(all_words)
# print("There are {0} words in the book. Only {1} are unique.".format(
#     len(all_words), len(book_words)))
# print("The first 100 words are \n{0}".format(book_words[:100]))

# >>> There are 27336 words in the book. Only 2569 are unique.
# >>> The first 100 words are...


# 14.6) Merging Sorted Lists

# A simple yet inefficient algorithm:
# newlist = xs + ys
# newlist.sort()

# Tests:
xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
ys = [4, 8, 12, 16, 20, 24]
zs = xs + ys
zs.sort()


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

# Keep two indexes and whichever item currently indexed is smaller,
# add that item to the result variable
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


assert merge(xs, []) == xs
assert merge([], []) == []
assert merge(xs, ys) == zs
assert merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5]
assert merge(['a', 'big', 'cat'], ['big', 'bite', 'dog']) == [
    'a', 'big', 'big', 'bite', 'cat', 'dog']


# 14.7)

# The pattern for the algorithm to merge sorted lists considers:
# What should we do when either list has no more items?
# What should we do if the smallest items from each list are equal to each other?
# What should we do if the smallest item in the first list is smaller than the smallest one
# in the second list?
# What should we do in the remaining case?


# Adapt the merge algorithm fo each of these cases:

# 1) Return only those items that are present in both lists

# def merge_common(lst_1, lst_2):
#     result = []
#     for element in lst_1:
#         if element in lst_2:
#             result.append(element)
#     return result


# Using list comprehensions:
# def merge_common(lst_1, lst_2):
#     return [element for element in lst_1 if element in lst_2]


# A more pythonic approach:
def merge_common(lst_1, lst_2):
    return sorted(list(set(lst_1).intersection(lst_2)))


lst1 = [1, 2, 3, 4, 4, 5, 55, 66, 33, 21]
lst2 = [3, 44, 5, 33, 4]


print(merge_common(lst1, lst2))


# 2) Return only those items that are present in the first list, but not in the second
first1 = [0, 1, 1, 2, 3, 4, 5, 7]
sec2 = [1, 3, 5, 6, 7, 10]


def lst1_unique(xs, ys):
    """ return a list of items from first and second list that are unique to
        list one
     """
    result = []
    xi = 0
    yi = 0

# Keep two indexes and whichever item currently indexed is smaller,
# add that item to the result variable
    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result
        # ******Unless for this case, the items are equal*****
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
        else:
            yi += 1


print(lst1_unique(first1, sec2))

# 3) Return only those items that are present in the second list, but not in the first
first2 = [0, 1, 1, 2, 3, 4, 5, 7]
sec3 = [1, 3, 5, 6, 7, 10]


def lst2_unique(xs, ys):
    """ return a list of items from first and second list that are unique to
        list one
     """
    result = []
    xi = 0
    yi = 0

# Keep two indexes and whichever item currently indexed is smaller,
# add that item to the result variable
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            return result

        # Both lists still have items, copy smaller item to result
        # ******Unless for this case, the items are equal*****
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] == ys[yi]:
            yi += 1
        else:
            result.append(ys[yi])
            yi += 1


print(lst2_unique(first2, sec3))

# 4) Return items that are present in either the first or second list:


def merge_lists(lst_1, lst_2):
    return sorted(list(lst_1)+(lst_2))


# print(merge_lists(lst1, lst2))


# 5) Return items from the first list that are not eliminated by a matching
# element in the second list. In this case, an item in the second list "knocks out"
# just one matching item in the first list. This operation is sometimes called bagdiff.
home = [5, 7, 11, 11, 11, 12, 13]
away = [7, 8, 11]


def bagdiff(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

# Keep two indexes and whichever item currently indexed is smaller,
# add that item to the result variable
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result
        # ******Unless for this case, the items are equal*****
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


print(bagdiff(home, away))


# Use a variant of the merge to return the words that occur in the Alice.txt,
#  but not in the vocabulary.

def find_unknowns_merge_pattern(vocab, wds):
    """Both the vocab and wds must be sorted. Return a new
       list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result
        # Good, word exists in vocab
        if vocab[xi] == wds[yi]:
            yi += 1
        # Move past this vocab word
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi += 1


all_words = get_words_from_book('Alice.txt')
t0 = time.perf_counter()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time.perf_counter()
print('There are {0} unknown words'.format(len(missing_words)))
print('That took {0:.4f} seconds'.format(t1-t0))


# >>> There are 827 unknown words
# >>> That took 0.0149 seconds


# 14.8) Eight Queens puzzle, pt.1

# Check if Queens share a diagonal:
# share_diagonal(5,2,2,0)

# def share_diagonal(x0, y0, x1, y1):
#     """Is (x0, y0) on a shared diagonal with (x1, y1)?"""
#     dy = abs(y1 - y0)
#     dx = abs(x1 - x0)
#     # they clash if dx == dy
#     return dx == dy


# def col_clashes(bs, c):
#     """ Return True if the queen at column c clashes with any queen to its left"""
#     for i in range(c):
#         if share_diagonal(i, bs[i], c, bs[c]):
#             return True
#     # No clashes - col c has a safe placement
#     return False


# def has_clashes(the_board):
#     """ Determine whether we have any queens clashing on the diagonals
#         We're assuming here that the_board is a permutation of column
#         numbers, so we're not explicitly checking row or
#         column clashes
#     """
#     for col in range(1, len(the_board)):
#         if col_clashes(the_board, col):
#             return True
#     return False

#     # Because of the many ways of choosing 8 squares of a 64 square game board,
#     # we will use permutatuions.

#     # We'll try a random shuffle of the permutation [0,1,2,3,4,5,6,7]


# def main():
#     import random
#     # import random
#     rng = random.Random()

#     # generate the initial permutation
#     bd = list(range(8))
#     num_found = 0
#     tries = 0
#     while num_found < 10:
#         rng.shuffle(bd)
#         tries += 1
#         if not has_clashes(bd):
#             print("Found solution {0} in {1} tries.".format(bd, tries))
#             tries = 0
#             num_found += 1


# main()


# Here is an interesting fact. On an 8x8 board, there are known to be
#  92 different solutions to this puzzle. We are randomly picking one
# of 40320 possible permutations of our representation. So our chances
#  of picking a solution on each try are 92/40320. Put another way, on
# average we’ll need 40320/92 tries — about 438.26 — before we stumble
# across a solution. The number of tries we printed looks like our experimental
# data agrees quite nicely with our theory!


# 14.11) Exercises:

# 1) Alice in Wonderland Merge
# See above


# 2) Modify the queens program to solve some boards of size 4, 12, and 16.
# What is the maximum size puzzle you can usually solve in under a minute?

# def share_diagonal(x0, y0, x1, y1):
#     """Is (x0, y0) on a shared diagonal with (x1, y1)?"""
#     dy = abs(y1 - y0)
#     dx = abs(x1 - x0)
#     # they clash if dx == dy
#     return dx == dy


# def col_clashes(bs, c):
#     """ Return True if the queen at column c clashes with any queen to its left"""
#     for i in range(c):
#         if share_diagonal(i, bs[i], c, bs[c]):
#             return True
#     # No clashes - col c has a safe placement
#     return False


# def has_clashes(the_board):
#     """ Determine whether we have any queens clashing on the diagonals
#         We're assuming here that the_board is a permutation of column
#         numbers, so we're not explicitly checking row or
#         column clashes
#     """
#     for col in range(1, len(the_board)):
#         if col_clashes(the_board, col):
#             return True
#     return False

#     # Because of the many ways of choosing 8 squares of a 64 square game board,
#     # we will use permutatuions.

#     # We'll try a random shuffle of the permutation [0,1,2,3,4,5,6,7]


# def main():
#     import random
#     # import random
#     rng = random.Random()

#     # generate the initial permutation
#     bd = list(range(16))
#     num_found = 0
#     tries = 0
#     t0 = time.perf_counter()
#     while num_found < 10:
#         rng.shuffle(bd)
#         tries += 1
#         if not has_clashes(bd):
#             print("Found solution {0} in {1} tries.".format(bd, tries))
#             tries = 0
#             num_found += 1
#     t1 = time.perf_counter()
#     print(t1 - t0)


# main()


# Board size of Four:
# Found solution [1, 3, 0, 2] in 1 tries.
# Found solution [2, 0, 3, 1] in 5 tries.
# Found solution [1, 3, 0, 2] in 10 tries.
# Found solution [1, 3, 0, 2] in 2 tries.
# Found solution [1, 3, 0, 2] in 26 tries.
# Found solution [2, 0, 3, 1] in 5 tries.
# Found solution [2, 0, 3, 1] in 9 tries.
# Found solution [2, 0, 3, 1] in 13 tries.
# Found solution [2, 0, 3, 1] in 8 tries.
# Found solution [1, 3, 0, 2] in 10 tries.
# 0.0003903910000000038

# Board size of 12:
# Found solution [3, 10, 4, 7, 11, 0, 6, 1, 9, 5, 8, 2] in 127616 tries.
# Found solution [8, 5, 9, 1, 6, 11, 3, 0, 7, 10, 4, 2] in 25748 tries.
# Found solution [4, 1, 8, 11, 7, 3, 0, 9, 5, 10, 2, 6] in 21588 tries.
# Found solution [8, 5, 3, 0, 6, 11, 1, 10, 7, 2, 4, 9] in 169467 tries.
# Found solution [3, 9, 6, 8, 10, 2, 0, 5, 1, 4, 11, 7] in 49349 tries.
# Found solution [4, 6, 1, 10, 5, 7, 9, 3, 0, 2, 8, 11] in 13077 tries.
# Found solution [7, 1, 6, 9, 0, 8, 11, 4, 2, 10, 5, 3] in 51184 tries.
# Found solution [6, 8, 3, 11, 9, 2, 5, 1, 10, 7, 0, 4] in 88882 tries.
# Found solution [3, 7, 9, 2, 0, 5, 10, 8, 1, 11, 4, 6] in 2092 tries.
# Found solution [3, 10, 7, 2, 6, 11, 1, 5, 0, 9, 4, 8] in 6695 tries.
# 3.950741986

# Board size of 16:
# Found solution [7, 9, 12, 0, 13, 3, 10, 8, 1, 4, 2, 11, 6, 15, 5, 14] in 1377112 tries.
# Found solution [14, 12, 3, 8, 6, 2, 9, 1, 4, 0, 10, 15, 5, 11, 13, 7] in 187288 tries.
# Found solution [11, 5, 8, 4, 0, 12, 15, 7, 10, 6, 2, 14, 1, 3, 9, 13] in 761302 tries.
# Found solution [11, 7, 0, 6, 13, 9, 1, 15, 10, 14, 2, 4, 8, 3, 5, 12] in 2537199 tries.
# Found solution [7, 10, 3, 6, 12, 5, 0, 11, 4, 15, 9, 2, 14, 8, 1, 13] in 369347 tries.
# Found solution [1, 8, 13, 3, 10, 15, 4, 11, 0, 2, 7, 5, 14, 12, 9, 6] in 1227528 tries.
# Found solution [7, 14, 10, 15, 6, 1, 11, 2, 0, 13, 4, 9, 12, 3, 5, 8] in 219311 tries.
# Found solution [8, 3, 0, 6, 15, 12, 7, 11, 2, 14, 1, 4, 9, 13, 10, 5] in 1888880 tries.
# Found solution [12, 5, 9, 11, 13, 8, 3, 0, 2, 15, 10, 7, 4, 14, 1, 6] in 2778809 tries.
# Found solution [7, 0, 6, 14, 12, 15, 9, 5, 1, 4, 11, 13, 2, 10, 8, 3] in 1009425 tries.
# 103.54650013000001


# 3) Adapt the queen program so that we keep a list of solutions that have already
# printed, so we don't print the same solution more than once:
#   Add empty list, set to variable solutions
#   At the end of main function, solutions.append(list(bd))
#   Add this line in main: if not has_clashes(bd) and bd not in solutions:


# def share_diagonal(x0, y0, x1, y1):
#     """Is (x0, y0) on a shared diagonal with (x1, y1)?"""
#     dy = abs(y1 - y0)
#     dx = abs(x1 - x0)
#     # they clash if dx == dy
#     return dx == dy


# def col_clashes(bs, c):
#     """ Return True if the queen at column c clashes with any queen to its left"""
#     for i in range(c):
#         if share_diagonal(i, bs[i], c, bs[c]):
#             return True
#     # No clashes - col c has a safe placement
#     return False


# def has_clashes(the_board):
#     """ Determine whether we have any queens clashing on the diagonals
#         We're assuming here that the_board is a permutation of column
#         numbers, so we're not explicitly checking row or
#         column clashes
#     """
#     for col in range(1, len(the_board)):
#         if col_clashes(the_board, col):
#             return True
#     return False

#     # Because of the many ways of choosing 8 squares of a 64 square game board,
#     # we will use permutatuions.

#     # We'll try a random shuffle of the permutation [0,1,2,3,4,5,6,7]


# def main():
#     import random
#     # import random
#     rng = random.Random()
#     solutions = []
#     # generate the initial permutation
#     bd = list(range(4))
#     num_found = 0
#     tries = 0
#     t0 = time.perf_counter()
#     while num_found < 10:
#         rng.shuffle(bd)
#         tries += 1
#         if not has_clashes(bd) and bd not in solutions:
#             print("Found solution {0} in {1} tries.".format(bd, tries))
#             solutions.append(list(bd))
#             tries = 0
#             num_found += 1
#     t1 = time.perf_counter()
#     print(t1 - t0)


# main()


# 4) Chess boards are symmetric: if we have a solution to the queens problem,
# its mirror solution — either flipping the board on the X or in the Y axis,
# is also a solution. And giving the board a 90 degree, 180 degree, or 270 degree
# rotation is also a solution. In some sense, solutions that are just mirror images
# or rotations of other solutions — in the same family — are less interesting than
# the unique “core cases”. Of the 92 solutions for the 8 queens problem, there are
# only 12 unique families if you take rotations and mirror images into account.
# Wikipedia has some fascinating stuff about this.

# a)Write a function to mirror a solution in the Y axis,


# b) Write a function to mirror a solution in the X axis,

# c) Write a function to rotate a solution by 90 degrees anti-clockwise,
# and use this to provide 180 and 270 degree rotations too.

# d) Write a function which is given a solution, and it generates the
#  family of symmetries for that solution. For example, the symmetries of

# e) Now adapt the queens program so it won’t list solutions that are in the same family.
# It only prints solutions from unique families.

# def share_diagonal(x0, y0, x1, y1):
#     """Is (x0, y0) on a shared diagonal with (x1, y1)?"""
#     dy = abs(y1 - y0)
#     dx = abs(x1 - x0)
#     # they clash if dx == dy
#     return dx == dy


# def col_clashes(bs, c):
#     """ Return True if the queen at column c clashes with any queen to its left"""
#     for i in range(c):
#         if share_diagonal(i, bs[i], c, bs[c]):
#             return True
#     # No clashes - col c has a safe placement
#     return False


# def has_clashes(the_board):
#     """ Determine whether we have any queens clashing on the diagonals
#         We're assuming here that the_board is a permutation of column
#         numbers, so we're not explicitly checking row or
#         column clashes
#     """
#     for col in range(1, len(the_board)):
#         if col_clashes(the_board, col):
#             return True
#     return False

#     # Because of the many ways of choosing 8 squares of a 64 square game board,
#     # we will use permutatuions.

#     # We'll try a random shuffle of the permutation [0,1,2,3,4,5,6,7]


# def main():
#     import random
#     # import random
#     rng = random.Random()
#     solutions = []
#     # generate the initial permutation
#     bd = list(range(4))
#     num_found = 0
#     tries = 0
#     t0 = time.perf_counter()
#     while num_found < 10:
#         rng.shuffle(bd)
#         tries += 1
#         if not has_clashes(bd):
#             # if not has_clashes(bd) and bd not in solutions:
#             print("Found solution {0} in {1} tries.".format(bd, tries))
#             solutions.append(list(bd))
#             tries = 0
#             num_found += 1
#     t1 = time.perf_counter()
#     print(t1 - t0)


# main()


# Every week a computer scientist buys four lotto tickets.
# She always chooses the same prime numbers, with the hope that
# if she ever hits the jackpot, she will be able to go onto TV and
# Facebook and tell everyone her secret. This will suddenly create
# widespread public interest in prime numbers, and will be the trigger
# event that ushers in a new age of enlightenment. She represents her weekly
# tickets in Python as a list of lists:

# my_tickets = [ [ 7, 17, 37, 19, 23, 43],
#                [ 7,  2, 13, 41, 31, 43],
#                [ 2,  5,  7, 11, 13, 17],
#                [13, 17, 37, 19, 23, 43] ]

# Complete these exercises.

# a) Each lotto draw takes six random balls, numbered from 1 to 49.
# Write a function to return a lotto draw.
# (I used the random.sample() function which returns k length of unique elements
# chosen from the population sequence.)

def lotto_draw():
    import random
    winner = sorted(random.sample(range(1, 50), 6))
    print(winner)
    return winner

# lotto_draw()

# b) Write a function that compares a single ticket and a draw,
# and returns the number of correct picks on that ticket:


def buy_lotto_ticket():
    import random
    number_of_tix = int(input('how many tickets would you like to buy?'))
    print_out = []
    draw = sorted(random.sample(range(1, 50), 6))
    for tix in range(number_of_tix):
        draw = sorted(random.sample(range(1, 50), 6))
        print_out.append(draw)
    print(print_out)
    return draw


# buy_lotto_ticket()


def did_you_win():
    import random
    winner = sorted(random.sample(range(1, 50), 6))
    print(winner)
    number_of_tix = int(input('how many tickets would you like to buy?'))
    print_out = []
    for items in range(number_of_tix):
        draw = sorted(random.sample(range(1, 50), 6))
        print_out.append(draw)
    for tix in print_out:
        if tix == winner:
            print('you Won!')
            print(tix, '->', winner)
    print('Sorry, no matches', print_out, winner)


# did_you_win()


# c.) Write a function that takes a list of tickets and a draw,
# and returns a list telling how many picks were correct on each ticket

def lucky_nums():
    import random

    winner = sorted(random.sample(range(1, 50), 6))
    # print(winner)
    number_of_tix = int(input('how many tickets would you like to buy?'))
    print_out = []
    for items in range(number_of_tix):
        draw = sorted(random.sample(range(1, 50), 6))
        print_out.append(draw)

    chosen = [list(set(num).intersection(winner)) for num in print_out]

    count = 0

    for lst in chosen:
        for num in lst:
            if num > 0:
                count += 1

    print(print_out, winner)
    print(chosen)
    print(f'{count} or your numbers/number matched winning numbers')


lucky_nums()
