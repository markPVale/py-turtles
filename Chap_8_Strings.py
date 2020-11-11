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
