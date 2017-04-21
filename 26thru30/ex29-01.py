people = 20
cats = 30
dogs = 15

# count people and cats. if less people, print.
# 20 < 30 so print
if people < cats:
    print "Too many cats! The world is doomed!"

# Count people and cats. If less cats, print.
# if 20 > 30, but its false! so no print.
if people > cats:
    print "Not many cats! The world is saved!"

# This is false, so print.
# 20 < 15
if people < dogs:
    print "The world is drooled on!"

# 20 > 15, true so print
if people > dogs:
    print "The world is dry!"

# Take the number of dogs and add 5 to it. 
dogs += 5

# If people are more or equal to dogs, print.
# 20 >= 20  - so print
if people >= dogs:
    print "People are greater than or equal to dogs."

# IF people are less or equal to dogs, print
# 20 <= 20 - so print
if people <= dogs:
    print "People are less than or equal to dogs."

#if people == dogs, print
# 20 == 20 so thats good.
if people == dogs:
    print "People are dogs."
