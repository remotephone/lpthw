#Strings and text

# This prints the % string at the end. The next few lines assign some more
# variables. 
# the y variable pulls in other % values in itself. so that's nifty


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print out the values

print x
print y

# r displays the raw data. That's why we end up with the ticks and quotes when
# it reprints the value of the variable we assigned above.
print "i said: %r." % x
print "I also said: '%s'." % y

# assign the false value here
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This is the same thing as above, except we're printing the variable instead
# of printing a string of text.
print joke_evaluation % hilarious

# And then you just stick these two things together. 
w = "This is the left of..."
e = "a string with a right side."

print w + e
