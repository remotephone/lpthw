# first we create the function. We pass variables to the function as we go.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# we're assigning the digit with the %d (instead of string %s) to the variable.
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
# Gotta have a new line at the end so it doesn't look funny with your prompt.
    print "Get a blanket.\n"

# You can just read the next line. 20 = cheese_count and 30 = boxes_of_crackers
# python will remember the positions of your stuff.
print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)



print "OR, we can use variables from our script:"
# Assign variables in our script
amount_of_cheese = 10
amount_of_crackers = 50

# And then immediately reuse them by retyping out the function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Math!
print "We can even do math inside too!"
cheese_and_crackers(10 + 20, 5 +6)
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


