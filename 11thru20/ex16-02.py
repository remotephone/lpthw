
# first you import the modules

from sys import argv

# define the args. First one is the script name, second one is your file name

script, filename = argv

# Now we print some text to let you know the file will be cleared.

print "We're going to erase %r." % filename
print " If you don't want that, hit CTRL + C."
print "If you do want that, hit RETURN."


# prompt the user for their OK

raw_input("?")

# get 'er done
print "Opening the file..."

# This opens the file to write, instead of read with r.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# prompt the user with the line x: and then ask for their input.

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# What we're here for...
print "I'm going to write these to the file."

# Write it to the file and insert a new line after each line.

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file cleanly.
print "And finally we close it."
target.close()
