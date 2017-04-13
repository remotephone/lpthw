from sys import argv


script, filename = argv

print "Let's read that last file!"

print "It's name was %r." % filename
target = open(filename,'r')

print "Here it is: "
print target.read()

target.close()
