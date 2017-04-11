from sys import argv

name = raw_input("What is your name? ")

print "your name is", name

script, action = argv

print "well " + name + ",", action + "!"
