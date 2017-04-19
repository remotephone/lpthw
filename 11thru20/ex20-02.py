# import the module
from sys import argv

# define your args, first one is the script name next one is the input file
# Maybe I missed something but i didn't see anything teling me how to write the
# input file. My file looked like this.

## This is line 1
## This is line 2
## This is line 3

# Back to work.
script, input_file = argv

# I didn't get this at first, this post cleared it up:
# http://stackoverflow.com/questions/16637518/python-file-variable-what-is-it
# Then you read it.
def print_all(f):
    print f.read()

# We define the fucntion rewind with seek(0) to get to the beginning of the
# file.
def rewind(f):
    f.seek(0)

# two arguments, line_count and the file you're reading.
def print_a_line(line_count, f):
# print the ine_count and read that file line
    print line_count, f.readline()

# define current file as the results of the opened input file.
current_file = open(input_file)

# duh.
print "First let's print the whole file:\n"

# print all lines in the file. We defined that earlier to make this function
# just read the file. 
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#go back to the first line
rewind(current_file)


print "Let's print three lines:"

# Current line is the first one, print it and the file contents
current_line = 1
print_a_line(current_line, current_file)

# Increment current line and print the next. 
current_line = current_line + 1
print_a_line(current_line, current_file)

# Same thing again. By this one youre adding to the previous one, python
# remembers you've already added to it.

current_line = current_line + 1
print_a_line(current_line, current_file)


