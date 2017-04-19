##I'm supposed to remove all instances of my_ here.
## with vim, you can :%s/my_//g and bam, it does them all

name = 'Zed Shaw'
age = 31
height = 70 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d years old" % age
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "he's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right
print "If I had %d, %d, and %d, I get %d." % (age, height, weight,
    age + height + weight)


