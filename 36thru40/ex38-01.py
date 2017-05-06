ten_things = "Apples Orange Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# split() - splits items in a list by white spaces. You can also specify
# different things to split the ist by. You'll see that later.
stuff = ten_things.split()

# Create another list of things to work on later. Separating th, this way lets
# python know you have a bunch of idfferent items.

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl",
        "Boy"]

# This is counting the amount of items in your list and while the items in that
# list does not equal 10, the fuinction contnues. This could be dangerous if
# you start above ten, it'll never end.
while len(stuff) != 10:
# pop returns the last item in a list. Here, we set that value to next_one
    next_one = more_stuff.pop()
    print "Adding: ", next_one
# Then we append next_one to the list.
    stuff.append(next_one)
# Then we print the count of current items.
    print "There are %d items now." % len(stuff)

# Altogether, the above function takes the list stuff, takes the last item off
# the list of stuff and appends it to the list of items you have.

print "There we go: ", stuff

print "Let's do some things with stuff."

# print item 1 in the list. remember, its 0 and then 1. 
print stuff[1]
# This works in reverse order. Start at 0, move backwards by 1.
print stuff[-1] # whoa! fancy!
# Remove and print the last item of stuff.
print stuff.pop()
# our list is one shorter now, but it prints each item with a space between it.
print ' '.join(stuff) #what? cool!
# This works the same, but prints a # between the items 3 and 5.
print '#'.join(stuff[3:5])
