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

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result


vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

find_unknown_words(vocab, book_words)

assert find_unknown_words(vocab, book_words) == ["from", "to"]
assert find_unknown_words([], book_words) == book_words
assert find_unknown_words(vocab, ["the", "boy", "fell"]) == []


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
print("There are {0} words in the vocab, starting with\n {1} ".format(
    len(bigger_vocab), bigger_vocab[:6]))


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
print("There are {0} words in the book, the first 100 are\n {1}".format(
    len(book_words), book_words[:100]))


# Now we have all the pieces ready, let us see what words in this book are not
# in the vocabulary:

missing_words = find_unknown_words(bigger_vocab, book_words)

# print(missing_words)


# We wait a considerable time now, something like a minute,
# before Python finally works its way through this


# Let us try to improve the efficiency of this:

# import time

# Note, that time.clock() has since been deprecated, using:
t0 = time.process_time()
missing_words = find_unknown_words(book_words, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
# >>> There are 0 unkown words.
# >>> That took 2.7484 seconds.

t0 = time.perf_counter()
missing_words = find_unknown_words(book_words, book_words)
t1 = time.perf_counter()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
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
