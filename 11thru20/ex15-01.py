# Probably good to remember its doing two things, first opening the file and
# keeping it in memory and the printing the file using read()
# Import the module


from sys import argv

# Define the argv's. The first one is the script name, second is the filename
# you pass the script when you run it.

script, filename = argv

# Now we open the filename that we passed above.

txt = open(filename)

# Prints the contents of the file.

print "Here's your file %r:" % filename
print txt.read()

# Prompts the user to enter the name of the file.

print "Type the filename again:"
file_again = raw_input("> ")

# prints the submitted filename from the prompt.
txt_again = open(file_again)

print txt_again.read()
