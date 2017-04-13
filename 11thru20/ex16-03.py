from sys import argv
import time

print "Let's read that last file!"

# sleep for 2 seconds

time.sleep(2)

print "..." 

print "What was that file name again?"
filename = raw_input("?") 

print "Ah yes! Opening that now..."
target = open(filename,'r')

print "Here it is: "
print target.read()

target.close()
