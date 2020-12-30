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
