# 13.11 Exercises

# 1.) Write a program that reads a file and writes out a new file with the lines in reversed
# order (i.e. the first line in the old file becomes the last one in the new file.)

# my_test_taxes = open('test_taxes.txt', 'w')
# my_test_taxes.write('This is the beginning\n')
# my_test_taxes.write('This is the 2nd\n')
# my_test_taxes.write('This is the 3rd\n')
# my_test_taxes.write('This is the 4th\n')
# my_test_taxes.write('This is the end\n')
# my_test_taxes.close()


def rev_read(original_file, new_file):
    infile = open(original_file, "r")
    read_file = infile.readlines()
    infile.close()
    outfile = open(new_file, "w")
    read_file.reverse()
    for line in read_file:
        outfile.write(line)
    outfile.close()


# rev_read("test_taxes.txt", "revtest_taxes.txt")


# 2.) Write a program that reads a file and prints only those lines that contain the
# substring snake.

# snake_string = open('snake_substring.txt', 'w')
# snake_string.write('This is a looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong snake 1 stringggggggggggg\n')
# snake_string.write('This is a snake 2 looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong stringggggggggggg\n')
# snake_string.write('This snake 3 is a looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong stringggggggggggg\n')
# snake_string.write('This is a looooooong snake 4 stringggggggggggg\n')
# snake_string.close()


def find_substring(file, substring):
    openfile = open(file, 'r')
    for lines in openfile.readlines():
        if substring in lines:
            print(lines)


# find_substring('snake_substring.txt', 'snake')


# 3). Write a program that reads a text file and produces an output file which is a
# copy of the file, except the first five columns of each line contain a four digit
# line number, followed by a space. Start numbering the first line in the output file at 1.
# Ensure that every line number is formatted to the same width in the output file.
# Use one of your Python programs as test data for this exercise: your output should be a
# printed and numbered listing of the Python program.


# my_enum_file = open('my_enum_file.txt', 'w')
# my_enum_file.write(
#     'You have power over your mind - not outside events. Realize this, and you will find strength.\n')
# my_enum_file.write(
#     'The universe is change; our life is what our thoughts make it.\n')
# my_enum_file.write(
#     'Waste no more time arguing about what a good man should be. Be one.\n')
# my_enum_file.write(
#     'Very little is needed to make a happy life; it is all within yourself, in your way of thinking.\n')
# my_enum_file.write(
#     'If it is not right do not do it; if it is not true do not say it.\n')
# my_enum_file.write(
#     'Love nothing but that which comes to you woven in the pattern of your destiny. For what could more aptly fit your needs?\n')
# my_enum_file.write(
#     'It is not death that a man should fear, but he should fear never beginning to live.\n')
# my_enum_file.write(
#     'The object of life is not to be on the side of the majority, but to escape finding oneself in the ranks of the insane.\n')
# my_enum_file.write('The soul becomes dyed with the color of its thoughts.\n')

# with open('my_enum_file.txt', 'r') as f:
#     for i, line in enumerate(f, start=1):
#         print(f'{i}  = {line}')


def number_file(file_to_read, new_output_file):
    outfile = open(new_output_file, 'w')
    infile = open(file_to_read, 'r')
    for i, line in enumerate(infile, start=1):
        outfile.write(f'{i}  = {line}')
    infile.close()
    outfile.close()


number_file('my_enum_file.txt', 'numbered_file.txt')


# 4.) Write a program that undoes the numbering of the previous exercise:
# it should read a file with numbered lines and produce another file without
# line numbers.

def filter_file(file_to_read, new_output_file):
    import re

    infile = open(file_to_read, 'r')
    outfile = open(new_output_file, 'w')
    read_file = infile.readlines()
    infile.close()
    for lines in read_file:
        for i in lines:
            letter = re.search(r'[A-z]', lines)
            # start = lines.index(letter)
        # print(letter.start())
        # print(lines[5:])
        outfile.write(lines[5:])
    outfile.close()


filter_file('numbered_file.txt', 'non_numbered_file.txt')
