import string
ss = "Hello World"
tt = ss.upper()

print(tt)


fruit = "banana"
print(list(enumerate(fruit)))

print(fruit)

print(fruit[:])

print(fruit[4:])

print("i" in "apple")


# 8.9 The in and not in operators
# Combine the in operator w/ string concatenation

def remove_vowels(s):
    vowels = ("aeiouAEIOU")
    sans_vowels = ""
    for x in s:
        if x not in vowels:
            sans_vowels += x
    print(sans_vowels)
    return sans_vowels


remove_vowels("abracadabra")


# 8.10 A find function
#  Write a function that finds the index of a character in a string

def find(strg, char):
    """
        Find and return the first index of a character in a given string
        return -1 if no idex is found
    """
    ix = 0
    while ix < len(strg):
        if strg[ix] == char:
            print(ix)
            return ix
        ix += 1
    return -1


find("macdaa", "c")


# 8.11 Looping and counting

def count_a(text):
    """
        Write a function that counts the number of
        times the character "a" is in the inserted text
    """
    ix = 0
    az = 0
    while ix < len(text):
        if text[ix] == "a":
            az += 1
        ix += 1
    print(az)
    return az


count_a("Macca lacca bobacca")


def count_b(text):
    """
        Write a function that counts the number of
        times the character b exists in the text input
    """
    ix = 0
    for chars in text:
        if chars == "b":
            ix += 1
    print(ix)
    return ix


assert count_b("bbb") == 3
assert count_b("mobba") == 2


count_b("babba labba")


# 8.12 Optional parameters

def find_2(strg, ch, start=0):
    """
        Write a function that finds a given character in
        a given text at a given start position.
    """
    ix = start
    while ix < len(strg):
        if strg[ix] == ch:
            print(ix)
            return ix
        ix += 1
    print(-1)
    return -1


find_2("bubba lunka", "u")
find_2("bubba lunka", "u", 2)


# 8.13 The built-in find method

print("bananas".find("nan"))


# 8.15 String Module


def remove_puncs(s):
    """
        write a function that will remove the punctuation from a
        str using python's built in string module
    """
    sans_puncs = ""
    for chars in s:
        if chars not in string.punctuation:
            sans_puncs += chars
    print(sans_puncs)
    return sans_puncs


stringy = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

remove_puncs(stringy)


print()
print(" == == == == == == == == == == == ")

print()


# 8.19 Excercises

# 1) What is the result of each of the following:

print("Python"[1])
print("Strings are sequences of characters."[5])
print(len("wonderful"))
print("Mystery"[:4])
print("p" in "Pineapple")
print("apple" in "Pineapple")
print("pear" not in "Pineapple")
print("apple" > "pineapple")
print("pineapple" < "Peach")


# 2) Modify the code below so that Ouack and Quack are spelled correctly

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

# 3) Encapsulate
# in a function named count_letters, and generalize it so that it accepts the string and
# the letter as arguments. Make the function return the number of characters, rather than print the answer.
# The caller should do the printing.

fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)


def count_letters(strng, char):
    count = 0
    for letters in strng:
        if letters == char:
            count += 1
    print(count)


count_letters("banana", "n")

print("--------------")

print(len("bob"))
# 4) Now rewrite the count_letters function so that instead of traversing the string,
# it repeatedly calls the find method, with the optional third parameter to locate new
# occurrences of the letter being counted.


# def find(strng, ch, start=0):
#     ix = start
#     while ix < len(strng):
#         if strng[ix] == ch:
#             print(ix)
#         ix += 1
#     return -1


# find("banana", "a")


# def find_letters(strng, char, start=0):
#     count = 0
#     ix = start
#     while ix < len(strng):
#         if strng[ix].find(char) != -1:
#             count += 1
#             ix = strng.find(char) + 1
#         else:
#             return -1
#     print(count)


# find_letters("bononana", "a")


# 5) Assign to a variable in your program a triple-quoted string that contains your
# favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake,
# some inspirational verses, etc.

# Write a function which removes all punctuation from the string, breaks the string into a
# list of words, and counts the number of words in your text that contain the letter “e”.
# Your program should print an analysis of the text like this:

# Your text contains 243 words, of which 109 (44.8%) contain an "e".


m = """ “If someone is able to show me that what I think or do is not right, I will happily change, 
for I seek the truth, by which no one was ever truly harmed. It is the person who continues in 
his self-deception and ignorance who is harmed.”
"""


def mod_quote(s):
    import string
    splitz = s.split()
    sans_punc = ""
    eList = []

    for letters in s:
        if letters not in string.punctuation:
            sans_punc += letters
    split_quote = sans_punc.split()
    for words in split_quote:
        if "e" in words:
            eList.append(words)
    s1 = "Your text contains {0} words, of which {1} ({2:.0%}) contain an 'e')".format(
        len(splitz), len(eList), len(eList)/len(splitz))
    print(s1)
    print(len(splitz))
    print(len(eList))


mod_quote(m)
