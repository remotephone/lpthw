print "This is a new game. Pick a number one through 10"

number = raw_input("> ")

if number <= "5":
    print "too low"
elif number >= "7":
    print "too high"
else:
    print "You got it!"
