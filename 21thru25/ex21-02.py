# Define a function where a and b are added and you return the answer.
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

# Define a function where b is subtracted from a and you return the answer.
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

# multiply a and b to return the answer. 
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a* b

# Divide A by B and return the answer.
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

# When the first value is A and the second value is B, do this.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# do the math and print the values in the string.
# %d is like %s, except for digits or numbers.
print "Age: %d, Height: %d, Weight: %d IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.

print "Here is a puzzle."

# Take IQ and divide by two. take that answer and multiply it by weight, take
# height and subtract your answer from it and then add it to the value of age. 
#  age + (height- ((iq/2) * weight))
# I Think thats right...

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
