import re
import string


def cleanword(s):
    return s.translate(str.maketrans(" ", " ", string.punctuation))


def has_dashdash(s):
    return "--" in s


def extract_words(s):
    return re.compile(r"\w+").findall(s.lower())


# "Now is the time!    'Now', is the time? Yes, now.") == [
#     'now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']

# print(extract_words("Now is the time!    'Now', is the time? Yes, now."))

def wordcount(word, lst):
    count = 0
    for words in lst:
        if words == word:
            count += 1
    return count

# print(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]))
