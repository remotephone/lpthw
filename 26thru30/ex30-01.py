# Set up the numbers, define what = what
people = 30
cars = 40
trucks = 15


## FIRST BLOCK

# If cars are more than people, then print we should take the cars
if cars > people:
        print "We should take the cars."

# If that's not true and cars are more than people, print do not take cars
elif cars < people:
    print "We should not take the cars."

#If anything else is true, print We can't decide.
else:
    print "We can't decide."


## SECOND BLOCK

# If there are more trucks than cars, print too many trucks.
if trucks > cars:
    print "That's too many tucks."

# If more cars than trucks, then recommend taking trucks.
elif trucks < cars:
    print "Maybe we could take the trucks."

# If none of that is true, then print it can't be decided. So like if cars =
# trucks then undecided.
else:
    print "We still can't decide."


## THIRD BLOCK

# If there are more poeple than trucks, they should take the trucks. Throw em
# all in the back I guess?
if people > trucks:
    print "Alrigth, let's just take the trucks."

# But if there's not enough trucks, then don't go at all. 
else:
    print "Fine, let's stay home then."
