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
book_words = "the apple fell from the tree to the grass".split()

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


# bigger_vocab = load_words_from_file("vocab.txt")
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


# book_words = get_words_from_book("alice.txt")
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
