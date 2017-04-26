

print "How high should we go?"

top = int(raw_input("> "))

numbers = []

for i in range(0, top):
    print "Our range is ", numbers
    print "The next number is %d " %i
    numbers.append(i)
