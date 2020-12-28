import urllib.request
myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("----------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

mynewhandle = open("test.txt", "r")
# Keep reading forever
while True:
    # Try to read the next line
    theline = mynewhandle.readline()
    # If there are no more lines, leave the loop
    if len(theline) == 0:
        break

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()

coworkers = open("coworkers.txt", "w")
coworkers.write("Joe Arai\n")
coworkers.write("Joe Barnes\n")
coworkers.write("Gabe Cruze\n")
coworkers.write("Dave Caddo\n")
coworkers.close()


f = open("coworkers.txt", "r")
xs = f.readlines()
f.close()

xs.sort()

g = open("sortedcoworkers.txt", "w")
for v in xs:
    g.write(v)
g.close()


coworkers_line = open("sortedcoworkers.txt", "r")

while True:
    co_line = coworkers_line.readline()

    if len(co_line) == 0:
        break

    print(co_line, end="")

coworkers_line.close()


quick_read = open("coworkers.txt")
content = quick_read.read()
quick_read.close()

words = content.split()
print("There are {0} words in the file.".format(len(words)))


# 13.6 Workin with binary files

# b1 = open("somefile.zip", "rb")
# b2 = open("thecopy.zip", "wb")

# while True:
#     b1r = b1.read(1024)
#     if len(b1r) == 0:
#         break
#     g.write(b1r)

# b1.close()
# b2.close()


# 13.7 An Example

# Many useful line-processing programs will read a text file line-for-line and do
# some minor processing at they write the lines to an output file.

# We call this kind of a program a filter

# E.g. - a filter that copies a file, omitting any lines that begin with a '#'

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue

        # Place any additional processing logic here
        outfile.write(text)

        infile.close()
        outfile.close()


# 13.9 Fetching something from the web
# This will copy the contents of a webpage to a local file:

# import urllib.request
# url = "http://xml.resource.org/public/rfc/txt/rfc798.txt"
# destination_filename = "rfc793.txt"

# urllib.request.urlretrieve(url, destination_filename)

url = "https://www.ietf.org/rfc/rfc793.txt"
destination_filename = "rfc793.txt"

# urllib.request.urlretrieve(url, destination_filename)


# A slightly different example:

def retrieve_page(url):
    """
        Retreive the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta


the_text = retrieve_page("https://www.ietf.org/rfc/rfc793.txt")
print(the_text)
